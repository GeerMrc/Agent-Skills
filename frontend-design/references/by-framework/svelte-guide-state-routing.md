# Svelte 状态管理与路由

> 🧡 **State & Routing** - Store高级用法、SvelteKit路由

---

## 📖 文档说明

本文档提供 Svelte 的状态管理高级用法和 SvelteKit 路由系统详解。

**相关文档**：
- [指南总览](svelte-guide.md) - 组件通信与状态管理基础
- [高级主题](svelte-guide-advanced.md) - 无障碍、测试、最佳实践
- [返回主文档](svelte.md)

---

## 📡 Store高级用法

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

## 🔗 相关文档

- [指南总览](svelte-guide.md) - 组件通信与状态管理基础
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
