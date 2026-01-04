# 组件状态覆盖指南

> 🎨 **8种状态完整覆盖** - 确保组件交互完整性

---

## 📖 核心概念

组件状态是用户与界面交互的核心。完整的状态覆盖确保：
- 用户行为得到及时反馈
- 界面状态清晰可辨
- 无障碍访问不受影响
- 交互体验流畅自然

**8种核心状态**：
1. **default** - 默认状态
2. **hover** - 悬停状态
3. **active** - 激活状态
4. **focus** - 焦点状态
5. **disabled** - 禁用状态
6. **loading** - 加载状态
7. **empty** - 空状态
8. **error** - 错误状态

---

## 📋 状态快速参考

### 交互状态（4种）

| 状态 | 触发时机 | 视觉变化 | 无障碍要求 |
|------|----------|----------|------------|
| **default** | 常规展示 | 基础样式 | 对比度≥4.5:1，语义化HTML |
| **hover** | 鼠标悬停 | 颜色加深/阴影 | 触摸设备忽略，支持reduced-motion |
| **active** | 点击按下 | 缩小/阴影减少 | 键盘生效，屏幕阅读器通知 |
| **focus** | Tab聚焦 | 焦点环 | 焦点环对比度≥3:1，顺序合理 |

**详细说明**: [交互状态详解](./component-states-interactive.md)

### 功能状态（4种）

| 状态 | 触发时机 | 视觉变化 | 无障碍要求 |
|------|----------|----------|------------|
| **disabled** | 不可用 | 降低透明度/灰化 | disabled属性或aria-disabled |
| **loading** | 处理中 | 加载动画 | aria-busy="true"，屏幕阅读器通知 |
| **empty** | 无内容 | 空状态插图/文字 | role="status"，提供操作建议 |
| **error** | 出错 | 红色边框/错误图标 | aria-invalid，role="alert" |

**详细说明**: [功能状态详解](./component-states-functional.md)

---

## 🎯 状态设计原则

### 1. 视觉一致性
- 同一状态在不同组件中保持一致
- 使用Design Token定义状态变量
- 遵循品牌设计规范

### 2. 交互反馈及时性
- hover: < 100ms响应
- active: 即时触发
- focus: 清晰可见
- 状态过渡: 200-300ms

### 3. 无障碍优先
- 所有状态支持键盘导航
- 屏幕阅读器可识别状态变化
- 颜色对比度符合WCAG AA标准
- 支持 `prefers-reduced-motion`

### 4. 渐进增强
- 基础功能不依赖JavaScript
- 高级交互平滑降级
- 移动端触摸友好

---

## 🔄 React实现示例

### 完整组件实现

```tsx
import { designTokens } from '@/tokens';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      className={clsx('button', `button--${variant}`, `button--${size}`, {
        'is-disabled': disabled,
        'is-loading': loading,
      })}
      disabled={disabled || loading}
      aria-disabled={disabled}
      aria-busy={loading}
      onClick={onClick}
    >
      {loading && <span className="sr-only">加载中...</span>}
      <span>{children}</span>
    </button>
  );
}
```

### 样式实现

```css
/* 基础样式 - Default state */
.button {
  background: var(--color-primary);
  border: 1px solid transparent;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
}

/* Hover state */
.button:hover:not(:disabled):not(.is-loading) {
  background: var(--color-primary-hover);
  transform: translateY(-1px);
}

/* Active state */
.button:active:not(:disabled):not(.is-loading) {
  background: var(--color-primary-active);
  transform: translateY(0) scale(0.98);
}

/* Focus state */
.button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

/* Disabled state */
.button:disabled,
.button.is-disabled {
  background: var(--color-disabled);
  cursor: not-allowed;
  opacity: 0.6;
  pointer-events: none;
}

/* Loading state */
.button.is-loading {
  position: relative;
  color: transparent;
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .button:hover {
    transform: none;
  }
  .button:active {
    transform: none;
  }
}
```

---

## ✅ 状态检查清单

### 交互状态
- [ ] Default状态设计清晰
- [ ] Hover状态反馈及时
- [ ] Active状态有按压感
- [ ] Focus状态焦点环清晰

### 功能状态
- [ ] Disabled状态不可交互
- [ ] Loading状态有指示器
- [ ] Empty状态有引导
- [ ] Error状态有说明

### 无障碍检查
- [ ] 所有状态支持键盘导航
- [ ] 屏幕阅读器能识别状态
- [ ] 颜色对比度符合标准
- [ ] 支持 `prefers-reduced-motion`

### 代码质量
- [ ] 使用Design Token变量
- [ ] 状态过渡平滑自然
- [ ] 无JavaScript依赖时可用
- [ ] 移动端触摸友好

---

## 📚 相关文档

### 详细状态指南
- [交互状态详解](./component-states-interactive.md) - Default、Hover、Active、Focus完整指南
- [功能状态详解](./component-states-functional.md) - Disabled、Loading、Empty、Error完整指南

### 相关设计文档
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准 ⏳ 计划中
- [响应式设计](./responsive-design.md) - 移动优先设计方法 ⏳ 计划中
- [Design Token方法论](../methodology/design-tokens.md) - Token基础概念
- [质量检查清单](../quality/checklist.md) - 完整质量验证流程

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (文档重构：拆分为3份)
> **维护者**: 项目团队
