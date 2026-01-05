# Svelte 指南总览

> 🧡 **Quick Start** - 组件通信、状态管理基础

---

## 📖 文档说明

本文档提供 Svelte 的快速入门指南，包括组件通信和状态管理基础。

**相关文档**：
- [状态管理与路由](svelte-guide-state-routing.md) - 状态管理和SvelteKit路由
- [高级主题](svelte-guide-advanced.md) - 无障碍、测试、最佳实践
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

---

## 🔗 相关文档

- [状态管理与路由](svelte-guide-state-routing.md) - 状态管理和SvelteKit路由详解
- [高级主题](svelte-guide-advanced.md) - 无障碍、测试和最佳实践
- [返回主文档](svelte.md) - Svelte总览

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
