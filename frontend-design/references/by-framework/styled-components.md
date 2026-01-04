# Styled Components 指南

> 💅 **Styled Components** - CSS-in-JS 样式解决方案

---

## 📖 文档说明

本文档提供 Styled Components 的完整指南，涵盖基础用法、高级特性、最佳实践等内容。

**目标读者**: React 开发者
**文档长度**: ~180行（主文档）
**阅读时间**: 约10分钟

**相关文档**:
- [完整实现指南](styled-components-guide.md) - 安装、配置、高级用法、测试、性能优化

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

## 🚀 快速开始

### 安装

```bash
# 安装 styled-components
npm install styled-components

# 安装 TypeScript 类型
npm install -D @types/styled-components
```

### 基础用法

```tsx
import styled from 'styled-components';

// 创建样式组件
const Button = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background: blue;
  color: white;
  cursor: pointer;

  &:hover {
    background: darkblue;
  }
`;

// 使用
<Button>点击我</Button>
```

### 动态样式

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
}

const Button = styled.button<ButtonProps>`
  background: ${(props) => {
    switch (props.variant) {
      case 'primary': return 'blue';
      case 'secondary': return 'gray';
      case 'danger': return 'red';
      default: return 'blue';
    }
  }};
  color: white;
`;

// 使用
<Button variant="danger">危险按钮</Button>
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **基础用法** | 创建组件、继承样式、样式化现有组件 | [查看详情](styled-components-guide.md#基础用法) |
| **高级用法** | 动态样式、attrs、条件样式 | [查看详情](styled-components-guide.md#高级用法) |
| **主题支持** | 主题系统、ThemeProvider | [查看详情](styled-components-guide.md#主题支持) |
| **动画** | 关键帧动画、复杂动画 | [查看详情](styled-components-guide.md#动画) |

### 工具和模式

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **组件模式** | 组合样式、原子化组件 | [查看详情](styled-components-guide.md#组件模式) |
| **工具函数** | 响应式工具、样式重置 | [查看详情](styled-components-guide.md#工具函数) |
| **测试** | 单元测试、快照测试 | [查看详情](styled-components-guide.md#测试) |
| **性能优化** | 避免重渲染、transient props | [查看详情](styled-components-guide.md#性能优化) |

---

## 📋 检查清单

### 配置

- [ ] 正确安装依赖
- [ ] TypeScript 类型配置
- [ ] SSR 环境配置（如需要）

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

### 1. 组件化

每个样式组件对应一个 UI 组件

```tsx
// ✅ 好的做法
const Button = styled.button`...`;

// ❌ 避免
const button = styled.button`...`;
```

### 2. 主题化

使用主题系统统一管理样式

```tsx
const Button = styled.button`
  background: ${(props) => props.theme.colors.primary};
`;
```

### 3. 性能优先

避免不必要的重渲染

```tsx
// ✅ 使用 transient props
const Button = styled.button<{ $isPrimary?: boolean }>`
  background: ${(props) => (props.$isPrimary ? 'blue' : 'gray')};
`;
```

### 4. 工具函数

创建可复用的样式工具

```tsx
const media = {
  mobile: (content: TemplateStringsArray) => `
    @media (max-width: 480px) {
      ${content}
    }
  `,
};
```

### 5. 类型安全

充分利用 TypeScript 类型

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'small' | 'medium' | 'large';
}

const Button = styled.button<ButtonProps>`...`;
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

## 🔗 相关资源

### 工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **styled-components** | 官方库 | https://styled-components.com |
| **styled-theming** | 主题增强 | https://github.com/styled-components/styled-theming |
| **polished** | 样式工具函数 | https://polished.js.org |

### 文档

| 资源 | 说明 | 链接 |
|------|------|------|
| Styled Components 文档 | 官方文档 | https://styled-components.com/docs |
| Best Practices | 最佳实践 | https://styled-components.com/docs/basics |
| TypeScript 支持 | 类型使用 | https://styled-components.com/docs/api#typescript |

---

## 🔗 相关文档

- [完整实现指南](styled-components-guide.md)
- [CSS Modules指南](css-modules.md)
- [React最佳实践](react.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
