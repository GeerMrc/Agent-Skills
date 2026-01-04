# 功能状态详解

> 🔧 **Disabled、Loading、Empty、Error** - 功能性反馈状态完整指南

---

## 📖 概述

功能状态是组件在特定业务场景下的状态表现，与用户交互行为无直接关联，但影响用户对系统状态的认知。

**功能状态覆盖场景**：
- 表单字段禁用/启用
- 异步数据加载中
- 列表/表格无数据
- 表单验证错误

---

## 🗂️ 功能状态分类

### 1. Disabled（禁用状态）

组件不可用时的视觉表现，明确传达"当前不可交互"的信息。

**核心特征**：
- 透明度降至50-60%
- 使用灰色系传达"不可用"
- 光标样式为 `not-allowed`
- 不响应鼠标和键盘事件

**适用场景**：
- 表单字段在满足条件前不可用
- 按钮在完成前置步骤前不可点击
- 功能需要特定权限才能使用

**详细文档**: [Disabled状态详解](./component-states-disabled.md)

### 2. Loading（加载状态）

组件正在处理数据或等待响应时的状态，告知用户系统正在工作。

**核心特征**：
- 显示加载指示器（旋转圆环、进度条、骨架屏）
- 禁用用户交互
- 保持组件尺寸避免抖动
- 加载完成后恢复正常

**适用场景**：
- 表单提交后等待服务器响应
- 异步数据加载中
- 文件上传/下载进行中

**详细文档**: [Loading状态详解](./component-states-loading.md)

### 3. Empty（空状态）

组件/区域没有内容时的友好提示，引导用户进行下一步操作。

**核心特征**：
- 大尺寸插图/图标（3-4rem）
- 描述性标题说明当前状态
- 友好的解释文字
- 明确的操作建议（CTA按钮）

**适用场景**：
- 列表/表格无数据
- 搜索无结果
- 筛选后无匹配项
- 用户首次使用

**详细文档**: [Empty状态详解](./component-states-empty.md) - [Error状态详解](./component-states-error.md)

### 4. Error（错误状态）

组件出现验证错误、系统错误时的视觉反馈，明确告知用户问题所在。

**核心特征**：
- 使用红色系传达"错误"
- 错误图标（⚠️、❌、✕）
- 错误消息靠近错误字段
- 提供修复建议

**适用场景**：
- 表单字段验证失败
- 网络请求失败
- 权限不足
- 服务器错误

**详细文档**: [Empty & Error状态详解](./component-states-empty-error.md#error状态详解)

---

## 🔄 功能状态组合场景

### 场景1: 表单提交

```tsx
function SubmitButton({ isSubmitting, hasErrors }) {
  return (
    <button
      disabled={isSubmitting || hasErrors}
      aria-disabled={isSubmitting || hasErrors}
      aria-busy={isSubmitting}
    >
      {isSubmitting ? (
        <>
          <Spinner aria-hidden="true" />
          <span className="sr-only">提交中...</span>
        </>
      ) : hasErrors ? (
        '请修正错误后提交'
      ) : (
        '提交'
      )}
    </button>
  );
}
```

### 场景2: 数据列表

```tsx
function DataList({ data, loading, error }) {
  if (loading) {
    return <SkeletonLoader aria-busy="true" />;
  }

  if (error) {
    return (
      <EmptyState
        role="alert"
        icon="⚠️"
        title="加载失败"
        description={error.message}
        action={<button onClick={retry}>重试</button>}
      />
    );
  }

  if (data.length === 0) {
    return (
      <EmptyState
        role="status"
        icon="📭"
        title="暂无数据"
        description="还没有任何内容"
        action={<button>创建新项目</button>}
      />
    );
  }

  return <ul>{data.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
}
```

### 场景3: 搜索输入

```tsx
function SearchInput({ query, results, searching }) {
  const hasQuery = query.trim().length > 0;
  const hasNoResults = hasQuery && results.length === 0;

  return (
    <div>
      <input
        type="search"
        value={query}
        aria-busy={searching}
        placeholder="搜索..."
      />
      {searching && <Spinner aria-hidden="true" />}
      {hasNoResults && (
        <EmptyState
          role="status"
          icon="🔍"
          title="没有找到结果"
          description={`没有找到与"${query}"匹配的结果`}
          action={<button>清除搜索</button>}
        />
      )}
    </div>
  );
}
```

---

## 📋 功能状态检查清单

### Disabled状态
- [ ] 视觉对比度明显（透明度+灰度）
- [ ] 光标样式为 `not-allowed`
- [ ] 使用 `disabled` 或 `aria-disabled`
- [ ] 屏幕阅读器宣布"disabled"
- [ ] 提供禁用原因说明

### Loading状态
- [ ] 加载指示器清晰可见（≥16×16px）
- [ ] 使用 `aria-busy="true"`
- [ ] 屏幕阅读器文字提示
- [ ] 加载完成后通知用户
- [ ] 避免加载时间过短导致闪烁（< 500ms）

### Empty状态
- [ ] 插图/图标 + 标题 + 说明 + CTA
- [ ] 使用 `role="status"` 或 `aria-live`
- [ ] 装饰性图标 `aria-hidden="true"`
- [ ] 提供明确的操作建议
- [ ] 友好的用户语言

### Error状态
- [ ] 错误消息具体且清晰
- [ ] 使用 `aria-invalid` 和 `aria-describedby`
- [ ] 错误字段自动聚焦
- [ ] 提供 `role="alert"` 或 `aria-live="assertive"`
- [ ] 避免技术术语

### 跨状态一致性
- [ ] 所有状态使用相同的Design Token
- [ ] 状态切换过渡平滑
- [ ] 错误/空状态符合品牌视觉风格
- [ ] 所有状态支持完整的无障碍访问
- [ ] 保持布局稳定，避免抖动

---

## 📚 相关文档

### 详细状态文档
- [Disabled状态详解](./component-states-disabled.md) - 禁用状态完整规范（~250行）
- [Loading状态详解](./component-states-loading.md) - 加载状态完整规范（~280行）
- [Empty & Error状态详解](./component-states-empty-error.md) - 空/错误状态完整规范（~350行）

### 相关文档
- [组件状态覆盖指南](./component-states.md) - 8种状态完整概述
- [交互状态详解](./component-states-interactive.md) - Default、Hover、Active、Focus
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准
- [Design Token方法论](../methodology/design-tokens.md) - Token基础概念

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (文档重构：拆分为4个子文档)
> **维护者**: 项目团队
