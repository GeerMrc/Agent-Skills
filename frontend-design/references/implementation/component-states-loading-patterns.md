# Loading状态 - 基础加载模式

> ⚙️ **Basic Loading Patterns** - 旋转圆环、进度条

---

## 📖 文档说明

本文档提供 2 种基础加载模式的完整实现代码和详细说明。

**相关文档**：
- [高级加载模式](component-states-loading-advanced.md) - 骨架屏、覆盖层、实用技巧
- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)

---

## 📋 基础加载模式

### 1. 旋转圆环（Spinner）

**适用场景**：
- 按钮、小组件加载
- 不确定加载时间
- 空间有限的场景

**优点**：
- 轻量级，实现简单
- 通用性强，用户熟悉
- 不占用过多空间

**缺点**：
- 不显示具体进度
- 长时间加载让用户焦虑

#### 完整实现

**CSS**：
```css
.spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 响应式尺寸 */
.spinner--sm { width: 16px; height: 16px; }
.spinner--md { width: 20px; height: 20px; }
.spinner--lg { width: 32px; height: 32px; }
.spinner--xl { width: 48px; height: 48px; }

/* 尊重用户动画偏好 */
@media (prefers-reduced-motion: reduce) {
  .spinner {
    animation: none;
    border-top-color: transparent;
    border-right-color: transparent;
    border-bottom-color: transparent;
  }
}
```

**HTML**：
```html
<button class="button is-loading"
        aria-busy="true"
        aria-live="polite">
  <span class="spinner" aria-hidden="true"></span>
  <span class="sr-only">加载中...</span>
  <span>保存</span>
</button>
```

**React 实现**：
```tsx
function LoadingButton({ isLoading, children, ...props }) {
  return (
    <button
      {...props}
      disabled={isLoading}
      aria-busy={isLoading}
      aria-live="polite"
    >
      {isLoading && (
        <span className="spinner" aria-hidden="true" />
      )}
      {isLoading && <span className="sr-only">加载中...</span>}
      <span>{children}</span>
    </button>
  );
}
```

**Vue 实现**：
```vue
<template>
  <button
    :disabled="loading"
    :aria-busy="loading"
    aria-live="polite"
  >
    <span v-if="loading" class="spinner" aria-hidden="true" />
    <span v-if="loading" class="sr-only">加载中...</span>
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps<{ loading: boolean }>();
</script>
```

---

### 2. 进度条（Progress Bar）

**适用场景**：
- 多步骤流程
- 文件上传
- 可计算进度的加载
- 明确时间范围的加载

**优点**：
- 显示具体进度
- 减少用户焦虑
- 提供完成时间预估

**缺点**：
- 需要准确的进度信息
- 占用额外空间

#### 完整实现

**CSS**：
```css
.progress {
  position: relative;
  height: 4px;
  background: var(--color-border);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress__bar {
  height: 100%;
  background: var(--color-primary);
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}

/* 尺寸变体 */
.progress--sm { height: 2px; }
.progress--md { height: 4px; }
.progress--lg { height: 8px; }

/* 颜色变体 */
.progress--success .progress__bar {
  background: var(--color-success);
}

.progress--warning .progress__bar {
  background: var(--color-warning);
}

.progress--error .progress__bar {
  background: var(--color-error);
}

/* 条纹动画 */
.progress__bar--striped {
  background-image: linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.15) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.15) 50%,
    rgba(255, 255, 255, 0.15) 75%,
    transparent 75%,
    transparent
  );
  background-size: 1rem 1rem;
  animation: progress-stripes 1s linear infinite;
}

@keyframes progress-stripes {
  from { background-position: 1rem 0; }
  to { background-position: 0 0; }
}
```

**HTML**：
```html
<div
  class="progress"
  role="progressbar"
  aria-valuenow="60"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-label="加载进度"
>
  <div class="progress__bar" style="width: 60%"></div>
</div>

<div class="sr-only">已加载 60%</div>
```

**React 实现**：
```tsx
function ProgressBar({ value = 0, max = 100, label }) {
  const percentage = Math.min(Math.max((value / max) * 100, 0), 100);

  return (
    <div
      className="progress"
      role="progressbar"
      aria-valuenow={value}
      aria-valuemin={0}
      aria-valuemax={max}
      aria-label={label}
    >
      <div
        className="progress__bar"
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
}
```

**Vue 实现**：
```vue
<template>
  <div
    class="progress"
    role="progressbar"
    :aria-valuenow="value"
    aria-valuemin="0"
    :aria-valuemax="max"
    :aria-label="label"
  >
    <div
      class="progress__bar"
      :style="{ width: `${percentage}%` }"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  value: number;
  max?: number;
  label?: string;
}>();

const percentage = computed(() => {
  return Math.min(Math.max((props.value / (props.max || 100)) * 100, 0), 100);
});
</script>
```

#### 进度状态文本

**HTML**：
```html
<div class="progress-group">
  <div class="progress-group__header">
    <span class="progress-group__label">上传文件</span>
    <span class="progress-group__value">60%</span>
  </div>
  <div class="progress" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">
    <div class="progress__bar" style="width: 60%"></div>
  </div>
  <span class="progress-group__helper">正在上传...</span>
</div>
```

**CSS**：
```css
.progress-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.progress-group__header {
  display: flex;
  justify-content: space-between;
  font-size: var(--font-size-sm);
}

.progress-group__label {
  font-weight: var(--font-weight-medium);
}

.progress-group__value {
  color: var(--color-text-muted);
}

.progress-group__helper {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
}
```

---

## 🔗 相关文档

- [高级加载模式](component-states-loading-advanced.md) - 骨架屏、覆盖层、实用技巧
- [返回主文档](component-states-loading.md)
- [视觉描述与交互设计](component-states-loading-visual.md)

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
