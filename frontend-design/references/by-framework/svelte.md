# Svelte最佳实践

> 🧡 **Svelte 5** - 响应式声明和组件设计

---

## 📖 文档说明

Svelte是编译型框架，在构建时将组件转换为高效的原生JavaScript。本指南涵盖核心概念、组件设计、响应式系统和性能优化等内容。

**目标读者**: Svelte开发者
**文档长度**: ~260行（主文档）
**阅读时间**: 约15分钟

**相关文档**:
- [完整实现指南](svelte-guide.md) - 组件通信、状态管理、路由、无障碍、测试

---

## 🎯 核心概念

**核心特性**：
- 编译时优化（无虚拟DOM）
- 响应式声明（`$:`语法）
- 真正的反应性（runes）
- 内置状态管理和过渡动画

Svelte在编译时生成高效的原生JavaScript代码，无需运行时虚拟DOM开销。

---

## 🎨 组件设计

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

<!-- 使用派生类名 -->
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

## 📋 最佳实践

### 组件化

每个组件职责单一，可复用性强

```svelte
<!-- ✅ 好的做法 -->
<UserCard {user} />

<!-- ❌ 避免：大而全的组件 -->
<UserProfileWithPostsAndComments />
```

### 响应式优先

优先使用响应式声明而非手动更新

```svelte
<script lang="ts">
  // ✅ 使用$derived
  let count = $state(0)
  let double = $derived(count * 2)

  // ❌ 避免：手动更新
  let double = 0
  $effect(() => {
    double = count * 2
  })
</script>
```

### 样式隔离

使用scoped CSS避免样式冲突

```svelte
<style>
  /* ✅ 自动scoped */
  .button {
    padding: 8px;
  }
</style>
```

---

## ⚠️ 常见陷阱

### 避免的陷阱

```svelte
<!-- ❌ 陷阱1：在模板中执行复杂逻辑 -->
<div>{items.filter(item => item.active).map(item => item.name).join(', ')}</div>

<!-- ✅ 正确做法：使用$derived -->
<script lang="ts">
  let activeNames = $derived(
    items.filter(item => item.active).map(item => item.name).join(', ')
  )
</script>
<div>{activeNames}</div>

<!-- ❌ 陷阱2：直接修改数组/对象 -->
<script lang="ts">
  let items = $state([1, 2, 3])

  // 可能不触发更新
  items[0] = 4
</script>

<!-- ✅ 正确做法：赋值整个数组 -->
<script lang="ts">
  let items = $state([1, 2, 3])

  items = [4, ...items.slice(1)]
</script>

<!-- ❌ 陷阱3：忘记清理副作用 -->
<script lang="ts">
  $effect(() => {
    const timer = setInterval(() => {}, 1000)
    // 忘记清理
  })
</script>

<!-- ✅ 正确做法：返回清理函数 -->
<script lang="ts">
  $effect(() => {
    const timer = setInterval(() => {}, 1000)
    return () => clearInterval(timer)
  })
</script>
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **组件通信** | Props down, Events up、双向绑定 | [查看详情](svelte-guide.md#组件通信) |
| **状态管理** | Svelte Stores、自定义Store | [查看详情](svelte-guide.md#状态管理) |
| **路由** | SvelteKit文件路由、导航 | [查看详情](svelte-guide.md#路由) |
| **无障碍** | 语义化、ARIA、键盘导航 | [查看详情](svelte-guide.md#无障碍) |
| **测试** | Vitest、Testing Library | [查看详情](svelte-guide.md#测试) |

---

## 📋 检查清单

### 组件设计

- [ ] 组件职责单一
- [ ] Props有明确的TypeScript类型
- [ ] 组件名使用多词形式
- [ ] 避免过度嵌套

### 响应式系统

- [ ] 正确使用$state定义响应式状态
- [ ] 使用$derived定义派生状态
- [ ] $effect包含清理函数
- [ ] 避免在模板中执行复杂逻辑

### 性能优化

- [ ] 列表渲染使用key
- [ ] 静态内容不使用响应式
- [ ] 大组件使用懒加载
- [ ] 避免不必要的重新渲染

---

## 🔗 相关资源

### 官方文档

- [Svelte官方文档](https://svelte.dev/docs)
- [SvelteKit文档](https://kit.svelte.dev/docs)

### 工具

- **Svelte for VS Code**: 官方VSCode插件
- **Svelte DevTools**: 浏览器调试工具

---

## 🔗 相关文档

- [完整实现指南](svelte-guide.md) - 组件通信、状态管理、路由、无障碍、测试
- [React最佳实践](./react.md)
- [Vue最佳实践](./vue.md)
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
