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

## 1. Default（默认状态）

### 视觉描述
组件的常规展示状态，没有用户交互

### 设计规范
```css
.button {
  background: var(--color-primary);
  color: var(--color-text-on-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  border: 1px solid transparent;
  border-radius: var(--radius-md);
  cursor: pointer;
  opacity: 1;
  transition: all var(--duration-fast) var(--ease-out);
}
```

### 无障碍要求
- 颜色对比度 ≥ 4.5:1
- 焦点指示器可见
- 语义化HTML元素

---

## 2. Hover（悬停状态）

### 视觉描述
鼠标悬停在组件上时的状态

### 设计规范
```css
.button:hover {
  background: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}
```

### 交互行为
- 即时响应（< 100ms）
- 平滑过渡动画
- 视觉变化明显但不突兀

### 无障碍要求
- 触摸设备应忽略hover
- 过渡效果不影响运动敏感性用户
- `prefers-reduced-motion` 媒体查询支持

```css
@media (prefers-reduced-motion: reduce) {
  .button:hover {
    transform: none;
    transition: none;
  }
}
```

---

## 3. Active（激活状态）

### 视觉描述
用户点击或按下组件时的状态

### 设计规范
```css
.button:active {
  background: var(--color-primary-active);
  transform: translateY(0) scale(0.98);
  box-shadow: var(--shadow-sm);
}
```

### 交互行为
- 按下时立即触发
- 按钮感觉"被按下"
- 触觉反馈（移动端）

### 无障碍要求
- 键盘 `:active` 伪类生效
- 触摸屏有视觉反馈
- 屏幕阅读器宣布状态变化

---

## 4. Focus（焦点状态）

### 视觉描述
组件获得键盘焦点时的状态

### 设计规范
```css
.button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

/* 鼠标点击时移除焦点环 */
.button:focus:not(:focus-visible) {
  outline: none;
}
```

### 交互行为
- Tab键导航时可见
- 焦点环清晰可辨
- 不遮挡重要内容

### 无障碍要求
- 焦点指示器对比度 ≥ 3:1
- 焦点顺序符合逻辑
- `tabindex` 合理设置

```html
<!-- 可交互元素默认可聚焦 -->
<button>可聚焦按钮</button>

<!-- 不可交互元素需设置tabindex -->
<div tabindex="0" role="button">自定义按钮</div>
```

---

## 5. Disabled（禁用状态）

### 视觉描述
组件不可用时的状态

### 设计规范
```css
.button:disabled,
.button[aria-disabled="true"] {
  background: var(--color-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  opacity: 0.6;
  pointer-events: none;
}
```

### 交互行为
- 不响应鼠标事件
- 不响应键盘事件
- 视觉上明显不可用

### 无障碍要求
- `disabled` 属性或 `aria-disabled="true"`
- 屏幕阅读器宣布"disabled"
- 焦点不应到达禁用元素

```html
<!-- 原生禁用 -->
<button disabled>禁用按钮</button>

<!-- 自定义禁用 -->
<button aria-disabled="true">视觉禁用但可聚焦</button>
```

---

## 6. Loading（加载状态）

### 视觉描述
组件正在处理数据时的状态

### 设计规范
```css
.button.is-loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.button.is-loading::after {
  content: "";
  position: absolute;
  width: 1em;
  height: 1em;
  top: 50%;
  left: 50%;
  margin-left: -0.5em;
  margin-top: -0.5em;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 交互行为
- 显示加载指示器
- 禁用用户交互
- 保持按钮宽度（防止布局抖动）

### 无障碍要求
- `aria-busy="true"` 属性
- 屏幕阅读器宣布"loading"
- 加载完成后宣布结果

```html
<button
  class="button is-loading"
  aria-busy="true"
  aria-live="polite"
>
  <span class="sr-only">加载中...</span>
</button>
```

---

## 7. Empty（空状态）

### 视觉描述
组件没有内容时的状态

### 设计规范
```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
  text-align: center;
  color: var(--color-text-muted);
}

.empty-state-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
  opacity: 0.5;
}

.empty-state-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-sm);
}

.empty-state-description {
  font-size: var(--font-size-sm);
  max-width: 400px;
}
```

### 内容要求
- 清晰的插图或图标
- 描述性标题
- 友好的说明文字
- 明确的操作建议

### 交互行为
- 提供可操作的按钮
- 引导用户到下一步
- 避免让用户感到困惑

### 示例
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon">📭</div>
  <h3 class="empty-state-title">暂无消息</h3>
  <p class="empty-state-description">
    您还没有收到任何消息。当有新消息时，它们会显示在这里。
  </p>
  <button>发送消息</button>
</div>
```

### 无障碍要求
- `role="status"` 或 `aria-live="polite"`
- 图标有 `aria-hidden="true"`
- 操作按钮可访问

---

## 8. Error（错误状态）

### 视觉描述
组件出现错误时的状态

### 设计规范
```css
.input.is-error {
  border-color: var(--color-error);
  background: var(--color-error-bg);
}

.error-message {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--color-error);
  font-size: var(--font-size-sm);
  margin-top: var(--spacing-xs);
}

.error-message::before {
  content: "⚠️";
}
```

### 内容要求
- 明确的错误消息
- 建议的解决方案
- 视觉上明显但不过分
- 错误图标或颜色

### 交互行为
- 错误字段自动聚焦
- 错误消息清晰可见
- 提供修复建议

### 示例
```html
<div class="form-field">
  <label for="email">邮箱地址</label>
  <input
    type="email"
    id="email"
    class="input is-error"
    aria-invalid="true"
    aria-describedby="email-error"
    aria-required="true"
  />
  <div id="email-error" class="error-message" role="alert">
    请输入有效的邮箱地址
  </div>
</div>
```

### 无障碍要求
- `aria-invalid="true"` 属性
- `role="alert"` 或 `aria-live="assertive"`
- 错误消息与控件关联（`aria-describedby`）
- 错误字段自动聚焦

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
/* 基础样式 */
.button {
  /* Default state */
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

/* Reduced motion */
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

---

## 📚 相关文档

- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准
- [响应式设计](./responsive-design.md) - 移动优先设计方法
- [Design Token方法论](../methodology/design-tokens.md) - Token基础概念

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
