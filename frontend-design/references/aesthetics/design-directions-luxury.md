# Luxury风格详解

> 💎 **奢华风格** - 优雅、精致、高端的设计美学

---

## 📖 风格概述

Luxury（奢华风格）是优雅、精致、高端的设计风格，使用金色、深色、衬线字体，传递品质和价值感。

**核心理念**：
- 低调奢华
- 精致细节
- 品质传达
- 高端定位

**情感诉求**：
- 尊贵、优雅
- 专业、可信
- 高品质感
- 独特品味

---

## 🎨 色彩方案

### CSS变量定义

```css
:root {
  /* 金色系 */
  --luxury-gold: #d4af37;
  --luxury-gold-light: #f4e4bc;
  --luxury-gold-dark: #996515;

  /* 深色背景 */
  --luxury-bg-primary: #0c0c0c;
  --luxury-bg-secondary: #1a1a1a;
  --luxury-bg-tertiary: #2a2a2a;

  /* 文字颜色 */
  --luxury-text-primary: #f4e4bc;
  --luxury-text-secondary: #d4af37;
  --luxury-text-muted: #888888;

  /* 分割线和边框 */
  --luxury-border: #d4af37;
  --luxury-border-light: rgba(212, 175, 55, 0.3);
}
```

### 色彩特点

**金色系作为主色**：
- 传达价值感和品质感
- 不宜过度使用，克制优雅
- 使用渐变增加层次感

**深色背景**：
- 营造高级感和神秘感
- 提升金色元素的对比度
- 舒适的阅读体验

**低饱和度配色**：
- 克制优雅，不喧宾夺主
- 统一的色调体系
- 微妙的色彩变化

**精致渐变**：
- 135度线性渐变
- 金色深浅变化
- 增加视觉层次

---

## ✍️ 字体选择

### CSS字体定义

```css
/* 主字体设置 */
font-family: 'Playfair Display', 'Cormorant Garamond', 'Bodoni Moda', serif;

/* 标题字体 */
h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  font-weight: 400;
  letter-spacing: 0.02em;
}

/* 大标题 */
h1 {
  font-size: 48px;
  font-weight: 300;
  line-height: 1.2;
}

/* 中标题 */
h2 {
  font-size: 36px;
  font-weight: 400;
}

/* 副标题 */
h3 {
  font-family: 'Bodoni Moda', serif;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 14px;
}

/* 正文 */
body {
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  line-height: 1.8;
}

/* 小文字 */
small, .luxury-small {
  font-size: 14px;
  line-height: 1.6;
}
```

### 推荐字体

| 字体 | 用途 | 特点 |
|------|------|------|
| **Playfair Display** | 标题 | 优雅、精致、高对比度 |
| **Cormorant Garamond** | 正文 | 易读、流畅、现代感 |
| **Bodoni Moda** | 副标题 | 时尚、纤细、精致 |

### 字体最佳实践

**✅ DO**：
- 使用衬线字体营造优雅感
- 标题使用大字号（≥36px）
- 正文使用舒适行高（1.6-1.8）
- 使用大写字母和字母间距

**❌ DON'T**：
- 使用无衬线字体（失去优雅）
- 过小的字号（<14px）
- 过紧的行高（<1.4）
- 过多的字重变化

---

## 🎨 组件风格

### 按钮

**主按钮**：
```css
.luxury-button {
  background: linear-gradient(135deg,
    var(--luxury-gold-dark) 0%,
    var(--luxury-gold) 100%);
  border: 1px solid var(--luxury-gold);
  color: var(--luxury-bg-primary);
  font-family: 'Bodoni Moda', serif;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 16px 48px;
  border-radius: 2px;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

.luxury-button::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,
    transparent 0%,
    rgba(255,255,255,0.2) 100%);
  opacity: 0;
  transition: opacity 0.3s;
}

.luxury-button:hover::before {
  opacity: 1;
}

.luxury-button:hover {
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.3);
  transform: translateY(-2px);
}
```

**次要按钮**：
```css
.luxury-button.secondary {
  background: transparent;
  border: 1px solid var(--luxury-gold);
  color: var(--luxury-gold);
}

.luxury-button.secondary:hover {
  background: rgba(212, 175, 55, 0.1);
}
```

### 卡片

```css
.luxury-card {
  background: var(--luxury-bg-secondary);
  border: 1px solid var(--luxury-gold-dark);
  border-radius: 4px;
  padding: 40px;
  position: relative;
  transition: all 0.4s ease;
}

/* 内装饰线 */
.luxury-card::after {
  content: '';
  position: absolute;
  top: 20px;
  left: 20px;
  right: 20px;
  bottom: 20px;
  border: 1px solid var(--luxury-gold-light);
  pointer-events: none;
}

.luxury-card:hover {
  box-shadow: 0 16px 48px rgba(212, 175, 55, 0.15);
  transform: translateY(-4px);
}

/* 卡片标题 */
.luxury-card-title {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  font-weight: 400;
  color: var(--luxury-text-primary);
  margin-bottom: 16px;
  border-bottom: 1px solid var(--luxury-border-light);
  padding-bottom: 16px;
}

/* 卡片内容 */
.luxury-card-body {
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  line-height: 1.8;
  color: var(--luxury-text-muted);
}
```

### 输入框

```css
.luxury-input {
  background: transparent;
  border: 1px solid var(--luxury-border-light);
  border-radius: 0;
  color: var(--luxury-text-primary);
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  padding: 16px 20px;
  transition: all 0.3s ease;
}

.luxury-input:focus {
  outline: none;
  border-color: var(--luxury-gold);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
}

.luxury-input::placeholder {
  color: var(--luxury-text-muted);
  font-style: italic;
}

/* 文本域 */
.luxury-textarea {
  min-height: 120px;
  resize: vertical;
}
```

---

## 🎭 装饰元素

### 金色分割线

```css
.luxury-divider {
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    var(--luxury-gold) 50%,
    transparent 100%);
  margin: 40px 0;
}
```

### 装饰性边框

```css
.luxury-frame {
  border: 1px solid var(--luxury-gold-dark);
  padding: 32px;
  position: relative;
}

/* 角落装饰 */
.luxury-frame::before,
.luxury-frame::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border: 1px solid var(--luxury-gold);
}

.luxury-frame::before {
  top: -1px;
  left: -1px;
  border-right: none;
  border-bottom: none;
}

.luxury-frame::after {
  bottom: -1px;
  right: -1px;
  border-left: none;
  border-top: none;
}
```

### 微妙纹理

```css
.luxury-texture {
  background-image:
    repeating-linear-gradient(45deg,
      transparent,
      transparent 10px,
      rgba(212, 175, 55, 0.03) 10px,
      rgba(212, 175, 55, 0.03) 20px
    );
}
```

---

## 📐 布局特点

### CSS布局定义

```css
/* 丰富的留白 */
.luxury-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 80px 40px;
}

/* 居中对齐营造对称感 */
.luxury-centered {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 精致网格布局 */
.luxury-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 40px;
  padding: 40px 0;
}
```

### 布局原则

**1. 丰富的留白**：
- 内容区域留白 ≥ 60px
- 元素间距 ≥ 32px
- 营造高级感和呼吸感

**2. 对称布局为主**：
- 居中对齐
- 左右对称
- 稳定感和秩序感

**3. 精致的间距**：
- 使用8px栅格系统（32px、40px、48px）
- 统一的间距体系
- 垂直韵律一致

**4. 微妙的动画效果**：
- 0.3s 缓动过渡
- 轻微的位移（≤4px）
- 不抢眼的动效

---

## 🏢 适用产品

| 产品类型 | 适用理由 | 典型案例 |
|----------|----------|----------|
| **奢侈品电商** | 传达品质和价值 | 高端时尚、珠宝、腕表 |
| **高端服务** | 专业可信形象 | 法律、金融、咨询 |
| **金融产品** | 安全可靠感 | 私人银行、投资管理 |
| **艺术作品集** | 品味和格调 | 设计师、摄影师作品集 |

---

## ✅ Luxury最佳实践

### DO（推荐）

**色彩**：
- ✅ 金色系但不过度（克制优雅）
- ✅ 深色背景提升高级感
- ✅ 低饱和度配色保持克制

**排版**：
- ✅ 大量留白（高级感）
- ✅ 衬线字体（精致感）
- ✅ 大字号标题（≥36px）

**装饰**：
- ✅ 微妙动画（不抢眼）
- ✅ 精致边框和分割线
- ✅ 纹理增加层次

### DON'T（避免）

**色彩**：
- ❌ 过度使用金色（俗气）
- ❌ 高饱和度色彩（廉价感）
- ❌ 过多渐变效果

**排版**：
- ❌ 无衬线字体（失去优雅）
- ❌ 过小字号（<14px）
- ❌ 过紧行高（<1.4）

**装饰**：
- ❌ 过度动画（破坏克制感）
- ❌ 过多装饰元素
- ❌ 不一致的样式

---

## 📊 实现示例

### 示例1：产品卡片

```html
<div class="luxury-card">
  <img src="product.jpg" alt="产品" class="luxury-card-image">
  <h3 class="luxury-card-title">精致产品名称</h3>
  <p class="luxury-card-body">
    产品描述文字，传达品质和价值感。
  </p>
  <button class="luxury-button">了解更多</button>
</div>
```

### 示例2：服务列表

```html
<div class="luxury-grid">
  <div class="luxury-card">
    <h3 class="luxury-card-title">服务一</h3>
    <p class="luxury-card-body">服务描述</p>
  </div>
  <div class="luxury-card">
    <h3 class="luxury-card-title">服务二</h3>
    <p class="luxury-card-body">服务描述</p>
  </div>
  <div class="luxury-card">
    <h3 class="luxury-card-title">服务三</h3>
    <p class="luxury-card-body">服务描述</p>
  </div>
</div>
```

### 示例3：联系表单

```html
<form class="luxury-form">
  <div class="luxury-form-group">
    <label>姓名</label>
    <input type="text" class="luxury-input" placeholder="请输入姓名">
  </div>
  <div class="luxury-form-group">
    <label>邮箱</label>
    <input type="email" class="luxury-input" placeholder="请输入邮箱">
  </div>
  <div class="luxury-form-group">
    <label>留言</label>
    <textarea class="luxury-input luxury-textarea" placeholder="请输入留言"></textarea>
  </div>
  <button type="submit" class="luxury-button">提交</button>
</form>
```

---

## 🔗 相关文档

- [表现风格详解](./design-directions-expressive.md) - Luxury & Playful总览
- [Playful风格详解](./design-directions-playful.md) - 俏皮风格规范
- [设计方向模板](./design-directions.md) - 5种设计方向完整概述
- [色彩理论](./color-theory.md) - 色彩系统基础

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (从design-directions-expressive.md拆分)
> **维护者**: 项目团队
