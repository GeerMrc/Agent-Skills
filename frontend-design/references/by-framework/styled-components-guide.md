# Styled Components 指南总览

> 💅 **Core Guide** - 安装、配置、基础用法、组件模式

---

## 📖 文档说明

本文档提供 Styled Components 的核心指南，包括安装配置、基础用法和常用组件模式。

**相关文档**：
- [高级模式](styled-components-guide-advanced.md) - 主题、测试、性能优化
- [返回主文档](styled-components.md)

---

## 🚀 安装和配置

### 安装

```bash
# 安装 styled-components
npm install styled-components

# 安装 TypeScript 类型
npm install -D @types/styled-components
```

### TypeScript 配置

```json
// tsconfig.json
{
  "compilerOptions": {
    "types": ["styled-components"]
  }
}
```

### SSR 配置 (Next.js)

```tsx
// pages/_document.tsx
import { ServerStyleSheet } from 'styled-components'

export default function Document() {
  return (
    <Html>
      <Head />
      <body />
    </Html>
  )
}

Document.getInitialProps = async (ctx) => {
  const sheet = new ServerStyleSheet()
  const originalRenderPage = ctx.renderPage

  try {
    ctx.renderPage = () =>
      originalRenderPage({
        enhanceApp: (App) => (props) =>
          sheet.collectStyles(<App {...props} />)
      })

    const initialProps = await Document.getInitialProps(ctx)
    return {
      ...initialProps,
      styles: (
        <>
          {initialProps.styles}
          <style dangerouslySetInnerHTML={{ __html: sheet.getStyleTags() }} />
        </>
      )
    }
  } finally {
    sheet.seal()
  }
}
```

---

## 🎨 基础用法

### 创建样式组件

```tsx
import styled from 'styled-components'

// 基础按钮
const Button = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background: blue;
  color: white;
  cursor: pointer;
  transition: background 0.2s;

  &:hover {
    background: darkblue;
  }

  &:active {
    transform: scale(0.98);
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`
```

### Props 样式

```tsx
// 基于 props 的动态样式
const Button = styled.button<{ $variant?: 'primary' | 'secondary' | 'danger' }>`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: ${(props) => {
    switch (props.$variant) {
      case 'primary':
        return 'blue'
      case 'secondary':
        return 'gray'
      case 'danger':
        return 'red'
      default:
        return 'blue'
    }
  }};
  color: white;
`

// 使用
<Button $variant="primary">主要按钮</Button>
<Button $variant="danger">危险按钮</Button>
```

### 样式继承

```tsx
// 基础组件
const BaseButton = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: blue;
  color: white;
`

// 继承并扩展
const PrimaryButton = styled(BaseButton)`
  background: #007bff;

  &:hover {
    background: #0056b3;
  }
`

const SecondaryButton = styled(BaseButton)`
  background: #6c757d;

  &:hover {
    background: #545b62;
  }
`
```

### 样式组合

```tsx
// 使用 css 工具函数
import styled, { css } from 'styled-components'

const buttonStyles = css`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
`

const primaryStyles = css`
  background: blue;
  color: white;

  &:hover {
    background: darkblue;
  }
`

const Button = styled.button`
  ${buttonStyles}
  ${primaryStyles}
`
```

### 条件样式

```tsx
const Button = styled.button<{
  $isPrimary?: boolean
  $isDisabled?: boolean
  $size?: 'small' | 'medium' | 'large'
}>`
  padding: ${(props) => {
    switch (props.$size) {
      case 'small':
        return '4px 8px'
      case 'large':
        return '12px 24px'
      default:
        return '8px 16px'
    }
  }};

  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
  opacity: ${(props) => (props.$isDisabled ? 0.6 : 1)};
  cursor: ${(props) => (props.$isDisabled ? 'not-allowed' : 'pointer')};
`
```

---

## 🎭 动画

### Keyframes

```tsx
import styled, { keyframes } from 'styled-components'

// 定义动画
const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`

const slideIn = keyframes`
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
`

// 使用动画
const FadeInDiv = styled.div`
  animation: ${fadeIn} 0.3s ease-in;
`

const SlideInMenu = styled.nav`
  animation: ${slideIn} 0.3s ease-out;
`
```

### 复杂动画

```tsx
const slideInUp = keyframes`
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
`

const bounceIn = keyframes`
  0% {
    transform: scale(0.3);
    opacity: 0;
  }
  50% {
    transform: scale(1.05);
  }
  70% {
    transform: scale(0.9);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
`

const Modal = styled.div`
  animation: ${slideInUp} 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
`

const BouncyButton = styled.button`
  animation: ${bounceIn} 0.5s ease-out;
`
```

---

## 🧩 组件模式

### 组合样式组件

```tsx
const Card = styled.div`
  background: white;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`

const CardHeader = styled.div`
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
`

const CardContent = styled.div`
  color: #666;
  line-height: 1.6;
`

const CardFooter = styled.div`
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  display: flex;
  gap: 8px;
  justify-content: flex-end;
`

// 使用
<Card>
  <CardHeader>标题</CardHeader>
  <CardContent>内容</CardContent>
  <CardFooter>
    <Button $variant="secondary">取消</Button>
    <Button>确认</Button>
  </CardFooter>
</Card>
```

### 原子化组件

```tsx
const Flex = styled.div<{ $direction?: 'row' | 'column'; $gap?: string }>`
  display: flex;
  flex-direction: ${(props) => props.$direction || 'row'};
  gap: ${(props) => props.$gap || '0'};
`

const Grid = styled.div<{ $columns?: number; $gap?: string }>`
  display: grid;
  grid-template-columns: repeat(${(props) => props.$columns || 1}, 1fr);
  gap: ${(props) => props.$gap || '0'};
`

const Container = styled.div<{ $maxWidth?: string; $padding?: string }>`
  max-width: ${(props) => props.$maxWidth || '1200px'};
  padding: ${(props) => props.$padding || '0 16px'};
  margin: 0 auto;
`

// 使用
<Flex $direction="column" $gap="16px">
  <Card>卡片1</Card>
  <Card>卡片2</Card>
</Flex>
```

### 样式化现有组件

```tsx
import { Link } from 'react-router-dom'

// 样式化第三方组件
const StyledLink = styled(Link)`
  color: blue;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }
`

// 样式化自定义组件
interface ButtonProps {
  $variant?: 'primary' | 'secondary'
}

const MyButton = ({ className, children }: { className?: string; children: React.ReactNode }) => (
  <button className={className}>{children}</button>
)

const StyledButton = styled(MyButton)<ButtonProps>`
  background: ${(props) => (props.$variant === 'primary' ? 'blue' : 'gray')};
  color: white;
`
```

### 属性传递

```tsx
// 使用 shouldForwardProops 控制属性传递
const Input = styled.input.withConfig({
  shouldForwardProp: (prop) => prop !== '$fullWidth'
})<{ $fullWidth?: boolean }>`
  width: ${(props) => (props.$fullWidth ? '100%' : 'auto')};
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
`
```

---

## 🔗 相关文档

- [高级模式](styled-components-guide-advanced.md) - 主题、测试、性能优化
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
