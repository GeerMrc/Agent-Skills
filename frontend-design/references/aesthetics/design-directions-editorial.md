# 编辑风格详解

> 📰 **Editorial** - 排版驱动的内容优先设计

---

## 📖 概述

受杂志和报纸启发的排版驱动设计。强调内容、排版层次、留白和视觉节奏。

**核心理念**：
- 内容为王
- 排版层次清晰
- 留白即奢侈
- 视觉节奏流畅

---

## 5. Editorial（编辑风格）

### 整体描述

受杂志和报纸启发的排版驱动设计。强调内容、排版层次、留白和视觉节奏。

**设计哲学**：
- "形式追随功能"在排版中的体现
- 优秀的内容不需要过度装饰
- 留白是设计的一部分
- 阅读体验优于视觉效果

### 色彩方案

```css
:root {
  /* 中性色彩 */
  --editorial-bg: #fafafa;
  --editorial-surface: #ffffff;
  --editorial-text: #1a1a1a;
  --editorial-text-muted: #666666;
  --editorial-accent: #c0392b;

  /* 分割线 */
  --editorial-divider: #e0e0e0;
  --editorial-divider-strong: #cccccc;

  /* 链接颜色 */
  --editorial-link: #0066cc;
  --editorial-link-hover: #004499;
}
```

**色彩特点**：
- 中性色为主（黑、白、灰）
- 强调色克制使用（通常1-2种）
- 高对比度确保可读性
- 淡雅的分割线

### 字体选择

```css
/* 标题：使用有性格的衬线字体 */
font-family: 'Libre Baskerville', 'Merriweather', 'Source Serif Pro', serif;

/* 正文：易读性优先 */
body {
  font-family: 'Source Serif Pro', Georgia, serif;
  font-size: 20px;
  line-height: 1.6;
  max-width: 70ch;
}

/* 大标题 */
h1 {
  font-family: 'Libre Baskerville', serif;
  font-size: 48px;
  font-weight: 400;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

/* 副标题：无衬线字体形成对比 */
h3 {
  font-family: 'Inter', system-ui, sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 14px;
}
```

**推荐字体**：
- `Libre Baskerville` - 优雅标题
- `Source Serif Pro` - 易读正文
- `Merriweather` - 经典衬线
- `Inter` - 无衬线副标题

### 排版层次

```css
/* H1 - 主标题 */
h1 {
  font-size: 42px;
  font-weight: 400;
  line-height: 1.2;
  margin-bottom: 24px;
}

/* H2 - 章节标题 */
h2 {
  font-size: 32px;
  font-weight: 400;
  line-height: 1.3;
  margin-top: 48px;
  margin-bottom: 16px;
}

/* H3 - 小节标题 */
h3 {
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 32px;
  margin-bottom: 12px;
}

/* H4 - 微标题 */
h4 {
  font-size: 18px;
  font-weight: 700;
  line-height: 1.4;
  margin-top: 24px;
  margin-bottom: 8px;
}

/* 正文 */
p {
  font-size: 20px;
  line-height: 1.6;
  margin-bottom: 24px;
}

/* 引用 */
blockquote {
  font-size: 24px;
  line-height: 1.4;
  font-style: italic;
  border-left: 4px solid var(--editorial-accent);
  padding-left: 24px;
  margin: 32px 0;
  color: var(--editorial-text-muted);
}

/* 列表 */
ul, ol {
  margin-bottom: 24px;
  padding-left: 24px;
}

li {
  margin-bottom: 8px;
  line-height: 1.6;
}
```

### 组件风格

#### 按钮

```css
.editorial-button {
  background: transparent;
  border: 1px solid var(--editorial-text);
  color: var(--editorial-text);
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 12px;
  padding: 16px 32px;
  transition: all 0.2s;
  border-radius: 2px;
}

.editorial-button:hover {
  background: var(--editorial-text);
  color: var(--editorial-surface);
}

/* 主要按钮 */
.editorial-button.primary {
  background: var(--editorial-accent);
  border-color: var(--editorial-accent);
  color: #fff;
}

.editorial-button.primary:hover {
  background: #a93226;
  border-color: #a93226;
}

/* 文字链接按钮 */
.editorial-button.text {
  border: none;
  padding: 0;
  color: var(--editorial-link);
  text-transform: none;
  letter-spacing: 0;
  font-size: 16px;
  border-bottom: 1px solid transparent;
}

.editorial-button.text:hover {
  background: transparent;
  color: var(--editorial-link-hover);
  border-bottom-color: var(--editorial-link-hover);
}
```

#### 卡片（文章卡片）

```css
.editorial-article {
  border-bottom: 1px solid var(--editorial-divider);
  padding: 48px 0;
  max-width: 900px;
}

.editorial-article-title {
  font-family: 'Libre Baskerville', serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 1.2;
  margin-bottom: 16px;
}

.editorial-article-title a {
  color: var(--editorial-text);
  text-decoration: none;
  transition: color 0.2s;
}

.editorial-article-title a:hover {
  color: var(--editorial-link);
}

.editorial-article-meta {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--editorial-text-muted);
  margin-bottom: 24px;
  display: flex;
  gap: 16px;
}

.editorial-article-excerpt {
  font-size: 20px;
  line-height: 1.6;
  color: var(--editorial-text-muted);
  margin-bottom: 24px;
}

.editorial-article-footer {
  display: flex;
  align-items: center;
  gap: 16px;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--editorial-text-muted);
}
```

#### 输入框

```css
.editorial-input {
  background: transparent;
  border: none;
  border-bottom: 2px solid var(--editorial-divider);
  border-radius: 0;
  color: var(--editorial-text);
  font-family: 'Source Serif Pro', serif;
  font-size: 18px;
  padding: 12px 0;
  transition: border-color 0.2s;
}

.editorial-input:focus {
  outline: none;
  border-color: var(--editorial-text);
}

.editorial-input::placeholder {
  color: var(--editorial-text-muted);
  font-style: italic;
}

/* 搜索框 */
.editorial-search {
  position: relative;
  max-width: 400px;
}

.editorial-search input {
  width: 100%;
  padding-right: 40px;
}

.editorial-search::after {
  content: '🔍';
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  font-size: 18px;
}
```

### 布局特点

```css
/* 大量留白 */
.editorial-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 80px 24px;
}

/* 网格系统 */
.editorial-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 48px;
}

.editorial-grid-sidebar {
  grid-column: 1 / 9;
}

.editorial-sidebar {
  grid-column: 9 / 13;
}

/* 文章流布局 */
.editorial-article-list {
  border-top: 4px solid var(--editorial-text);
}

.editorial-article-list > * {
  border-bottom: 1px solid var(--editorial-divider);
}

.editorial-article-list > *:first-child {
  border-top: 4px solid var(--editorial-text);
  margin-top: -4px;
}
```

**布局原则**：
- 大量留白（呼吸空间）
- 清晰的排版层次
- 网格系统对齐
- 强调阅读体验

### 装饰元素

```css
/* 分割线 */
.editorial-divider {
  border: none;
  border-top: 1px solid var(--editorial-divider);
  margin: 48px 0;
}

.editorial-divider.strong {
  border-top: 2px solid var(--editorial-divider-strong);
}

.editorial-divider.accent {
  border-top: 2px solid var(--editorial-accent);
}

/* 装饰性首字母 */
.editorial-dropcap::first-letter {
  font-family: 'Libre Baskerville', serif;
  font-size: 64px;
  float: left;
  line-height: 0.8;
  margin-right: 12px;
  margin-top: 8px;
}

/* 引用块 */
.editorial-pullquote {
  font-family: 'Libre Baskerville', serif;
  font-size: 32px;
  line-height: 1.3;
  font-weight: 400;
  color: var(--editorial-accent);
  padding: 48px 0;
  text-align: center;
  border-top: 1px solid var(--editorial-divider);
  border-bottom: 1px solid var(--editorial-divider);
  margin: 48px 0;
}

/* 图片说明 */
.editorial-caption {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: var(--editorial-text-muted);
  text-align: center;
  padding: 12px 0;
  border-bottom: 1px solid var(--editorial-divider);
  margin-top: 16px;
}
```

### 响应式设计

```css
/* 移动端 */
@media (max-width: 768px) {
  .editorial-container {
    padding: 48px 16px;
  }

  h1 {
    font-size: 32px;
  }

  h2 {
    font-size: 24px;
  }

  p {
    font-size: 18px;
  }

  .editorial-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .editorial-grid-sidebar,
  .editorial-sidebar {
    grid-column: 1;
  }
}

/* 平板 */
@media (min-width: 769px) and (max-width: 1024px) {
  .editorial-container {
    padding: 64px 32px;
  }

  h1 {
    font-size: 38px;
  }
}
```

### 适用产品

| 产品类型 | 适用理由 |
|----------|----------|
| 新闻和媒体网站 | 内容驱动，阅读优先 |
| 博客平台 | 文章为主，排版重要 |
| 出版物 | 杂志风格，专业可信 |
| 内容驱动的应用 | 降低视觉干扰 |

### Editorial最佳实践

✅ **推荐**：
- 大量留白（奢侈感）
- 清晰的排版层次
- 高对比度确保可读
- 限制行宽（50-75字符）

❌ **避免**：
- 过度装饰（干扰内容）
- 小字号（可读性差）
- 低对比度（难以阅读）
- 不一致的间距（视觉混乱）

---

## 📊 Editorial排版系统

### 标题系统

| 级别 | 字号 | 字重 | 行高 | 用途 |
|------|------|------|------|------|
| H1 | 42-48px | 400 | 1.2 | 文章标题 |
| H2 | 28-32px | 400 | 1.3 | 章节标题 |
| H3 | 14px | 600 | 1.4 | 微标题/标签 |
| H4 | 18px | 700 | 1.4 | 小节标题 |

### 间距系统

```css
/* 间距单位（基于8px网格） */
--editorial-space-xs: 8px;
--editorial-space-sm: 16px;
--editorial-space-md: 24px;
--editorial-space-lg: 32px;
--editorial-space-xl: 48px;
--editorial-space-2xl: 64px;
```

### 行宽建议

| 内容类型 | 最大行宽 | 字符数 |
|----------|----------|--------|
| 正文 | 65ch | 约50-75字符 |
| 标题 | 90ch | 无限制 |
| 引用 | 60ch | 约40-50字符 |

---

## 🎯 Editorial设计原则

### 1. 内容优先
- 排版服务于内容
- 装饰最小化
- 不干扰阅读

### 2. 层次清晰
- 标题层次分明
- 字号对比明显
- 字重变化微妙

### 3. 留白即奢侈
- 充足的段落间距
- 页面边距宽敞
- 图片周围留白

### 4. 视觉节奏
- 标题与正文交替
- 长短段落混合
- 图文穿插布局

---

## 📚 相关文档

- [设计方向模板](./design-directions.md) - 5种设计方向完整概述
- [现代风格详解](./design-directions-modern.md) - Brutalist、Retro-Futuristic
- [表现风格详解](./design-directions-expressive.md) - Luxury、Playful
- [排版指南](./typography.md) - 字体选择与排版 ⏳ 计划中

---

## 🔗 快速导航

- [返回aesthetics/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (文档重构：从design-directions.md拆分)
> **维护者**: 项目团队
