# Playful风格装饰与动画

> 🎭 **Decoration & Animation** - 装饰元素、动画效果

---

## 📖 文档说明

本文档提供 Playful（俏皮风格）的装饰元素和动画效果实现，包括圆形装饰、波浪线、图标容器、彩虹边框、星星装饰，以及弹跳、脉冲、摇晃、浮动、旋转、渐变动画等。

**相关文档**：
- [核心组件](design-directions-playful-guide.md) - 按钮、卡片、输入框
- [布局与游戏化](design-directions-playful-layout-gamification.md) - 布局与游戏化
- [返回主文档](design-directions-playful.md)

---

## 🎭 装饰元素

### 圆形装饰

```css
.playful-circle {
  border-radius: 50%;
  background: var(--playful-gradient);
  box-shadow: 0 8px 20px rgba(255, 107, 107, 0.3);
  position: relative;
  overflow: hidden;
}

.playful-circle::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: conic-gradient(
    from 0deg,
    transparent 0deg,
    rgba(255, 255, 255, 0.3) 180deg,
    transparent 360deg
  );
  animation: rotate 4s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* 大圆形装饰 */
.playful-circle.large {
  width: 200px;
  height: 200px;
}

/* 中圆形装饰 */
.playful-circle.medium {
  width: 120px;
  height: 120px;
}

/* 小圆形装饰 */
.playful-circle.small {
  width: 64px;
  height: 64px;
}
```

### 波浪线装饰

```css
.playful-wave {
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 1200 120' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0v120c120 0 120-60 240-60s120 60 240 60 120-60 240-60 120 60 240-60 120 60 240 60V0z' fill='%23ffe66d' fill-opacity='0.1'/%3E%3C/svg%3E");
  background-size: 1200px 120px;
  animation: wave 10s linear infinite;
}

@keyframes wave {
  0% { background-position-x: 0; }
  100% { background-position-x: 1200px; }
}

/* 底部波浪 */
.playful-wave-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
}

/* 顶部波浪 */
.playful-wave-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 120px;
  transform: scaleY(-1);
}
```

### 图标容器

```css
.playful-icon-box {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  background: var(--playful-gradient-alt);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 20px rgba(162, 155, 254, 0.3);
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.playful-icon-box:hover {
  transform: scale(1.1) rotate(5deg);
  box-shadow: 0 12px 30px rgba(162, 155, 254, 0.4);
}

/* 图标容器变体 */
.playful-icon-box.primary {
  background: var(--playful-gradient);
}

.playful-icon-box.accent {
  background: var(--playful-gradient-warm);
}

/* 大图标容器 */
.playful-icon-box.large {
  width: 80px;
  height: 80px;
  font-size: 40px;
}
```

### 彩虹边框

```css
.playful-rainbow-border {
  position: relative;
  border-radius: 20px;
  padding: 4px;
  background: linear-gradient(135deg,
    var(--playful-primary),
    var(--playful-secondary),
    var(--playful-accent),
    var(--playful-purple));
  background-size: 300% 300%;
  animation: rainbow 3s ease infinite;
}

.playful-rainbow-border > * {
  background: #fff;
  border-radius: 16px;
}

@keyframes rainbow {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

### 星星装饰

```css
.playful-stars {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  pointer-events: none;
}

.playful-star {
  position: absolute;
  font-size: 24px;
  animation: twinkle 2s infinite;
  opacity: 0.6;
}

@keyframes twinkle {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.2); }
}

/* 随机位置星星 */
.playful-star:nth-child(1) { top: 10%; left: 20%; animation-delay: 0s; }
.playful-star:nth-child(2) { top: 30%; left: 80%; animation-delay: 0.5s; }
.playful-star:nth-child(3) { top: 70%; left: 30%; animation-delay: 1s; }
.playful-star:nth-child(4) { top: 50%; left: 70%; animation-delay: 1.5s; }
```

---

## 🎬 动画效果

### 弹跳动画

```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.playful-bounce {
  animation: bounce 2s infinite;
}

/* 快速弹跳 */
.playful-bounce-fast {
  animation: bounce 1s infinite;
}

/* 弹性弹跳 */
.playful-bounce-elastic {
  animation: bounce 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

### 脉冲动画

```css
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.playful-pulse {
  animation: pulse 2s infinite;
}

/* 脉冲阴影 */
.playful-pulse-shadow {
  animation: pulse-shadow 2s infinite;
}

@keyframes pulse-shadow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.4); }
  50% { box-shadow: 0 0 0 20px rgba(255, 107, 107, 0); }
}
```

### 摇晃动画

```css
@keyframes shake {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-5deg); }
  75% { transform: rotate(5deg); }
}

.playful-shake:hover {
  animation: shake 0.5s infinite;
}

/* 快速摇晃 */
.playful-shake-fast {
  animation: shake 0.2s infinite;
}
```

### 浮动动画

```css
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.playful-float {
  animation: float 3s ease-in-out infinite;
}

/* 浮动+旋转 */
.playful-float-rotate {
  animation:
    float 3s ease-in-out infinite,
    rotate 6s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

### 旋转动画

```css
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.playful-spin {
  animation: spin-slow 10s linear infinite;
}

/* 反向旋转 */
.playful-spin-reverse {
  animation: spin-slow 10s linear infinite reverse;
}

/* 快速旋转 */
.playful-spin-fast {
  animation: spin-slow 2s linear infinite;
}
```

### 渐变动画

```css
.playful-gradient-animated {
  background: linear-gradient(
    -45deg,
    var(--playful-primary),
    var(--playful-secondary),
    var(--playful-accent),
    var(--playful-purple)
  );
  background-size: 400% 400%;
  animation: gradient 5s ease infinite;
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

---

## 📋 最佳实践总结

### 2. 装饰元素

- 圆形、波浪等有趣形状
- 彩虹边框和渐变
- 星星等装饰元素
- 图标容器

### 3. 动画效果

- 弹跳、脉冲、摇晃
- 浮动、旋转
- 渐变动画
- 适度的动画时长（0.3-0.5s）

---

## 🔗 相关文档

- [核心组件](design-directions-playful-guide.md) - 按钮与卡片样式
- [布局与游戏化](design-directions-playful-layout-gamification.md) - 布局与游戏化元素
- [返回主文档](design-directions-playful.md) - Playful风格总览

---

## 🔗 快速导航

- [返回aesthetics/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
