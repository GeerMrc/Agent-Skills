# 动画示例

> 🎬 **Animation Examples** - 常用动画模式和最佳实践

---

## 📖 文档说明

本文档提供常用的 Web 动画示例，涵盖过渡效果、关键帧动画、交互动画等内容。

**目标读者**: 前端开发者
**文档长度**: 约270行
**阅读时间**: 约15分钟

---

## 🎯 动画核心原则

### 动画原则

| 原则 | 说明 | 应用 |
|------|------|------|
| **有目的性** | 动画服务于功能 | 引导注意力、提供反馈 |
| **微妙适度** | 不过度使用动画 | 短暂、平滑、自然 |
| **性能优先** | 使用高效属性 | transform、opacity |
| **可禁用** | 尊重用户偏好 | prefers-reduced-motion |

---

## 🎨 CSS 过渡动画

### 基础过渡

```css
/* ✅ 好的做法：声明过渡属性 */
.button {
  background: blue;
  /* 声明需要过渡的属性 */
  transition-property: background, transform;
  transition-duration: 0.2s;
  transition-timing-function: ease;
}

.button:hover {
  background: darkblue;
  transform: translateY(-2px);
}

/* ✅ 简写形式 */
.button {
  transition: background 0.2s ease, transform 0.2s ease;
}
```

### 缓动函数

```css
/* 常用缓动函数 */
:root {
  --ease-linear: linear;
  --ease-in: ease-in;
  --ease-out: ease-out;
  --ease-in-out: ease-in-out;
  /* 自定义贝塞尔曲线 */
  --ease-custom: cubic-bezier(0.4, 0, 0.2, 1);
}

/* 使用示例 */
.fade-in {
  animation: fadeIn 0.3s var(--ease-out);
}
```

### 多属性过渡

```css
/* ✅ 不同属性不同持续时间 */
.card {
  transition:
    background 0.3s ease,
    transform 0.2s ease,
    opacity 0.4s ease;
}

.card:hover {
  background: #f0f0f0;
  transform: scale(1.02);
}
```

---

## 🎭 关键帧动画

### 淡入淡出

```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

/* 使用 */
.fade-in {
  animation: fadeIn 0.3s ease-in;
}

.fade-out {
  animation: fadeOut 0.3s ease-out;
}
```

### 滑动动画

```css
/* 从右侧滑入 */
@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* 从底部滑入 */
@keyframes slideInUp {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
```

### 缩放动画

```css
/* 放大效果 */
@keyframes scaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

/* 脉冲效果 */
@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}
```

### 旋转动画

```css
/* 持续旋转 */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.loading-spinner {
  animation: spin 1s linear infinite;
}
```

---

## 🎪 交互动画

### 悬停效果

```css
/* 按钮悬停 */
.button {
  transition: all 0.2s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* 卡片悬停 */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}
```

### 焦点效果

```css
/* 焦点指示器 */
.input:focus {
  outline: none;
  animation: focusRing 0.3s ease;
}

@keyframes focusRing {
  from {
    box-shadow: 0 0 0 0 rgba(59, 130, 246, 0);
  }
  to {
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  }
}
```

### 点击效果

```css
/* 点击波纹效果 */
.button {
  position: relative;
  overflow: hidden;
}

.button:active {
  transform: scale(0.98);
}

/* 使用伪元素创建波纹 */
.button::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
  transform: scale(0);
  opacity: 0;
  transition: transform 0.3s, opacity 0.3s;
}

.button:active::after {
  transform: scale(2);
  opacity: 1;
  transition: 0s;
}
```

---

## 🚀 页面过渡动画

### 页面加载动画

```css
/* 渐进式显示页面 */
.page-enter {
  animation: pageEnter 0.5s ease-out;
}

@keyframes pageEnter {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### 路由切换动画

```css
/* 淡入淡出切换 */
.fade-enter {
  opacity: 0;
}

.fade-enter-active {
  opacity: 1;
  transition: opacity 0.3s ease;
}

.fade-exit {
  opacity: 1;
}

.fade-exit-active {
  opacity: 0;
  transition: opacity 0.3s ease;
}

/* 滑动切换 */
.slide-enter {
  transform: translateX(100%);
}

.slide-enter-active {
  transform: translateX(0);
  transition: transform 0.3s ease;
}

.slide-exit {
  transform: translateX(0);
}

.slide-exit-active {
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}
```

---

## 📢 通知动画

### Toast 消息

```css
/* 滑入并自动淡出 */
.toast {
  animation: toastSlideIn 0.3s ease-out;
}

.toast.hiding {
  animation: toastFadeOut 0.3s ease-in forwards;
}

@keyframes toastSlideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes toastFadeOut {
  to {
    opacity: 0;
    transform: translateX(20px);
  }
}
```

### Modal 弹窗

```css
/* 模态框背景淡入 */
.modal-backdrop {
  animation: backdropFadeIn 0.3s ease;
}

@keyframes backdropFadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* 模态框缩放进入 */
.modal-content {
  animation: modalScaleIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes modalScaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
```

---

## ⚡ 性能优化动画

### 使用 transform 和 opacity

```css
/* ✅ 高性能：只使用 transform 和 opacity */
.animated-element {
  will-change: transform, opacity;
  transform: translateZ(0); /* 开启硬件加速 */
}

/* ❌ 避免：使用引起重排的属性 */
.bad-animation {
  /* 避免动画这些属性 */
  left: 100px;
  top: 100px;
  width: 100px;
  height: 100px;
}
```

### will-change 提示

```css
/* 提示浏览器优化 */
.animated {
  will-change: transform, opacity;
}

/* 动画结束后移除 */
.animated.finished {
  will-change: auto;
}
```

---

## ♿ 可访问性动画

### 尊重减少动画偏好

```css
/* 检测用户的减少动画偏好 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* 或提供替代方案 */
.animated {
  animation: fadeIn 0.3s ease;
}

@media (prefers-reduced-motion: reduce) {
  .animated {
    animation: none;
    opacity: 1;
  }
}
```

### 提供暂停控制

```css
/* 允许用户暂停动画 */
.playing .animation {
  animation-play-state: running;
}

.paused .animation {
  animation-play-state: paused;
}
```

---

## 🎯 常用动画库

### 常用动画效果

```css
/* 弹跳进入 */
@keyframes bounceIn {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

/* 抖动 */
@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-5px);
  }
  75% {
    transform: translateX(5px);
  }
}

/* 闪烁 */
@keyframes blink {
  0%, 50%, 100% {
    opacity: 1;
  }
  25%, 75% {
    opacity: 0;
  }
}
```

### 加载动画

```css
/* 旋转加载器 */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loader {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* 点状加载器 */
@keyframes dots {
  0%, 20% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.dot {
  animation: dots 1.4s infinite ease-in-out both;
}

.dot:nth-child(1) { animation-delay: -0.32s; }
.dot:nth-child(2) { animation-delay: -0.16s; }
.dot:nth-child(3) { animation-delay: 0s; }
```

---

## 📋 动画检查清单

### 性能

- [ ] 使用 transform 和 opacity
- [ ] 避免引起重排的属性
- [ ] 合理使用 will-change
- [ ] 测试帧率（60fps）

### 可访问性

- [ ] 尊重 prefers-reduced-motion
- [ ] 提供暂停控制
- [ ] 动画不过快或过慢
- [ ] 不引起眩晕

### 用户体验

- [ ] 动画有明确目的
- [ ] 持续时间适中（<1秒）
- [ ] 使用合适的缓动函数
- [ ] 提供视觉反馈

---

## 💡 最佳实践总结

1. **性能优先**：只动画 transform 和 opacity
2. **适度使用**：不过度使用动画效果
3. **用户控制**：支持禁用和暂停动画
4. **平滑自然**：使用合适的缓动函数
5. **测试验证**：在多种设备上测试性能

---

## 🔗 相关资源

### 工具

- ** Animate.css**: 即用型动画库
- ** Framer Motion**: React 动画库
- ** GSAP**: 高性能动画平台
- ** Lottie**: JSON 动画格式

### 文档

- [CSS 动画指南](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Animations)
- [Web 动画最佳实践](https://web.dev/animations-guide/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
