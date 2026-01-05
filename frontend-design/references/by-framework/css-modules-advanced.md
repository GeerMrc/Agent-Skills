# CSS Modules 高级主题

> 🎨 **Advanced CSS Modules** - 主题、性能、测试、迁移

---

## 📖 文档说明

本文档提供 CSS Modules 的高级主题，包括主题支持、性能优化、测试策略和迁移指南。

**目标读者**: React/Vue 开发者

**相关文档**：
- [基础指南](css-modules.md) - 核心概念、配置、基础用法
- [返回框架文档](../README.md)

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

## 🔗 相关文档

- [基础指南](css-modules.md) - 核心概念、配置、基础用法
- [返回框架文档](../README.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
