# 交互状态详解

> 📱 **Default、Hover、Active、Focus** - 用户交互反馈的核心状态

---

## 📖 概述

交互状态是用户与界面进行直接交互时的反馈状态。这4种状态构成了最基础的用户体验反馈循环，确保用户能够感知自己的操作是否被识别。

**交互状态覆盖场景**：
- 鼠标悬停预览
- 点击/触摸反馈
- 键盘焦点导航
- 视觉反馈确认

---

## 1. Default（默认状态）

### 视觉描述
组件的常规展示状态，没有用户交互时的外观。

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

### 设计要点
- **颜色选择**: 使用品牌主色，确保识别度
- **边框处理**: 默认无边框或细边框，hover时加强
- **圆角半径**: 遵循设计系统的radius规范
- **光标样式**: 交互元素使用 `pointer`，文本使用 `text`

### 无障碍要求
- 颜色对比度 ≥ 4.5:1 (WCAG AA标准)
- 焦点指示器在获得焦点时可见
- 使用语义化HTML元素（`<button>` 而非 `<div>`）
- 交互元素大小 ≥ 44×44px (移动端触摸目标)

### 常见问题
❌ **避免**:
- 默认状态过于花哨，干扰其他状态
- 边框过细或缺失，导致白色背景下不可见
- 文字颜色与背景对比度不足

✅ **推荐**:
- 保持简洁清晰
- 使用Design Token定义颜色变量
- 确保在浅色和深色主题下都清晰可见

---

## 2. Hover（悬停状态）

### 视觉描述
鼠标指针悬停在组件上时的状态变化。

### 设计规范
```css
.button:hover {
  background: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}
```

### 设计要点
- **颜色变化**: 通常加深10-15%亮度
- **位置变化**: 轻微上移（1-2px）增强"可点击"感
- **阴影效果**: 添加阴影营造"浮起"效果
- **过渡时间**: 150-250ms平滑过渡

### 交互行为
- 即时响应（< 100ms检测延迟）
- 平滑过渡动画
- 视觉变化明显但不突兀
- 鼠标移出时恢复原状态

### 无障碍要求
- **触摸设备**: 应忽略hover状态（`@media (hover: none)`）
- **运动敏感性**: 支持 `prefers-reduced-motion` 媒体查询
- **键盘导航**: 不影响Tab焦点顺序

```css
/* 触摸设备忽略hover */
@media (hover: none) {
  .button:hover {
    transform: none;
    box-shadow: none;
  }
}

/* 支持用户减少动画偏好 */
@media (prefers-reduced-motion: reduce) {
  .button:hover {
    transform: none;
    transition: background 0s;
  }
}
```

### 常见问题
❌ **避免**:
- 过度动画（旋转、缩放等）引起干扰
- hover时改变布局导致周围元素跳动
- 颜色变化过于微妙导致不可察觉

✅ **推荐**:
- 微妙的视觉反馈（颜色、阴影、轻微位移）
- 使用CSS变量控制hover效果
- 测试在触摸设备上的表现

---

## 3. Active（激活状态）

### 视觉描述
用户点击或按下组件时的瞬时状态变化。

### 设计规范
```css
.button:active {
  background: var(--color-primary-active);
  transform: translateY(0) scale(0.98);
  box-shadow: var(--shadow-sm);
}
```

### 设计要点
- **颜色变化**: 通常比hover更深（模拟"按下"效果）
- **缩放效果**: 98-99%缩放模拟物理按钮
- **位置变化**: 从hover的上移状态回到原位
- **瞬时反馈**: 状态变化即时且短暂

### 交互行为
- 按下时立即触发（mousedown/touchstart）
- 按钮感觉"被按下"（物理反馈模拟）
- 松开后恢复到hover或default状态
- 移动端提供触觉反馈（振动）

### 无障碍要求
- **键盘支持**: `:active` 伪类在键盘Enter/Space时生效
- **触摸反馈**: 移动端有视觉反馈
- **屏幕阅读器**: 通过ARIA状态通知（如果状态持续）

```html
<!-- 按钮默认支持active伪类 -->
<button>点击我</button>

<!-- 自定义交互元素需处理 -->
<div
  role="button"
  tabindex="0"
  onKeyPress={(e) => e.key === 'Enter' && handleClick()}
>
  自定义按钮
</div>
```

### 常见问题
❌ **避免**:
- active状态不明显，用户不确定是否触发
- 过度缩放导致文字模糊
- active状态持续时间过长

✅ **推荐**:
- 明显的视觉变化（颜色+缩放）
- 与hover状态形成对比
- 快速响应并恢复

---

## 4. Focus（焦点状态）

### 视觉描述
组件通过键盘Tab键导航获得焦点时的状态指示。

### 设计规范
```css
/* 仅在键盘导航时显示焦点环 */
.button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

/* 鼠标点击时移除焦点环 */
.button:focus:not(:focus-visible) {
  outline: none;
}
```

### 设计要点
- **焦点环**: 使用对比色（通常蓝色或品牌色）
- **粗细**: 2-3px确保可见
- **偏移**: outline-offset避免与边框重叠
- **圆角**: 匹配组件圆角半径

### 交互行为
- Tab键导航时依次获得焦点
- 焦点环清晰指示当前位置
- 不遮挡重要内容或文字
- Shift+Tab反向导航

### 无障碍要求
- **焦点对比度**: 焦点环与背景对比度 ≥ 3:1
- **焦点顺序**: 符合逻辑的Tab顺序（文档流顺序）
- **焦点可见**: 焦点环始终可见（不能移除）
- **焦点陷阱**: 模态框内焦点正确循环

```html
<!-- 可交互元素默认可聚焦 -->
<button>可聚焦按钮</button>
<a href="#">可聚焦链接</a>
<input type="text" />
<select><option>选项</option></select>

<!-- 不可交互元素需设置tabindex -->
<div tabindex="0" role="button">自定义按钮</div>
<div tabindex="-1">程序化聚焦（不可Tab聚焦）</div>
```

### 焦点管理最佳实践
1. **focus-visible 伪类**: 仅在键盘导航时显示焦点环
2. **skip links**: 页面顶部添加"跳到主内容"链接
3. **模态框焦点**: 打开时聚焦到关闭按钮，关闭时返回触发元素
4. **焦点限制**: 模态框内循环焦点，不允许Tab出去

### 常见问题
❌ **避免**:
- 完全移除焦点环（`outline: none` 且无替代方案）
- 焦点环颜色与背景对比度不足
- 焦点顺序不符合逻辑
- 焦点环遮挡内容导致文字不可读

✅ **推荐**:
- 使用 `:focus-visible` 仅在键盘导航时显示
- 为焦点环设置独立的颜色变量
- 测试完整页面的键盘导航流程
- 确保焦点环在深色和浅色主题下都可见

---

## 🔄 交互状态组合场景

### 场景1: 表单提交按钮
```css
.submit-button {
  /* Default: 绿色主按钮 */
  background: var(--color-success);
}

.submit-button:hover {
  /* Hover: 更深的绿色 */
  background: var(--color-success-dark);
}

.submit-button:active {
  /* Active: 最深的绿色 + 缩小 */
  background: var(--color-success-darker);
  transform: scale(0.98);
}

.submit-button:focus-visible {
  /* Focus: 蓝色焦点环 */
  outline: 2px solid var(--color-focus);
}
```

### 场景2: 卡片点击区域
```css
.card {
  /* Default: 默认卡片样式 */
  border: 1px solid var(--color-border);
}

.card:hover {
  /* Hover: 阴影 + 轻微上移 */
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card:active {
  /* Active: 回到原位 + 缩小 */
  transform: translateY(0) scale(0.99);
}

.card:focus-visible {
  /* Focus: 整个卡片可聚焦 */
  outline: 2px solid var(--color-focus);
  outline-offset: 4px;
}
```

### 场景3: 输入框焦点
```css
.input {
  /* Default: 灰色边框 */
  border: 1px solid var(--color-border);
}

.input:hover {
  /* Hover: 稍深的边框 */
  border-color: var(--color-border-hover);
}

.input:focus-visible {
  /* Focus: 品牌色边框 + 无outline */
  border-color: var(--color-primary);
  outline: none;
  box-shadow: 0 0 0 3px var(--color-primary-alpha);
}
```

---

## 📋 交互状态检查清单

### Default状态
- [ ] 颜色对比度 ≥ 4.5:1
- [ ] 使用语义化HTML元素
- [ ] 触摸目标 ≥ 44×44px
- [ ] 光标样式正确（pointer/text/default）

### Hover状态
- [ ] 视觉变化明显但不突兀
- [ ] 触摸设备正确忽略hover
- [ ] 支持 `prefers-reduced-motion`
- [ ] 过渡时间150-250ms

### Active状态
- [ ] 视觉反馈即时且明显
- [ ] 键盘Enter/Space触发active
- [ ] 移动端有触摸反馈
- [ ] 与hover状态形成对比

### Focus状态
- [ ] 焦点环对比度 ≥ 3:1
- [ ] 焦点顺序符合逻辑
- [ ] 使用 `:focus-visible` 区分鼠标/键盘
- [ ] 焦点环不遮挡内容

### 跨状态一致性
- [ ] 所有交互组件使用相同的状态变量
- [ ] 状态过渡时间一致
- [ ] 状态变化符合用户预期
- [ ] 支持完整的键盘导航流程

---

## 📚 相关文档

- [组件状态覆盖指南](./component-states.md) - 8种状态完整概述
- [功能状态详解](./component-states-functional.md) - Disabled、Loading、Empty、Error
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
