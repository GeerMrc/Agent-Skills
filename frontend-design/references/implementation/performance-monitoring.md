# 性能监控与测试

> 📚 **性能优化系列 - 文档3/3** - 性能测试、监控与检查清单
> 🔗 **返回主文档**：[性能优化指南](./performance-optimization.md)

---

## 📖 文档说明

本文档详细介绍性能测试、监控体系建设和完整的检查清单，涵盖三个核心领域：

1. **🧪 性能测试** - Lighthouse、WebPageTest、Chrome DevTools
2. **📊 性能监控** - Real User Monitoring、Core Web Vitals监控
3. **✅ 性能检查清单** - 完整的优化检查项

**相关文档**：
- [性能渲染优化](./performance-rendering.md) - 加载和运行时优化
- [资源优化指南](./performance-resources.md) - 图片和网络优化

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

**Lighthouse评分标准**：
- **Performance**: 0-100分（>90优秀）
- **Accessibility**: 0-100分（>90优秀）
- **Best Practices**: 0-100分（>90优秀）
- **SEO**: 0-100分（>90优秀）

### WebPageTest

```bash
# 使用API测试
curl "https://www.webpagetest.org/runtest.php?url=https://example.com&k=YOUR_API_KEY"
```

**WebPageTest关键指标**：
- **TTFB**: Time to First Byte
- **Start Render**: 首次渲染时间
- **Speed Index**: 视觉完整性
- **Load Time**: 完全加载时间

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

**DevTools使用技巧**：

1. **Performance面板**
   - 录制页面加载和交互
   - 分析长任务和渲染性能
   - 查看火焰图

2. **Network面板**
   - 分析资源加载顺序
   - 查看请求/响应大小
   - 检查缓存使用情况

3. **Coverage面板**
   - 检测未使用的CSS/JS
   - 优化代码分割
   - 减小包体积

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

### 监控最佳实践

#### 1. 数据采样策略
```javascript
// 采样率配置
const SAMPLING_RATE = 0.1 // 10%采样

if (Math.random() < SAMPLING_RATE) {
  // 发送监控数据
  sendToAnalytics(metrics)
}
```

#### 2. 分层监控
```javascript
// 页面级别监控
function trackPagePerformance() {
  const navigation = performance.getEntriesByType('navigation')[0]
  sendToAnalytics({
    pageLoadTime: navigation.loadEventEnd - navigation.fetchStart,
    domReady: navigation.domContentLoadedEventEnd - navigation.fetchStart
  })
}

// 资源级别监控
function trackResourceTiming() {
  const resources = performance.getEntriesByType('resource')
  resources.forEach(resource => {
    if (resource.duration > 1000) {
      sendToAnalytics({
        resource: resource.name,
        duration: resource.duration
      })
    }
  })
}
```

#### 3. 自定义指标
```javascript
// 业务指标监控
function trackCustomMetrics() {
  // 首次渲染时间
  const fcp = performance.getEntriesByName('first-contentful-paint')[0]

  // 可交互时间
  const tti = calculateTTI()

  // 自定义业务指标
  sendToAnalytics({
    fcp: fcp?.startTime,
    tti: tti,
    conversionRate: calculateConversion()
  })
}
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

## 🎯 优化优先级

### P0 - 必须优化（影响用户体验）
1. LCP > 4s
2. FID > 300ms
3. CLS > 0.25
4. 首屏白屏时间长

### P1 - 应该优化（改善体验）
1. TTFB > 1s
2. Bundle大小 > 500KB
3. 未优化的图片
4. 缺少缓存策略

### P2 - 可以优化（锦上添花）
1. 预连接优化
2. Service Worker缓存
3. 骨架屏改善
4. 动画优化

---

## 📚 系列文档导航

- **[⬅️ 返回主文档](./performance-optimization.md)** - 查看完整的性能优化系列
- **[性能渲染优化 ⬅️](./performance-rendering.md)** - 加载和运行时优化
- **[资源优化指南 ⬅️](./performance-resources.md)** - 图片和网络优化

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
> **最后更新**: 2026-01-04
> **维护者**: 项目团队
