# Vue 指南总览

> 🟢 **Core Guide** - 状态管理、路由、基础组件

---

## 📖 文档说明

本文档提供 Vue.js 3 的核心指南，包括状态管理、路由和基础组件。

**相关文档**：
- [组合式API与测试](vue-guide-composition.md) - 组合式API、无障碍、测试
- [返回主文档](vue.md)

---

## 📡 状态管理

### Pinia（推荐）

```typescript
// stores/counter.ts
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),

  getters: {
    doubleCount: (state) => state.count * 2
  },

  actions: {
    increment() {
      this.count++
    }
  }
})

// 使用
<script setup lang="ts">
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()

counter.count++
counter.increment()
</script>
```

### 组合式Store

```typescript
// stores/useTheme.ts
import { ref } from 'vue'
import { useStorage } from '@vueuse/core'

export function useTheme() {
  const theme = useStorage('theme', 'light')

  const isDark = computed(() => theme.value === 'dark')

  function toggle() {
    theme.value = theme.value === 'light' ? 'dark' : 'light'
  }

  return {
    theme,
    isDark,
    toggle
  }
}

// 使用
<script setup lang="ts">
import { useTheme } from '@/stores/useTheme'

const { theme, isDark, toggle } = useTheme()
</script>
```

### Store 组合

```typescript
// stores/index.ts
import { useUserStore } from './user'
import { useCartStore } from './cart'

export function useAppStores() {
  const user = useUserStore()
  const cart = useCartStore()

  return {
    user,
    cart
  }
}
```

---

## 🛣️ 路由（Vue Router）

### 路由配置

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/users/:id',
    name: 'user',
    component: () => import('@/views/User.vue'),
    props: true
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### 编程式导航

```typescript
import { useRouter } from 'vue-router'

const router = useRouter()

// 导航到命名路由
router.push({ name: 'user', params: { id: '123' } })

// 带查询参数
router.push({ path: '/user', query: { q: 'search' } })

// 替换当前路由
router.replace({ path: '/home' })

// 后退
router.go(-1)
```

### 路由守卫

```typescript
// 全局前置守卫
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/login')
  } else {
    next()
  }
})

// 组件内守卫
<script setup lang="ts">
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

onBeforeRouteLeave((to, from, next) => {
  if (hasUnsavedChanges()) {
    const answer = confirm('有未保存的更改，确定离开吗？')
    if (answer) {
      next()
    } else {
      next(false)
    }
  } else {
    next()
  }
})

onBeforeRouteUpdate((to, from, next) => {
  // 路由参数变化时调用
  fetchData(to.params.id)
  next()
})
</script>
```

### 懒加载

```typescript
const routes = [
  {
    path: '/dashboard',
    component: () => import('@/views/Dashboard.vue')
  }
]
```

---

## 🔗 组件通信

### Props 和 Emits

```vue
<script setup lang="ts">
// 定义 props
interface Props {
  title: string
  count?: number
  items?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  count: 0,
  items: () => []
})

// 定义 emits
const emit = defineEmits<{
  update: [value: number]
  change: [id: string, value: string]
}>()

function handleClick() {
  emit('update', props.count + 1)
  emit('change', '123', 'new value')
}
</script>
```

### v-model

```vue
<script setup lang="ts">
interface Props {
  modelValue: string
  modelModifiers?: { capitalize: boolean }
}

interface Emits {
  'update:modelValue': [value: string]
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

function onInput(e: Event) {
  let value = (e.target as HTMLInputElement).value

  if (props.modelModifiers?.capitalize) {
    value = value.charAt(0).toUpperCase() + value.slice(1)
  }

  emit('update:modelValue', value)
}
</script>

<template>
  <input
    :value="modelValue"
    @input="onInput"
  />
</template>
```

### Provide / Inject

```typescript
// 父组件
<script setup lang="ts">
import { provide, ref, readonly } from 'vue'

const theme = ref('light')

provide('theme', readonly(theme))
provide('toggleTheme', () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
})
</script>

// 子组件
<script setup lang="ts">
import { inject } from 'vue'

const theme = inject<Ref<string>>('theme')
const toggleTheme = inject<(() => void)>('toggleTheme')
</script>
```

### 插槽

```vue
<!-- 父组件 -->
<template>
  <MyComponent>
    <template #header>
      <h1>标题</h1>
    </template>

    <template #default>
      <p>内容</p>
    </template>

    <template #footer>
      <button>按钮</button>
    </template>
  </MyComponent>
</template>

<!-- MyComponent.vue -->
<template>
  <div>
    <slot name="header" />
    <slot />
    <slot name="footer" />
  </div>
</template>
```

### 作用域插槽

```vue
<!-- 父组件 -->
<template>
  <UserList>
    <template #default="{ user }">
      <span>{{ user.name }}</span>
    </template>
  </UserList>
</template>

<!-- UserList.vue -->
<template>
  <ul>
    <li v-for="user in users" :key="user.id">
      <slot :user="user" />
    </li>
  </ul>
</template>
```

---

## 🎨 组件样式

### Scoped CSS

```vue
<template>
  <div class="card">
    <h2 class="title">{{ title }}</h2>
  </div>
</template>

<style scoped>
.card {
  padding: 16px;
  border: 1px solid #ddd;
}

.title {
  font-size: 18px;
}
</style>
```

### CSS Modules

```vue
<template>
  <div :class="$style.card">
    <h2 :class="$style.title">{{ title }}</h2>
  </div>
</template>

<style module>
.card {
  padding: 16px;
}

.title {
  font-size: 18px;
}
</style>
```

### 动态样式

```vue
<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  isActive: boolean
  size: 'small' | 'medium' | 'large'
}>()

const classes = computed(() => [
  'button',
  {
    'button-active': props.isActive,
    'button-small': props.size === 'small',
    'button-medium': props.size === 'medium',
    'button-large': props.size === 'large'
  }
])
</script>

<template>
  <button :class="classes">
    <slot />
  </button>
</template>

<style>
.button {
  padding: 8px 16px;
}

.button-active {
  background: blue;
}

.button-small {
  padding: 4px 8px;
}

.button-medium {
  padding: 8px 16px;
}

.button-large {
  padding: 12px 24px;
}
</style>
```

---

## 🔗 相关文档

- [组合式API与测试](vue-guide-composition.md) - 组合式API、无障碍、测试
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
