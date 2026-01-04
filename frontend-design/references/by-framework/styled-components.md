# Styled Components 指南

> 💅 **Styled Components** - CSS-in-JS 样式解决方案

---

## 📖 文档说明

本文档提供 Styled Components 的完整指南，涵盖基础用法、高级特性、最佳实践等内容。

**目标读者**: React 开发者
**文档长度**: 约290行
**阅读时间**: 约16分钟

---

## 🎯 Styled Components 核心概念

### 什么是 Styled Components

Styled Components 是一个 CSS-in-JS 库，允许在 JavaScript 中编写组件样式，自动生成唯一类名。

```tsx
import styled from 'styled-components';

const Button = styled.button`
  background: blue;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

// 使用
<Button>点击我</Button>
```

### 优势

| 优势 | 说明 |
|------|------|
| **自动作用域** | 样式自动隔离，避免冲突 |
| **动态样式** | 基于 props 动态改变样式 |
| **主题支持** | 内置主题系统 |
| **无需 CSS 文件** | 样式和组件在一起 |

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

### SSR 配置

```tsx
// _document.tsx (Next.js)
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
`;

// 使用
<Button>点击我</Button>
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
`;

// 继承并扩展
const PrimaryButton = styled(Button)`
  background: blue;
  color: white;
`;

const SecondaryButton = styled(Button)`
  background: gray;
  color: white;
`;
```

---

## 🎭 高级用法

### 基于 Props 的动态样式

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
}

const Button = styled.button<ButtonProps>`
  padding: ${(props) => {
    switch (props.size) {
      case 'small': return '4px 8px';
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
`;

// 使用
<Button variant="primary" size="large">点击我</Button>
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
  }
`;
```

### 条件样式

```tsx
import { css, StyledProp } from 'styled-components';

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

// 使用动画
const FadeInDiv = styled.div`
  animation: ${fadeIn} 0.3s ease-in;
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

const Modal = styled.div`
  animation: ${slideInUp} 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
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

// 使用
<Card>
  <CardHeader>标题</CardHeader>
  <CardContent>内容</CardContent>
</Card>
```

### 原子化组件

```tsx
const Flex = styled.div<{ direction?: 'row' | 'column'; gap?: string }>`
  display: flex;
  flex-direction: ${(props) => props.direction || 'row'};
  gap: ${(props) => props.gap || '0'};
`;

const Container = styled.div<{ maxWidth?: string }>`
  max-width: ${(props) => props.maxWidth || '1200px'};
  margin: 0 auto;
  padding: 0 16px;
`;

// 使用
<Flex direction="column" gap="16px">
  内容
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

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: #333;
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
import { render, screen } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>点击我</Button>);
    expect(screen.getByText('点击我')).toBeInTheDocument();
  });

  it('applies variant styles', () => {
    const { container } = render(
      <Button variant="danger">危险按钮</Button>
    );
    const button = container.querySelector('button');
    expect(button).toHaveStyle({ background: 'red' });
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
```

---

## ⚡ 性能优化

### 避免不必要的重渲染

```tsx
// ❌ 避免：每次创建新样式
const BadComponent = ({ isPrimary }) => {
  const Button = styled.button`
    background: ${isPrimary ? 'blue' : 'gray'};
  `;
  return <Button>按钮</Button>;
};

// ✅ 推荐：使用条件样式
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
`;

const GoodComponent = ({ isPrimary }) => {
  return <Button $isPrimary={isPrimary}>按钮</Button>;
};
```

### 使用 transient props

```tsx
// 使用 $ 前缀标记不应传递给 DOM 的 props
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
`;

// $isPrimary 不会传递给 <button> 元素
<Button $isPrimary={true}>按钮</Button>
```

---

## 📋 最佳实践

### 命名规范

```tsx
// ✅ 好的做法：大写开头的组件名
const Button = styled.button``;
const CardHeader = styled.div``;

// ❌ 避免：小写开头
const button = styled.button``;
const cardHeader = styled.div``;
```

### 样式组织

```tsx
// ✅ 好的做法：相关样式放一起
const Card = styled.div`
  background: white;
  border-radius: 8px;
  padding: 16px;

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

---

## 🔄 迁移指南

### 从 CSS 迁移

```css
/* Button.css */
.button {
  background: blue;
  color: white;
}
```

```tsx
// 到 styled-components
const Button = styled.button`
  background: blue;
  color: white;
`;
```

### 从 CSS Modules 迁移

```tsx
// CSS Modules
import styles from './Button.module.css';
<button className={styles.button}>按钮</button>;

// 到 styled-components
const Button = styled.button``;
<Button>按钮</Button>;
```

---

## 📋 检查清单

### 配置

- [ ] 正确安装依赖
- [ ] TypeScript 类型配置
- [ ] SSR 环境配置

### 使用

- [ ] 使用组件命名规范
- [ ] 正确处理动态样式
- [ ] 使用 transient props
- [ ] 避免过度嵌套

### 性能

- [ ] 避免创建新样式组件
- [ ] 使用主题缓存
- [ ] 测试渲染性能

---

## 💡 最佳实践总结

1. **组件化**：每个样式组件对应一个 UI 组件
2. **主题化**：使用主题系统统一管理样式
3. **性能优先**：避免不必要的重渲染
4. **工具函数**：创建可复用的样式工具
5. **类型安全**：充分利用 TypeScript 类型

---

## 🔗 相关资源

### 工具

- ** styled-components**: 官方库
- ** styled-theming**: 主题增强库
- ** polished**: 样式工具函数

### 文档

- [Styled Components 文档](https://styled-components.com/)
- [Best Practices](https://styled-components.com/docs/basics)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
