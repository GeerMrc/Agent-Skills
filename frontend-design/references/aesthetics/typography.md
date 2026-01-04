# 排版指南

> ✍️ **Typography** - 构建可读、美观的文字系统

---

## 📖 文档说明

本文档提供Web排版的完整指南，涵盖字体选择、层级系统、响应式排版等核心内容。

**目标读者**: UI设计师、前端开发者
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 排版核心原则

### 可读性优先

| 原则 | 说明 | 应用 |
|------|------|------|
| **层级清晰** | 使用对比建立视觉层级 | 标题、正文、辅助文字 |
| **适度对比** | 文字与背景有足够对比 | 符合 WCAG AA 标准 |
| **舒适行宽** | 每行字符数控制在合理范围 | 45-75 个字符最佳 |
| **适当留白** | 段落、行间距适中 | 提升阅读舒适度 |

---

## 🔤 字体选择

### 字体分类

```css
/* 衬线体 - 传统、正式 */
@font-face {
  font-family: 'Merriweather';
  src: url('/fonts/merriweather.woff2') format('woff2');
}

/* 无衬线体 - 现代、简洁 */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter.woff2') format('woff2');
}

/* 等宽字体 - 代码、数据 */
@font-face {
  font-family: 'Fira Code';
  src: url('/fonts/fira-code.woff2') format('woff2');
}
```

### 字体配对

```css
/* ✅ 推荐：对比明显的配对 */
:root {
  --font-heading: 'Merriweather', serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
}

/* 标题使用衬线体 */
h1, h2, h3 {
  font-family: var(--font-heading);
}

/* 正文使用无衬线体 */
body {
  font-family: var(--font-body);
}

/* 代码使用等宽字体 */
code, pre {
  font-family: var(--font-mono);
}
```

### Web 安全字体

```css
/* 降级方案 */
font-family: 'Inter', -apple-system, BlinkMacSystemFont,
  'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
  'Helvetica Neue', sans-serif;
```

---

## 📏 字体大小系统

### 模块化比例（Type Scale）

```css
/* ✅ 推荐：使用模块化比例 */
:root {
  /* 基准字号 */
  --font-base: 16px;

  /* 黄金比例 (1.618) */
  --font-xs: calc(var(--font-base) * 0.75);   /* 12px */
  --font-sm: calc(var(--font-base) * 0.875);  /* 14px */
  --font-md: var(--font-base);                /* 16px */
  --font-lg: calc(var(--font-base) * 1.125);  /* 18px */
  --font-xl: calc(var(--font-base) * 1.25);   /* 20px */
  --font-2xl: calc(var(--font-base) * 1.5);   /* 24px */
  --font-3xl: calc(var(--font-base) * 1.875); /* 30px */
  --font-4xl: calc(var(--font-base) * 2.25);  /* 36px */
  --font-5xl: calc(var(--font-base) * 3);     /* 48px */
}
```

### 标题层级

```css
/* h1 - 页面主标题 */
h1 {
  font-size: var(--font-3xl);
  line-height: 1.2;
  font-weight: 700;
  letter-spacing: -0.02em;
}

/* h2 - 章节标题 */
h2 {
  font-size: var(--font-2xl);
  line-height: 1.3;
  font-weight: 600;
  letter-spacing: -0.01em;
}

/* h3 - 小节标题 */
h3 {
  font-size: var(--font-xl);
  line-height: 1.4;
  font-weight: 600;
}

/* h4 - 子标题 */
h4 {
  font-size: var(--font-lg);
  line-height: 1.5;
  font-weight: 600;
}
```

---

## 📐 行高和间距

### 行高（Line Height）

```css
/* ✅ 推荐：根据字号调整行高 */
:root {
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;
  --leading-loose: 2;
}

/* 标题：较紧的行高 */
h1, h2, h3 {
  line-height: var(--leading-tight);
}

/* 正文：标准行高 */
p {
  line-height: var(--leading-normal);
}

/* 长文本：宽松行高 */
article p {
  line-height: var(--leading-relaxed);
}
```

### 段落间距

```css
/* ✅ 推荐：段落间距 = 行高 */
article {
  p + p {
    margin-top: 1.5em; /* 与行高一致 */
  }
}

/* 或使用固定值 */
p {
  margin-bottom: 1rem;
}
```

---

## 🔤 字符间距（Letter Spacing）

### 字母间距

```css
/* ✅ 推荐：根据字号调整字母间距 */
:root {
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
}

/* 大标题：负字母间距 */
h1, h2 {
  letter-spacing: var(--tracking-tight);
}

/* 小号文字：正字母间距 */
small, .caption {
  letter-spacing: var(--tracking-wide);
}

/* 全大写文字：更宽间距 */
.uppercase {
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}
```

---

## 📱 响应式排版

### 流式字体

```css
/* ✅ 推荐：使用 clamp() 实现流式缩放 */
:root {
  /* 基准字号在 16px 到 20px 之间缩放 */
  --font-base: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);

  /* 标题也使用流式缩放 */
  --font-3xl: clamp(1.875rem, 1.5rem + 1.875vw, 2.5rem);
}

body {
  font-size: var(--font-base);
}
```

### 断点字体

```css
/* 移动端优先 */
body {
  font-size: 16px;
  line-height: 1.6;
}

@media (min-width: 768px) {
  body {
    font-size: 18px;
    line-height: 1.5;
  }
}

h1 {
  font-size: 1.75rem;
  line-height: 1.2;
}

@media (min-width: 768px) {
  h1 {
    font-size: 2.5rem;
    line-height: 1.1;
  }
}
```

---

## 🎨 字重（Font Weight）

### 字重系统

```css
/* ✅ 推荐：使用命名变量 */
:root {
  --font-thin: 100;
  --font-extralight: 200;
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
  --font-black: 900;
}

/* 正文 */
body {
  font-weight: var(--font-normal);
}

/* 强调 */
strong, b {
  font-weight: var(--font-bold);
}

/* 标题 */
h1, h2, h3 {
  font-weight: var(--font-semibold);
}
```

### 字重使用

```css
/* ✅ 好的做法：适度使用字重 */
.text-light { font-weight: 300; }
.text-normal { font-weight: 400; }
.text-medium { font-weight: 500; }
.text-semibold { font-weight: 600; }
.text-bold { font-weight: 700; }

/* ❌ 避免：过度使用极端字重 */
.text-thin { font-weight: 100; } /* 可读性差 */
.text-black { font-weight: 900; } /* 过粗 */
```

---

## 📐 行宽（Line Length）

### 推荐行宽

```css
/* ✅ 推荐：每行 45-75 个字符最佳 */
article {
  max-width: 65ch; /* 约 65 个字符 */
  margin: 0 auto;
}

/* 小屏幕 */
@media (max-width: 640px) {
  article {
    max-width: 100%;
    padding: 0 1rem;
  }
}
```

### 行宽过长的处理

```css
/* ✅ 好的做法：限制最大宽度 */
.content {
  max-width: 75ch;
  padding: 0 1rem;
}

/* ❌ 避免：无限宽的文本 */
.bad {
  width: 100%;
}
```

---

## 🎭 文本样式

### 强调文本

```css
/* 粗体强调 */
strong, b {
  font-weight: 600;
}

/* 斜体强调 */
em, i {
  font-style: italic;
}

/* 标记 */
mark {
  background: oklch(0.9 0.1 120);
  color: inherit;
  padding: 0.125em 0.25em;
  border-radius: 0.125em;
}
```

### 链接样式

```css
/* ✅ 推荐：清晰的链接样式 */
a {
  color: oklch(0.5 0.2 250);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}

a:hover {
  color: oklch(0.4 0.2 250);
  text-decoration-thickness: 2px;
}

a:focus-visible {
  outline: 2px solid oklch(0.5 0.2 250);
  outline-offset: 2px;
  border-radius: 2px;
}
```

---

## 📊 特殊场景

### 引用样式

```css
/* 块引用 */
blockquote {
  margin: 1.5em 0;
  padding: 0.5em 1.5em;
  border-left: 4px solid oklch(0.5 0.2 250);
  font-style: italic;
  color: oklch(0.4 0.02 250);
}

blockquote cite {
  display: block;
  margin-top: 1em;
  font-size: 0.875em;
  font-style: normal;
  color: oklch(0.5 0.05 250);
}
```

### 代码样式

```css
/* 行内代码 */
code {
  font-family: var(--font-mono);
  font-size: 0.875em;
  background: oklch(0.95 0.01 250);
  padding: 0.125em 0.375em;
  border-radius: 0.25em;
}

/* 代码块 */
pre {
  font-family: var(--font-mono);
  font-size: 0.875em;
  line-height: 1.6;
  background: oklch(0.15 0.01 250);
  color: oklch(0.95 0.01 250);
  padding: 1rem;
  border-radius: 0.5em;
  overflow-x: auto;
}

pre code {
  background: none;
  padding: 0;
}
```

### 列表样式

```css
/* 无序列表 */
ul {
  padding-left: 1.5em;
  list-style-type: disc;
}

ul li {
  margin-bottom: 0.5em;
}

ul li::marker {
  color: oklch(0.5 0.2 250);
}

/* 有序列表 */
ol {
  padding-left: 1.5em;
  list-style-type: decimal;
}

ol li {
  margin-bottom: 0.5em;
}
```

---

## 🧩 组件示例

### 标题组件

```css
.display-xl {
  font-size: clamp(2.5rem, 2rem + 2.5vw, 4rem);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.display-lg {
  font-size: clamp(2rem, 1.75rem + 1.25vw, 3rem);
  line-height: 1.2;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.headline-xl {
  font-size: var(--font-3xl);
  line-height: 1.2;
  font-weight: 600;
}
```

### 正文组件

```css
.lead {
  font-size: var(--font-xl);
  line-height: 1.6;
  color: oklch(0.4 0.02 250);
}

.body-lg {
  font-size: var(--font-lg);
  line-height: 1.6;
}

.body {
  font-size: var(--font-md);
  line-height: 1.5;
}

.body-sm {
  font-size: var(--font-sm);
  line-height: 1.5;
}
```

---

## 📋 排版检查清单

### 字体选择

- [ ] 选择易读的字体
- [ ] 提供合适的降级方案
- [ ] 考虑字重和字形的完整性

### 层级系统

- [ ] 建立清晰的标题层级
- [ ] 使用一致的字号比例
- [ ] 确保对比度符合 WCAG 标准

### 响应式

- [ ] 使用流式字体或断点字体
- [ ] 确保移动端可读性
- [ ] 测试多种屏幕尺寸

### 细节优化

- [ ] 行高适中
- [ ] 行宽控制在合理范围
- [ ] 字母间距适当
- [ ] 段落间距充足

---

## 💡 最佳实践总结

1. **可读性优先**：所有决策以提升可读性为目标
2. **建立系统**：使用统一的字号、行高、字重系统
3. **适度留白**：给文字足够的呼吸空间
4. **响应式设计**：确保在所有设备上都有良好体验
5. **测试验证**：在真实设备和浏览器上测试

---

## 🔗 相关资源

### 工具

- ** Typescale**: 模块化比例计算器
- ** Fontpair**: 字体配对灵感
- ** Google Fonts**: 免费 Web 字体库

### 文档

- [MDN Typography](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)
- [Butterick's Practical Typography](https://practicaltypography.com/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
