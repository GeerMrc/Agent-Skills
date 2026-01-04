# 资源优化指南

> 📚 **性能优化系列 - 文档2/3** - 图片优化与网络优化
> 🔗 **返回主文档**：[性能优化指南](./performance-optimization.md)

---

## 📖 文档说明

本文档详细介绍静态资源和网络层面的性能优化策略，涵盖两个核心领域：

1. **🖼️ 图片优化** - 现代格式、压缩调整、响应式图片
2. **🌐 网络优化** - HTTP/2、缓存策略、CDN使用

**相关文档**：
- [性能渲染优化](./performance-rendering.md) - 加载和运行时优化
- [性能监控与测试](./performance-monitoring.md) - 测试和监控

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

### 图片优化最佳实践

1. **使用现代格式**
   - WebP：比JPEG小25-35%
   - AVIF：比WebP再小20%
   - 提供fallback支持

2. **响应式图片**
   - 使用srcset提供多种尺寸
   - 使用sizes控制选择逻辑
   - 结合picture元素实现艺术指导

3. **懒加载策略**
   - 使用loading="lazy"原生支持
   - Intersection Observer作为后备
   - 为首屏图片预加载

4. **压缩工具**
   - imagemin：构建时压缩
   - sharp：服务器端处理
   - squoosh：在线优化工具

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

**HTTP/2优势**：
- 多路复用：单个TCP连接并发请求
- 服务器推送：主动推送关键资源
- 头部压缩：减少传输开销
- 二进制协议：更高效解析

**HTTP/3优势**：
- 基于UDP：减少连接建立时间
- 解决队头阻塞：独立的数据流
- 更好的网络切换支持

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

**缓存策略分层**：

1. **强缓存**
   - Cache-Control: max-age=31536000
   - 适用于：版本化的静态资源

2. **协商缓存**
   - ETag：内容哈希
   - Last-Modified：修改时间
   - 适用于：HTML文件

3. **Service Worker**
   - 离线支持
   - 缓存优先策略
   - 网络优先策略

### CDN使用

```html
<!-- 使用CDN加载库 -->
<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js"></script>

<!-- 预连接到CDN -->
<link rel="preconnect" href="https://cdn.jsdelivr.net">
```

**CDN最佳实践**：

1. **选择合适的CDN**
   - Cloudflare：全球覆盖
   - AWS CloudFront：AWS集成
   - Vercel/Netlify：现代平台

2. **优化CDN配置**
   - 启用HTTP/2
   - 配置缓存规则
   - 使用边缘函数

3. **预连接优化**
   - dns-prefetch：DNS解析
   - preconnect：TCP握手
   - preload：资源预加载

---

## 📊 网络性能指标

### 关键指标

- **TTFB** (Time to First Byte) < 800ms
- **FCP** (First Contentful Paint) < 1.8s
- **LCP** (Largest Contentful Paint) < 2.5s

### 优化检查清单

#### 传输优化
- [ ] 启用HTTP/2或HTTP/3
- [ ] 启用Gzip或Brotli压缩
- [ ] 使用CDN分发静态资源
- [ ] 优化TLS握手时间

#### 缓存优化
- [ ] 配置Cache-Control头
- [ ] 使用ETag和Last-Modified
- [ ] 实现Service Worker缓存
- [ ] 设置合理的缓存时长

#### 资源优化
- [ ] 图片使用WebP格式
- [ ] 实现响应式图片
- [ ] 启用图片懒加载
- [ ] 压缩所有静态资源

---

## 📚 系列文档导航

- **[⬅️ 返回主文档](./performance-optimization.md)** - 查看完整的性能优化系列
- **[性能渲染优化 ⬅️](./performance-rendering.md)** - 加载和运行时优化
- **[性能监控与测试 ➡️](./performance-monitoring.md)** - 测试和监控

---

## 🔗 快速导航

- [返回implementation/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04
> **维护者**: 项目团队
