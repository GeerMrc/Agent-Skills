# 布局示例

> 📐 **Layout Examples** - 常用布局模式和实现

---

## 📖 文档说明

本文档提供常用的 Web 布局模式示例，涵盖经典布局、响应式布局和现代 CSS 技术。

**目标读者**: 前端开发者
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 布局核心原则

### 布局原则

| 原则 | 说明 | 应用 |
|------|------|------|
| **移动优先** | 从小屏幕开始设计 | 使用 min-width 断点 |
| **内容优先** | 内容决定布局结构 | 优先考虑内容展示 |
| **响应式** | 适配多种屏幕尺寸 | 灵活的网格系统 |
| **无障碍** | 支持键盘和屏幕阅读器 | 语义化 HTML 结构 |

---

## 📄 经典布局

### Header-Footer 布局

```html
<!-- ✅ 语义化 HTML 结构 -->
<body>
  <header class="site-header">
    <nav>导航菜单</nav>
  </header>

  <main class="site-main">
    <h1>页面标题</h1>
    <p>主要内容...</p>
  </main>

  <footer class="site-footer">
    <p>&copy; 2025 公司名称</p>
  </footer>
</body>
```

```css
/* CSS 实现 */
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.site-main {
  flex: 1;
  /* 或使用 min-height 确保内容填充 */
  min-height: 0;
}

.site-header,
.site-footer {
  flex-shrink: 0;
}
```

### 两栏布局（主内容 + 侧边栏）

```html
<div class="two-column-layout">
  <main class="main-content">
    <h1>主内容</h1>
    <p>主要内容区域...</p>
  </main>

  <aside class="sidebar">
    <h2>侧边栏</h2>
    <nav>侧边导航</nav>
  </aside>
</div>
```

```css
/* CSS Grid 实现 */
.two-column-layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 2rem;
  min-height: 100vh;
}

/* 响应式：移动端变为单列 */
@media (max-width: 768px) {
  .two-column-layout {
    grid-template-columns: 1fr;
  }
}
```

### 三栏布局

```html
<div class="three-column-layout">
  <aside class="left-sidebar">左侧边栏</aside>
  <main class="main-content">主内容</main>
  <aside class="right-sidebar">右侧边栏</aside>
</div>
```

```css
/* CSS Grid 实现 */
.three-column-layout {
  display: grid;
  grid-template-columns: 250px 1fr 250px;
  gap: 2rem;
  min-height: 100vh;
}

/* 响应式 */
@media (max-width: 1024px) {
  .three-column-layout {
    grid-template-columns: 200px 1fr;
  }
  .right-sidebar {
    display: none;
  }
}

@media (max-width: 768px) {
  .three-column-layout {
    grid-template-columns: 1fr;
  }
}
```

---

## 🎴 圣杯布局

### 固定宽度 + 自适应中间

```html
<div class="holy-grail-layout">
  <header class="header">页头</header>
  <div class="content-wrapper">
    <main class="main-content">主内容</main>
    <aside class="left-sidebar">左侧边栏</aside>
    <aside class="right-sidebar">右侧边栏</aside>
  </div>
  <footer class="footer">页脚</footer>
</div>
```

```css
/* 现代实现：使用 Grid */
.holy-grail-layout {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  gap: 2rem;
}

/* 响应式 */
@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr 200px;
  }
  .left-sidebar {
    grid-row: 2;
  }
  .main-content {
    grid-column: 1 / -1;
  }
}
```

---

## 🃏 卡片网格布局

### 响应式卡片网格

```html
<div class="card-grid">
  <article class="card">卡片 1</article>
  <article class="card">卡片 2</article>
  <article class="card">卡片 3</article>
  <article class="card">卡片 4</article>
</div>
```

```css
/* ✅ 推荐：使用 auto-fit/auto-fill */
.card-grid {
  display: grid;
  /* 自动填充，最小宽度 280px */
  grid-template-columns: repeat(
    auto-fit,
    minmax(min(100%, 280px), 1fr)
  );
  gap: 1.5rem;
}

.card {
  aspect-ratio: 4 / 3;
  background: white;
  border-radius: 0.5rem;
  padding: 1.5rem;
}
```

### 固定列数网格

```css
/* ✅ 固定 3 列网格 */
.card-grid-fixed {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

@media (max-width: 768px) {
  .card-grid-fixed {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .card-grid-fixed {
    grid-template-columns: 1fr;
  }
}
```

---

## 📊 仪表板布局

### 顶部导航 + 内容区

```html
<div class="dashboard-layout">
  <header class="dashboard-header">
    <h1>仪表板</h1>
    <nav>用户菜单</nav>
  </header>

  <div class="dashboard-content">
    <aside class="dashboard-sidebar">
      <nav>侧边导航</nav>
    </aside>

    <main class="dashboard-main">
      <div class="stats-grid">
        <div class="stat-card">统计卡片 1</div>
        <div class="stat-card">统计卡片 2</div>
        <div class="stat-card">统计卡片 3</div>
        <div class="stat-card">统计卡片 4</div>
      </div>

      <div class="content-area">
        主要内容区域
      </div>
    </main>
  </div>
</div>
```

```css
.dashboard-layout {
  display: grid;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
}

.dashboard-content {
  display: grid;
  grid-template-columns: 250px 1fr;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

@media (max-width: 1024px) {
  .dashboard-content {
    grid-template-columns: 1fr;
  }
  .dashboard-sidebar {
    display: none;
  }
}
```

---

## 🖼️ 图片画廊布局

### 瀑布流布局

```html
<div class="masonry-gallery">
  <img src="image1.jpg" alt="图片 1" class="masonry-item">
  <img src="image2.jpg" alt="图片 2" class="masonry-item">
  <img src="image3.jpg" alt="图片 3" class="masonry-item">
</div>
```

```css
/* ✅ CSS Columns 实现 */
.masonry-gallery {
  column-count: 3;
  column-gap: 1rem;
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: 1rem;
  width: 100%;
}

@media (max-width: 768px) {
  .masonry-gallery {
    column-count: 2;
  }
}

@media (max-width: 480px) {
  .masonry-gallery {
    column-count: 1;
  }
}
```

### 网格画廊

```css
/* ✅ Grid 实现 */
.grid-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 0.5rem;
}

.grid-gallery img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
```

---

## 📱 移动端导航

### 底部导航栏

```html
<div class="mobile-nav">
  <a href="/" class="nav-item active">首页</a>
  <a href="/search" class="nav-item">搜索</a>
  <a href="/profile" class="nav-item">我的</a>
</div>
```

```css
.mobile-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  background: white;
  border-top: 1px solid #e5e7eb;
  padding: 0.5rem 0;
  z-index: 100;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem;
  color: #6b7280;
  text-decoration: none;
}

.nav-item.active {
  color: #3b82f6;
}
```

---

## 🎛️ 弹性居中布局

### 完美居中

```html
<div class="center-container">
  <div class="center-content">
    <h1>居中内容</h1>
  </div>
</div>
```

```css
/* ✅ Flexbox 实现垂直水平居中 */
.center-container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
  min-height: 100vh;
}

/* ✅ Grid 实现居中 */
.center-container {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
```

### 绝对定位居中

```css
/* ✅ 绝对定位 + transform */
.center-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* ✅ 绝对定位 + inset */
.center-content {
  position: absolute;
  inset: 0;
  margin: auto;
  width: fit-content;
  height: fit-content;
}
```

---

## 📐 等高列布局

### Flexbox 等高列

```html
<div class="equal-height-columns">
  <div class="column">列 1<br>内容高度不同</div>
  <div class="column">列 2</div>
  <div class="column">列 3<br>更多内容<br>更多内容</div>
</div>
```

```css
/* ✅ Flexbox 自动等高 */
.equal-height-columns {
  display: flex;
  gap: 1rem;
}

.column {
  flex: 1;
  background: white;
  padding: 1rem;
  /* 所有列自动等高 */
}
```

### Grid 等高列

```css
/* ✅ Grid 自动等高 */
.equal-height-columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  align-items: stretch; /* 默认值，列等高 */
}
```

---

## 🔄 切换布局

### 列表/网格切换

```html
<div class="layout-switcher">
  <button id="listView">列表</button>
  <button id="gridView">网格</button>
</div>

<div class="content-container" data-layout="grid">
  <!-- 内容项 -->
</div>
```

```css
.content-container[data-layout="grid"] {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.content-container[data-layout="list"] {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
```

```javascript
// JavaScript 切换
const container = document.querySelector('.content-container');
const listViewBtn = document.getElementById('listView');
const gridViewBtn = document.getElementById('gridView');

listViewBtn.addEventListener('click', () => {
  container.dataset.layout = 'list';
});

gridViewBtn.addEventListener('click', () => {
  container.dataset.layout = 'grid';
});
```

---

## 📋 布局检查清单

### 响应式

- [ ] 移动端布局合理
- [ ] 平板端布局合理
- [ ] 桌面端布局合理
- [ ] 横屏布局考虑

### 语义化

- [ ] 使用语义化 HTML5 标签
- [ ] 正确的标题层级
- [ ] 合理的 ARIA 标签

### 性能

- [ ] 避免过度嵌套
- [ ] 使用高效的选择器
- [ ] 合理的布局算法

### 兼容性

- [ ] 测试主流浏览器
- [ ] 优雅降级方案
- [ ] CSS 前缀处理

---

## 💡 最佳实践总结

1. **移动优先**：从小屏幕开始设计
2. **语义化 HTML**：使用正确的标签
3. **Grid 优先**：复杂布局使用 CSS Grid
4. **Flexbox 补充**：一维布局使用 Flexbox
5. **响应式设计**：考虑所有屏幕尺寸

---

## 🔗 相关资源

### 工具

- ** CSS Grid Generator**: 网格布局生成器
- ** Flexbox Froggy**: Flexbox 游戏学习
- ** LayoutIT**: 交互式布局工具

### 文档

- [CSS Grid 布局](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Grid_Layout)
- [Flexbox 布局](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Flexible_Box_Layout)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
