# React最佳实践

> ⚛️ **React 18+** - 函数组件和 Hooks

---

## 📖 核心概念

React 18 引入并发特性，提供更好的用户体验和性能。本指南涵盖现代React开发的最佳实践。

**核心特性**：
- 函数组件 + Hooks
- 并发渲染（Concurrent Rendering）
- 自动批处理（Automatic Batching）
- Suspense + Transitions
- TypeScript 支持

---

## 🎯 组件设计

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

## 🎨 Context 使用

### 创建 Context

```tsx
import { createContext, useContext, ReactNode } from 'react'

// 定义 Context 类型
interface ThemeContextType {
  theme: 'light' | 'dark'
  toggleTheme: () => void
}

// 创建 Context
const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

// Provider 组件
export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light')

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'))
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

// 自定义 Hook
export function useTheme() {
  const context = useContext(ThemeContext)
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider')
  }
  return context
}
```

### 使用 Context

```tsx
// 在组件中使用
function ThemeButton() {
  const { theme, toggleTheme } = useTheme()

  return (
    <button onClick={toggleTheme}>
      Current theme: {theme}
    </button>
  )
}
```

---

## 📝 表单处理

### 受控组件

```tsx
function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // 提交逻辑
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  )
}
```

### 使用 React Hook Form

```tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const loginSchema = z.object({
  email: z.string().email('Invalid email'),
  password: z.string().min(8, 'Password too short')
})

type LoginForm = z.infer<typeof loginSchema>

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema)
  })

  const onSubmit = (data: LoginForm) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} placeholder="Email" />
      {errors.email && <span>{errors.email.message}</span>}

      <input {...register('password')} type="password" placeholder="Password" />
      {errors.password && <span>{errors.password.message}</span>}

      <button type="submit">Login</button>
    </form>
  )
}
```

---

## 🧪 测试

### 单元测试（Vitest）

```tsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, it, expect } from 'vitest'
import { Button } from './Button'

describe('Button', () => {
  it('renders children', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })

  it('calls onClick when clicked', async () => {
    const user = userEvent.setup()
    const handleClick = vi.fn()

    render(<Button onClick={handleClick}>Click me</Button>)

    await user.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>)
    expect(screen.getByRole('button')).toBeDisabled()
  })
})
```

### 集成测试（Testing Library）

```tsx
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { LoginForm } from './LoginForm'

describe('LoginForm', () => {
  it('submits form with valid data', async () => {
    const onSubmit = vi.fn()
    render(<LoginForm onSubmit={onSubmit} />)

    await user.type(screen.getByLabelText(/email/i), 'test@example.com')
    await user.type(screen.getByLabelText(/password/i), 'password123')
    await user.click(screen.getByRole('button', { name: /login/i }))

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123'
      })
    })
  })
})
```

---

## ⚠️ 常见陷阱

### 避免的陷阱

```tsx
// ❌ 陷阱1：在循环中创建 Hooks
function BadComponent({ items }: { items: string[] }) {
  return (
    <div>
      {items.map(item => {
        const [value, setValue] = useState(item) // ❌ 错误！
        return <div key={item}>{value}</div>
      })}
    </div>
  )
}

// ✅ 正确做法：创建子组件
function Item({ initialValue }: { initialValue: string }) {
  const [value, setValue] = useState(initialValue)
  return <div>{value}</div>
}

function GoodComponent({ items }: { items: string[] }) {
  return (
    <div>
      {items.map(item => (
        <Item key={item} initialValue={item} />
      ))}
    </div>
  )
}

// ❌ 陷阱2：直接修改状态
function BadCounter() {
  const [count, setCount] = useState(0)
  const increment = () => setCount(count + 1) // 可能有问题
  // ...
}

// ✅ 正确做法：使用函数更新
function GoodCounter() {
  const [count, setCount] = useState(0)
  const increment = () => setCount(c => c + 1)
  // ...
}

// ❌ 陷阱3：缺少依赖项
useEffect(() => {
  fetchData(userId)
}, []) // 缺少 userId 依赖

// ✅ 正确做法：包含所有依赖
useEffect(() => {
  fetchData(userId)
}, [userId])
```

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

## 🔗 相关资源

### 官方文档

- [React 官方文档](https://react.dev/)
- [React TypeScript 类型](https://www.typescriptlang.org/docs/handbook/react.html)

### 工具库

- ** React Hook Form**: 表单管理
- ** TanStack Query**: 服务端状态管理
- ** Zustand**: 轻量状态管理
- ** Vitest**: 单元测试

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
