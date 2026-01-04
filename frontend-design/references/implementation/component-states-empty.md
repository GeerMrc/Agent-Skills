# Empty状态详解

> 📭 **空状态** - 数据缺失时的友好提示和引导规范

---

## 📖 状态概述

Empty（空状态）是组件/区域没有内容时的友好提示，引导用户进行下一步操作。

**适用场景**：
- 列表/表格无数据
- 搜索无结果
- 筛选后无匹配项
- 用户首次使用

**核心价值**：
- 友好的用户体验
- 明确的操作引导
- 减少用户困惑
- 提升产品亲和力

---

## 📭 Empty状态详解

### 视觉设计

**设计规范**：
```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
  text-align: center;
  color: var(--color-text-muted);
  min-height: 300px;
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
  color: var(--color-text);
}

.empty-state-description {
  font-size: var(--font-size-sm);
  max-width: 400px;
  line-height: 1.5;
  margin-bottom: var(--spacing-md);
}

.empty-state-action {
  margin-top: var(--spacing-sm);
}
```

**设计要点**：
1. **插图/图标**：大尺寸（3-4rem），降低透明度
2. **标题**：描述性文字，告知用户当前状态
3. **说明**：友好的解释文字，告知原因
4. **操作建议**：明确的CTA按钮或链接

### 内容要求

**完整结构**：
- 清晰的插图或图标（📭、📂、🔍等）
- 描述性标题（"暂无消息"、"没有找到结果"）
- 友好的说明文字（解释原因或提供帮助）
- 明确的操作建议（"发送消息"、"清除筛选"）

**内容示例**：
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">📭</div>
  <h3 class="empty-state-title">暂无消息</h3>
  <p class="empty-state-description">
    您还没有收到任何消息。当有新消息时，它们会显示在这里。
  </p>
  <div class="empty-state-action">
    <button>发送消息</button>
  </div>
</div>
```

### 空状态类型

| 类型 | 场景 | 标题示例 | 操作建议 |
|------|------|----------|----------|
| **首次使用** | 新用户，无数据 | "开始创建您的第一个项目" | "创建项目" |
| **清空状态** | 用户删除所有内容 | "列表已清空" | "添加新项目" |
| **搜索无结果** | 搜索/筛选后无匹配 | "没有找到结果" | "清除筛选" |
| **权限不足** | 无权限查看内容 | "您没有权限访问此内容" | "联系管理员" |
| **网络错误** | 加载失败 | "加载失败" | "重试" |
| **功能未开放** | 功能未上线 | "功能即将上线" | "了解更多" |

### 交互行为

- 提供可操作的按钮
- 引导用户到下一步
- 避免让用户感到困惑
- 保持界面布局稳定

### 无障碍要求

**关键ARIA属性**：
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">📭</div>
  <h3 class="empty-state-title">暂无消息</h3>
  <p class="empty-state-description">
    您还没有收到任何消息。
  </p>
  <div class="empty-state-action">
    <button>发送消息</button>
  </div>
</div>
```

- `role="status"` 或 `aria-live="polite"`：通知屏幕阅读器
- `aria-hidden="true"`：装饰性图标隐藏
- 操作按钮标准无障碍：确保可访问
- 语义化HTML：使用 `<h3>`、`<p>` 等标签

### Empty状态示例

**示例1：首次使用空状态**
```html
<div class="empty-state" role="status">
  <svg class="empty-state-icon" aria-hidden="true">
    <!-- 插图SVG -->
  </svg>
  <h3 class="empty-state-title">开始您的第一个项目</h3>
  <p class="empty-state-description">
    项目是组织您工作的好方法。创建第一个项目，开始您的工作之旅。
  </p>
  <div class="empty-state-action">
    <button type="button">创建项目</button>
  </div>
</div>
```

**示例2：搜索无结果**
```html
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">🔍</div>
  <h3 class="empty-state-title">没有找到结果</h3>
  <p class="empty-state-description">
    没有找到与"<span id="search-term">关键词</span>"匹配的结果。
  </p>
  <div class="empty-state-action">
    <button type="button">清除筛选</button>
    <button type="button" variant="secondary">查看全部内容</button>
  </div>
</div>
```

**示例3：网络错误空状态**
```html
<div class="empty-state" role="alert">
  <div class="empty-state-icon" aria-hidden="true">⚠️</div>
  <h3 class="empty-state-title">加载失败</h3>
  <p class="empty-state-description">
    网络连接出现问题，无法加载内容。
  </p>
  <div class="empty-state-action">
    <button type="button">重试</button>
  </div>
</div>
```

---

## 🎯 Empty状态最佳实践

### 设计原则

**1. 友好性**
- 使用鼓励性语言
- 提供明确的解决方案
- 避免技术术语

**2. 引导性**
- 明确告知用户当前状态
- 提供下一步操作建议
- 降低认知负担

**3. 一致性**
- 统一的视觉风格
- 统一的文案语气
- 统一的交互模式

### 文案建议

| 场景 | 好的文案 | 避免的文案 |
|------|----------|------------|
| 首次使用 | "开始创建您的第一个项目" | "无数据" |
| 搜索无结果 | "没有找到结果，试试其他关键词" | "搜索为空" |
| 清空状态 | "列表已清空，添加新项目开始" | "没有内容" |
| 权限不足 | "您没有权限访问此内容" | "403错误" |

### 视觉设计建议

**图标选择**：
- 📭 消息/邮件类空状态
- 📂 文件/文件夹类空状态
- 🔍 搜索类空状态
- 🛒 购物车类空状态
- 📊 数据类空状态
- ⚠️ 警告/错误类空状态

**色彩建议**：
- 使用中性色彩（灰色系）
- 图标透明度 50-70%
- 保持品牌色彩在操作按钮上

**布局建议**：
- 居中对齐
- 充足的垂直间距（至少60px）
- 插图尺寸：64-128px
- 标题字号：18-24px
- 说明字号：14-16px

---

## ⚠️ 常见错误

### ❌ 避免

**1. 只显示"无数据"**
- 没有解释原因
- 没有操作建议
- 用户不知道下一步做什么

**2. 使用技术术语**
- "404 Not Found"
- "Null result"
- "Empty array"

**3. 没有视觉吸引力**
- 纯文字，无图标
- 布局混乱
- 色彩单调

**4. 没有操作引导**
- 用户无法继续操作
- 没有CTA按钮
- 返回路径不清晰

### ✅ 推荐

**1. 完整的空状态结构**
- 插图 + 标题 + 说明 + 操作
- 友好的用户语言
- 明确的操作建议

**2. 场景化设计**
- 根据不同场景定制内容
- 使用相关插图
- 提供针对性的操作

**3. 保持一致性**
- 统一的视觉风格
- 统一的文案语气
- 统一的交互模式

**4. 提供多种操作**
- 主要操作（主按钮）
- 次要操作（次按钮）
- 返回操作（取消/返回）

---

## 📊 实现示例

### React实现

```tsx
interface EmptyStateProps {
  icon?: React.ReactNode;
  title: string;
  description?: string;
  action?: React.ReactNode;
  role?: 'status' | 'alert';
}

export function EmptyState({
  icon,
  title,
  description,
  action,
  role = 'status'
}: EmptyStateProps) {
  return (
    <div className="empty-state" role={role}>
      {icon && (
        <div className="empty-state-icon" aria-hidden="true">
          {icon}
        </div>
      )}
      <h3 className="empty-state-title">{title}</h3>
      {description && (
        <p className="empty-state-description">{description}</p>
      )}
      {action && (
        <div className="empty-state-action">{action}</div>
      )}
    </div>
  );
}

// 使用示例
<EmptyState
  icon={<MailIcon />}
  title="暂无消息"
  description="您还没有收到任何消息。当有新消息时，它们会显示在这里。"
  action={<Button>发送消息</Button>}
/>
```

### Vue实现

```vue
<template>
  <div class="empty-state" :role="role">
    <div v-if="icon" class="empty-state-icon" aria-hidden="true">
      <component :is="icon" />
    </div>
    <h3 class="empty-state-title">{{ title }}</h3>
    <p v-if="description" class="empty-state-description">
      {{ description }}
    </p>
    <div v-if="action" class="empty-state-action">
      <slot name="action">
        <component :is="action" />
      </slot>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  icon?: Component;
  title: string;
  description?: string;
  action?: Component;
  role?: 'status' | 'alert';
}

withDefaults(defineProps<Props>(), {
  role: 'status'
});
</script>
```

---

## 📚 相关文档

- [功能状态详解](./component-states-functional.md) - 功能状态总览
- [Error状态详解](./component-states-error.md) - 错误状态规范
- [Loading状态详解](./component-states-loading.md) - 加载状态规范
- [Disabled状态详解](./component-states-disabled.md) - 禁用状态规范
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-05 (从component-states-empty-error.md拆分)
> **维护者**: 项目团队
