# Vue 完整实现指南

> 🟢 **Complete Implementation Guide** - 状态管理、路由、测试

---

## 📖 文档说明

本文档提供 Vue.js 3 的完整实现细节，包括状态管理、路由、无障碍和测试等高级功能。

**相关文档**：
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

### Store持久化

```typescript
// stores/useAuth.ts
import { ref, watch } from 'vue'
import { useStorage } from '@vueuse/core'

export function useAuth() {
  const token = useStorage('auth_token', '')
  const user = ref<User | null>(null)

  // 监听token变化，自动加载用户信息
  watch(token, async (newToken) => {
    if (newToken) {
      user.value = await fetchUser(newToken)
    } else {
      user.value = null
    }
  }, { immediate: true })

  function login(credentials: Credentials) {
    // 登录逻辑
  }

  function logout() {
    token.value = ''
    user.value = null
  }

  return {
    token,
    user,
    login,
    logout,
    isAuthenticated: computed(() => !!token.value)
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
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/users/:id',
    name: 'user',
    component: () => import('@/views/UserView.vue'),
    props: true
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/views/AdminView.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('@/views/NotFoundView.vue')
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
```

### 路由导航

```vue
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// 编程式导航
function goToAbout() {
  router.push({ name: 'about' })
}

function goToUser(id: string) {
  router.push({ name: 'user', params: { id } })
}

function goToSearch() {
  router.push({
    name: 'search',
    query: { q: 'vue', page: 1 }
  })
}

// 路由参数
const userId = route.params.id
const searchQuery = route.query.q

// 路由元信息
const isAdmin = route.meta.requiresAdmin
</script>

<template>
  <div>
    <router-link :to="{ name: 'about' }">About</router-link>
    <button @click="goToAbout">Go to About</button>
  </div>
</template>
```

### 路由守卫

```typescript
// router/index.ts
import { useAuthStore } from '@/stores/auth'

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()

  // 检查是否需要认证
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  }
  // 检查是否需要管理员权限
  else if (to.meta.requiresAdmin && !auth.isAdmin) {
    next({ name: 'home' })
  }
  else {
    next()
  }
})

// 组件内守卫
<script setup lang="ts">
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

// 离开守卫
onBeforeRouteLeave((to, from, next) => {
  const answer = window.confirm('确定要离开吗？未保存的更改将丢失。')
  if (answer) {
    next()
  } else {
    next(false)
  }
})

// 更新守卫
onBeforeRouteUpdate((to, from, next) => {
  // 路由参数变化时执行
  next()
})
</script>
```

### 路由懒加载

```typescript
// 基础懒加载
const HomeView = () => import('@/views/HomeView.vue')

// 带加载状态的懒加载
const AdminView = () => ({
  component: import('@/views/AdminView.vue'),
  loading: LoadingComponent,
  error: ErrorComponent,
  delay: 200,
  timeout: 3000
})

// 分组懒加载（webpack chunk）
const AdminViews = () => import(/* webpackChunkName: "admin" */ '@/views/admin/AdminDashboard.vue')
```

---

## ♿ 无障碍最佳实践

### 语义化HTML

```vue
<template>
  <!-- ✅ 好的做法：语义化元素 -->
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>

  <main>
    <h1>Page Title</h1>
    <article>
      <h2>Article Title</h2>
      <p>Article content...</p>
    </article>
  </main>

  <aside>
    <h3>Sidebar</h3>
  </aside>

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
  <!-- 可聚焦的div -->
  <div
    role="button"
    tabindex="0"
    @click="handleClick"
    @keydown.enter="handleClick"
    @keydown.space.prevent="handleClick"
  >
    Click me or press Enter/Space
  </div>

  <!-- 键盘陷阱（模态框） -->
  <div
    ref="modalRef"
    role="dialog"
    aria-modal="true"
    @keydown="handleKeydown"
  >
    <!-- ... -->
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

const modalRef = ref<HTMLElement>()
const focusableElements = ref<HTMLElement[]>()

onMounted(() => {
  if (modalRef.value) {
    focusableElements.value = Array.from(
      modalRef.value.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
    )
    focusableElements.value[0]?.focus()
  }
})

function handleClick() {
  console.log('Clicked')
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'Tab') {
    const firstElement = focusableElements.value[0]
    const lastElement = focusableElements.value[focusableElements.value.length - 1]

    if (event.shiftKey && document.activeElement === firstElement) {
      event.preventDefault()
      lastElement?.focus()
    } else if (
      !event.shiftKey &&
      document.activeElement === lastElement
    ) {
      event.preventDefault()
      firstElement?.focus()
    }
  }

  if (event.key === 'Escape') {
    close()
  }
}

function close() {
  // 关闭模态框
}

onBeforeUnmount(() => {
  // 清理
})
</script>
```

### 屏幕阅读器支持

```vue
<template>
  <!-- 隐藏内容（仅屏幕阅读器可见） -->
  <span class="sr-only">Only visible to screen readers</span>

  <!-- 跳过导航链接 -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <main id="main-content">
    <!-- ... -->
  </main>
</template>

<style scoped>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
</style>
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
    const store = useUserStore()
    store.fetchUsers = vi.fn()

    mount(UserList)

    expect(store.fetchUsers).toHaveBeenCalled()
  })
})
```

### 路由测试

```typescript
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createMemoryHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

describe('HomeView', () => {
  it('renders home page', async () => {
    const router = createRouter({
      history: createMemoryHistory(),
      routes: [
        { path: '/', component: HomeView }
      ]
    })

    await router.push('/')

    const wrapper = mount(HomeView, {
      global: {
        plugins: [router]
      }
    })

    expect(wrapper.html()).toContain('Welcome')
  })
})
```

### 测试工具函数

```typescript
// 测试响应式状态
it('should update ref value', () => {
  const count = ref(0)
  count.value = 5
  expect(count.value).toBe(5)
})

// 测试计算属性
it('should compute double count', () => {
  const count = ref(5)
  const doubleCount = computed(() => count.value * 2)
  expect(doubleCount.value).toBe(10)
})

// 测试异步操作
it('should fetch data asynchronously', async () => {
  const data = await fetchData()
  expect(data).toBeDefined()
})

// 测试表单验证
it('should validate required field', () => {
  const username = ref('')
  const isValid = computed(() => username.value.length > 0)

  expect(isValid.value).toBeFalsy()

  username.value = 'test'

  expect(isValid.value).toBeTruthy()
})
```

---

## 📋 最佳实践总结

### 1. 状态管理

- 使用 Pinia 管理全局状态
- 创建可复用的组合式Store
- 使用 localStorage 持久化状态
- 避免过度使用全局状态

### 2. 路由

- 使用懒加载优化性能
- 使用路由守卫保护路由
- 合理组织路由结构
- 使用命名路由和参数

### 3. 无障碍

- 使用语义化HTML元素
- 添加适当的 ARIA 属性
- 确保键盘导航可用
- 支持屏幕阅读器

### 4. 测试

- 保持测试简单明了
- 使用测试替身（Mock/Stub）
- 测试用户行为而非实现细节
- 保持高测试覆盖率

### 5. 性能

- 使用 v-once 和 v-memo
- 异步加载组件
- 计算属性缓存
- 路由懒加载

---

## 🔗 相关文档

- [返回主文档](vue.md)
- [React最佳实践](./react.md)
- [Svelte最佳实践](./svelte.md)
- [Angular最佳实践](./angular.md)
- [无障碍指南](../implementation/accessibility.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
