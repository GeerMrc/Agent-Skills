# Vue 组合式API与测试

> 🟢 **Composition API & Testing** - 组合式函数、无障碍、测试

---

## 📖 文档说明

本文档提供 Vue.js 3 的组合式API详解、无障碍最佳实践和测试策略。

**相关文档**：
- [指南总览](vue-guide.md) - 状态管理、路由、基础组件
- [返回主文档](vue.md)

---

## 🔧 组合式函数

### 可复用逻辑

```typescript
// composables/useMouse.ts
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(event: MouseEvent) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  return { x, y }
}

// 使用
<script setup lang="ts">
import { useMouse } from '@/composables/useMouse'

const { x, y } = useMouse()
</script>
```

### 异步状态

```typescript
// composables/useAsync.ts
import { ref } from 'vue'

export function useAsync<T>(fn: () => Promise<T>) {
  const state = ref<{
    data: T | null
    error: Error | null
    isLoading: boolean
  }>({
    data: null,
    error: null,
    isLoading: false
  })

  async function execute() {
    state.value.isLoading = true
    state.value.error = null

    try {
      state.value.data = await fn()
    } catch (error) {
      state.value.error = error as Error
    } finally {
      state.value.isLoading = false
    }
  }

  return {
    ...toRefs(state.value),
    execute
  }
}
```

### 防抖与节流

```typescript
// composables/useDebounce.ts
import { ref, watch } from 'vue'
import { useDebounceFn, useThrottleFn } from '@vueuse/core'

export function useDebounce<T>(value: Ref<T>, delay: number) {
  const debouncedValue = ref(value.value) as Ref<T>

  watch(value, useDebounceFn((newValue) => {
    debouncedValue.value = newValue
  }, delay))

  return debouncedValue
}

export function useThrottle<T>(value: Ref<T>, delay: number) {
  const throttledValue = ref(value.value) as Ref<T>

  watch(value, useThrottleFn((newValue) => {
    throttledValue.value = newValue
  }, delay))

  return throttledValue
}
```

### 表单验证

```typescript
// composables/useForm.ts
import { ref, reactive, computed } from 'vue'

export function useForm<T extends Record<string, any>>(
  initialValues: T,
  validate: (values: T) => Record<keyof T, string[]>
) {
  const values = reactive<T>({ ...initialValues })
  const errors = ref<Record<keyof T, string[]>>({} as any)
  const touched = ref<Record<keyof T, boolean>>({} as any)

  const isValid = computed(() => {
    return Object.keys(errors.value).every(
      (key) => errors.value[key as keyof T].length === 0
    )
  })

  function setFieldValue<K extends keyof T>(field: K, value: T[K]) {
    values[field] = value
    touched.value[field] = true
    validateField(field)
  }

  function validateField<K extends keyof T>(field: K) {
    const fieldErrors = validate(values)[field]
    errors.value[field] = fieldErrors || []
  }

  function reset() {
    Object.assign(values, initialValues)
    Object.keys(touched.value).forEach((key) => {
      touched.value[key as keyof T] = false
    })
    errors.value = {} as any
  }

  return {
    values,
    errors,
    touched,
    isValid,
    setFieldValue,
    validateField,
    reset
  }
}
```

---

## ♿ 无障碍最佳实践

### 语义化HTML

```vue
<template>
  <!-- ✅ 好的做法：语义化元素 -->
  <nav aria-label="主导航">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
    </ul>
  </nav>

  <main>
    <h1>页面标题</h1>
    <article>
      <h2>文章标题</h2>
      <p>文章内容...</p>
    </article>
  </main>

  <footer>
    <p>&copy; 2025</p>
  </footer>

  <!-- ❌ 避免：纯div -->
  <div class="nav">
    <div class="nav-item" @click="goHome">Home</div>
  </div>
</template>
```

### ARIA属性

```vue
<template>
  <!-- 按钮状态 -->
  <button
    :aria-pressed="isPressed"
    :aria-expanded="isExpanded"
    :aria-controls="panelId"
    @click="toggle"
  >
    Toggle
  </button>

  <!-- 加载状态 -->
  <div
    role="status"
    :aria-busy="isLoading"
    aria-live="polite"
  >
    {{ isLoading ? 'Loading...' : 'Done' }}
  </div>

  <!-- 模态框 -->
  <div
    role="dialog"
    aria-modal="true"
    :aria-labelledby="modalTitleId"
    :aria-describedby="modalDescId"
  >
    <h2 :id="modalTitleId">Modal Title</h2>
    <p :id="modalDescId">Modal description</p>
  </div>

  <!-- 表单关联 -->
  <label for="username">Username</label>
  <input
    id="username"
    :aria-required="true"
    :aria-invalid="errors.username ? 'true' : 'false'"
    :aria-describedby="usernameErrorId"
    v-model="username"
  />
  <span :id="usernameErrorId" role="alert">
    {{ errors.username }}
  </span>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isPressed = ref(false)
const isExpanded = ref(false)
const isLoading = ref(false)
const panelId = 'panel-1'
const modalTitleId = 'modal-title-1'
const modalDescId = 'modal-desc-1'
const usernameErrorId = 'username-error-1'

const username = ref('')
const errors = ref<{ username?: string }>({})

function toggle() {
  isPressed.value = !isPressed.value
  isExpanded.value = !isExpanded.value
}
</script>
```

### 键盘导航

```vue
<template>
  <div
    role="button"
    tabindex="0"
    @click="handleClick"
    @keydown="handleKeydown"
  >
    点击或按 Enter/Space
  </div>
</template>

<script setup lang="ts">
function handleClick() {
  console.log('Clicked')
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault()
    handleClick()
  }
}
</script>
```

### 焦点管理

```vue
<template>
  <dialog ref="dialogRef">
    <form method="dialog">
      <button @click="close">关闭</button>
    </form>
  </dialog>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const dialogRef = ref<HTMLDialogElement>()

onMounted(() => {
  dialogRef.value?.showModal()
  // 管理焦点
  const focusableElements = dialogRef.value?.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  )
  focusableElements?.[0]?.focus()
})

function close() {
  dialogRef.value?.close()
}
</script>
```

---

## 🧪 测试

### 单元测试（Vitest）

```typescript
// Counter.test.ts
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Counter from '@/components/Counter.vue'

describe('Counter', () => {
  it('increments count when button clicked', async () => {
    const wrapper = mount(Counter, {
      props: {
        title: 'Test Counter',
        count: 0
      }
    })

    expect(wrapper.find('p').text()).toContain('0')

    await wrapper.find('button').trigger('click')

    expect(wrapper.find('p').text()).toContain('1')
  })

  it('emits update event', async () => {
    const wrapper = mount(Counter)

    await wrapper.find('button').trigger('click')

    expect(wrapper.emitted('update')).toBeTruthy()
    expect(wrapper.emitted('update')[0]).toEqual([1])
  })

  it('displays double message when count > 1', async () => {
    const wrapper = mount(Counter, {
      props: { count: 1 }
    })

    await wrapper.find('button').trigger('click')

    expect(wrapper.html()).toContain('Double!')
  })
})
```

### 组件测试（带Store）

```typescript
import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import UserList from '@/components/UserList.vue'
import { useUserStore } from '@/stores/users'

describe('UserList', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('displays users from store', () => {
    const store = useUserStore()
    store.users = [
      { id: '1', name: 'Alice' },
      { id: '2', name: 'Bob' }
    ]

    const wrapper = mount(UserList)

    expect(wrapper.findAll('.user')).toHaveLength(2)
  })

  it('calls fetchUsers on mount', async () => {
    const fetchUsers = vi.fn()
    const wrapper = mount(UserList, {
      global: {
        mocks: {
          fetchUsers
        }
      }
    })

    await wrapper.vm.$nextTick()

    expect(fetchUsers).toHaveBeenCalled()
  })
})
```

### 路由测试

```typescript
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createMemoryHistory } from 'vue-router'
import Home from '@/views/Home.vue'

describe('Home', () => {
  it('navigates to about', async () => {
    const router = createRouter({
      history: createMemoryHistory(),
      routes: [
        { path: '/', component: Home },
        { path: '/about', component: { template: '<div>About</div>' } }
      ]
    })

    const wrapper = mount(Home, {
      global: {
        plugins: [router]
      }
    })

    await wrapper.find('.about-link').trigger('click')

    expect(router.currentRoute.value.path).toBe('/about')
  })
})
```

### 组合式函数测试

```typescript
import { describe, it, expect } from 'vitest'
import { useMouse } from '@/composables/useMouse'

describe('useMouse', () => {
  it('tracks mouse position', () => {
    const { x, y } = useMouse()

    window.dispatchEvent(new MouseEvent('mousemove', {
      pageX: 100,
      pageY: 200
    }))

    expect(x.value).toBe(100)
    expect(y.value).toBe(200)
  })
})
```

---

## 📋 最佳实践总结

### 1. 组合式API

- 使用组合式函数提取可复用逻辑
- 避免在组合式函数中引入过多依赖
- 保持组合式函数简单专注
- 使用 toRefs 保持响应式

### 2. 状态管理

- 使用 Pinia 进行全局状态管理
- 组合式Store适用于简单状态
- 避免过度使用全局状态

### 3. 组件通信

- Props down, Events up
- 使用 provide/inject 处理深层嵌套
- 利用插槽实现内容分发

### 4. 无障碍

- 使用语义化HTML元素
- 添加适当的ARIA属性
- 确保键盘导航可用
- 管理焦点状态

### 5. 测试

- 测试用户行为而非实现
- 使用Vue Test Utils
- 保持测试简单明了
- 覆盖关键功能

### 6. 性能

- 使用 v-once 渲染静态内容
- 使用 v-memo 跳过不必要的更新
- 懒加载路由组件
- 使用 computed 缓存计算结果

```vue
<template>
  <!-- v-once: 只渲染一次 -->
  <h1 v-once>{{ title }}</h1>

  <!-- v-memo: 条件缓存 -->
  <div v-memo="[valueA, valueB]">
    ...
  </div>
</template>
```

---

## 🔗 相关文档

- [指南总览](vue-guide.md) - 状态管理、路由、基础组件
- [返回主文档](vue.md) - Vue总览

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
