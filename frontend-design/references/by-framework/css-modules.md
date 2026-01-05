# CSS Modules 指南

> 🎨 **CSS Modules** - 局部作用域的 CSS 解决方案

---

## 📖 文档说明

本文档提供 CSS Modules 的完整指南，涵盖配置、使用、最佳实践等内容。

**目标读者**: React/Vue 开发者

**相关文档**：
- [高级主题](css-modules-advanced.md) - 预处理器、主题、性能、测试、迁移
- [返回框架文档](../README.md)

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

## 🔗 相关文档

- [高级主题](css-modules-advanced.md) - 预处理器、主题、性能、测试、迁移
- [返回框架文档](../README.md)
- [返回references/](../README.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
