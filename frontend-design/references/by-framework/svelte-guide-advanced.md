# Svelte 高级主题

> 🧡 **Advanced Topics** - 无障碍、测试、最佳实践

---

## 📖 文档说明

本文档提供 Svelte 的高级主题，包括无障碍最佳实践、测试策略和最佳实践总结。

**相关文档**：
- [指南总览](svelte-guide.md) - 组件通信与状态管理基础
- [状态管理与路由](svelte-guide-state-routing.md) - Store高级用法、SvelteKit路由
- [返回主文档](svelte.md)

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

- [指南总览](svelte-guide.md) - 组件通信与状态管理基础
- [状态管理与路由](svelte-guide-state-routing.md) - Store高级用法、SvelteKit路由
- [返回主文档](svelte.md) - Svelte总览
- [无障碍指南](../implementation/accessibility.md) - WCAG AA标准

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
