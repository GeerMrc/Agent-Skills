# React最佳实践

> ⚛️ **React 18+** - 函数组件和 Hooks

---

## 📖 文档说明

本文档提供 React 18 的完整最佳实践指南，涵盖组件设计、Hooks使用和性能优化等内容。

**目标读者**: React 开发者
**文档长度**: ~260行（主文档）
**阅读时间**: 约15分钟

**相关文档**:
- [完整实现指南](react-guide.md) - Context、表单、测试等详细内容

---

## 🎯 核心概念

React 18 引入并发特性，提供更好的用户体验和性能。本指南涵盖现代React开发的最佳实践。

**核心特性**：
- 函数组件 + Hooks
- 并发渲染（Concurrent Rendering）
- 自动批处理（Automatic Batching）
- Suspense + Transitions
- TypeScript 支持

---

## 🎨 组件设计

### 组件定义

```tsx
// ✅ 推荐：函数组件 + TypeScript
interface ButtonProps {
  children: React.ReactNode
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
  onClick?: () => void
}

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick
}: ButtonProps) {
  const baseStyles = 'rounded font-medium transition-colors'
  const variantStyles = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    ghost: 'bg-transparent text-gray-900 hover:bg-gray-100'
  }
  const sizeStyles = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  }

  return (
    <button
      className={`${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  )
}
```

### 组件命名

```tsx
// ✅ 好的做法：多词组件名、PascalCase
export function UserProfile() {}
export function DataTable() {}
export function SearchInput() {}

// ❌ 避免：单词组件名、camelCase
export function User() {}
export function Table() {}
export function searchInput() {}
```

### Props 最佳实践

```tsx
// ✅ 详细定义 Props
interface CardProps {
  // 必填 props
  title: string
  children: React.ReactNode

  // 可选 props（有默认值）
  variant?: 'elevated' | 'outlined' | 'flat'
  padding?: 'none' | 'sm' | 'md' | 'lg'

  // 事件处理
  onClick?: () => void
  onDelete?: (id: string) => void
}

export function Card({
  title,
  children,
  variant = 'elevated',
  padding = 'md',
  onClick,
  onDelete
}: CardProps) {
  // ...
}
```

---

## 🪝 Hooks 使用

### State 管理

```tsx
import { useState, useReducer } from 'react'

// ✅ 简单状态：useState
function Counter() {
  const [count, setCount] = useState(0)

  const increment = () => setCount(c => c + 1)
  const decrement = () => setCount(c => c - 1)

  return (
    <div>
      <span>{count}</span>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  )
}

// ✅ 复杂状态：useReducer
type State = {
  count: number
  step: number
}

type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStep'; payload: number }
  | { type: 'reset' }

const initialState: State = { count: 0, step: 1 }

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step }
    case 'decrement':
      return { ...state, count: state.count - state.step }
    case 'setStep':
      return { ...state, step: action.payload }
    case 'reset':
      return initialState
    default:
      return state
  }
}

function CounterWithStep() {
  const [state, dispatch] = useReducer(reducer, initialState)

  return (
    <div>
      <span>{state.count}</span>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <input
        type="number"
        value={state.step}
        onChange={e => dispatch({ type: 'setStep', payload: Number(e.target.value) })}
      />
    </div>
  )
}
```

### Effect 使用

```tsx
import { useEffect, useRef } from 'react'

// ✅ 好的做法：明确依赖
function UserProfile({ userId }: { userId: string }) {
  const [data, setData] = useState<UserData | null>(null)

  useEffect(() => {
    let cancelled = false

    async function fetchData() {
      const result = await fetchUser(userId)
      if (!cancelled) {
        setData(result)
      }
    }

    fetchData()

    return () => {
      cancelled = true
    }
  }, [userId]) // 明确依赖 userId

  return data ? <div>{data.name}</div> : <div>Loading...</div>
}

// ✅ 清理副作用
function ResizeListener() {
  useEffect(() => {
    function handleResize() {
      console.log('Window resized')
    }

    window.addEventListener('resize', handleResize)

    // 清理函数
    return () => {
      window.removeEventListener('resize', handleResize)
    }
  }, [])

  return null
}
```

### 自定义 Hooks

```tsx
// ✅ 可复用逻辑：自定义 Hook
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key)
      return item ? JSON.parse(item) : initialValue
    } catch {
      return initialValue
    }
  })

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value
      setStoredValue(valueToStore)
      window.localStorage.setItem(key, JSON.stringify(valueToStore))
    } catch (error) {
      console.error(error)
    }
  }

  return [storedValue, setValue] as const
}

// 使用
function App() {
  const [name, setName] = useLocalStorage('name', '')

  return (
    <input
      type="text"
      value={name}
      onChange={e => setName(e.target.value)}
    />
  )
}
```

---

## 🚀 性能优化

### memo 使用

```tsx
import { memo } from 'react'

// ✅ 避免不必要的重渲染
const ExpensiveComponent = memo(function ExpensiveComponent({
  data,
  onUpdate
}: {
  data: DataType
  onUpdate: (id: string) => void
}) {
  return (
    <div>
      {data.items.map(item => (
        <div key={item.id}>
          {item.name}
          <button onClick={() => onUpdate(item.id)}>Update</button>
        </div>
      ))}
    </div>
  )
})
```

### useCallback 和 useMemo

```tsx
import { useCallback, useMemo } from 'react'

function ParentComponent() {
  const [items, setItems] = useState<Item[]>([])

  // ✅ 缓存回调函数
  const handleDelete = useCallback((id: string) => {
    setItems(prev => prev.filter(item => item.id !== id))
  }, [])

  // ✅ 缓存计算结果
  const total = useMemo(() => {
    return items.reduce((sum, item) => sum + item.value, 0)
  }, [items])

  // ✅ 缓存派生状态
  const sortedItems = useMemo(() => {
    return [...items].sort((a, b) => a.name.localeCompare(b.name))
  }, [items])

  return (
    <div>
      <ChildComponent items={sortedItems} onDelete={handleDelete} />
      <div>Total: {total}</div>
    </div>
  )
}
```

### 代码分割

```tsx
import { lazy, Suspense } from 'react'

// ✅ 路由级别代码分割
const HomePage = lazy(() => import('./pages/HomePage'))
const AboutPage = lazy(() => import('./pages/AboutPage'))
const DashboardPage = lazy(() => import('./pages/DashboardPage'))

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </Suspense>
  )
}
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **Context** | 创建和使用Context | [查看详情](react-guide.md#context使用) |
| **表单** | 受控组件、React Hook Form | [查看详情](react-guide.md#表单处理) |
| **测试** | 单元测试、集成测试 | [查看详情](react-guide.md#测试) |
| **最佳实践** | 常见陷阱、检查清单 | [查看详情](react-guide.md#最佳实践) |

---

## 📋 检查清单

### 组件设计

- [ ] 组件职责单一
- [ ] Props 有明确的 TypeScript 类型
- [ ] 组件名使用 PascalCase 且是多词
- [ ] 避免过度嵌套

### Hooks 使用

- [ ] 遵循 Hooks 规则（只在顶层调用）
- [ ] useEffect 包含所有依赖项
- [ ] 复杂状态使用 useReducer
- [ ] 可复用逻辑提取为自定义 Hook

### 性能优化

- [ ] 大列表使用虚拟化
- [ ] 昂贵计算使用 useMemo
- [ ] 回调函数使用 useCallback
- [ ] 组件适当使用 memo

---

## 💡 最佳实践总结

### 1. 组件化

每个组件职责单一，可复用性强

```tsx
// ✅ 好的做法
export function UserCard({ user }: { user: User }) {
  return <Card>{user.name}</Card>
}
```

### 2. Hooks优先

优先使用 Hooks 而非类组件

```tsx
// ✅ 使用 Hooks
function Component() {
  const [count, setCount] = useState(0)
  return <div>{count}</div>
}

// ❌ 避免：类组件
class Component extends React.Component {
  state = { count: 0 }
  render() { return <div>{this.state.count}</div> }
}
```

### 3. 性能优先

使用 memo、useCallback、useMemo 优化性能

```tsx
const ExpensiveComponent = memo(function ExpensiveComponent({ data }) {
  return <div>{data.name}</div>
})
```

### 4. 类型安全

充分利用 TypeScript

```tsx
interface Props {
  title: string
  count?: number
}

export function Component({ title, count = 0 }: Props) {
  return <div>{title}: {count}</div>
}
```

---

## 🔗 相关文档

- [完整实现指南](react-guide.md) - Context、表单、测试
- [Vue最佳实践](./vue.md)
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
