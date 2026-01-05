# Styled Components 高级模式

> 💅 **Advanced Patterns** - 主题、CSS重置、测试、性能优化

---

## 📖 文档说明

本文档提供 Styled Components 的高级模式，包括主题系统、CSS重置、测试策略和性能优化。

**相关文档**：
- [指南总览](styled-components-guide.md) - 安装、配置、基础用法
- [返回主文档](styled-components.md)

---

## 🎨 主题系统

### 创建主题

```tsx
// theme.ts
export const theme = {
  colors: {
    primary: '#007bff',
    secondary: '#6c757d',
    danger: '#dc3545',
    success: '#28a745',
    warning: '#ffc107',
    light: '#f8f9fa',
    dark: '#343a40'
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px'
  },
  fonts: {
    body: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    heading: '"Poppins", sans-serif',
    mono: '"Monaco", "Courier New", monospace'
  },
  fontSizes: {
    xs: '12px',
    sm: '14px',
    md: '16px',
    lg: '18px',
    xl: '24px',
    '2xl': '32px'
  },
  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px'
  }
}
```

### 使用主题

```tsx
import styled, { ThemeProvider } from 'styled-components'
import { theme } from './theme'

// App 组件
export const App = () => (
  <ThemeProvider theme={theme}>
    <YourComponent />
  </ThemeProvider>
)

// 在组件中使用主题
const ThemedButton = styled.button`
  background: ${(props) => props.theme.colors.primary};
  padding: ${(props) => props.theme.spacing.md};
  font-size: ${(props) => props.theme.fontSizes.md};
  font-family: ${(props) => props.theme.fonts.body};
`
```

### 主题变体

```tsx
// 亮色主题
const lightTheme = {
  colors: {
    background: '#ffffff',
    text: '#333333',
    primary: '#007bff'
  }
}

// 暗色主题
const darkTheme = {
  colors: {
    background: '#1a1a1a',
    text: '#f0f0f0',
    primary: '#4dabf7'
  }
}

// 使用主题切换
export const App = () => {
  const [isDark, setIsDark] = useState(false)

  return (
    <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
      <button onClick={() => setIsDark(!isDark)}>
        切换主题
      </button>
    </ThemeProvider>
  )
}
```

### 上下文主题

```tsx
// 使用 useTheme Hook
import { useTheme } from 'styled-components'

const MyComponent = () => {
  const theme = useTheme()

  return (
    <div style={{ background: theme.colors.primary }}>
      使用主题颜色
    </div>
  )
}
```

---

## 🔄 CSS重置

### 创建全局样式

```tsx
// global-styles.ts
import { createGlobalStyle } from 'styled-components'

export const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html {
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  body {
    font-family: ${(props) => props.theme.fonts.body};
    line-height: 1.6;
    color: ${(props) => props.theme.colors.text};
    background: ${(props) => props.theme.colors.background};
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: ${(props) => props.theme.fonts.heading};
    line-height: 1.2;
    margin-bottom: ${(props) => props.theme.spacing.md};
  }

  p {
    margin-bottom: ${(props) => props.theme.spacing.md};
  }

  a {
    color: ${(props) => props.theme.colors.primary};
    text-decoration: none;

    &:hover {
      text-decoration: underline;
    }
  }

  button {
    font: inherit;
    cursor: pointer;
  }

  input, textarea {
    font: inherit;
  }
`

// 在 App 中使用
import { GlobalStyle } from './global-styles'

export const App = () => (
  <>
    <GlobalStyle />
    <YourComponent />
  </>
)
```

---

## 🧪 测试

### 单元测试

```tsx
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from './Button'

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>点击我</Button>)
    expect(screen.getByText('点击我')).toBeInTheDocument()
  })

  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>点击</Button>)
    fireEvent.click(screen.getByText('点击'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('applies variant styles', () => {
    const { container } = render(
      <Button $variant="danger">危险按钮</Button>
    )
    const button = container.querySelector('button')
    expect(button).toHaveStyle({ background: 'red' })
  })

  it('is disabled when isLoading', () => {
    const { container } = render(
      <Button $isLoading>加载中</Button>
    )
    const button = container.querySelector('button')
    expect(button).toBeDisabled()
  })
})
```

### 快照测试

```tsx
// Button.snapshot.test.tsx
import { render } from '@testing-library/react'
import { Button } from './Button'

test('Button snapshot', () => {
  const { container } = render(<Button>点击我</Button>)
  expect(container).toMatchSnapshot()
})

test('Button variants snapshot', () => {
  const { container: primary } = render(<Button $variant="primary">主要</Button>)
  const { container: secondary } = render(<Button $variant="secondary">次要</Button>)
  const { container: danger } = render(<Button $variant="danger">危险</Button>)

  expect(primary).toMatchSnapshot()
  expect(secondary).toMatchSnapshot()
  expect(danger).toMatchSnapshot()
})
```

---

## ⚡ 性能优化

### 避免不必要的重渲染

```tsx
// ❌ 避免：每次渲染创建新样式
const BadComponent = ({ isPrimary }: { isPrimary: boolean }) => {
  const Button = styled.button`
    background: ${isPrimary ? 'blue' : 'gray'};
  `
  return <Button>按钮</Button>
}

// ✅ 推荐：使用条件样式
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
`

const GoodComponent = ({ isPrimary }: { isPrimary: boolean }) => {
  return <Button $isPrimary={isPrimary}>按钮</Button>
}
```

### 使用 React.memo

```tsx
import React from 'react'

const ExpensiveComponent = React.memo(({ title }: { title: string }) => {
  return <StyledTitle>{title}</StyledTitle>
})

const StyledTitle = styled.h1`
  color: ${(props) => props.theme.colors.primary};
`
```

### 避免内联样式函数

```tsx
// ❌ 避免：每次渲染创建新函数
const BadButton = styled.button`
  color: ${(props) => props.theme.colors.text};
  background: ${(props) => {
    const color = props.$primary ? props.theme.colors.primary : props.theme.colors.secondary
    return color
  }};
`

// ✅ 推荐：使用预定义值
const GoodButton = styled.button<{ $primary?: boolean }>`
  color: ${(props) => props.theme.colors.text};
  background: ${(props) =>
    props.$primary ? props.theme.colors.primary : props.theme.colors.secondary};
`
```

### 样式复用

```tsx
// 使用 css 辅助函数复用样式
const flexLayout = css`
  display: flex;
  align-items: center;
  justify-content: space-between;
`

const Header = styled.header`
  ${flexLayout}
  padding: ${(props) => props.theme.spacing.md};
`

const Footer = styled.footer`
  ${flexLayout}
  padding: ${(props) => props.theme.spacing.lg};
`
```

---

## 📋 最佳实践总结

### 1. 组件命名

- 使用语义化组件名称
- 遵循命名约定（PascalCase）
- 避免过于简短的名称

```tsx
// ✅ 好的命名
const PrimaryButton = styled.button`...`
const CardHeader = styled.div`...`

// ❌ 避免
const B = styled.button`...`
const CH = styled.div`...`
```

### 2. Props 命名

- 使用 `$` 前缀标识样式 props
- 保持 props 简单直观
- 避免过多 props

```tsx
// ✅ 好的做法
const Button = styled.button<{ $variant?: 'primary' | 'secondary' }>`
  background: ${(props) =>
    props.$variant === 'primary' ? 'blue' : 'gray'};
`

// ❌ 避免
const Button = styled.button<{ variant?: 'primary' | 'secondary' }>`
  background: ${(props) =>
    props.variant === 'primary' ? 'blue' : 'gray'};
`
```

### 3. 样式组织

- 按功能组织样式文件
- 使用主题管理颜色和间距
- 创建可复用的样式组件

```tsx
// styles/index.ts
export * from './buttons'
export * from './cards'
export * from './forms'
export * from './layout'
```

### 4. 类型安全

- 使用 TypeScript 定义 props
- 使用主题类型定义
- 创建类型化的样式组件

```tsx
// theme.types.ts
export interface Theme {
  colors: {
    primary: string
    secondary: string
    danger: string
  }
  spacing: {
    sm: string
    md: string
    lg: string
  }
}

// 组件使用类型
const Button = styled.button<{ $variant?: keyof Theme['colors'] }>`
  background: ${(props) => props.theme.colors[props.$variant || 'primary']};
`
```

### 5. 测试

- 测试组件渲染
- 测试 props 变化
- 使用快照测试
- 测试交互行为

### 6. 可访问性

- 使用语义化 HTML 元素
- 添加适当的 ARIA 属性
- 确保键盘导航
- 支持屏幕阅读器

```tsx
const AccessibleButton = styled.button`
  // 样式...
`

// 使用
<AccessibleButton
  aria-label="关闭对话框"
  aria-pressed={isPressed}
  onClick={handleClose}>
  ×
</AccessibleButton>
```

### 7. 性能

- 避免在渲染中创建样式
- 使用 React.memo 优化
- 复用样式组件
- 使用主题而非内联样式

### 8. 文档

- 添加组件文档
- 使用示例代码
- 说明 props 用法
- 记录主题变量

---

## 🔗 相关文档

- [指南总览](styled-components-guide.md) - 安装、配置、基础用法
- [返回主文档](styled-components.md) - Styled Components总览

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
