# SEO最佳实践

> 🔍 **搜索引擎优化** - 提升排名和可见性

---

## 📖 核心概念

SEO（Search Engine Optimization）通过优化网站结构、内容和技术实现，提升在搜索引擎中的排名和可见性。

**核心目标**：
- 提高自然搜索流量
- 改善用户搜索体验
- 增强网站权威性
- 优化移动端体验

---

## 🏷️ 元数据优化

### 页面标题

```html
<!-- ✅ 好的做法：描述性、唯一、关键词前置 -->
<title>前端设计框架 - Vue/React/Svelte 最佳实践 | Site Name</title>

<!-- ✅ 主页 -->
<title>Site Name - 产品描述和价值主张</title>

<!-- ❌ 避免：通用、无描述 -->
<title>首页</title>
<title>Welcome</title>
```

### Meta描述

```html
<!-- ✅ 好的做法：150-160字符，包含关键词和行动号召 -->
<meta
  name="description"
  content="学习前端设计框架的最佳实践。涵盖Vue、React、Svelte的组件设计、状态管理、性能优化。立即提升开发效率！"
>

<!-- ✅ 产品页面 -->
<meta
  name="description"
  content="购买高质量产品，享受免费送货和30天退款保证。现在下单，立享20%折扣！"
>

<!-- ❌ 避免：过短、无价值 -->
<meta name="description" content="这是一个网页">
```

### Open Graph标签

```html
<!-- Facebook/LinkedIn/社交媒体分享 -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://example.com/page">
<meta property="og:title" content="前端设计框架 - Vue/React/Svelte 最佳实践">
<meta
  property="og:description"
  content="学习前端设计框架的最佳实践。涵盖Vue、React、Svelte的组件设计、状态管理、性能优化。"
>
<meta property="og:image" content="https://example.com/og-image.jpg">
<meta property="og:locale" content="zh_CN">
<meta property="og:site_name" content="Site Name">
```

### Twitter Card标签

```html
<!-- Twitter分享 -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@site_handle">
<meta name="twitter:creator" content="@creator_handle">
<meta name="twitter:title" content="前端设计框架 - Vue/React/Svelte 最佳实践">
<meta
  name="twitter:description"
  content="学习前端设计框架的最佳实践。涵盖Vue、React、Svelte的组件设计、状态管理、性能优化。"
>
<meta name="twitter:image" content="https://example.com/twitter-image.jpg">
```

---

## 📐 结构化数据

### JSON-LD格式

```html
<!-- 网站信息 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://example.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>

<!-- 组织信息 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+86-123-4567-8900",
    "contactType": "Customer Service"
  }
}
</script>

<!-- 文章/博客 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "文章标题",
  "image": "https://example.com/article-image.jpg",
  "author": {
    "@type": "Person",
    "name": "作者名"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2025-01-03",
  "dateModified": "2025-01-03",
  "description": "文章描述"
}
</script>

<!-- 产品 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "产品名称",
  "image": "https://example.com/product-image.jpg",
  "description": "产品描述",
  "brand": {
    "@type": "Brand",
    "name": "品牌名"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "CNY",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "120"
  }
}
</script>

<!-- 面包屑导航 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "首页",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "分类",
      "item": "https://example.com/category"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "文章标题",
      "item": "https://example.com/article"
    }
  ]
}
</script>
```

---

## 📝 内容优化

### 标题层次

```html
<!-- ✅ 好的做法：清晰的层次结构 -->
<h1>页面主标题（唯一）</h1>
  <h2>章节标题</h2>
    <h3>小节标题</h3>
    <h3>小节标题</h3>
  <h2>章节标题</h2>
    <h3>小节标题</h3>

<!-- ❌ 避免：跳过层次、多个H1 -->
<h1>标题</h1>
<h4>跳过H2和H3</h4>
<h1>第二个H1</h1>
```

### 关键词优化

```html
<!-- ✅ 好的做法：自然使用关键词 -->
<h1>前端设计框架 - Vue、React、Svelte最佳实践</h1>
<p>学习前端设计框架的核心概念和最佳实践。本文将介绍Vue、React、Svelte三大框架的组件设计、状态管理和性能优化技巧。</p>

<!-- ❌ 避免：关键词堆砌 -->
<p>前端框架、前端框架、前端框架、Vue框架、React框架、Svelte框架、前端设计框架、最佳前端框架、前端框架比较、前端框架教程...</p>
```

### 内部链接

```html
<!-- ✅ 好的做法：描述性锚文本 -->
<a href="/vue-guide">Vue组件设计指南</a>
<a href="/react-performance">React性能优化技巧</a>

<!-- ❌ 避免：无意义锚文本 -->
<a href="/vue-guide">点击这里</a>
<a href="/react-performance">更多</a>
```

---

## 🏗️ 技术SEO

### 规范URL

```html
<!-- 避免重复内容 -->
<link rel="canonical" href="https://example.com/original-page">

<!-- 分页 -->
<link rel="canonical" href="https://example.com/category">
<link rel="next" href="https://example.com/category?page=2">
<link rel="prev" href="https://example.com/category">
```

### Robots.txt

```txt
# 允许所有爬虫
User-agent: *
Allow: /

# 禁止特定目录
User-agent: *
Disallow: /admin/
Disallow: /private/

# 禁止特定文件
Disallow: /*.pdf

# 站点地图位置
Sitemap: https://example.com/sitemap.xml
```

### XML站点地图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-03</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/page1</loc>
    <lastmod>2025-01-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### 404页面

```html
<!-- 自定义404页面 -->
<!DOCTYPE html>
<html>
<head>
  <meta name="robots" content="noindex, follow">
  <title>页面未找到 - Site Name</title>
</head>
<body>
  <h1>页面未找到</h1>
  <p>抱歉，您访问的页面不存在。</p>
  <a href="/">返回首页</a>
  <!-- 提供有用的导航链接 -->
</body>
</html>
```

---

## 📱 移动端SEO

### 响应式设计

```html
<!-- 视口配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- 移动端URL（可选）-->
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.example.com">
<link rel="canonical" href="https://example.com">
```

### 移动友好测试

```javascript
// 确保触摸目标足够大（≥44×44px）
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
}

// 确保文本可读（≥16px）
body {
  font-size: 16px;
  line-height: 1.5;
}

// 避免水平滚动
body {
  max-width: 100%;
  overflow-x: hidden;
}
```

---

## ⚡ 性能和SEO

### Core Web Vitals

```html
<!-- 预加载关键资源 -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="main-font.woff2" as="font" crossorigin>

<!-- 预连接到外部域名 -->
<link rel="preconnect" href="https://cdn.example.com">
<link rel="dns-prefetch" href="https://analytics.example.com">
```

### 懒加载

```html
<!-- 图片懒加载 -->
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="描述">

<!-- iframe懒加载 -->
<iframe data-src="https://example.com/embed" loading="lazy"></iframe>
```

---

## 🔗 链接优化

### 内部链接结构

```html
<!-- 面包屑导航 -->
<nav aria-label="面包屑">
  <ol>
    <li><a href="/">首页</a></li>
    <li><a href="/category">分类</a></li>
    <li>当前页面</li>
  </ol>
</nav>

<!-- 相关文章 -->
<section>
  <h2>相关文章</h2>
  <ul>
    <li><a href="/article1">相关文章1</a></li>
    <li><a href="/article2">相关文章2</a></li>
  </ul>
</section>
```

### 外部链接

```html
<!-- 使用rel="noopener"防止安全风险 -->
<a href="https://example.com" rel="noopener nofollow">外部链接</a>

<!-- 赞助链接（nofollow） -->
<a href="https://sponsor.com" rel="sponsored nofollow">赞助商</a>

<!-- 用户生成内容（ugc） -->
<a href="https://user-comment.com" rel="ugc">用户链接</a>
```

---

## 🌍 国际化SEO

### hreflang标签

```html
<!-- 语言和地区变体 -->
<link rel="alternate" hreflang="en" href="https://example.com/en">
<link rel="alternate" hreflang="zh-CN" href="https://example.com/zh-CN">
<link rel="alternate" hreflang="zh-TW" href="https://example.com/zh-TW">
<link rel="alternate" hreflang="x-default" href="https://example.com">
```

### 多语言内容

```html
<html lang="zh-CN">

<!-- 或动态切换 -->
<html lang="<?php echo $currentLanguage; ?>">
```

---

## 📊 SEO工具和验证

### Google Search Console

```html
<!-- 验证所有权 -->
<meta name="google-site-verification" content="verification-code">

<!-- 或使用DNS TXT记录 -->
google-site-verification=verification-code
```

### 结构化数据测试

```bash
# Google富媒体结果测试
https://search.google.com/test/rich-results

# Schema.org验证器
https://validator.schema.org/
```

### 移动友好测试

```bash
# Google移动友好测试
https://search.google.com/test/mobile-friendly
```

---

## 🧪 SEO检查清单

### 元数据
- [ ] 每个页面有唯一的`<title>`
- [ ] Meta描述完整（150-160字符）
- [ ] Open Graph标签完整
- [ ] Twitter Card标签完整
- [ ] 规范URL（`<link rel="canonical">`）

### 结构化数据
- [ ] JSON-LD格式正确
- [ ] Schema.org标记完整
- [ ] 面包屑导航标记
- [ ] 文章/产品标记

### 内容
- [ ] H1标签唯一
- [ ] 标题层次清晰
- [ ] 关键词自然使用
- [ ] 内部链接完整
- [ ] 图片alt描述性

### 技术SEO
- [ ] XML站点地图
- [ ] Robots.txt配置
- [ ] 404页面自定义
- [ ] 重定向（301）
- [ ] 页面加载速度

### 移动端
- [ ] 响应式设计
- [ ] 移动友好测试通过
- [ ] 触摸元素足够大
- [ ] 无横向滚动

---

## 📚 相关文档

- [性能优化](./performance.md) - 性能最佳实践
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
