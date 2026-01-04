# React 完整实现指南

> ⚛️ **Complete Implementation Guide** - Context、表单、测试

---

## 📖 文档说明

本文档提供 React 的完整实现细节，包括 Context、表单处理、测试和最佳实践等内容。

**相关文档**：
- [返回主文档](react.md)

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

### Context 优化

```tsx
// 拆分 Context 避免不必要的重渲染
const ThemeStateContext = createContext<ThemeState | undefined>(undefined)
const ThemeActionsContext = createContext<ThemeActions | undefined>(undefined)

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light')

  const toggleTheme = useCallback(() => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'))
  }, [])

  return (
    <ThemeStateContext.Provider value={theme}>
      <ThemeActionsContext.Provider value={{ toggleTheme }}>
        {children}
      </ThemeActionsContext.Provider>
    </ThemeStateContext.Provider>
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

### 表单验证

```tsx
import { z } from 'zod'

// 定义验证规则
const userSchema = z.object({
  name: z.string().min(2, 'Name too short'),
  email: z.string().email('Invalid email'),
  age: z.number().min(18, 'Must be 18+'),
  role: z.enum(['user', 'admin'])
})

// 使用验证
function validateUser(data: unknown) {
  return userSchema.safeParse(data)
}

// 异步验证
const asyncSchema = z.object({
  username: z.string().refine(async (username) => {
    const exists = await checkUsernameExists(username)
    return !exists
  }, 'Username already taken')
})
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

### Hook 测试

```tsx
import { renderHook, act } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('increments count', () => {
    const { result } = renderHook(() => useCounter())

    expect(result.current.count).toBe(0)

    act(() => {
      result.current.increment()
    })

    expect(result.current.count).toBe(1)
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

### 性能陷阱

```tsx
// ❌ 陷阱：在渲染中创建新对象/函数
function BadComponent() {
  const items = [{ id: 1, name: 'Item' }] // 每次渲染都是新对象
  return <ChildComponent items={items} />
}

// ✅ 正确做法：使用 useMemo
function GoodComponent() {
  const items = useMemo(() => [{ id: 1, name: 'Item' }], [])
  return <ChildComponent items={items} />
}

// ❌ 陷阱：不稳定的回调引用
function BadComponent() {
  const handleClick = () => { // 每次渲染都是新函数
    console.log('clicked')
  }
  return <ChildComponent onClick={handleClick} />
}

// ✅ 正确做法：使用 useCallback
function GoodComponent() {
  const handleClick = useCallback(() => {
    console.log('clicked')
  }, [])
  return <ChildComponent onClick={handleClick} />
}
```

---

## 📋 最佳实践总结

### 1. 组件设计

- 单一职责原则
- Props 类型明确
- 避免过度嵌套
- 合理拆分组件

### 2. Hooks 使用

- 遵循 Hooks 规则
- useEffect 依赖完整
- 复杂状态用 useReducer
- 提取自定义 Hooks

### 3. 性能优化

- 使用 memo 缓存组件
- 使用 useCallback 缓存回调
- 使用 useMemo 缓存计算
- 代码分割和懒加载

### 4. 测试

- 测试用户行为
- 避免测试实现细节
- 使用 Testing Library
- 保持测试简单

### 5. 类型安全

- 充分利用 TypeScript
- 避免 any 类型
- 定义清晰的接口
- 使用类型推断

---

## 🔗 相关资源

### 官方文档

- [React 官方文档](https://react.dev/)
- [React TypeScript 类型](https://www.typescriptlang.org/docs/handbook/react.html)

### 工具库

- **React Hook Form**: 表单管理
- **TanStack Query**: 服务端状态管理
- **Zustand**: 轻量状态管理
- **Zod**: Schema 验证
- **Vitest**: 单元测试
- **Testing Library**: 组件测试

---

## 🔗 相关文档

- [返回主文档](react.md)
- [Vue最佳实践](./vue.md)
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
