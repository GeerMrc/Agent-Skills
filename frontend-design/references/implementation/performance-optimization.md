# 性能优化指南

> ⚡ **性能最佳实践** - LCP < 2.5s，FID < 100ms，CLS < 0.1
> 📚 **系列文档** - 本文是性能优化系列的主文档，提供核心概念和整体导航

---

## 📖 核心概念

性能优化是用户体验的关键。快速、流畅的界面提升用户满意度和转化率。

**核心指标（Core Web Vitals）**：
- LCP（Largest Contentful Paint） < 2.5s
- FID（First Input Delay） < 100ms
- CLS（Cumulative Layout Shift） < 0.1

---

## 🎯 Core Web Vitals

### LCP（最大内容绘制）

**定义**：页面主要内容渲染完成的时间

**目标**：< 2.5s

**优化策略**：

```html
<!-- 1. 预加载关键资源 -->
<link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/hero-image.jpg" as="image">

<!-- 2. 优先获取 -->
<link rel="prefetch" href="/next-page.html">

<!-- 3. 预连接 -->
<link rel="preconnect" href="https://api.example.com">
<link rel="dns-prefetch" href="https://cdn.example.com">
```

```javascript
// 4. 延迟非关键JS
// 方式1：defer（按顺序执行）
<script defer src="non-critical.js"></script>

// 方式2：async（独立执行）
<script async src="analytics.js"></script>

// 方式3：动态导入
const lazyModule = await import('./lazy-module.js')

// 5. 内联关键CSS
<style>
  /* 关键路径CSS */
  .hero { background: var(--color-primary); }
</style>
```

### FID（首次输入延迟）

**定义**：用户首次交互到浏览器响应的时间

**目标**：< 100ms

**优化策略**：

```javascript
// 1. 减少JS执行时间
// ✅ 好的做法：代码分割
import(/* webpackChunkName: "dashboard" */ './dashboard')

// ❌ 避免：大bundle
import Dashboard from './dashboard' // 整个bundle

// 2. 减少长任务
// ✅ 使用requestIdleCallback
function heavyTask() {
  requestIdleCallback(() => {
    // 在浏览器空闲时执行
    performHeavyCalculation()
  })
}

// 或使用时间切片
async function processInChunks(items) {
  for (const item of items) {
    await processItem(item)
    // 让出主线程
    await new Promise(resolve => setTimeout(resolve, 0))
  }
}

// 3. 使用Web Workers
const worker = new Worker('heavy-worker.js')
worker.postMessage({ data: largeDataSet })
```

### CLS（累积布局偏移）

**定义**：页面内容在加载过程中的意外移动

**目标**：< 0.1

**优化策略**：

```html
<!-- 1. 为图片和视频设置尺寸 -->
<img
  src="image.jpg"
  width="800"
  height="600"
  alt="描述"
>

<!-- 或使用CSS aspect-ratio -->
<img
  src="image.jpg"
  style="aspect-ratio: 4/3; width: 100%;"
  alt="描述"
>

<!-- 2. 为广告和嵌入内容保留空间 -->
<div class="ad-placeholder" style="min-height: 250px;">
  <ins class="adsbygoogle"></ins>
</div>

<!-- 3. 为动态内容设置最小高度 -->
<div class="feed" style="min-height: 400px;">
  <!-- 动态加载内容 -->
</div>

<!-- 4. 使用font-display防止FOIT -->
<style>
  @font-face {
    font-family: 'Custom Font';
    src: url('/fonts/custom.woff2') format('woff2');
    font-display: swap; /* 立即显示后备字体 */
  }
</style>
```

---

## 📚 系列文档导航

本系列文档涵盖性能优化的各个方面，按主题分为4个部分：

### 1. [性能渲染优化](./performance-rendering.md)
**加载性能 + 运行时性能 + 构建优化**

包含：
- 🚀 加载性能优化（代码分割、懒加载、资源优先级）
- 💻 运行时性能优化（虚拟滚动、防抖节流、memo优化）
- 🗜️ 构建优化（Tree Shaking、压缩混淆、Bundle分析）

**适用场景**：需要优化前端渲染性能和构建产物体积

---

### 2. [资源优化指南](./performance-resources.md)
**图片优化 + 网络优化**

包含：
- 🖼️ 图片优化（现代格式、压缩调整、响应式图片）
- 🌐 网络优化（HTTP/2、缓存策略、CDN使用）

**适用场景**：需要优化静态资源加载和网络传输性能

---

### 3. [性能监控与测试](./performance-monitoring.md)
**性能测试 + 性能监控 + 检查清单**

包含：
- 🧪 性能测试（Lighthouse、WebPageTest、Chrome DevTools）
- 📊 性能监控（RUM、Core Web Vitals监控）
- ✅ 性能检查清单（加载、运行时、视觉、网络）

**适用场景**：需要建立性能测试和监控体系

---

## 🎯 快速开始指南

根据您的需求选择对应的文档：

| 场景 | 推荐文档 | 关键指标 |
|------|----------|----------|
| **页面加载慢** | [性能渲染优化](./performance-rendering.md) | LCP < 2.5s |
| **交互卡顿** | [性能渲染优化](./performance-rendering.md) | FID < 100ms |
| **页面抖动** | [性能渲染优化](./performance-rendering.md) | CLS < 0.1 |
| **资源体积大** | [资源优化指南](./performance-resources.md) | Bundle大小 |
| **图片加载慢** | [资源优化指南](./performance-resources.md) | 图片格式/大小 |
| **需要测试工具** | [性能监控与测试](./performance-monitoring.md) | 测试覆盖率 |
| **生产监控** | [性能监控与测试](./performance-monitoring.md) | RUM数据 |

---

## 🔗 相关文档

- [SEO最佳实践](./seo-best-practices.md) - SEO优化
- [无障碍指南](./accessibility.md) - WCAG AA标准
- [质量检查清单](../quality/checklist.md) - 完整检查清单

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04
> **维护者**: 项目团队
