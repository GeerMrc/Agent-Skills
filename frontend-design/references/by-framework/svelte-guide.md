# Svelte 完整指南

> 🧡 **Advanced Features** - 组件通信、状态管理、路由、无障碍、测试

---

## 📖 文档说明

本文档提供 Svelte 的高级功能和最佳实践，包括组件通信、状态管理、路由、无障碍和测试等内容。

**相关文档**：
- [返回主文档](svelte.md)

---

## 🔗 组件通信

### Props down, Events up

**父组件传递数据给子组件**：

```svelte
<!-- 父组件 Parent.svelte -->
<script lang="ts">
  import Child from './Child.svelte'

  let parentCount = $state(0)

  function handleUpdate(value: number) {
    parentCount = value
  }
</script>

<Child
  count={parentCount}
  onupdate={handleUpdate}
/>

<!-- 子组件 Child.svelte -->
<script lang="ts">
  interface Props {
    count: number
  }

  let { count }: Props = $props()

  const emit = createEventDispatcher<{
    update: number
  }>()

  function increment() {
    emit('update', count + 1)
  }
</script>

<button on:click={increment}>{count}</button>
```

### 双向绑定（bind:）

**简化父子数据同步**：

```svelte
<!-- 父组件 Parent.svelte -->
<script lang="ts">
  import ChildInput from './ChildInput.svelte'

  let text = $state('')
</script>

<ChildInput bind:value={text} />
<p>输入的值: {text}</p>

<!-- 子组件 ChildInput.svelte -->
<script lang="ts">
  interface Props {
    value: string
  }

  let { value }: Props = $props()
</script>

<input bind:value={value} />
```

**双向绑定最佳实践**：

```svelte
<!-- ✅ 使用双向绑定简化代码 -->
<input bind:value={name} />
<Checkbox bind:checked={isSelected} />
<Select bind:value={option} />

<!-- ❌ 避免手动处理更新 -->
<input
  value={name}
  on:input={(e) => name = e.target.value}
/>
```

### createEventDispatcher（事件派发）

**向父组件发送事件**：

```svelte
<script lang="ts">
  import { createEventDispatcher } from 'svelte'

  const dispatch = createEventDispatcher<{
    click: MouseEvent
    change: { value: string }
    submit: FormData
  }>()

  function handleClick(event: MouseEvent) {
    dispatch('click', event)
  }

  function handleChange(value: string) {
    dispatch('change', { value })
  }

  function handleSubmit() {
    const formData = new FormData(form)
    dispatch('submit', formData)
  }
</script>

<form bind:this={form} on:submit={handleSubmit}>
  <input on:change={(e) => handleChange(e.target.value)} />
  <button on:click={handleClick}>Submit</button>
</form>
```

### 组件插槽（Slots）

**默认插槽**：

```svelte
<!-- 父组件 -->
<Card>
  <h2>标题</h2>
  <p>内容</p>
</Card>

<!-- Card.svelte -->
<div class="card">
  <slot />
</div>
```

**命名插槽**：

```svelte
<!-- 父组件 -->
<Card>
  <header slot="header">
    <h2>标题</h2>
  </header>
  <p slot="default">内容</p>
  <footer slot="footer">
    <small>页脚</small>
  </footer>
</Card>

<!-- Card.svelte -->
<div class="card">
  <div class="card-header">
    <slot name="header" />
  </div>
  <div class="card-body">
    <slot />
  </div>
  <div class="card-footer">
    <slot name="footer" />
  </div>
</div>
```

**插槽 Props**：

```svelte
<!-- 父组件 -->
<List data={items} let:item>
  <span>{item.name}</span>
</List>

<!-- List.svelte -->
<script lang="ts">
  interface Props {
    data: Array<{ name: string }>
  }

  let { data }: Props = $props()
</script>

{#each data as item}
  <slot item={item} />
{/each}
```

---

## 📡 状态管理

### Svelte Stores（内置）

**writable Store**：

```typescript
// stores/counter.ts
import { writable } from 'svelte/store'

// 创建可写 store
export const count = writable(0)

// 读取和更新
import { count } from '@/stores/counter'

// 订阅
count.subscribe(value => console.log(value))

// 更新
count.set(1)
count.update(n => n + 1)
```

**derived Store**：

```typescript
// stores/counter.ts
import { writable, derived } from 'svelte/store'

export const count = writable(0)

// 派生 store（自动更新）
export const doubleCount = derived(
  count,
  $count => $count * 2
)

// 多个依赖
export const tripleCount = derived(
  [count, doubleCount],
  ([$count, $doubleCount]) => $count + $doubleCount
)

// 带缓存的派生
export const expensiveValue = derived(
  count,
  ($count, set) => {
    const timeout = setTimeout(() => {
      set(computeExpensiveValue($count))
    }, 1000)

    return () => clearTimeout(timeout)
  }
)
```

**readable Store**：

```typescript
// stores/time.ts
import { readable } from 'svelte/store'

// 只读 store
export const time = readable(new Date(), set => {
  const interval = setInterval(() => {
    set(new Date())
  }, 1000)

  return () => clearInterval(interval)
})

// 使用
<script lang="ts">
  import { time } from '@/stores/time'
</script>

<p>当前时间: {$time}</p>
```

### 自定义Store

**创建可复用的 Store**：

```typescript
// stores/useTheme.ts
import { writable } from 'svelte/store'

function createTheme(initialTheme: 'light' | 'dark' = 'light') {
  const { subscribe, set, update } = writable(initialTheme)

  return {
    subscribe,
    toggle: () => update(theme =>
      theme === 'light' ? 'dark' : 'light'
    ),
    set,
    setLight: () => set('light'),
    setDark: () => set('dark')
  }
}

export const theme = createTheme()
```

**带持久化的 Store**：

```typescript
// stores/useAuth.ts
import { writable } from 'svelte/store'
import { browser } from '$app/environment'

function createPersistedStore<T>(key: string, initialValue: T) {
  const storedValue = browser
    ? localStorage.getItem(key)
      ? JSON.parse(localStorage.getItem(key)!)
      : initialValue
    : initialValue

  const { subscribe, set, update } = writable(storedValue)

  return {
    subscribe,
    set: (value: T) => {
      if (browser) {
        localStorage.setItem(key, JSON.stringify(value))
      }
      set(value)
    },
    update
  }
}

export const user = createPersistedStore('user', null)
```

### Store使用

**在组件中使用 Store**：

```svelte
<script lang="ts">
  import { count } from '@/stores/counter'

  // 自动订阅（$语法）
  $count = 5

  // 或使用subscribe
  $effect(() => {
    console.log($count)
  })

  // 方法
  function increment() {
    count.update(n => n + 1)
  }
</script>

<p>Count: {$count}</p>
<button on:click={increment}>+</button>
```

**Store 组合**：

```typescript
// stores/index.ts
import { writable, derived } from 'svelte/store'

// 基础 stores
export const user = writable(null)
export const posts = writable([])
export const filter = writable('all')

// 派生 stores
export const filteredPosts = derived(
  [posts, filter],
  ([$posts, $filter]) => {
    if ($filter === 'all') return $posts
    return $posts.filter(post => post.status === $filter)
  }
)

export const userPosts = derived(
  [user, posts],
  ([$user, $posts]) => {
    if (!$user) return []
    return $posts.filter(post => post.authorId === $user.id)
  }
)
```

---

## 🛣️ 路由（SvelteKit）

### 文件路由

**目录结构**：

```
src/routes/
├── +page.svelte              # /
├── +page.server.ts          # 服务端数据加载
├── +layout.svelte            # 布局组件
├── +error.svelte             # 错误页面
├── about/
│   ├── +page.svelte          # /about
│   └── +page.server.ts       # /about 服务端数据
├── blog/
│   ├── +page.svelte          # /blog
│   ├── +page.server.ts       # /blog 服务端数据
│   └── [slug]/
│       ├── +page.svelte      # /blog/:slug
│       └── +page.server.ts   # /blog/:slug 服务端数据
└── api/
    └── posts/
        └── +server.ts        # /api/posts API 路由
```

### 页面组件

**服务端数据加载**：

```svelte
<!-- src/routes/+page.svelte -->
<script lang="ts">
  // 服务端数据加载
  export async function load({ fetch, params, url }) {
    const res = await fetch('/api/posts')
    const posts = await res.json()

    return {
      posts,
      meta: {
        title: 'Blog',
        description: 'Latest posts'
      }
    }
  }
</script>

<svelte:head>
  <title>{data.meta.title}</title>
  <meta name="description" content={data.meta.description} />
</svelte:head>

{#each data.posts as post}
  <article>{post.title}</article>
{/each}
```

**客户端数据加载**：

```svelte
<!-- src/routes/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte'

  let posts = $state([])

  onMount(async () => {
    const res = await fetch('/api/posts')
    posts = await res.json()
  })
</script>

{#each posts as post}
  <article>{post.title}</article>
{/each}
```

### 路由导航

**编程式导航**：

```svelte
<script lang="ts">
  import { goto, preloadData } from '$app/navigation'
  import { page } from '$app/stores'

  function goToAbout() {
    goto('/about')
  }

  function goBack() {
    history.back()
  }

  function goToPost(id: string) {
    // 预加载数据
    preloadData(`/blog/${id}`).then(() => {
      goto(`/blog/${id}`)
    })
  }

  // 带选项的导航
  function navigateWithState() {
    goto('/dashboard', {
      replaceState: true,  // 替换历史记录
      noScroll: true,       // 不滚动到顶部
      keepFocus: true       // 保持焦点
    })
  }

  // 获取当前路由信息
  $effect(() => {
    console.log($page.url.pathname)
    console.log($page.params.slug)
    console.log($page.query.search)
  })
</script>

<a href="/about">About</a>
<button on:click={goToAbout}>Go to About</button>
```

### 路由守卫

**保护路由**：

```svelte
<!-- src/routes/admin/+page.server.ts -->
export async function load({ url, fetch }) {
  const res = await fetch('/api/auth')
  const user = await res.json()

  if (!user.isAdmin) {
    throw redirect(302, '/login')
  }

  return { user }
}
```

**布局级别守卫**：

```svelte
<!-- src/routes/+layout.server.ts -->
export async function load({ fetch, url }) {
  const res = await fetch('/api/auth')
  const user = await res.json()

  // 未认证用户重定向
  if (!user && url.pathname !== '/login') {
    throw redirect(302, '/login')
  }

  return { user }
}
```

### API 路由

**创建 API 端点**：

```typescript
// src/routes/api/posts/+server.ts
import { json } from '@sveltejs/kit'

export async function GET({ url }) {
  const limit = url.searchParams.get('limit') || '10'

  const posts = await db.posts.findMany({
    take: parseInt(limit)
  })

  return json(posts)
}

export async function POST({ request }) {
  const data = await request.json()

  const post = await db.posts.create({
    data
  })

  return json(post, { status: 201 })
}
```

---

## ♿ 无障碍最佳实践

### 语义化HTML

**使用正确的 HTML 元素**：

```svelte
<!-- ✅ 好的做法：语义化元素 -->
<nav aria-label="主导航">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <h1>页面标题</h1>
  <article>
    <h2>文章标题</h2>
    <p>文章内容...</p>
  </article>
</main>

<aside>
  <h3>侧边栏</h3>
</aside>

<footer>
  <p>&copy; 2025</p>
</footer>

<!-- ❌ 避免：纯div -->
<div class="nav">
  <div class="nav-item" on:click={goHome}>Home</div>
</div>
```

### ARIA属性

**按钮状态**：

```svelte
<script lang="ts">
  let isPressed = $state(false)
  let isExpanded = $state(false)

  function toggle() {
    isPressed = !isPressed
    isExpanded = !isExpanded
  }
</script>

<button
  aria-pressed={isPressed}
  aria-expanded={isExpanded}
  aria-controls="panel-1"
  on:click={toggle}
>
  Toggle
</button>

<div id="panel-1" hidden={!isExpanded}>
  面板内容
</div>
```

**加载状态**：

```svelte
<script lang="ts">
  let isLoading = $state(false)
</script>

<div
  role="status"
  aria-busy={isLoading}
  aria-live="polite"
>
  {#if isLoading}
    <p>加载中...</p>
  {:else}
    <p>完成</p>
  {/if}
</div>
```

**表单关联**：

```svelte
<script lang="ts">
  let username = $state('')
  let errors = $state<{ username?: string }>({})
</script>

<label for="username">用户名</label>
<input
  id="username"
  aria-required="true"
  aria-invalid={errors.username ? 'true' : 'false'}
  aria-describedby="username-error"
  bind:value={username}
/>
{#if errors.username}
  <span id="username-error" role="alert">
    {errors.username}
  </span>
{/if}
```

### 键盘导航

**可聚焦的div**：

```svelte
<script lang="ts">
  function handleClick() {
    console.log('Clicked')
  }
</script>

<div
  role="button"
  tabindex="0"
  on:click={handleClick}
  on:keydown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault()
      handleClick()
    }
  }}
>
  点击我或按 Enter/Space
</div>
```

**键盘陷阱（模态框）**：

```svelte
<script lang="ts">
  import { onMount, onBeforeMount } from 'svelte'

  let modalRef: HTMLElement
  let focusableElements: HTMLElement[]

  onMount(() => {
    if (modalRef) {
      focusableElements = Array.from(
        modalRef.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        )
      )
      focusableElements[0]?.focus()
    }
  })

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Tab') {
      const firstElement = focusableElements[0]
      const lastElement = focusableElements[focusableElements.length - 1]

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
</script>

<div
  bind:this={modalRef}
  role="dialog"
  aria-modal="true"
  on:keydown={handleKeydown}
>
  <!-- 模态框内容 -->
</div>
```

---

## 🧪 测试

### 单元测试（Vitest）

**测试组件**：

```typescript
// Counter.test.ts
import { describe, it, expect } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/svelte'
import Counter from '@/components/Counter.svelte'

describe('Counter', () => {
  it('increments count when button clicked', async () => {
    render(Counter)

    const button = screen.getByRole('button')
    await fireEvent.click(button)

    expect(screen.getByText(/1/)).toBeInTheDocument()
  })

  it('renders initial count', () => {
    render(Counter)
    expect(screen.getByText(/0/)).toBeInTheDocument()
  })

  it('calls onUpdate when count changes', async () => {
    const onUpdate = vi.fn()
    render(Counter, { props: { onUpdate } })

    const button = screen.getByRole('button')
    await fireEvent.click(button)

    await waitFor(() => {
      expect(onUpdate).toHaveBeenCalledWith(1)
    })
  })
})
```

### 集成测试

**测试表单**：

```typescript
// LoginForm.test.ts
import { describe, it, expect } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/svelte'
import LoginForm from '@/components/LoginForm.svelte'

describe('LoginForm', () => {
  it('submits form with valid data', async () => {
    const onSubmit = vi.fn()
    render(LoginForm, { props: { onSubmit } })

    const emailInput = screen.getByLabelText(/邮箱/i)
    const passwordInput = screen.getByLabelText(/密码/i)
    const submitButton = screen.getByRole('button', { name: /登录/i })

    await fireEvent.input(emailInput, { target: { value: 'test@example.com' } })
    await fireEvent.input(passwordInput, { target: { value: 'password123' } })
    await fireEvent.click(submitButton)

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123'
      })
    })
  })
})
```

### 测试Store

**测试writable store**：

```typescript
// stores/counter.test.ts
import { describe, it, expect } from 'vitest'
import { get } from 'svelte/store'
import { count } from './counter'

describe('count store', () => {
  it('initializes with 0', () => {
    expect(get(count)).toBe(0)
  })

  it('increments value', () => {
    count.update(n => n + 1)
    expect(get(count)).toBe(1)
  })

  it('sets value', () => {
    count.set(5)
    expect(get(count)).toBe(5)
  })
})
```

### 测试SvelteKit

**测试load函数**：

```typescript
// routes/+page.server.test.ts
import { describe, it, expect, vi } from 'vitest'
import { load } from './+page.server'

describe('blog page load', () => {
  it('loads posts', async () => {
    const mockFetch = vi.fn(() =>
      Promise.resolve({
        json: async () => ({ posts: [] })
      })
    )

    const result = await load({ fetch: mockFetch })

    expect(result).toHaveProperty('posts')
    expect(mockFetch).toHaveBeenCalledWith('/api/posts')
  })
})
```

---

## 📋 最佳实践总结

### 1. 组件通信

- Props down, Events up
- 使用双向绑定简化代码
- 利用插槽实现内容分发
- 避免过度嵌套

### 2. 状态管理

- 小应用使用内置Stores
- 大应用考虑外部状态管理
- 创建可复用的Store函数
- 保持Store的单一职责

### 3. 路由

- 使用文件路由
- 服务端加载优化性能
- 实现路由守卫保护路由
- 编程式导航配合预加载

### 4. 无障碍

- 使用语义化HTML元素
- 添加适当的ARIA属性
- 确保键盘导航可用
- 支持屏幕阅读器

### 5. 测试

- 测试用户行为而非实现
- 使用Testing Library
- 保持测试简单明了
- 测试覆盖关键功能

---

## 🔗 相关文档

- [返回主文档](svelte.md)
- [React最佳实践](./react.md)
- [Vue最佳实践](./vue.md)
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
