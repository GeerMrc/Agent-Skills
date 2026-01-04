# Vue最佳实践

> 🟢 **Vue.js 3** - Composition API 和组件设计

---

## 📖 文档说明

本文档提供 Vue.js 3 的完整最佳实践指南，涵盖组件设计、Composition API、样式管理和性能优化等内容。

**目标读者**: Vue 开发者
**文档长度**: ~280行（主文档）
**阅读时间**: 约15分钟

**相关文档**:
- [完整实现指南](vue-guide.md) - 状态管理、路由、测试等详细内容

---

## 🎯 核心概念

Vue 3 采用Composition API，提供更灵活的代码组织和更好的TypeScript支持。本指南涵盖Vue开发的最佳实践。

**核心特性**：
- Composition API
- 响应式系统（Proxy）
- 单文件组件（SFC）
- Teleport、Suspense、Fragments

---

## 🎨 组件设计

### 组件定义

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

// Props定义（使用TypeScript）
interface Props {
  title: string
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})

// Emits定义
interface Emits {
  (e: 'update', value: number): void
  (e: 'delete', id: string): void
}

const emit = defineEmits<Emits>()

// 响应式状态
const localCount = ref(props.count)
const isDouble = computed(() => localCount.value > 1)

// 方法
function increment() {
  localCount.value++
  emit('update', localCount.value)
}
</script>

<template>
  <div class="counter">
    <h2>{{ title }}</h2>
    <p>Count: {{ localCount }}</p>
    <p v-if="isDouble">Double!</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<style scoped>
.counter {
  padding: var(--spacing-md);
}
</style>
```

### 组件命名

```vue
<!-- ✅ 好的做法：多词组件名 -->
<UserProfile />
<DataTable />
<SearchInput />

<!-- ❌ 避免：单词组件名 -->
<User />
<Table />
<Input />
```

### Props最佳实践

```typescript
// ✅ 好的做法：详细定义Props
interface Props {
  // 必填props
  title: string
  id: string

  // 可选props（有默认值）
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  size: 'md',
  disabled: false,
  count: 0
})

// ✅ 使用Prop验证
defineProps({
  value: {
    type: [String, Number],
    required: true,
    validator: (value: string | number) => {
      return value > 0
    }
  }
})
```

---

## 🔨 Composition API

### 响应式状态

```typescript
import { ref, reactive, computed, toRefs } from 'vue'

// ref：基础类型
const count = ref(0)
count.value++ // 需要.value

// reactive：对象
const state = reactive({
  count: 0,
  message: 'Hello'
})
state.count++ // 不需要.value

// computed：计算属性
const doubleCount = computed(() => count.value * 2)

// toRefs：解构reactive对象
const { count, message } = toRefs(state)
```

### Composables（可复用逻辑）

```typescript
// composables/useCounter.ts
import { ref } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)

  function increment() {
    count.value++
  }

  function decrement() {
    count.value--
  }

  function reset() {
    count.value = initialValue
  }

  return {
    count,
    increment,
    decrement,
    reset
  }
}

// 使用
<script setup lang="ts">
import { useCounter } from '@/composables/useCounter'

const { count, increment, decrement, reset } = useCounter(10)
</script>
```

### 生命周期

```typescript
import {
  onMounted,
  onBeforeUnmount,
  onUpdated
} from 'vue'

onMounted(() => {
  console.log('组件已挂载')
})

onBeforeUnmount(() => {
  console.log('组件即将卸载')
  // 清理：移除事件监听器、定时器等
})

onUpdated(() => {
  console.log('组件已更新')
})
```

---

## 🎨 样式管理

### CSS Modules

```vue
<template>
  <div :class="$style.container">
    <button :class="$style.button">Click</button>
  </div>
</template>

<style module>
.container {
  padding: var(--spacing-md);
}

.button {
  background: var(--color-primary);
}
</style>
```

### Scoped CSS

```vue
<template>
  <div class="container">
    <button class="button">Click</button>
  </div>
</template>

<style scoped>
.container {
  padding: var(--spacing-md);
}

.button {
  background: var(--color-primary);
}
</style>
```

### 动态样式

```vue
<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  variant: 'primary' | 'secondary'
  size: 'sm' | 'md' | 'lg'
}>()

const classes = computed(() => [
  'button',
  `button--${props.variant}`,
  `button--${props.size}`
])
</script>

<template>
  <button :class="classes">Click</button>
</template>
```

---

## 🚀 性能优化

### v-once（静态内容）

```vue
<template>
  <!-- 只渲染一次，不响应数据变化 -->
  <h1 v-once>{{ title }}</h1>
</template>
```

### v-memo（条件缓存）

```vue
<template>
  <!-- 仅当ids变化时重新渲染 -->
  <div v-for="item in list" :key="item.id" v-memo="[item.id]">
    {{ item.name }}
  </div>
</template>
```

### 计算属性缓存

```typescript
// ✅ 好的做法：使用computed
const filteredList = computed(() => {
  return list.value.filter(item => item.active)
})

// ❌ 避免：在模板中使用方法
{{ filterList() }}
```

### 异步组件

```typescript
import { defineAsyncComponent } from 'vue'

// 异步加载组件
const AsyncComponent = defineAsyncComponent(() =>
  import('./HeavyComponent.vue')
)

// 带加载状态的异步组件
const AsyncComponent = defineAsyncComponent({
  loader: () => import('./HeavyComponent.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  delay: 200,
  timeout: 3000
})
```

---

## 🔗 组件通信

### Props down, Events up

```vue
<!-- 父组件 -->
<script setup lang="ts">
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const parentCount = ref(0)

function handleUpdate(value: number) {
  parentCount.value = value
}
</script>

<template>
  <ChildComponent
    :count="parentCount"
    @update="handleUpdate"
  />
</template>

<!-- 子组件 -->
<script setup lang="ts">
interface Props {
  count: number
}

interface Emits {
  (e: 'update', value: number): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

function increment() {
  emit('update', props.count + 1)
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

### v-model（双向绑定）

```vue
<!-- 父组件 -->
<script setup lang="ts">
import { ref } from 'vue'
import ChildInput from './ChildInput.vue'

const text = ref('')
</script>

<template>
  <ChildInput v-model="text" />
  {{ text }}
</template>

<!-- 子组件 -->
<script setup lang="ts">
interface Props {
  modelValue: string
}

interface Emits {
  (e: 'update:modelValue', value: string): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

function updateValue(event: Event) {
  emit('update:modelValue', (event.target as HTMLInputElement).value)
}
</script>

<template>
  <input :value="modelValue" @input="updateValue" />
</template>
```

### Provide/Inject（跨层级通信）

```typescript
// 父组件提供
import { provide, ref } from 'vue'

const theme = ref('light')

provide('theme', theme)

// 子组件注入
import { inject } from 'vue'

const theme = inject<Ref<string>>('theme')
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **状态管理** | Pinia、组合式Store | [查看详情](vue-guide.md#状态管理) |
| **路由** | Vue Router配置、导航 | [查看详情](vue-guide.md#路由) |
| **无障碍** | ARIA、键盘导航 | [查看详情](vue-guide.md#无障碍最佳实践) |
| **测试** | 单元测试、集成测试 | [查看详情](vue-guide.md#测试) |

---

## 📋 检查清单

### 组件设计

- [ ] 使用 `<script setup>` 语法
- [ ] TypeScript定义Props和Emits
- [ ] 多词组件命名
- [ ] Props验证和默认值

### Composition API

- [ ] 使用 ref/reactive
- [ ] 创建可复用Composables
- [ ] 生命周期钩子正确使用
- [ ] 清理副作用

### 性能优化

- [ ] v-once静态内容
- [ ] v-memo条件缓存
- [ ] 计算属性缓存
- [ ] 异步组件加载

### 样式管理

- [ ] Scoped CSS或CSS Modules
- [ ] 动态样式计算
- [ ] CSS变量使用

---

## 💡 最佳实践总结

### 1. 组件化

每个组件职责单一，可复用性强

```vue
<!-- ✅ 好的做法 -->
<script setup lang="ts">
interface Props {
  user: User
}
const props = defineProps<Props>()
</script>

<template>
  <UserProfileCard :user="user" />
</template>
```

### 2. Composition优先

优先使用 Composition API

```typescript
// ✅ 使用 Composition API
const { count, increment } = useCounter()

// ❌ 避免：Options API
export default {
  data() {
    return { count: 0 }
  }
}
```

### 3. 性能优先

使用计算属性和异步组件

```typescript
// ✅ 计算属性
const filteredList = computed(() => list.filter(...))

// ❌ 避免：方法调用
{{ filterList() }}
```

### 4. 类型安全

充分利用 TypeScript

```typescript
interface Props {
  title: string
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})
```

---

## 🔗 相关文档

- [完整实现指南](vue-guide.md) - 状态管理、路由、测试
- [React最佳实践](./react.md)
- [Svelte最佳实践](./svelte.md)
- [Angular最佳实践](./angular.md)
- [组件状态覆盖](../implementation/component-states.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
