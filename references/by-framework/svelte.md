# Svelte最佳实践

> 🧡 **Svelte 5** - 响应式声明和组件设计

---

## 📖 核心概念

Svelte是编译型框架，在构建时将组件转换为高效的原生JavaScript。无虚拟DOM，运行时开销极小。

**核心特性**：
- 编译时优化（无虚拟DOM）
- 响应式声明（`$:`语法）
- 真正的反应性（ runes）
- 内置状态管理和过渡动画

---

## 🎯 组件设计

### 组件定义（Svelte 5 Runes）

```svelte
<script lang="ts">
  // Props定义
  interface Props {
    title: string
    count?: number
  }

  let { title, count = 0 }: Props = $props()

  // 响应式状态
  let localCount = $state(count)

  // 派生状态
  const isDouble = $derived(localCount > 1)

  // 代码执行（依赖变化时执行）
  $effect(() => {
    console.log('Count changed:', localCount)
  })

  // 方法
  function increment() {
    localCount++
  }
</script>

<div class="counter">
  <h2>{title}</h2>
  <p>Count: {localCount}</p>
  {#if isDouble}
    <p>Double!</p>
  {/if}
  <button on:click={increment}>Increment</button>
</div>

<style>
  .counter {
    padding: var(--spacing-md);
  }
</style>
```

### 组件命名

```svelte
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

```svelte
<script lang="ts">
  // ✅ 使用interface定义Props
  interface Props {
    // 必填props
    title: string
    id: string

    // 可选props（有默认值）
    size?: 'sm' | 'md' | 'lg'
    disabled?: boolean
  }

  let {
    title,
    id,
    size = 'md',
    disabled = false
  }: Props = $props()

  // ✅ Prop验证（通过getter）
  let value = $props()

  $effect(() => {
    if (value <= 0) {
      throw new Error('Value must be positive')
    }
  })
</script>
```

---

## 🔨 响应式系统

### $state（响应式状态）

```svelte
<script lang="ts">
  // 基础类型
  let count = $state(0)
  count++ // 自动触发更新

  // 对象（深度响应式）
  let user = $state({
    name: 'Alice',
    age: 30
  })
  user.name = 'Bob' // 自动触发更新

  // 数组
  let items = $state([1, 2, 3])
  items.push(4) // 自动触发更新
</script>
```

### $derived（派生状态）

```svelte
<script lang="ts">
  let count = $state(0)

  // 派生状态（自动缓存）
  let doubleCount = $derived(count * 2)

  // 复杂派生
  let filteredList = $derived(
    items.filter(item => item.active)
  )
</script>
```

### $effect（副作用）

```svelte
<script lang="ts">
  let count = $state(0)

  // 依赖变化时执行
  $effect(() => {
    console.log('Count changed:', count)
  })

  // 清理副作用
  $effect(() => {
    const timer = setInterval(() => {
      console.log('Tick')
    }, 1000)

    return () => {
      clearInterval(timer) // 清理
    }
  })

  // 多个依赖
  $effect(() => {
    console.log(`${name} is ${age} years old`)
  })
</script>
```

---

## 🎨 样式管理

### Scoped CSS

```svelte
<style>
  /* 自动scoped，无需特殊配置 */
  .container {
    padding: var(--spacing-md);
  }

  .button {
    background: var(--color-primary);
  }

  /* :global() - 全局样式 */
  :global(body) {
    margin: 0;
  }
</style>
```

### 动态类名

```svelte
<script lang="ts">
  let variant = $state('primary')
  let size = $state('md')

  let classes = $derived(
    `button button--${variant} button--${size}`
  )
</script>

<button class={classes}>Click</button>

<!-- 或使用模板字面量 -->
<button class="button button--{variant} button--{size}">
  Click
</button>

<!-- 或使用数组 -->
<button
  class={[
    'button',
    `button--${variant}`,
    `button--${size}`
  ]}
>
  Click
</button>
```

### CSS自定义属性

```svelte
<script lang="ts">
  // 响应式CSS变量
  let color = $state('#3b82f6')
  let size = $state('16px')
</script>

<div
  style="--color: {color}; --size: {size};"
  class="box"
>
  Content
</div>

<style>
  .box {
    background: var(--color);
    font-size: var(--size);
  }
</style>
```

---

## 🚀 性能优化

### 静态内容

```svelte
<!-- 不需要在花括号中 -->
<h1>{title}</h1>

<!-- ✅ 好的做法：静态内容直接写 -->
<h1>Hello World</h1>

<!-- ❌ 避免：不必要的响应式 -->
<h1>{'Hello World'}</h1>
```

### 列表渲染优化

```svelte
<script lang="ts">
  let items = $state([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ])
</script>

<!-- ✅ 使用key优化列表渲染 -->
{#each items as item (item.id)}
  <div>{item.name}</div>
{/each}

<!-- ❌ 避免无key的列表 -->
{#each items as item}
  <div>{item.name}</div>
{/each}
```

### 组件懒加载

```svelte
<script lang="ts">
  import { onMount } from 'svelte'

  let HeavyComponent = $state(null)

  onMount(async () => {
    const module = await import('./HeavyComponent.svelte')
    HeavyComponent = module.default
  })
</script>

{#if HeavyComponent}
  <svelte:component this={HeavyComponent} />
{/if}
```

---

## 🔗 组件通信

### Props down, Events up

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

```svelte
<!-- 父组件 Parent.svelte -->
<script lang="ts">
  import ChildInput from './ChildInput.svelte'

  let text = $state('')
</script>

<ChildInput bind:value={text} />
<p>{text}</p>

<!-- 子组件 ChildInput.svelte -->
<script lang="ts">
  interface Props {
    value: string
  }

  let { value }: Props = $props()
</script>

<input bind:value={value} />
```

### createEventDispatcher（事件派发）

```svelte
<script lang="ts">
  import { createEventDispatcher } from 'svelte'

  const dispatch = createEventDispatcher<{
    click: MouseEvent
    change: { value: string }
  }>()

  function handleClick(event: MouseEvent) {
    dispatch('click', event)
  }

  function handleChange(value: string) {
    dispatch('change', { value })
  }
</script>
```

---

## 📡 状态管理

### Svelte Stores（内置）

```typescript
// stores/counter.ts
import { writable, derived, readable } from 'svelte/store'

// writable（可写store）
export const count = writable(0)

// 读取和更新
import { count } from '@/stores/counter'

count.subscribe(value => console.log(value))
count.set(1)
count.update(n => n + 1)

// derived（派生store）
export const doubleCount = derived(
  count,
  $count => $count * 2
)

// readable（只读store）
export const time = readable(new Date(), set => {
  const interval = setInterval(() => {
    set(new Date())
  }, 1000)
  return () => clearInterval(interval)
)
```

### 自定义Store

```typescript
// stores/useTheme.ts
import { writable } from 'svelte/store'

function createTheme() {
  const { subscribe, set, update } = writable('light')

  return {
    subscribe,
    toggle: () => update(theme =>
      theme === 'light' ? 'dark' : 'light'
    ),
    set
  }
}

export const theme = createTheme()
```

### Store使用

```svelte
<script lang="ts">
  import { count } from '@/stores/counter'

  // 自动订阅（$语法）
  $count = 5

  // 或使用subscribe
  $effect(() => {
    console.log($count)
  })
</script>

<p>Count: {$count}</p>
```

---

## 🛣️ 路由（SvelteKit）

### 文件路由

```
src/routes/
├── +page.svelte          # /
├── about/
│   └── +page.svelte      # /about
├── blog/
│   ├── +page.svelte      # /blog
│   └── [slug]/
│       └── +page.svelte  # /blog/:slug
```

### 页面组件

```svelte
<!-- src/routes/+page.svelte -->
<script lang="ts">
  // 服务端数据加载
  export async function load({ fetch }) {
    const res = await fetch('/api/posts')
    const posts = await res.json()
    return { posts }
  }
</script>

{#each data.posts as post}
  <article>{post.title}</article>
{/each}
```

### 路由导航

```svelte
<script lang="ts">
  import { goto } from '$app/navigation'

  function goToAbout() {
    goto('/about')
  }

  function goBack() {
    history.back()
  }
</script>

<a href="/about">About</a>
<button on:click={goToAbout}>Go to About</button>
```

---

## ♿ 无障碍最佳实践

### 语义化HTML

```svelte
<!-- ✅ 好的做法：语义化元素 -->
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<!-- ❌ 避免：纯div -->
<div class="nav">
  <div class="nav-item" on:click={goHome}>Home</div>
</div>
```

### ARIA属性

```svelte
<button
  aria-pressed={isPressed}
  aria-expanded={isExpanded}
  on:click={toggle}
>
  Toggle
</button>

<div
  role="status"
  aria-busy={isLoading}
  aria-live="polite"
>
  {#if isLoading}
    Loading...
  {:else}
    Done
  {/if}
</div>
```

### 键盘导航

```svelte
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
  Click me or press Enter/Space
</div>
```

---

## 🧪 测试

### 单元测试（Vitest）

```typescript
// Counter.test.ts
import { describe, it, expect } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/svelte'
import Counter from '@/components/Counter.svelte'

describe('Counter', () => {
  it('increments count when button clicked', async () => {
    render(Counter)

    const button = screen.getByRole('button')
    await fireEvent.click(button)

    expect(screen.getByText(/1/)).toBeInTheDocument()
  })
})
```

---

## 📚 相关文档

- [Vue](./vue.md) - Vue最佳实践
- [React](./react.md) - React最佳实践
- [Angular](./angular.md) - Angular最佳实践
- [组件状态覆盖](../implementation/component-states.md) - 组件状态管理

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
