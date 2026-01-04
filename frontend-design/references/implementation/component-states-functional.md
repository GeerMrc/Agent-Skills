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

## 5. Disabled（禁用状态）

### 视觉描述
组件不可用时的视觉表现，明确传达"当前不可交互"的信息。

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

.input:disabled {
  background: var(--color-bg-disabled);
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

### 设计要点
- **透明度**: 通常降至50-60%
- **颜色变化**: 使用灰色系传达"不可用"
- **光标样式**: `cursor: not-allowed` 明确提示
- **pointer-events**: 禁用鼠标事件

### 交互行为
- 不响应鼠标点击
- 不响应键盘事件
- 不接收焦点（`<button disabled>`）
- 视觉上明显不可用

### 无障碍要求
- **原生禁用**: 使用 `disabled` 属性
- **自定义禁用**: 使用 `aria-disabled="true"`
- **屏幕阅读器**: 宣布"disabled"或"不可用"
- **焦点处理**: 禁用元素不应接收焦点

```html
<!-- 原生禁用按钮（不可聚焦） -->
<button disabled>禁用按钮</button>

<!-- 自定义禁用（可聚焦，告知原因） -->
<button aria-disabled="true" aria-describedby="disabled-reason">
  禁用按钮
</button>
<span id="disabled-reason" class="sr-only">
  需要完成前面的步骤才能继续
</span>

<!-- 禁用表单字段 -->
<input type="text" disabled aria-label="用户名（只读）" />
```

### 禁用状态最佳实践

1. **提供禁用原因**
   - 如果可能，在禁用元素附近说明原因
   - 使用 `aria-describedby` 关联说明文字

2. **考虑可聚焦性**
   - 完全禁用：`disabled` 属性（不可聚焦）
   - 条件禁用：`aria-disabled="true"`（可聚焦，说明原因）

3. **视觉层次清晰**
   - 禁用状态与正常状态对比明显
   - 不仅仅依赖透明度（色盲用户）
   - 添加图标或文字说明

### 常见问题
❌ **避免**:
- 仅降低透明度，色盲用户无法区分
- 禁用状态与正常状态过于相似
- 不提供禁用原因，用户困惑

✅ **推荐**:
- 结合透明度、灰度、图标变化
- 明确传达"不可用"的信息
- 提供禁用原因或解锁条件

---

## 6. Loading（加载状态）

### 视觉描述
组件正在处理数据或等待响应时的状态，告知用户系统正在工作。

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

/* 骨架屏加载 */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-skeleton-start) 25%,
    var(--color-skeleton-middle) 50%,
    var(--color-skeleton-end) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### 设计要点
- **加载指示器**: 旋转圆环、进度条、骨架屏
- **文字隐藏**: 加载时隐藏文字避免重复
- **禁用交互**: `pointer-events: none` 防止重复点击
- **保持布局**: 避免加载完成后布局抖动

### 交互行为
- 显示加载指示器
- 禁用用户交互
- 保持按钮/组件宽度
- 加载完成后恢复正常

### 无障碍要求
- **aria-busy**: `aria-busy="true"` 表示正在加载
- **aria-live**: `aria-live="polite"` 通知屏幕阅读器
- **屏幕阅读器文字**: 隐藏文字保留在DOM中
- **加载完成通知**: 状态变化时告知用户

```html
<button
  class="button is-loading"
  aria-busy="true"
  aria-live="polite"
>
  <span class="sr-only">加载中...</span>
  <span>保存</span>
</button>

<!-- 骨架屏 -->
<div aria-busy="true" aria-live="polite">
  <div class="skeleton-text" aria-hidden="true"></div>
  <div class="skeleton-text" aria-hidden="true"></div>
  <span class="sr-only">正在加载内容...</span>
</div>

<!-- 进度条 -->
<div role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" aria-label="加载进度">
  <div class="progress-bar" style="width: 60%"></div>
</div>
```

### 加载模式选择

| 模式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **旋转圆环** | 按钮、小组件 | 轻量级，通用 | 不显示进度 |
| **进度条** | 文件上传、长任务 | 显示进度百分比 | 需要知道总进度 |
| **骨架屏** | 列表、卡片、feed | 保持布局结构 | 实现复杂 |
| **模糊+覆盖层** | 模态框、页面级 | 明确的区域划分 | 阻塞用户操作 |

### 常见问题
❌ **避免**:
- 加载时间过短（< 500ms）导致闪烁
- 加载指示器过小或对比度不足
- 没有屏幕阅读器文字提示

✅ **推荐**:
- 加载时间短于500ms时不显示加载状态
- 加载指示器至少16×16px
- 提供加载进度或预估时间
- 加载超时（> 10s）提供取消选项

---

## 7. Empty（空状态）

### 视觉描述
组件/区域没有内容时的友好提示，引导用户进行下一步操作。

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

### 设计要点
- **插图/图标**: 大尺寸（3-4rem），降低透明度
- **标题**: 描述性文字，告知用户当前状态
- **说明**: 友好的解释文字，告知原因
- **操作建议**: 明确的CTA按钮或链接

### 内容要求
- 清晰的插图或图标（📭、📂、🔍等）
- 描述性标题（"暂无消息"、"没有找到结果"）
- 友好的说明文字（解释原因或提供帮助）
- 明确的操作建议（"发送消息"、"清除筛选"）

### 交互行为
- 提供可操作的按钮
- 引导用户到下一步
- 避免让用户感到困惑
- 保持界面布局稳定

### 无障碍要求
- **role="status"**: 或 `aria-live="polite"` 通知屏幕阅读器
- **aria-hidden="true"**: 装饰性图标隐藏
- **操作按钮可访问**: CTA按钮标准无障碍
- **语义化HTML**: 使用 `<h3>`、`<p>` 等标签

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

<!-- 搜索结果为空 -->
<div class="empty-state" role="status">
  <div class="empty-state-icon" aria-hidden="true">🔍</div>
  <h3 class="empty-state-title">没有找到结果</h3>
  <p class="empty-state-description">
    没有找到与"<span id="search-term">关键词</span>"匹配的结果。
  </p>
  <div class="empty-state-action">
    <button>清除筛选</button>
    <button>查看全部内容</button>
  </div>
</div>

<!-- 错误空状态 -->
<div class="empty-state" role="alert">
  <div class="empty-state-icon" aria-hidden="true">⚠️</div>
  <h3 class="empty-state-title">加载失败</h3>
  <p class="empty-state-description">
    网络连接出现问题，无法加载内容。
  </p>
  <div class="empty-state-action">
    <button>重试</button>
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

### 常见问题
❌ **避免**:
- 空状态只有文字，无视觉吸引力
- 不提供操作建议，用户不知如何继续
- 使用技术术语（"空数据"、"null"）

✅ **推荐**:
- 插图/图标 + 标题 + 说明 + CTA按钮
- 友好的用户语言，避免技术术语
- 提供明确的下一步操作
- 保持与品牌风格一致的视觉设计

---

## 8. Error（错误状态）

### 视觉描述
组件出现验证错误、系统错误时的视觉反馈，明确告知用户问题所在。

### 设计规范
```css
.input.is-error {
  border-color: var(--color-error);
  background: var(--color-error-bg);
}

.input.is-error:focus-visible {
  outline-color: var(--color-error);
  box-shadow: 0 0 0 3px var(--color-error-alpha);
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
  font-size: 1.2em;
}

/* 内联错误 */
.input-wrapper {
  position: relative;
}

.input-wrapper .error-icon {
  position: absolute;
  right: var(--spacing-sm);
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-error);
}

/* Toast错误通知 */
.toast-error {
  background: var(--color-error);
  color: white;
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}
```

### 设计要点
- **颜色**: 使用红色系传达"错误"
- **图标**: ⚠️、❌、✕ 等警告图标
- **位置**: 靠近错误字段（内联或下方）
- **对比度**: 确保错误信息清晰可见

### 内容要求
- 明确的错误消息（什么出错）
- 建议的解决方案（如何修复）
- 视觉上明显但不过分
- 错误图标或颜色强调

### 交互行为
- 错误字段自动聚焦
- 错误消息清晰可见
- 提供修复建议
- 错误解除后移除提示

### 无障碍要求
- **aria-invalid**: `aria-invalid="true"` 标记错误字段
- **aria-describedby**: 关联错误消息与表单字段
- **role="alert"**: 或 `aria-live="assertive"` 立即通知
- **自动聚焦**: 错误字段自动获得焦点
- **屏幕阅读器**: 清晰的错误描述

```html
<!-- 表单字段错误 -->
<div class="form-field">
  <label for="email">邮箱地址</label>
  <div class="input-wrapper">
    <input
      type="email"
      id="email"
      class="input is-error"
      aria-invalid="true"
      aria-describedby="email-error"
      aria-required="true"
    />
    <span class="error-icon" aria-hidden="true">⚠️</span>
  </div>
  <div id="email-error" class="error-message" role="alert">
    请输入有效的邮箱地址
  </div>
</div>

<!-- 多个错误 -->
<ul class="error-summary" role="alert" aria-labelledby="error-title">
  <li id="error-title">表单提交失败，请修正以下问题：</li>
  <li><a href="#field-email">邮箱地址格式不正确</a></li>
  <li><a href="#field-password">密码长度至少8位</a></li>
  <li><a href="#field-phone">手机号码格式不正确</a></li>
</ul>

<!-- Toast错误通知 -->
<div class="toast toast-error" role="alert" aria-live="assertive">
  <span aria-hidden="true">⚠️</span>
  <span>网络连接失败，请检查您的网络设置</span>
  <button aria-label="关闭通知">×</button>
</div>
```

### 错误消息最佳实践

1. **明确具体**
   - ❌ "输入无效"
   - ✅ "邮箱地址格式不正确，请包含@符号"

2. **提供解决方案**
   - ❌ "错误"
   - ✅ "密码长度至少8位，当前6位"

3. **避免技术术语**
   - ❌ "404 Not Found"
   - ✅ "页面不存在，可能已被删除"

4. **保持友好语气**
   - ❌ "您输入了错误的数据"
   - ✅ "请检查您的输入"

### 错误状态场景

| 场景 | 错误类型 | 消息示例 | 解决方案 |
|------|----------|----------|----------|
| **表单验证** | 字段错误 | "邮箱地址格式不正确" | 提供格式示例 |
| **网络请求** | API错误 | "网络连接失败" | 提供重试按钮 |
| **权限不足** | 403错误 | "您没有权限访问" | 联系管理员 |
| **资源不存在** | 404错误 | "页面不存在" | 返回首页 |
| **服务器错误** | 500错误 | "服务器出现问题" | 稍后重试 |

### 常见问题
❌ **避免**:
- 错误消息过于模糊（"错误"、"无效"）
- 使用技术术语（"400 Bad Request"）
- 错误消息远离错误字段
- 错误颜色对比度不足

✅ **推荐**:
- 具体的错误描述
- 提供修复建议
- 错误字段自动聚焦
- 错误消息使用 `role="alert"`

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

### Loading状态
- [ ] 加载指示器清晰可见（≥16×16px）
- [ ] 使用 `aria-busy="true"`
- [ ] 屏幕阅读器文字提示
- [ ] 加载完成后通知用户

### Empty状态
- [ ] 插图/图标 + 标题 + 说明 + CTA
- [ ] 使用 `role="status"` 或 `aria-live`
- [ ] 装饰性图标 `aria-hidden="true"`
- [ ] 提供明确的操作建议

### Error状态
- [ ] 错误消息具体且清晰
- [ ] 使用 `aria-invalid` 和 `aria-describedby`
- [ ] 错误字段自动聚焦
- [ ] 提供 `role="alert"` 或 `aria-live="assertive"`

### 跨状态一致性
- [ ] 所有状态使用相同的Design Token
- [ ] 状态切换过渡平滑
- [ ] 错误/空状态符合品牌视觉风格
- [ ] 所有状态支持完整的无障碍访问

---

## 📚 相关文档

- [组件状态覆盖指南](./component-states.md) - 8种状态完整概述
- [交互状态详解](./component-states-interactive.md) - Default、Hover、Active、Focus
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准 ⏳ 计划中
- [Design Token方法论](../methodology/design-tokens.md) - Token基础概念

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (文档重构：从component-states.md拆分)
> **维护者**: 项目团队
