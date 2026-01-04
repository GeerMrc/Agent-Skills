# Styled Components 完整实现指南

> 💅 **Complete Implementation Guide** - 安装、配置、高级用法、测试、性能优化

---

## 📖 文档说明

本文档提供 Styled Components 的完整实现细节，包括所有配置选项、高级功能和最佳实践。

**相关文档**：
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
// _document.tsx
import { ServerStyleSheet } from 'styled-components';

export default function Document() {
  return (
    <Html>
      <Head />
      <body />
    </Html>
  );
}

Document.getInitialProps = async (ctx) => {
  const sheet = new ServerStyleSheet();
  const originalRenderPage = ctx.renderPage;

  try {
    ctx.renderPage = () =>
      originalRenderPage({
        enhanceApp: (App) => (props) =>
          sheet.collectStyles(<App {...props} />),
      });

    const initialProps = await Document.getInitialProps(ctx);
    return {
      ...initialProps,
      styles: (
        <>
          {initialProps.styles}
          <style dangerouslySetInnerHTML={{ __html: sheet.getStyleTags() }} />
        </>
      ),
    };
  } finally {
    sheet.seal();
  }
};
```

---

## 🎨 基础用法

### 创建样式组件

```tsx
import styled from 'styled-components';

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
    opacity: 0.5;
    cursor: not-allowed;
  }
`;
```

### 样式化现有组件

```tsx
import { Link } from 'react-router-dom';

// 样式化路由链接
const StyledLink = styled(Link)`
  color: blue;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }

  &:visited {
    color: purple;
  }
`;
```

### 继承样式

```tsx
// 基础按钮
const Button = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
`;

// 继承并扩展
const PrimaryButton = styled(Button)`
  background: blue;
  color: white;

  &:hover {
    background: darkblue;
  }
`;

const SecondaryButton = styled(Button)`
  background: gray;
  color: white;

  &:hover {
    background: darkgray;
  }
`;

const DangerButton = styled(Button)`
  background: red;
  color: white;

  &:hover {
    background: darkred;
  }
`;
```

---

## 🎭 高级用法

### 基于 Props 的动态样式

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  fullWidth?: boolean;
}

const Button = styled.button<ButtonProps>`
  padding: ${(props) => {
    switch (props.size) {
      case 'small': return '4px 8px';
      case 'medium': return '8px 16px';
      case 'large': return '12px 24px';
      default: return '8px 16px';
    }
  }};

  background: ${(props) => {
    switch (props.variant) {
      case 'primary': return 'blue';
      case 'secondary': return 'gray';
      case 'danger': return 'red';
      default: return 'blue';
    }
  }};

  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: ${(props) => (props.fullWidth ? '100%' : 'auto')};

  &:hover {
    opacity: 0.9;
  }
`;

// 使用
<Button variant="danger" size="large" fullWidth>
  点击我
</Button>
```

### 使用 attrs 添加属性

```tsx
const Input = styled.input.attrs({
  type: 'text',
  placeholder: '请输入...',
})`
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;

  &:focus {
    outline: none;
    border-color: blue;
    box-shadow: 0 0 0 2px rgba(0, 0, 255, 0.1);
  }

  &::placeholder {
    color: #999;
  }
`;

// 带动态 attrs
const PasswordInput = styled.input.attrs<{ type?: 'text' | 'password' }>(
  (props) => ({
    type: props.type || 'password',
    placeholder: '请输入密码...',
  })
)`
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;
```

### 条件样式

```tsx
import { css } from 'styled-components';

const modifierStyles = {
  primary: css`
    background: blue;
    color: white;
  `,
  secondary: css`
    background: gray;
    color: white;
  `,
  danger: css`
    background: red;
    color: white;
  `,
};

const Button = styled.button<{ variant?: keyof typeof modifierStyles }>`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  ${(props) => modifierStyles[props.variant || 'primary']}
`;
```

---

## 🌐 主题支持

### 创建主题

```tsx
// theme.ts
export const theme = {
  colors: {
    primary: 'blue',
    secondary: 'gray',
    danger: 'red',
    text: '#333',
    background: '#fff',
  },
  spacing: {
    small: '8px',
    medium: '16px',
    large: '24px',
  },
  breakpoints: {
    mobile: '480px',
    tablet: '768px',
    desktop: '1024px',
  },
  fonts: {
    body: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    heading: 'Georgia, serif',
  },
};
```

### 主题提供者

```tsx
import { ThemeProvider } from 'styled-components';
import { theme } from './theme';

export function App({ children }) {
  return (
    <ThemeProvider theme={theme}>
      {children}
    </ThemeProvider>
  );
}

// 多主题支持
const darkTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    background: '#1a1a1a',
    text: '#fff',
  },
};

export function ThemedApp({ children, isDark }) {
  return (
    <ThemeProvider theme={isDark ? darkTheme : theme}>
      {children}
    </ThemeProvider>
  );
}
```

### 使用主题

```tsx
const Button = styled.button`
  background: ${(props) => props.theme.colors.primary};
  color: ${(props) => props.theme.colors.text};
  padding: ${(props) => props.theme.spacing.medium};

  @media (max-width: ${(props) => props.theme.breakpoints.mobile}) {
    padding: ${(props) => props.theme.spacing.small};
  }
`;
```

---

## 🎪 动画

### 关键帧动画

```tsx
import styled, { keyframes } from 'styled-components';

// 定义动画
const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const slideIn = keyframes`
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
`;

// 使用动画
const FadeInDiv = styled.div`
  animation: ${fadeIn} 0.3s ease-in;
`;

const SlideInMenu = styled.nav`
  animation: ${slideIn} 0.3s ease-out;
`;
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
`;

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
`;

const Modal = styled.div`
  animation: ${slideInUp} 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
`;

const BouncyButton = styled.button`
  animation: ${bounceIn} 0.5s ease-out;
`;
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
`;

const CardHeader = styled.div`
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
`;

const CardContent = styled.div`
  color: #666;
  line-height: 1.6;
`;

const CardFooter = styled.div`
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  display: flex;
  gap: 8px;
  justify-content: flex-end;
`;

// 使用
<Card>
  <CardHeader>标题</CardHeader>
  <CardContent>内容</CardContent>
  <CardFooter>
    <Button variant="secondary">取消</Button>
    <Button>确认</Button>
  </CardFooter>
</Card>
```

### 原子化组件

```tsx
const Flex = styled.div<{ direction?: 'row' | 'column'; gap?: string }>`
  display: flex;
  flex-direction: ${(props) => props.direction || 'row'};
  gap: ${(props) => props.gap || '0'};
`;

const Grid = styled.div<{ cols?: number; gap?: string }>`
  display: grid;
  grid-template-columns: repeat(${(props) => props.cols || 3}, 1fr);
  gap: ${(props) => props.gap || '16px'};
`;

const Container = styled.div<{ maxWidth?: string }>`
  max-width: ${(props) => props.maxWidth || '1200px'};
  margin: 0 auto;
  padding: 0 16px;
`;

// 使用
<Flex direction="column" gap="16px">
  <Container maxWidth="800px">
    <Grid cols={3} gap="24px">
      {/* 内容 */}
    </Grid>
  </Container>
</Flex>
```

---

## 🔧 工具函数

### 响应式工具

```tsx
// breakpoints.ts
export const breakpoints = {
  mobile: '480px',
  tablet: '768px',
  desktop: '1024px',
};

export const media = {
  mobile: (content: TemplateStringsArray) => `
    @media (max-width: ${breakpoints.mobile}) {
      ${content}
    }
  `,
  tablet: (content: TemplateStringsArray) => `
    @media (min-width: ${breakpoints.tablet}) {
      ${content}
    }
  `,
  desktop: (content: TemplateStringsArray) => `
    @media (min-width: ${breakpoints.desktop}) {
      ${content}
    }
  `,
};

// 使用
const Container = styled.div`
  padding: 16px;

  ${media.tablet`
    padding: 24px;
  `}

  ${media.desktop`
    padding: 32px;
  `}
`;
```

### 样式重置

```tsx
import { createGlobalStyle } from 'styled-components';

export const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html {
    font-size: 16px;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: #333;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  button {
    font: inherit;
    cursor: pointer;
  }

  input, textarea {
    font: inherit;
  }
`;

// 在 App 中使用
<GlobalStyle />
```

---

## 🧪 测试

### 单元测试

```tsx
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>点击我</Button>);
    expect(screen.getByText('点击我')).toBeInTheDocument();
  });

  it('calls onClick when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>点击</Button>);
    fireEvent.click(screen.getByText('点击'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('applies variant styles', () => {
    const { container } = render(
      <Button variant="danger">危险按钮</Button>
    );
    const button = container.querySelector('button');
    expect(button).toHaveStyle({ background: 'red' });
  });

  it('is disabled when isLoading', () => {
    const { container } = render(
      <Button isLoading>加载中</Button>
    );
    const button = container.querySelector('button');
    expect(button).toBeDisabled();
  });
});
```

### 快照测试

```tsx
// Button.snapshot.test.tsx
import { render } from '@testing-library/react';
import { Button } from './Button';

test('Button snapshot', () => {
  const { container } = render(<Button>点击我</Button>);
  expect(container).toMatchSnapshot();
});

test('Button variants snapshot', () => {
  const { container: primary } = render(<Button variant="primary">主要</Button>);
  const { container: secondary } = render(<Button variant="secondary">次要</Button>);
  const { container: danger } = render(<Button variant="danger">危险</Button>);

  expect(primary).toMatchSnapshot();
  expect(secondary).toMatchSnapshot();
  expect(danger).toMatchSnapshot();
});
```

---

## ⚡ 性能优化

### 避免不必要的重渲染

```tsx
// ❌ 避免：每次渲染创建新样式
const BadComponent = ({ isPrimary }: { isPrimary: boolean }) => {
  const Button = styled.button`
    background: ${isPrimary ? 'blue' : 'gray'};
  `;
  return <Button>按钮</Button>;
};

// ✅ 推荐：使用条件样式
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
`;

const GoodComponent = ({ isPrimary }: { isPrimary: boolean }) => {
  return <Button $isPrimary={isPrimary}>按钮</Button>;
};
```

### 使用 transient props

```tsx
// 使用 $ 前缀标记不应传递给 DOM 的 props
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
  color: white;
`;

// $isPrimary 不会传递给 <button> 元素
<Button $isPrimary={true}>按钮</Button>
```

### 避免内联样式函数

```tsx
// ❌ 避免：复杂的内联函数
const Button = styled.button`
  color: ${(props) => {
    const result = calculateColor(props);
    return result;
  }};
`;

// ✅ 推荐：使用简单的样式映射
const colorMap = {
  primary: 'blue',
  secondary: 'gray',
  danger: 'red',
};

const Button = styled.button<{ variant?: keyof typeof colorMap }>`
  color: ${(props) => colorMap[props.variant || 'primary']};
`;
```

---

## 📋 最佳实践

### 命名规范

```tsx
// ✅ 好的做法：大写开头的组件名
const Button = styled.button``;
const CardHeader = styled.div``;
const Navigation = styled.nav``;

// ❌ 避免：小写开头
const button = styled.button``;
const cardHeader = styled.div``;
```

### 样式组织

```tsx
// ✅ 好的做法：相关样式放一起
const Card = styled.div<{ $elevated?: boolean }>`
  background: white;
  border-radius: 8px;
  padding: 16px;
  box-shadow: ${(props) => (props.$elevated ? '0 4px 12px rgba(0, 0, 0, 0.15)' : 'none')};

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
`;

// ❌ 避免：过度嵌套
const Card = styled.div`
  .header {
    .title {
      .text {
        color: red;
      }
    }
  }
}
```

### 避免样式重复

```tsx
// ❌ 避免：重复样式
const Button = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

const Input = styled.input`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

// ✅ 推荐：使用基础组件或 mixin
const baseStyles = css`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

const Button = styled.button`
  ${baseStyles}
  background: blue;
`;

const Input = styled.input`
  ${baseStyles}
  border: 1px solid #ccc;
`;
```

---

## 🔗 相关文档

- [返回主文档](styled-components.md)
- [CSS Modules指南](css-modules.md)
- [React最佳实践](react.md)

---

> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
