# CSS Modules 指南

> 🎨 **CSS Modules** - 局部作用域的 CSS 解决方案

---

## 📖 文档说明

本文档提供 CSS Modules 的完整指南，涵盖配置、使用、最佳实践等内容。

**目标读者**: React/Vue 开发者
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 CSS Modules 核心概念

### 什么是 CSS Modules

CSS Modules 是一种 CSS 作用域解决方案，通过自动生成唯一的类名来避免样式冲突。

```css
/* Button.module.css */
.button {
  background: blue;
  color: white;
}
```

```tsx
// 编译后自动生成
import styles from './Button.module.css';

// <button class="Button_button__abc123">点击</button>
<button className={styles.button}>点击</button>
```

### 优势

| 优势 | 说明 |
|------|------|
| **局部作用域** | 样式只在组件内生效 |
| **避免冲突** | 自动生成唯一类名 |
| **清晰依赖** | 明确样式依赖关系 |
| **易于维护** | 组件样式独立管理 |

---

## ⚙️ 配置

### Vite 配置

```javascript
// vite.config.ts
export default {
  css: {
    modules: {
      localsConvention: 'camelCase', // 转换为驼峰命名
      scopeBehaviour: 'local',       // 局部作用域
      generateScopedName: '[name]__[local]___[hash:base64:5]',
    },
  },
};
```

### Webpack 配置

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.module\.css$/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: {
                localIdentName: '[name]__[local]___[hash:base64:5]',
                exportLocalsConvention: 'camelCase',
              },
            },
          },
        ],
      },
    ],
  },
};
```

### TypeScript 类型支持

```typescript
// css-modules.d.ts
declare module '*.module.css' {
  const classes: { [key: string]: string };
  export default classes;
}

declare module '*.module.scss' {
  const classes: { [key: string]: string };
  export default classes;
}
```

---

## 🚀 基础使用

### 创建 CSS Module

```css
/* Card.module.css */
.card {
  background: white;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.header {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
}

.content {
  color: #666;
  line-height: 1.6;
}
```

### 在组件中使用

```tsx
// Card.tsx
import styles from './Card.module.css';

export function Card({ title, children }: CardProps) {
  return (
    <div className={styles.card}>
      <h3 className={styles.header}>{title}</h3>
      <p className={styles.content}>{children}</p>
    </div>
  );
}
```

---

## 🎨 高级用法

### 组合类名

```css
/* Button.module.css */
.button {
  padding: 8px 16px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.primary {
  background: blue;
  color: white;
}

.secondary {
  background: gray;
  color: white;
}

.large {
  padding: 12px 24px;
  font-size: 18px;
}
```

```tsx
// Button.tsx
import styles from './Button.module.css';
import { cn } from '../utils/cn';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'normal' | 'large';
  children: React.ReactNode;
}

export function Button({
  variant = 'primary',
  size = 'normal',
  children,
}: ButtonProps) {
  return (
    <button
      className={cn(
        styles.button,
        styles[variant],
        styles[size]
      )}
    >
      {children}
    </button>
  );
}
```

### 动态类名

```tsx
// 使用 clsx 或 classnames 库
import { cn } from '../utils/cn';

<div className={cn(
  styles.card,
  isActive && styles.active,
  isDisabled && styles.disabled
)} />
```

### 全局样式

```css
/* globals.css - 不使用 .module 后缀 */
:global(.global-class) {
  color: red;
}

/* 或在 module 文件中使用 :global */
:global(.reset) {
  margin: 0;
  padding: 0;
}
```

---

## 🔗 预处理器集成

### Sass/SCSS 支持

```scss
/* Card.module.scss */
.card {
  background: white;
  border-radius: $border-radius;
  padding: $spacing-md;

  &:hover {
    box-shadow: $shadow-lg;
  }

  &.primary {
    border-color: $primary-color;
  }
}
```

### Less 支持

```less
/* Card.module.less */
@import 'variables.less';

.card {
  background: @white;
  border-radius: @border-radius;
  padding: @spacing-md;
}
```

---

## 🎭 主题支持

### CSS 变量主题

```css
/* themes.css */
:root {
  --primary-color: blue;
  --text-color: #333;
  --bg-color: white;
}

[data-theme='dark'] {
  --primary-color: #4a9eff;
  --text-color: #f0f0f0;
  --bg-color: #1a1a1a;
}
```

```css
/* Button.module.css */
.button {
  background: var(--primary-color);
  color: var(--text-color);
}
```

### 主题切换

```tsx
// ThemeProvider.tsx
import { createContext, useContext } from 'react';

const ThemeContext = createContext('light');

export function ThemeProvider({ children, theme = 'light' }) {
  return (
    <ThemeContext.Provider value={theme}>
      <div data-theme={theme}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}
```

---

## 🧩 组件模式

### 原子化 CSS Modules

```css
/* atoms.module.css */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-4 { gap: 1rem; }
.p-4 { padding: 1rem; }
```

```tsx
// 组合使用
<div className={`${styles.flex} ${styles.itemsCenter} ${styles.gap4}`}>
  内容
</div>
```

### 组件级样式

```css
/* UserCard.module.css */
.card {
  composes: flex p-4 from './atoms.module.css';
  background: white;
  border-radius: 8px;
}
```

---

## ⚡ 性能优化

### 按需加载

```tsx
// 懒加载组件样式
const HeavyComponent = React.lazy(() =>
  import('./HeavyComponent').then(m => ({
    default: m.HeavyComponent,
  }))
);
```

### 样式提取

```javascript
// 生产环境提取 CSS
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [
      {
        test: /\.module\.css$/,
        use: [
          process.env.NODE_ENV === 'production'
            ? MiniCssExtractPlugin.loader
            : 'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: true,
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
    }),
  ],
};
```

---

## 🧪 测试

### 单元测试

```tsx
// Card.test.tsx
import { render, screen } from '@testing-library/react';
import { Card } from './Card';

describe('Card', () => {
  it('applies correct styles', () => {
    const { container } = render(
      <Card title="测试标题">测试内容</Card>
    );

    const card = container.querySelector('.card');
    expect(card).toHaveClass(/card/);
  });
});
```

### 快照测试

```tsx
// Card.snapshot.test.tsx
import { render } from '@testing-library/react';
import { Card } from './Card';

test('Card snapshot', () => {
  const { container } = render(
    <Card title="测试标题">测试内容</Card>
  );
  expect(container).toMatchSnapshot();
});
```

---

## 📋 最佳实践

### 命名规范

```css
/* ✅ 好的做法：BEM 风格 */
.card { }
.card__header { }
.card__content { }
.card--primary { }

/* ✅ 好的做法：驼峰命名 */
.card { }
.cardHeader { }
.cardContent { }
.cardPrimary { }
```

### 文件组织

```
components/
├── Button/
│   ├── Button.tsx
│   ├── Button.module.css
│   └── Button.test.tsx
├── Card/
│   ├── Card.tsx
│   ├── Card.module.css
│   └── Card.test.tsx
└── index.ts
```

### 避免深层嵌套

```css
/* ❌ 避免 */
.card {
  .header {
    .title {
      .text {
        color: red;
      }
    }
  }
}

/* ✅ 推荐 */
.card {
  background: white;
}
.cardTitle {
  color: red;
}
```

---

## 🔄 迁移指南

### 从普通 CSS 迁移

```css
/* 重命名文件 */
button.css → button.module.css
```

```tsx
// 更新导入
// import './button.css';
import styles from './button.module.css';

// 更新类名
// <button className="button">点击</button>
<button className={styles.button}>点击</button>
```

### 从 CSS-in-JS 迁移

```tsx
// 从 styled-components
const Button = styled.button`
  background: blue;
  color: white;
`;

// 到 CSS Modules
// Button.module.css
.button {
  background: blue;
  color: white;
}

// Button.tsx
import styles from './Button.module.css';
const Button = (props) => (
  <button className={styles.button} {...props} />
);
```

---

## 📋 检查清单

### 配置

- [ ] 构建工具正确配置
- [ ] TypeScript 类型支持
- [ ] 命名规范统一

### 使用

- [ ] 组件样式独立管理
- [ ] 避免全局样式污染
- [ ] 正确处理动态类名

### 性能

- [ ] 按需加载组件
- [ ] 生产环境提取 CSS
- [ ] 避免过度嵌套

---

## 💡 最佳实践总结

1. **组件隔离**：每个组件独立样式文件
2. **命名规范**：使用 BEM 或驼峰命名
3. **避免全局**：默认使用局部作用域
4. **工具函数**：使用 cn/clsx 组合类名
5. **类型安全**：提供 TypeScript 类型支持

---

## 🔗 相关资源

### 工具

- ** clsx**: 条件类名工具
- ** classnames**: 类名组合库
- ** React CSS Modules**: React 绑定库

### 文档

- [CSS Modules 规范](https://github.com/css-modules/css-modules)
- [Webpack CSS Loader](https://webpack.js.org/loaders/css-loader/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
