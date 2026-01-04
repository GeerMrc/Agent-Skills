# 响应式设计指南

> 📱 **移动优先** - 适配所有设备的现代界面设计

---

## 📖 文档说明

本文档提供响应式设计的完整指南，涵盖从移动优先策略到具体实现的所有核心内容。

**目标读者**: 前端开发者、UI设计师
**文档长度**: 约290行
**阅读时间**: 约16分钟

---

## 🎯 响应式设计核心原则

### 移动优先策略

```
设计流程：
1. 从最小屏幕开始设计（320px）
2. 逐步增强到更大屏幕
3. 添加复杂布局和交互
```

### 为什么移动优先？

| 优势 | 说明 |
|------|------|
| **性能优先** | 移动设备资源受限，优先保证性能 |
| **内容聚焦** | 小屏幕强迫识别核心内容 |
| **渐进增强** | 基础功能在所有设备可用 |
| **触摸优先** | 天然支持触摸交互设计 |

---

## 📏 断点系统

### 标准断点

```css
/* ✅ 推荐：使用语义化断点变量 */
:root {
  --bp-xs: 375px;   /* 小型手机 */
  --bp-sm: 640px;   /* 手机横屏 / 小平板 */
  --bp-md: 768px;   /* 平板竖屏 */
  --bp-lg: 1024px;  /* 平板横屏 / 小笔记本 */
  --bp-xl: 1280px;  /* 桌面 */
  --bp-2xl: 1536px; /* 大屏幕 */
}

/* 使用 min-width（移动优先） */
@media (min-width: 640px) {
  /* sm 及以上 */
}

@media (min-width: 1024px) {
  /* lg 及以上 */
}
```

### 断点使用最佳实践

```css
/* ✅ 正确：使用 min-width（移动优先） */
.container {
  width: 100%;
  padding: 1rem;
}

@media (min-width: 768px) {
  .container {
    max-width: 720px;
    margin: 0 auto;
  }
}

/* ❌ 避免：使用 max-width（桌面优先） */
.container {
  max-width: 1200px;
}

@media (max-width: 767px) {
  .container {
    width: 100%;
  }
}
```

---

## 🎨 布局技术

### Flexbox 响应式布局

```css
/* 移动端：单列 */
.card-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* 平板及以上：多列 */
@media (min-width: 768px) {
  .card-grid {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .card {
    flex: 1 1 calc(50% - 1rem);
  }
}

/* 桌面：更多列 */
@media (min-width: 1024px) {
  .card {
    flex: 1 1 calc(33.333% - 1rem);
  }
}
```

### CSS Grid 响应式布局

```css
/* 移动端：单列自动 */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* 平板：2列 */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 桌面：3列 */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* 大屏幕：4列 */
@media (min-width: 1280px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

### 自动适应列数（推荐）

```css
/* ✅ 最佳实践：使用 auto-fit 和 minmax */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(
    auto-fit,
    minmax(min(100%, 280px), 1fr)
  );
  gap: 1rem;
}
/* 自动计算最佳列数，无需媒体查询 */
```

---

## 🖼️ 响应式图片

### srcset 属性

```html
<!-- ✅ 使用 srcset 提供多种分辨率 -->
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 640px) 100vw,
    (max-width: 1024px) 50vw,
    33vw
  "
  alt="响应式图片"
>
```

### picture 元素

```html
<!-- 艺术指导：不同屏幕使用不同图片 -->
<picture>
  <!-- 移动端：竖版图片 -->
  <source
    media="(max-width: 767px)"
    srcset="portrait.webp"
    type="image/webp"
  >
  <source
    media="(max-width: 767px)"
    srcset="portrait.jpg"
  >

  <!-- 桌面端：横版图片 -->
  <source
    srcset="landscape.webp"
    type="image/webp"
  >
  <img
    src="landscape.jpg"
    alt="响应式图片"
    loading="lazy"
  >
</picture>
```

### CSS 响应式图片

```css
/* 使用容器查询或 aspect-ratio */
.responsive-image {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

/* 背景图片响应式 */
.hero {
  background-image: url('hero-small.jpg');
  background-size: cover;
  background-position: center;
}

@media (min-width: 768px) {
  .hero {
    background-image: url('hero-large.jpg');
  }
}
```

---

## ✍️ 响应式排版

### 流式字体

```css
/* ✅ 推荐：使用 clamp() 设置字体范围 */
:root {
  --font-sm: clamp(0.875rem, 0.8rem + 0.375vw, 1rem);
  --font-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --font-lg: clamp(1.125rem, 1rem + 0.625vw, 1.25rem);
  --font-xl: clamp(1.25rem, 1rem + 1.25vw, 1.5rem);
  --font-2xl: clamp(1.5rem, 1.25rem + 1.25vw, 2rem);
  --font-3xl: clamp(1.875rem, 1.5rem + 1.875vw, 2.5rem);
}

h1 {
  font-size: var(--font-3xl);
  line-height: 1.2;
}

p {
  font-size: var(--font-base);
  line-height: 1.6;
}
```

### 行高和间距

```css
/* 移动端需要更大的行高 */
body {
  font-size: var(--font-base);
  line-height: 1.6;
}

@media (min-width: 768px) {
  body {
    line-height: 1.5;
  }
}

/* 标题行高随字体大小调整 */
h1 {
  font-size: var(--font-3xl);
  line-height: 1.2;
}

@media (min-width: 768px) {
  h1 {
    line-height: 1.1;
  }
}
```

---

## 👆 触摸目标

### 最小触摸尺寸

```css
/* WCAG 建议：至少 44×44 像素 */
.button,
.link,
.input {
  min-height: 44px;
  min-width: 44px;
  padding: 0.75rem 1rem;
}

/* 链接内联时，增加点击区域 */
.inline-link {
  display: inline-block;
  padding: 0.25rem 0;
  text-decoration: underline;
  text-underline-offset: 4px;
}
```

### 间距和布局

```css
/* ✅ 触摸目标之间有足够间距 */
.nav-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 1rem;
  margin: 0.25rem;
}

/* ❌ 避免：触摸目标太密集 */
.tight-nav .nav-link {
  padding: 0;
  margin: 0;
  min-height: 20px;
}
```

---

## 🔄 布局模式

### 导航响应式

```css
/* 移动端：汉堡菜单 */
.nav {
  display: flex;
  flex-direction: column;
}

.nav-menu {
  display: none;
  position: fixed;
  inset: 0;
  background: white;
  padding: 4rem 2rem;
}

.nav-menu.active {
  display: flex;
  flex-direction: column;
}

/* 桌面端：水平导航 */
@media (min-width: 1024px) {
  .nav {
    flex-direction: row;
    align-items: center;
  }

  .nav-menu {
    display: flex;
    position: static;
    flex-direction: row;
    padding: 0;
    background: transparent;
  }

  .nav-toggle {
    display: none;
  }
}
```

### 侧边栏布局

```css
/* 移动端：单列 */
.layout {
  display: grid;
  grid-template-columns: 1fr;
}

/* 桌面端：侧边栏 + 主内容 */
@media (min-width: 1024px) {
  .layout {
    grid-template-columns: 280px 1fr;
  }
}
```

---

## 🎬 响应式动画

### 减少动画偏好

```css
/* 尊重用户偏好 */
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

/* 检测运动偏好 */
@media (prefers-reduced-motion: no-preference) {
  .animate {
    animation: fadeIn 0.3s ease-out;
  }
}
```

---

## 📐 容器查询（现代方案）

```css
/* ✅ 未来方向：基于容器的响应式 */
.card-container {
  container-type: inline-size;
}

.card {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* 当容器宽度大于 400px 时 */
@container (min-width: 400px) {
  .card {
    grid-template-columns: 1fr 1fr;
  }
}

/* 当容器宽度大于 600px 时 */
@container (min-width: 600px) {
  .card {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
```

---

## 🧪 测试响应式

### 开发工具

```bash
# Chrome DevTools 设备模拟
# 1. 打开 DevTools (F12)
# 2. 点击设备工具栏图标 (Ctrl+Shift+M)
# 3. 选择预设设备或自定义尺寸

# 常用测试尺寸
- iPhone SE: 375×667
- iPhone 12 Pro: 390×844
- iPad: 768×1024
- iPad Pro: 1024×1366
- Desktop: 1920×1080
```

### 真实设备测试

| 设备类型 | 测试重点 |
|----------|----------|
| **手机** | 触摸交互、竖屏/横屏切换 |
| **平板** | 中等屏幕布局、手势操作 |
| **桌面** | 大屏布局、键盘导航、鼠标悬停 |

---

## 📋 响应式检查清单

### 设计阶段

- [ ] 从最小屏幕（320px）开始设计
- [ ] 定义清晰的断点系统
- [ ] 规划内容优先级和重排

### 开发阶段

- [ ] 使用移动优先的媒体查询（min-width）
- [ ] 图片使用 srcset 或 picture
- [ ] 触摸目标至少 44×44px
- [ ] 字体使用 clamp() 流式缩放
- [ ] 测试横屏/竖屏切换
- [ ] 尊重用户的减少动画偏好

### 测试阶段

- [ ] 在真实设备上测试
- [ ] 测试多种屏幕尺寸
- [ ] 验证触摸目标可访问性
- [ ] 检查图片加载性能

---

## 💡 最佳实践总结

1. **移动优先**：从小屏幕开始，逐步增强
2. **内容优先**：识别核心内容，优先显示
3. **性能优先**：响应式不仅是布局，也是性能
4. **触摸友好**：确保足够的触摸目标尺寸
5. **渐进增强**：基础功能在所有设备可用
6. **测试真实**：在真实设备上验证体验

---

## 🔗 相关资源

### 工具

- ** Responsively App**: 多设备预览工具
- ** BrowserStack**: 真实设备云测试
- ** Chrome DevTools**: 内置设备模拟

### 文档

- [MDN 响应式设计](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [web.dev 响应式设计](https://web.dev/responsive-web-design-basics/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
