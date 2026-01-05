# Playful风格核心指南

> 🎈 **Core Components** - 按钮、卡片、输入框等核心组件样式

---

## 📖 文档说明

本文档提供 Playful（俏皮风格）的核心组件样式实现，包括按钮、卡片、输入框等基础组件的完整CSS代码。

**相关文档**：
- [装饰元素与动画](design-directions-playful-decoration-animation.md)
- [布局与游戏化](design-directions-playful-layout-gamification.md)
- [返回主文档](design-directions-playful.md)

---

## 🎨 组件风格

### 按钮

**主按钮**：

```css
.playful-button {
  background: var(--playful-gradient);
  border: none;
  border-radius: 50px;
  color: #fff;
  font-family: 'Nunito', sans-serif;
  font-weight: 700;
  padding: 16px 32px;
  box-shadow: 0 8px 20px rgba(255, 107, 107, 0.3);
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  position: relative;
  overflow: hidden;
}

.playful-button:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: 0 12px 30px rgba(255, 107, 107, 0.4);
}

.playful-button:active {
  transform: translateY(-2px) scale(1.02);
}

/* 按钮光效 */
.playful-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  transition: left 0.5s;
}

.playful-button:hover::before {
  left: 100%;
}
```

**次要按钮**：

```css
.playful-button.secondary {
  background: #fff;
  color: var(--playful-primary);
  border: 3px solid var(--playful-primary);
}

.playful-button.secondary:hover {
  background: var(--playful-primary);
  color: #fff;
  box-shadow: 0 8px 20px rgba(255, 107, 107, 0.3);
}
```

**图标按钮**：

```css
.playful-button.icon-only {
  width: 56px;
  height: 56px;
  padding: 0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.playful-button.icon-only:hover {
  transform: rotate(15deg) scale(1.1);
}
```

**幽灵按钮**：

```css
.playful-button.ghost {
  background: transparent;
  color: var(--playful-primary);
  border: none;
  box-shadow: none;
}

.playful-button.ghost:hover {
  background: rgba(255, 107, 107, 0.1);
  transform: translateY(-2px);
}
```

### 卡片

**基础卡片**：

```css
.playful-card {
  background: var(--playful-surface);
  border-radius: 24px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
  padding: 32px;
  transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  border: 3px solid transparent;
}

.playful-card:hover {
  transform: translateY(-8px) rotate(1deg);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
  border-color: var(--playful-accent);
}

/* 卡片标题 */
.playful-card-title {
  font-family: 'Nunito', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: var(--playful-primary);
  margin-bottom: 12px;
}

/* 卡片内容 */
.playful-card-body {
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #666;
}

/* 卡片图标 */
.playful-card-icon {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  background: var(--playful-gradient-alt);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  font-size: 32px;
  box-shadow: 0 8px 20px rgba(162, 155, 254, 0.3);
}
```

**卡片变体**：

```css
/* 彩色边框卡片 */
.playful-card.colorful {
  border: 3px solid;
  border-image: var(--playful-gradient) 1;
}

/* 玻璃态卡片 */
.playful-card.glass {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

/* 3D卡片 */
.playful-card.three-d {
  transform-style: preserve-3d;
  perspective: 1000px;
}

.playful-card.three-d:hover {
  transform: rotateY(10deg) rotateX(5deg);
}
```

### 输入框

**基础输入框**：

```css
.playful-input {
  background: #fff;
  border: 3px solid #e0e0e0;
  border-radius: 16px;
  color: #333;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
  padding: 16px 24px;
  transition: all 0.3s ease;
  width: 100%;
}

.playful-input:focus {
  outline: none;
  border-color: var(--playful-secondary);
  box-shadow: 0 0 0 6px rgba(78, 205, 196, 0.1);
  transform: scale(1.02);
}

.playful-input::placeholder {
  color: #aaa;
  font-weight: 500;
}

/* 错误状态 */
.playful-input.error {
  border-color: var(--playful-primary);
  box-shadow: 0 0 0 6px rgba(255, 107, 107, 0.1);
}

/* 成功状态 */
.playful-input.success {
  border-color: var(--playful-green);
  box-shadow: 0 0 0 6px rgba(149, 225, 211, 0.1);
}
```

**输入组**：

```css
.playful-input-group {
  display: flex;
  gap: 12px;
}

.playful-input-group .playful-input {
  flex: 1;
}

.playful-input-group .playful-button {
  flex-shrink: 0;
}
```

**文本域**：

```css
.playful-textarea {
  min-height: 120px;
  resize: vertical;
}
```

---

## 📋 最佳实践总结

### 1. 组件风格

- 使用大圆角（≥16px）
- 明亮但不刺眼的色彩
- 弹性动画效果
- 丰富的渐变

---

## 🔗 相关文档

- [装饰元素与动画](design-directions-playful-decoration-animation.md) - 装饰与动画详解
- [布局与游戏化](design-directions-playful-layout-gamification.md) - 布局与游戏化详解
- [返回主文档](design-directions-playful.md) - Playful风格总览
- [设计方向模板](./design-directions.md) - 5种设计方向完整概述

---

## 🔗 快速导航

- [返回aesthetics/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
