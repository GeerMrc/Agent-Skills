# Design Token 方法论

> 🎨 **设计令牌系统** - 设计系统的基础构件

---

## 📖 核心概念

Design Token是设计系统的基础构件，它将设计决策（颜色、间距、字体等）转换为可命名的变量。这些Token可以在设计和代码中共享使用，确保一致性和可维护性。

**核心价值**：
- 一致性：确保整个产品使用相同的设计值
- 可维护性：一处修改，处处更新
- 跨平台：设计工具和代码使用相同的Token
- 可扩展性：轻松添加新的设计变量

---

## 🎯 Token分类

### 1. 语义Token vs 原始Token

**原始Token（Primitive Tokens）**：
- 基础设计值，不依赖上下文
- 示例：`$color-red-500`, `$spacing-4`, `$font-size-base`

**语义Token（Semantic Tokens）**：
- 描述用途，不描述具体值
- 示例：`$color-primary`, `$spacing-medium`, `$font-size-body`

### 2. Token类别

| 类别 | 说明 | 示例 |
|------|------|------|
| **颜色（Color）** | 品牌、UI、语义颜色 | `color-primary`, `color-success` |
| **间距（Spacing）** | padding, margin, gap | `spacing-1` ~ `spacing-12` |
| **字体（Typography）** | 字体家族、大小、行高 | `font-size-base`, `line-height-normal` |
| **阴影（Shadow）** | 阴影效果 | `shadow-sm`, `shadow-md`, `shadow-lg` |
| **圆角（Border Radius）** | 边框圆角 | `radius-sm`, `radius-md`, `radius-full` |
| **断点（Breakpoints）** | 响应式断点 | `breakpoint-sm`, `breakpoint-md` |
| **动画（Animation）** | 过渡和动画 | `duration-fast`, `ease-in-out` |

---

## 📐 命名规范

### 推荐命名方式

**使用语义化命名**：
```
✅ color-primary
✅ spacing-medium
✅ font-size-body

❌ color-blue-500
❌ spacing-16px
❌ font-size-16
```

**命名结构**：
```
[类别]-[概念]-[变体]
```

**示例**：
- `color-primary` - 主色
- `color-primary-hover` - 主色悬停态
- `spacing-content-horizontal` - 内容水平间距
- `font-size-heading-large` - 大标题字号

---

## 🎨 色彩系统

### OKLCH色彩空间（推荐）

**优势**：
- 感知均匀性
- 更好的插值效果
- 更大的色彩范围

```css
:root {
  --color-primary: oklch(0.7 0.15 250);
  --color-secondary: oklch(0.65 0.12 180);
}
```

### 主题管理

```css
/* Light Theme */
:root {
  --color-bg: oklch(0.98 0 0);
  --color-text: oklch(0.2 0 0);
}

/* Dark Theme */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: oklch(0.15 0 0);
    --color-text: oklch(0.95 0 0);
  }
}
```

---

## 💻 实现示例

### CSS自定义属性

```css
:root {
  /* 颜色 */
  --color-primary: oklch(0.7 0.15 250);
  --color-secondary: oklch(0.65 0.12 180);

  /* 间距 */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;

  /* 字体 */
  --font-size-base: 1rem;
  --line-height-normal: 1.5;
}

/* 使用 */
.button {
  background: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: var(--font-size-base);
}
```

### JavaScript/TypeScript

```typescript
// tokens.ts
export const designTokens = {
  color: {
    primary: 'oklch(0.7 0.15 250)',
    secondary: 'oklch(0.65 0.12 180)',
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
  },
};

// 使用
const buttonStyle = {
  background: designTokens.color.primary,
  padding: `${designTokens.spacing.sm} ${designTokens.spacing.md}`,
};
```

---

## 📚 相关文档

- [令牌工作流](./token-workflow.md) - Token开发流程
- [系统化方法](./systematic-approach.md) - 完整设计系统
- [色彩理论](../aesthetics/color-theory.md) - 色彩理论

---

## 🔗 快速导航

- [返回methodology/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ⏳ IN_PROGRESS (框架已完成，待完善详细内容)
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
