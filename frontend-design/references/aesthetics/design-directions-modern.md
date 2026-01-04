# 现代风格详解

> 🎨 **Brutalist、Retro-Futuristic** - 原始与复古未来的碰撞

---

## 📖 概述

现代风格强调视觉冲击力和技术感，包含两个截然不同的方向：
- **Brutalist（野兽派）**：原始、粗犷、功能优先
- **Retro-Futuristic（复古未来主义）**：复古未来、霓虹、渐变

这两种风格都拒绝传统美学，追求独特的视觉识别度。

---

## 1. Brutalist（野兽派）

### 整体描述

原始、粗犷、未修饰的设计风格。强调功能性而非装饰，使用大胆的边框、强烈的对比和原始的排版。

**核心理念**：
- 形式追随功能
- 拒绝过度装饰
- 原始材料质感
- 大胆的视觉对比

### 色彩方案

```css
:root {
  /* 主色：高对比黑白 */
  --brutalist-bg: #ffffff;
  --brutalist-text: #000000;
  --brutalist-accent: #ff0000;
  --brutalist-border: #000000;

  /* 暗色模式 */
  --brutalist-dark-bg: #000000;
  --brutalist-dark-text: #ffffff;
  --brutalist-dark-accent: #00ff00;
}
```

**色彩特点**：
- 极简配色（通常2-3色）
- 高对比度（黑白对比）
- 强调色点缀（红色、绿色等）
- 无渐变或简单渐变

### 字体选择

```css
/* 避免Inter/Roboto，使用等宽或粗字体 */
font-family: 'Courier New', 'Space Mono', 'IBM Plex Mono', monospace;

/* 粗体标题 */
font-weight: 900;
text-transform: uppercase;
letter-spacing: -0.05em;
```

**推荐字体**：
- `Space Mono` - 现代等宽字体
- `IBM Plex Mono` - 可读性强的等宽字体
- `Courier New` - 经典等宽字体

**避免字体**：
- ❌ Inter、Roboto、Arial（过于通用）
- ❌ 衬线字体（与粗犷风格不符）

### 组件风格

#### 按钮

```css
.brutalist-button {
  background: transparent;
  border: 3px solid #000;
  color: #000;
  font-family: 'Space Mono', monospace;
  font-weight: 700;
  text-transform: uppercase;
  padding: 16px 32px;
  cursor: pointer;
  transition: all 0.1s;
}

.brutalist-button:hover {
  background: #000;
  color: #fff;
}

.brutalist-button:active {
  transform: translate(4px, 4px);
}

/* 主要按钮 */
.brutalist-button.primary {
  background: #000;
  color: #fff;
}

.brutalist-button.primary:hover {
  background: #fff;
  color: #000;
}
```

#### 卡片

```css
.brutalist-card {
  border: 4px solid #000;
  box-shadow: 8px 8px 0 #000;
  background: #fff;
  padding: 0;
  margin: 16px;
}

.brutalist-card:hover {
  transform: translate(-4px, -4px);
  box-shadow: 12px 12px 0 #000;
}

/* 卡片标题 */
.brutalist-card-title {
  border-bottom: 2px solid #000;
  padding: 16px;
  font-weight: 900;
  text-transform: uppercase;
}

/* 卡片内容 */
.brutalist-card-body {
  padding: 16px;
}
```

#### 输入框

```css
.brutalist-input {
  background: #fff;
  border: 3px solid #000;
  color: #000;
  font-family: 'Space Mono', monospace;
  font-size: 16px;
  padding: 12px 16px;
  border-radius: 0;
}

.brutalist-input:focus {
  outline: none;
  border-color: var(--brutalist-accent);
  box-shadow: 4px 4px 0 var(--brutalist-accent);
}
```

### 布局特点

```css
/* 使用CSS Grid创建不对称布局 */
.brutalist-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 0;
}

.brutalist-grid-item {
  border: 2px solid #000;
}

/* 大胆的间距（0或大间距） */
.brutalist-section {
  padding: 0;
  margin-bottom: 64px;
}

.brutalist-section.gap {
  padding: 32px;
}

/* 粗边框和分割线 */
.brutalist-divider {
  border: 4px solid #000;
  margin: 32px 0;
}

/* 无圆角或最小圆角 */
.brutalist-box {
  border-radius: 0;
}
```

**布局原则**：
- 使用CSS Grid创建不对称布局
- 大胆的间距（0或大间距）
- 粗边框和分割线
- 无圆角或最小圆角

### 适用产品

| 产品类型 | 适用理由 |
|----------|----------|
| 开发者工具 | 功能优先，技术感强 |
| 创意作品集 | 独特性强，视觉记忆点 |
| 实验性项目 | 自由度高，突破常规 |
| 独立博客 | 内容驱动，无干扰 |

### Brutalist最佳实践

✅ **推荐**：
- 保持极简配色（2-3色）
- 使用粗边框和阴影
- 等宽字体增强技术感
- 大胆的留白或密集布局

❌ **避免**：
- 过度装饰和渐变
- 圆角和柔和效果
- 衬线字体
- 复杂的动画效果

---

## 2. Retro-Futuristic（复古未来主义）

### 整体描述

80-90年代对未来的想象，霓虹色彩、渐变、几何形状。结合复古美学和现代技术。

**核心理念**：
- 80年代赛博朋克美学
- 霓虹灯光和暗色背景
- 合成波（Synthwave）风格
- 复古科技感

### 色彩方案

```css
:root {
  /* 霓虹色彩 */
  --retro-neon-pink: #ff00ff;
  --retro-neon-blue: #00ffff;
  --retro-neon-purple: #9d00ff;
  --retro-neon-yellow: #ffff00;

  /* 渐变背景 */
  --retro-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --retro-gradient-alt: linear-gradient(180deg, #ff00ff 0%, #9d00ff 100%);

  /* 暗色背景 */
  --retro-bg-dark: #0a0a1a;
  --retro-bg-light: #1a1a2e;
  --retro-bg-accent: #16213e;
}
```

**色彩特点**：
- 霓虹色（品红、青色、紫色）
- 深色背景（暗蓝、暗紫）
- 渐变效果（线性、径向）
- 辉光和阴影效果

### 字体选择

```css
/* 合成波风格字体 */
font-family: 'Orbitron', 'Rajdhani', 'Exo 2', sans-serif;

/* 标题效果 */
h1 {
  text-shadow:
    0 0 10px var(--retro-neon-pink),
    0 0 20px var(--retro-neon-pink),
    0 0 40px var(--retro-neon-pink);
}

/* 副标题 */
h2 {
  font-family: 'Rajdhani', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
```

**推荐字体**：
- `Orbitron` - 科幻风格标题
- `Rajdhani` - 技术感正文
- `Exo 2` - 现代感通用字体

### 组件风格

#### 按钮

```css
.retro-button {
  background: linear-gradient(180deg, #ff00ff 0%, #9d00ff 100%);
  border: none;
  color: #fff;
  font-family: 'Orbitron', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding: 12px 24px;
  box-shadow:
    0 0 20px rgba(255, 0, 255, 0.5),
    inset 0 0 20px rgba(255, 255, 255, 0.2);
  transition: all 0.3s;
  clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px);
}

.retro-button:hover {
  box-shadow:
    0 0 40px rgba(255, 0, 255, 0.8),
    inset 0 0 30px rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

/* 次要按钮 */
.retro-button.secondary {
  background: transparent;
  border: 2px solid var(--retro-neon-blue);
  color: var(--retro-neon-blue);
  box-shadow:
    0 0 10px rgba(0, 255, 255, 0.3),
    inset 0 0 10px rgba(0, 255, 255, 0.1);
}

.retro-button.secondary:hover {
  background: rgba(0, 255, 255, 0.1);
}
```

#### 卡片

```css
.retro-card {
  background: rgba(26, 26, 46, 0.9);
  border: 2px solid var(--retro-neon-blue);
  border-radius: 16px;
  backdrop-filter: blur(10px);
  box-shadow:
    0 0 20px rgba(0, 255, 255, 0.3),
    inset 0 0 20px rgba(0, 255, 255, 0.1);
  padding: 24px;
  position: relative;
  overflow: hidden;
}

.retro-card::before {
  content: '';
  position: absolute;
  inset: -2px;
  background: linear-gradient(45deg,
    var(--retro-neon-pink),
    var(--retro-neon-blue),
    var(--retro-neon-purple));
  border-radius: 16px;
  z-index: -1;
  opacity: 0.5;
  animation: borderGlow 3s linear infinite;
}

@keyframes borderGlow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

.retro-card:hover {
  box-shadow:
    0 0 40px rgba(0, 255, 255, 0.5),
    inset 0 0 30px rgba(0, 255, 255, 0.2);
}
```

#### 输入框

```css
.retro-input {
  background: rgba(26, 26, 46, 0.8);
  border: 2px solid var(--retro-neon-purple);
  border-radius: 8px;
  color: var(--retro-neon-blue);
  font-family: 'Rajdhani', sans-serif;
  font-size: 16px;
  padding: 12px 16px;
  box-shadow:
    0 0 10px rgba(157, 0, 255, 0.3),
    inset 0 0 10px rgba(157, 0, 255, 0.1);
}

.retro-input::placeholder {
  color: rgba(0, 255, 255, 0.5);
}

.retro-input:focus {
  outline: none;
  border-color: var(--retro-neon-blue);
  box-shadow:
    0 0 20px rgba(0, 255, 255, 0.5),
    inset 0 0 15px rgba(0, 255, 255, 0.2);
}
```

### 装饰元素

```css
/* 网格背景 */
.retro-grid-bg {
  background-image:
    linear-gradient(rgba(0, 255, 255, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 255, 0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  background-position: -1px -1px;
}

/* 扫描线效果 */
.retro-scanlines::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.15),
    rgba(0, 0, 0, 0.15) 1px,
    transparent 1px,
    transparent 2px
  );
  pointer-events: none;
}

/* 几何形状装饰 */
.retro-shape {
  position: absolute;
  border: 2px solid var(--retro-neon-pink);
  box-shadow: 0 0 10px var(--retro-neon-pink);
}

.retro-shape.circle {
  border-radius: 50%;
  width: 100px;
  height: 100px;
}

.retro-shape.triangle {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 86px solid var(--retro-neon-blue);
  box-shadow: 0 0 20px var(--retro-neon-blue);
}
```

### 动画效果

```css
/* 辉光动画 */
@keyframes neonGlow {
  0%, 100% {
    text-shadow:
      0 0 10px var(--retro-neon-pink),
      0 0 20px var(--retro-neon-pink),
      0 0 40px var(--retro-neon-pink);
  }
  50% {
    text-shadow:
      0 0 20px var(--retro-neon-pink),
      0 0 40px var(--retro-neon-pink),
      0 0 80px var(--retro-neon-pink);
  }
}

/* 渐变背景动画 */
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.retro-gradient-animated {
  background: linear-gradient(270deg,
    var(--retro-neon-pink),
    var(--retro-neon-blue),
    var(--retro-neon-purple));
  background-size: 600% 600%;
  animation: gradientShift 10s ease infinite;
}

/* 故障效果 */
@keyframes glitch {
  0% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
  100% { transform: translate(0); }
}

.retro-glitch:hover {
  animation: glitch 0.3s infinite;
}
```

### 适用产品

| 产品类型 | 适用理由 |
|----------|----------|
| 游戏界面 | 符合游戏美学，视觉震撼 |
| 音乐应用 | 沉浸式体验，情感共鸣 |
| 科技产品 | 传达创新和未来感 |
| 创意平台 | 独特风格，吸引眼球 |

### Retro-Futuristic最佳实践

✅ **推荐**：
- 霓虹色作为强调色
- 深色背景增强对比
- 适度的辉光和阴影
- 几何形状装饰

❌ **避免**：
- 过度使用动画（性能问题）
- 过多装饰元素（干扰内容）
- 低对比度文字（可读性差）
- 复杂的3D效果（加载慢）

---

## 🔄 两种风格的对比

### 相同点

| 方面 | Brutalist | Retro-Futuristic |
|------|-----------|-------------------|
| 拒绝传统美学 | ✅ | ✅ |
| 追求独特识别度 | ✅ | ✅ |
| 高视觉冲击力 | ✅ | ✅ |
| 非主流设计 | ✅ | ✅ |

### 差异点

| 方面 | Brutalist | Retro-Futuristic |
|------|-----------|-------------------|
| 色彩 | 黑白极简 | 霓虹多彩 |
| 质感 | 原始粗犷 | 未来科技 |
| 装饰 | 无装饰 | 大量装饰 |
| 动画 | 最少 | 丰富 |
| 氛围 | 冷酷 | 热情 |

---

## 🎯 使用场景建议

### 选择Brutalist当你需要：
- ✅ 传达技术专业性
- ✅ 强调功能和效率
- ✅ 创造原始冲击力
- ✅ 避免过度设计

### 选择Retro-Futuristic当你需要：
- ✅ 创造沉浸式体验
- ✅ 传达未来科技感
- ✅ 情感化用户界面
- ✅ 游戏化产品体验

---

## 📚 相关文档

- [设计方向模板](./design-directions.md) - 5种设计方向完整概述
- [表现风格详解](./design-directions-expressive.md) - Luxury、Playful
- [编辑风格详解](./design-directions-editorial.md) - Editorial

---

## 🔗 快速导航

- [返回aesthetics/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ✅ DONE
> **最后更新**: 2026-01-04 (文档重构：从design-directions.md拆分)
> **维护者**: 项目团队
