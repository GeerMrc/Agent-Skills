# Disabled状态详解

> 🔧 **禁用状态** - 组件不可用时的视觉表现和交互规范

---

## 📖 状态概述

Disabled（禁用状态）表示组件当前不可交互，用户无法对该组件进行任何操作。

**适用场景**：
- 表单字段在满足特定条件前不可用
- 按钮在完成前置步骤前不可点击
- 选项在特定配置下不可选择
- 功能需要特定权限才能使用

---

## 🎨 视觉描述

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

**1. 透明度调整**
- 通常降至50-60%
- 不仅依赖透明度（色盲用户友好）
- 结合灰度变化

**2. 颜色变化**
- 使用灰色系传达"不可用"
- 保持边框和背景的对比度
- 避免与正常状态过于相似

**3. 光标样式**
- `cursor: not-allowed` 明确提示
- 鼠标悬停时显示禁用图标

**4. 事件禁用**
- `pointer-events: none` 禁用鼠标事件
- 防止点击和悬停效果

---

## 🖱️ 交互行为

### 标准行为

- **不响应鼠标点击**：点击无效，无视觉反馈
- **不响应键盘事件**：Tab键跳过，Enter/Space无效
- **不接收焦点**：`<button disabled>` 不可聚焦
- **视觉上明显不可用**：与正常状态对比明显

### 交互限制

| 交互类型 | 行为 | 说明 |
|---------|------|------|
| 鼠标点击 | 无效 | 不触发任何事件 |
| 键盘导航 | 跳过 | Tab键不聚焦禁用元素 |
| 触摸操作 | 无效 | 移动端点击无效 |
| 屏幕阅读器 | 宣布 | 宣布"disabled"或"不可用" |

---

## ♿ 无障碍要求

### 原生禁用 vs 自定义禁用

**1. 原生禁用（完全禁用）**

```html
<!-- 不可聚焦，不接收任何交互 -->
<button disabled>禁用按钮</button>
<input type="text" disabled aria-label="用户名（只读）" />
```

**特点**：
- 使用 `disabled` 属性
- 不可通过键盘聚焦
- 屏幕阅读器宣布"disabled"
- 适用于完全不可用的元素

**2. 自定义禁用（条件禁用）**

```html
<!-- 可聚焦，说明禁用原因 -->
<button
  aria-disabled="true"
  aria-describedby="disabled-reason"
>
  禁用按钮
</button>
<span id="disabled-reason" class="sr-only">
  需要完成前面的步骤才能继续
</span>
```

**特点**：
- 使用 `aria-disabled="true"`
- 可以通过键盘聚焦
- 屏幕阅读器宣布原因
- 适用于需要说明原因的场景

### 无障碍最佳实践

**✅ DO（推荐）**：
1. 使用标准 `disabled` 属性或 `aria-disabled`
2. 为自定义禁用提供原因说明
3. 使用 `aria-describedby` 关联说明文字
4. 确保屏幕阅读器正确宣布状态

**❌ DON'T（避免）**：
1. 仅用CSS禁用（不使用disabled属性）
2. 不提供禁用原因说明
3. 禁用状态与正常状态过于相似
4. 仅依赖透明度传达禁用状态

---

## 📋 实现示例

### 示例1：表单字段禁用

```html
<!-- 用户协议未同意时禁用提交按钮 -->
<form>
  <label>
    <input type="checkbox" id="agree" />
    我同意用户协议
  </label>

  <button
    disabled
    id="submit-btn"
    aria-describedby="submit-hint"
  >
    提交
  </button>
  <span id="submit-hint" class="sr-only">
    需要同意用户协议后才能提交
  </span>
</form>

<script>
const checkbox = document.getElementById('agree');
const submitBtn = document.getElementById('submit-btn');

checkbox.addEventListener('change', () => {
  submitBtn.disabled = !checkbox.checked;
  // 更新提示信息
  const hint = document.getElementById('submit-hint');
  if (checkbox.checked) {
    hint.textContent = '';
  } else {
    hint.textContent = '需要同意用户协议后才能提交';
  }
});
</script>
```

### 示例2：条件禁用

```html
<!-- 金额不足时禁用支付按钮 -->
<div>
  <p>账户余额: <span id="balance">100</span>元</p>
  <p>支付金额: <span id="amount">150</span>元</p>

  <button
    aria-disabled="true"
    aria-describedby="insufficient-funds"
    id="pay-btn"
  >
    立即支付
  </button>

  <div id="insufficient-funds" class="sr-only">
    余额不足，当前账户100元，需要150元
  </div>
</div>

<script>
function checkBalance() {
  const balance = 100;
  const amount = 150;
  const btn = document.getElementById('pay-btn');
  const hint = document.getElementById('insufficient-funds');

  if (balance >= amount) {
    btn.removeAttribute('aria-disabled');
    hint.textContent = '';
  } else {
    btn.setAttribute('aria-disabled', 'true');
    hint.textContent = `余额不足，当前账户${balance}元，需要${amount}元`;
  }
}

checkBalance();
</script>
```

### 示例3：多步骤表单

```html
<!-- 当前步骤未完成时禁用后续步骤 -->
<nav>
  <button
    aria-current="step"
    aria-disabled="false"
  >
    1. 基本信息
  </button>
  <button
    aria-disabled="true"
    aria-describedby="step-2-hint"
  >
    2. 联系方式
  </button>
  <span id="step-2-hint" class="sr-only">
    请先完成基本信息填写
  </span>
  <button aria-disabled="true">
    3. 确认提交
  </button>
</nav>
```

---

## 🎯 最佳实践

### 1. 提供禁用原因

**最佳做法**：
- 在禁用元素附近说明原因
- 使用 `aria-describedby` 关联说明文字
- 原因说明简短明确

```html
<!-- ❌ 不推荐 -->
<button disabled>提交</button>

<!-- ✅ 推荐 -->
<button disabled aria-describedby="submit-reason">提交</button>
<span id="submit-reason">请填写所有必填字段</span>
```

### 2. 考虑可聚焦性

**完全禁用**：
- 使用 `disabled` 属性
- 元素不可聚焦
- 适用于完全不可用的场景

```html
<button disabled>删除</button>
```

**条件禁用**：
- 使用 `aria-disabled="true"`
- 元素可以聚焦
- 向用户说明原因和解锁条件

```html
<button aria-disabled="true" aria-describedby="unlock-hint">
  保存
</button>
<span id="unlock-hint">修改内容后可保存</span>
```

### 3. 视觉层次清晰

**视觉对比要求**：
- 禁用状态与正常状态对比明显
- 不仅依赖透明度（色盲用户友好）
- 添加图标或文字说明

```css
/* ❌ 仅透明度 */
.button:disabled {
  opacity: 0.5;
}

/* ✅ 透明度 + 灰度 + 图标 */
.button:disabled {
  opacity: 0.6;
  filter: grayscale(100%);
  color: var(--color-text-disabled);
  background: var(--color-bg-disabled);
}

.button:disabled::after {
  content: "（不可用）";
  font-size: 0.8em;
  margin-left: 0.5em;
}
```

### 4. 保持布局稳定

**避免布局抖动**：
- 禁用状态保持相同尺寸
- 预留图标和文字空间
- 避免内容变化导致重新布局

```css
.button {
  min-width: 100px;  /* 固定最小宽度 */
  min-height: 40px;  /* 固定最小高度 */
}

.button:disabled {
  /* 不改变尺寸，只改变样式 */
  opacity: 0.6;
  filter: grayscale(100%);
}
```

---

## ⚠️ 常见问题

### ❌ 避免

1. **仅降低透明度**
   - 色盲用户无法区分
   - 对比度可能不足
   - 不符合WCAG标准

2. **禁用状态与正常状态过于相似**
   - 用户难以判断是否可用
   - 导致误操作和困惑

3. **不提供禁用原因**
   - 用户不知道为什么不可用
   - 不知如何解锁功能

4. **仅用CSS禁用**
   - 屏幕阅读器仍认为可用
   - 键盘仍可操作
   - 无障碍体验差

### ✅ 推荐

1. **结合多种视觉提示**
   - 透明度 + 灰度 + 图标变化
   - 确保所有用户都能识别

2. **明确传达"不可用"**
   - 清晰的视觉对比
   - 明确的文字说明

3. **提供禁用原因**
   - 解释为什么不可用
   - 告知解锁条件

4. **使用标准属性**
   - `disabled` 或 `aria-disabled`
   - 配合ARIA属性提供完整信息

---

## 📊 对比表

| 方面 | 原生 disabled | aria-disabled |
|------|-------------|---------------|
| **可聚焦性** | 不可聚焦 | 可以聚焦 |
| **键盘导航** | Tab跳过 | Tab可达 |
| **屏幕阅读器** | 宣布"disabled" | 宣布"disabled" |
| **适用场景** | 完全不可用 | 需要说明原因 |
| **原因说明** | 难以关联 | aria-describedby |
| **最佳实践** | 默认选择 | 需要提供原因时 |

---

## 🔗 相关文档

- [功能状态详解](./component-states-functional.md) - 功能状态总览
- [Loading状态详解](./component-states-loading.md) - 加载状态规范
- [Empty & Error状态详解](./component-states-empty-error.md) - 空/错误状态规范
- [无障碍指南](./accessibility.md) - WCAG AA无障碍标准

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (从component-states-functional.md拆分)
> **维护者**: 项目团队
