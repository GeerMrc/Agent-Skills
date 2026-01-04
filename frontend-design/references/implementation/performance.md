# 性能优化指南

> ⚡ **性能最佳实践** - LCP < 2.5s，FID < 100ms，CLS < 0.1

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

## 🚀 加载性能优化

### 代码分割

```javascript
// 路由级别分割
const routes = [
  {
    path: '/dashboard',
    component: () => import('./views/Dashboard.vue')
  },
  {
    path: '/settings',
    component: () => import('./views/Settings.vue')
  }
]

// 组件级别分割
const HeavyChart = defineAsyncComponent(() =>
  import('./components/HeavyChart.vue')
)

// 条件分割
async function loadEditor() {
  if (user.canEdit) {
    const { default: Editor } = await import('./Editor')
    return Editor
  }
}
```

### 懒加载

```javascript
// 图片懒加载
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" class="lazy">

// Intersection Observer实现
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target
      img.src = img.dataset.src
      observer.unobserve(img)
    }
  })
})

document.querySelectorAll('img.lazy').forEach(img => observer.observe(img))

// 组件懒加载
<div v-lazy-load="HeavyComponent"></div>
```

### 资源优先级

```html
<!-- 高优先级 -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="hero-font.woff2" as="font" crossorigin>

<!-- 中优先级 -->
<link rel="prefetch" href="next-page.html">

<!-- 低优先级 -->
<link rel="dns-prefetch" href="analytics.com">

<!-- 预加载视频海报 -->
<link rel="preload" href="poster.jpg" as="image">
```

---

## 💻 运行时性能优化

### 虚拟滚动

```javascript
// 长列表优化
import { useVirtualizer } from '@tanstack/react-virtual'

function VirtualList({ items }) {
  const parentRef = useRef(null)

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50, // 每项高度
    overscan: 5 // 额外渲染项数
  })

  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px` }}>
        {virtualizer.getVirtualItems().map(item => (
          <div
            key={item.key}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${item.size}px`,
              transform: `translateY(${item.start}px)`
            }}
          >
            {items[item.index]}
          </div>
        ))}
      </div>
    </div>
  )
}
```

### 防抖和节流

```javascript
// 防抖：延迟执行
function debounce(fn, delay) {
  let timeoutId
  return function (...args) {
    clearTimeout(timeoutId)
    timeoutId = setTimeout(() => fn.apply(this, args), delay)
  }
}

// 使用：搜索输入
const handleSearch = debounce((query) => {
  searchAPI(query)
}, 300)

// 节流：限制执行频率
function throttle(fn, limit) {
  let inThrottle
  return function (...args) {
    if (!inThrottle) {
      fn.apply(this, args)
      inThrottle = true
      setTimeout(() => inThrottle = false, limit)
    }
  }
}

// 使用：滚动事件
const handleScroll = throttle(() => {
  checkScrollPosition()
}, 100)
```

### memo和useMemo

```javascript
// React: memo防止不必要的重新渲染
const ExpensiveComponent = memo(function ExpensiveComponent({ data }) {
  return <div>{/* 复杂渲染 */}</div>
})

// useMemo缓存计算结果
function DataTable({ items, filter }) {
  const filteredItems = useMemo(() => {
    return items.filter(item => item.category === filter)
  }, [items, filter])

  return <div>{/* 渲染 */}</div>
}

// Vue: computed缓存
const filteredItems = computed(() => {
  return items.value.filter(item => item.category === filter.value)
})
```

---

## 🗜️ 构建优化

### Tree Shaking

```javascript
// ✅ 好的做法：按需导入
import { debounce } from 'lodash-es'
import Button from 'library/Button'

// ❌ 避免：导入整个库
import _ from 'lodash'
import Library from 'library'
```

### 压缩和混淆

```javascript
// webpack配置
module.exports = {
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true, // 移除console
            pure_funcs: ['console.log'] // 移除特定函数
          }
        }
      })
    ]
  }
}

// Vite已内置压缩
// vite.config.js
export default {
  build: {
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true
      }
    }
  }
}
```

### Bundle分析

```bash
# webpack
npm run build -- --profile --json > stats.json
npx webpack-bundle-analyzer stats.json

# Vite
npm run build
npx vite-bundle-visualizer
```

---

## 🖼️ 图片优化

### 现代格式

```html
<!-- WebP优先，JPEG后备 -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="描述" loading="lazy">
</picture>

<!-- 响应式图片 -->
<img
  srcset="image-320w.jpg 320w,
          image-640w.jpg 640w,
          image-1280w.jpg 1280w"
  sizes="(max-width: 640px) 100vw,
         (max-width: 1280px) 50vw,
         33vw"
  src="image-640w.jpg"
  alt="描述"
>
```

### 压缩和调整尺寸

```javascript
// 自动压缩图片
const imagemin = require('imagemin')
const imageminWebp = require('imagemin-webp')

await imagemin(['images/*.{jpg,png}'], {
  destination: 'build/images',
  plugins: [
    imageminWebp({ quality: 75 })
  ]
})
```

---

## 🌐 网络优化

### HTTP/2和HTTP/3

```nginx
# nginx配置
server {
  listen 443 ssl http2;
  listen 443 ssl http3;

  ssl_protocols TLSv1.3;
}
```

### 缓存策略

```javascript
// Service Worker缓存
const CACHE_NAME = 'v1'
const urlsToCache = ['/', '/styles.css', '/script.js']

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  )
})

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  )
})

// Cache-Control头
// 服务器配置
app.use(express.static('public', {
  maxAge: '1y', // 静态资源
  setHeaders: (res, path) => {
    if (path.endsWith('.html')) {
      res.setHeader('Cache-Control', 'no-cache') // HTML文件
    }
  }
}))
```

### CDN使用

```html
<!-- 使用CDN加载库 -->
<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js"></script>

<!-- 预连接到CDN -->
<link rel="preconnect" href="https://cdn.jsdelivr.net">
```

---

## 🧪 性能测试

### Lighthouse

```bash
# 命令行运行
npx lighthouse https://example.com --view
npx lighthouse https://example.com --output=json --output=html

# CI中运行
npm install -g @lhci/cli
lhci autorun
```

### WebPageTest

```bash
# 使用API测试
curl "https://www.webpagetest.org/runtest.php?url=https://example.com&k=YOUR_API_KEY"
```

### Chrome DevTools

```javascript
// Performance API
// 测量特定操作
performance.mark('myOperation-start')
await performOperation()
performance.mark('myOperation-end')
performance.measure('myOperation', 'myOperation-start', 'myOperation-end')

const measure = performance.getEntriesByName('myOperation')[0]
console.log(`Duration: ${measure.duration}ms`)

// 测量LCP
new PerformanceObserver((list) => {
  const entries = list.getEntries()
  const lastEntry = entries[entries.length - 1]
  console.log('LCP:', lastEntry.startTime)
}).observe({ entryTypes: ['largest-contentful-paint'] })
```

---

## 📊 性能监控

### Real User Monitoring (RUM)

```javascript
// 发送性能数据到分析服务器
function sendToAnalytics(metric) {
  const body = JSON.stringify(metric)
  navigator.sendBeacon('/analytics', body)
}

// 测量LCP
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    sendToAnalytics({
      name: 'LCP',
      value: entry.startTime
    })
  }
}).observe({ entryTypes: ['largest-contentful-paint'] })

// 测量FID
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    sendToAnalytics({
      name: 'FID',
      value: entry.processingStart - entry.startTime
    })
  }
}).observe({ entryTypes: ['first-input'] })

// 测量CLS
let clsValue = 0
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      clsValue += entry.value
      sendToAnalytics({
        name: 'CLS',
        value: clsValue
      })
    }
  }
}).observe({ entryTypes: ['layout-shift'] })
```

---

## ✅ 性能检查清单

### 加载性能
- [ ] LCP < 2.5s
- [ ] 关键资源预加载
- [ ] 代码分割完成
- [ ] 懒加载实现
- [ ] 图片优化（WebP、压缩）

### 运行时性能
- [ ] FID < 100ms
- [ ] 无长任务（> 50ms）
- [ ] 帧率 ≥ 60fps
- [ ] 内存使用合理
- [ ] 虚拟滚动（长列表）

### 视觉稳定性
- [ ] CLS < 0.1
- [ ] 图片和视频设置尺寸
- [ ] 广告位预留空间
- [ ] 字体加载优化

### 网络性能
- [ ] HTTP/2启用
- [ ] 缓存策略配置
- [ ] CDN使用
- [ ] 资源压缩

---

## 📚 相关文档

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
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
