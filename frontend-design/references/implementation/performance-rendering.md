# 性能渲染优化

> 📚 **性能优化系列 - 文档1/3** - 加载性能、运行时性能与构建优化
> 🔗 **返回主文档**：[性能优化指南](./performance-optimization.md)

---

## 📖 文档说明

本文档详细介绍前端渲染性能的优化策略，涵盖三个核心领域：

1. **🚀 加载性能优化** - 减少首屏加载时间
2. **💻 运行时性能优化** - 提升交互响应速度
3. **🗜️ 构建优化** - 减小打包体积

**相关文档**：
- [资源优化指南](./performance-resources.md) - 图片和网络优化
- [性能监控与测试](./performance-monitoring.md) - 测试和监控

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

## 📚 系列文档导航

- **[⬅️ 返回主文档](./performance-optimization.md)** - 查看完整的性能优化系列
- **[资源优化指南 ➡️](./performance-resources.md)** - 图片和网络优化
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
