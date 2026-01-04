# 无障碍设计指南

> ♿ **WCAG AA标准** - 确保所有用户都能访问您的界面

---

## 📖 文档说明

本文档提供无障碍设计的完整指南，涵盖WCAG 2.1 AA标准的所有核心要求。

**目标读者**: 前端开发者、UI设计师
**文档长度**: 约280行
**阅读时间**: 约15分钟

---

## 🎯 无障碍核心原则

### WCAG 2.1 四大原则

| 原则 | 英文 | 说明 | 关键要求 |
|------|------|------|----------|
| **可感知性** | Perceivable | 用户必须能够感知信息 | 文本替代、时间媒体、适应、可区分 |
| **可操作性** | Operable | 用户必须能够操作界面 | 键盘访问、足够时间、癫痫预防、导航 |
| **可理解性** | Understandable | 用户必须能够理解信息 | 可读、可预测、输入协助 |
| **健壮性** | Robust | 内容必须健壮可靠 | 兼容辅助技术 |

---

## 🎨 颜色对比度

### 对比度要求（WCAG AA）

| 元素类型 | 最小对比度 | 示例 |
|----------|-----------|------|
| **普通文本** | 4.5:1 | 正文、段落 |
| **大文本** (18pt+) | 3:1 | 标题、大字 |
| **UI组件** | 3:1 | 按钮、边框、表单字段 |
| **图形对象** | 3:1 | 图标、图表 |

### 使用 OKLCH 颜色空间

```css
/* ✅ 推荐：使用 OKLCH 确保对比度 */
.text-primary {
  color: oklch(0.2 0.02 250);  /* 深色 */
  background: oklch(0.98 0.01 250);  /* 浅色 */
  /* 对比度: 16.5:1 ✅ */
}

.text-secondary {
  color: oklch(0.5 0.08 250);  /* 中等灰 */
  background: oklch(0.98 0.01 250);  /* 浅色 */
  /* 对比度: 5.2:1 ✅ */
}

/* ❌ 避免：对比度不足 */
.low-contrast {
  color: oklch(0.7 0.05 250);  /* 浅灰 */
  background: oklch(0.8 0.05 250);  /* 相近浅色 */
  /* 对比度: 1.8:1 ❌ 不足4.5:1 */
}
```

### 验证对比度

使用提供的工具验证颜色对比度：

```bash
# 检查HTML文件中的对比度
python scripts/validate/check-accessibility.py index.html

# 输出示例
# 🔴 CRITICAL: 颜色对比度不足: 2.8:1 (要求 4.5:1)
# 💡 建议: 调整前景色或背景色以提高对比度
```

---

## 🏷️ 语义化 HTML

### 正确使用 HTML 标签

```html
<!-- ✅ 正确：使用语义化标签 -->
<header>
  <nav aria-label="主导航">
    <ul>
      <li><a href="/home">首页</a></li>
      <li><a href="/products">产品</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>文章标题</h1>
    <p>文章内容...</p>
  </article>
  <aside aria-label="相关链接">
    <!-- 侧边栏内容 -->
  </aside>
</main>

<footer>
  <p>&copy; 2025 公司名称</p>
</footer>

<!-- ❌ 避免：过度使用 div -->
<div class="header">
  <div class="nav">
    <div class="nav-item">首页</div>
  </div>
</div>
```

### 标题层级规则

- 必须按顺序递增（h1 → h2 → h3）
- 不能跳级（h1 → h3 ❌）
- 每页只能有一个 h1

```html
<!-- ✅ 正确：按顺序递增 -->
<h1>页面主标题</h1>
  <h2>章节标题</h2>
    <h3>小节标题</h3>
  <h2>另一章节</h2>

<!-- ❌ 避免：跳级 -->
<h1>页面主标题</h1>
<h3>跳过 h2 ❌</h3>
```

---

## 🖼️ 图片替代文本

### Alt 属性规则

```html
<!-- ✅ 信息性图片：描述内容 -->
<img src="chart.png" alt="2025年销售增长30%的柱状图">

<!-- ✅ 装饰性图片：空 alt -->
<img src="divider.png" alt="" role="presentation">

<!-- ❌ 避免：缺失 alt -->
<img src="logo.png">
<!-- 屏幕阅读器会读出文件名或路径 -->

<!-- ❌ 避免：无意义的 alt -->
<img src="profile.jpg" alt="图片">
<!-- 应该描述图片内容，如"用户头像" -->
```

### 复杂图片的详细描述

```html
<img src="complex-chart.png" alt="销售趋势图" longdesc="#chart-desc">

<!-- 或使用 figure + figcaption -->
<figure>
  <img src="chart.png" alt="2025年Q1-Q4销售数据柱状图">
  <figcaption id="chart-desc">
    图表显示2025年四个季度的销售数据：
    Q1: 100万，Q2: 120万，Q3: 150万，Q4: 180万，
    全年增长80%。
  </figcaption>
</figure>
```

---

## 🔗 链接和按钮

### 链接文本规则

```html
<!-- ✅ 正确：描述性链接文本 -->
<a href="/user-guide">查看用户指南</a>
<a href="/downloads">下载 PDF 报告 (2MB)</a>

<!-- ❌ 避免：模糊的链接文本 -->
<a href="/guide">点击这里</a>
<a href="/more">更多</a>
<a href="https://example.com/very/long/url">https://example.com/very/long/url</a>
```

### 按钮可访问性

```html
<!-- ✅ 正确：使用 button 元素 -->
<button type="button">提交</button>
<button type="submit" aria-label="关闭对话框">×</button>

<!-- ⚠️ 谨慎：非 button 元素作按钮 -->
<div role="button" tabindex="0" aria-label="关闭">
  ×
</div>
<!-- 需要额外实现键盘事件处理 -->
```

---

## 📝 表单无障碍

### 标签关联

```html
<!-- ✅ 方法1: for + id -->
<label for="email">电子邮件</label>
<input type="email" id="email" name="email" required>

<!-- ✅ 方法2: 隐式关联 -->
<label>
  电子邮件
  <input type="email" name="email" required>
</label>

<!-- ✅ 方法3: aria-label -->
<input type="search" aria-label="搜索产品" placeholder="搜索...">

<!-- ✅ 方法4: aria-labelledby -->
<input type="text" id="field" aria-labelledby="label1 label2">
<span id="label1">用户名</span>
<span id="label2">（必填）</span>
```

### 表单验证提示

```html
<div class="form-group">
  <label for="password">密码</label>
  <input
    type="password"
    id="password"
    required
    minlength="8"
    aria-required="true"
    aria-describedby="password-hint password-error"
  >
  <small id="password-hint">至少8个字符</small>
  <span id="password-error" role="alert" aria-live="assertive">
    密码太短，至少需要8个字符
  </span>
</div>
```

---

## ⌨️ 键盘导航

### 焦点管理

```css
/* ✅ 为键盘用户提供可见焦点 */
:focus-visible {
  outline: 3px solid oklch(0.5 0.2 250);
  outline-offset: 2px;
}

/* 或使用 box-shadow */
:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.5 0.2 250);
}
```

### Tab 顺序

```html
<!-- 正确的 Tab 顺序应该是逻辑性的 -->
<form>
  <label for="name">姓名</label>
  <input type="text" id="name" tabindex="1">

  <label for="email">邮箱</label>
  <input type="email" id="email" tabindex="2">

  <button type="submit" tabindex="3">提交</button>
</form>
```

### 跳过导航链接

```html
<body>
  <!-- 首次加载时隐藏，Tab 时可见 -->
  <a href="#main-content" class="skip-link">跳到主内容</a>

  <header>导航栏...</header>

  <main id="main-content">
    主要内容
  </main>
</body>

<style>
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: oklch(0.2 0.02 250);
    color: white;
    padding: 8px;
    text-decoration: none;
    z-index: 100;
  }
  .skip-link:focus {
    top: 0;
  }
</style>
```

---

## 🎭 ARIA 属性

### 角色（Roles）

```html
<!-- 常用 ARIA 角色 -->
<div role="navigation" aria-label="主导航">
  <!-- 导航内容 -->
</div>

<div role="complementary" aria-label="侧边栏">
  <!-- 侧边栏内容 -->
</div>

<div role="alert" aria-live="assertive">
  操作成功！
</div>

<div role="status" aria-live="polite">
  已保存草稿
</div>
```

### 状态和属性

```html
<!-- 隐藏元素 -->
<div aria-hidden="true">
  <!-- 对屏幕阅读器隐藏 -->
</div>

<!-- 展开/收起状态 -->
<button aria-expanded="false" aria-controls="menu">
  显示菜单
</button>

<!-- 当前页面 -->
<nav aria-label="面包屑">
  <ol>
    <li><a href="/">首页</a></li>
    <li><a href="/products">产品</a></li>
    <li aria-current="page">详情</li>
  </ol>
</nav>

<!-- 加载状态 -->
<div role="status" aria-live="polite" aria-busy="true">
  正在加载...
</div>
```

---

## 🔍 动态内容更新

### 实时区域（Live Regions）

```html
<!-- 主动通知：立即通知 -->
<div role="alert" aria-live="assertive">
  表单提交失败，请检查错误
</div>

<!-- 被动通知：空闲时通知 -->
<div role="status" aria-live="polite">
  已自动保存
</div>

<!-- 非紧急：不中断用户 -->
<div aria-live="polite">
  还有 3 个未读消息
</div>
```

---

## 📋 无障碍检查清单

### 开发阶段检查

- [ ] 所有图片有描述性 alt 文本
- [ ] 颜色对比度符合 WCAG AA 标准
- [ ] 所有交互元素可键盘访问
- [ ] 表单输入有关联的 label
- [ ] 标题层级正确（不跳级）
- [ ] 链接文本具有描述性
- [ ] 焦点指示器清晰可见
- [ ] 动态内容使用 ARIA live regions

### 自动化测试

```bash
# 使用提供的无障碍检查工具
python scripts/validate/check-accessibility.html index.html

# 输出格式选项
python scripts/validate/check-accessibility.html index.html --format json
python scripts/validate/check-accessibility.html index.html --format markdown --output report.md
```

### 手动测试

1. **键盘导航测试**
   - 使用 Tab 键遍历所有交互元素
   - 确认焦点顺序符合逻辑
   - 确认焦点指示器可见

2. **屏幕阅读器测试**
   - macOS: VoiceOver (Cmd+F5)
   - Windows: NVDA (免费) 或 JAWS
   - Android: TalkBack
   - iOS: VoiceOver

3. **缩放测试**
   - 浏览器缩放到 200%
   - 确认布局不破坏
   - 确认内容仍可访问

---

## 🔗 相关资源

### 工具

- ** axe DevTools**: 浏览器扩展，无障碍检查
- ** WAVE**: Web Accessibility Evaluation Tool
- ** Lighthouse**: Chrome 内置性能和可访问性工具
- ** colour contrast analyser**: 颜色对比度检查

### 文档

- [WCAG 2.1 标准](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA 实践指南](https://www.w3.org/WAI/ARIA/apg/)
- [MDN 无障碍指南](https://developer.mozilla.org/zh-CN/docs/Web/Accessibility)

---

## 💡 最佳实践总结

1. **从一开始就考虑无障碍**，而非事后补救
2. **使用语义化 HTML**，这是无障碍的基础
3. **提供多种访问方式**，不依赖单一感官
4. **测试真实用户**，包括使用辅助技术的用户
5. **保持学习和改进**，无障碍是持续的过程

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
