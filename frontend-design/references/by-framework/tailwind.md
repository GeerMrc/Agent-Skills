# Tailwind CSS 指南

> 🎨 **Utility-First CSS** - 快速构建现代界面

---

## 📖 文档说明

Tailwind CSS 是一个功能类优先的 CSS 框架，提供高度可定制的设计系统。本指南涵盖安装、配置、响应式设计和最佳实践。

**目标读者**: 前端开发者
**文档长度**: ~265行（主文档）
**阅读时间**: 约15分钟

**相关文档**:
- [完整配置指南](tailwind-guide.md) - 设计令牌、自定义配置、性能优化

---

## 🚀 安装和配置

### 使用 Vite 安装

```bash
# 创建项目
npm create vite@latest my-app -- --template react-ts

# 安装 Tailwind CSS
npm install -D tailwindcss postcss autoprefixer

# 初始化配置
npx tailwindcss init -p
```

### 配置文件

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      // 自定义设计令牌
      colors: {
        primary: {
          50: '#f0f9ff',
          500: '#0ea5e9',
          900: '#0c4a6e',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
```

### CSS 入口

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 自定义基础样式 */
@layer base {
  body {
    @apply font-sans text-gray-900 bg-white;
  }
}

/* 自定义组件样式 */
@layer components {
  .btn {
    @apply px-4 py-2 rounded font-medium transition-colors;
  }
  .btn-primary {
    @apply btn bg-blue-600 text-white hover:bg-blue-700;
  }
}
```

---

## 📱 响应式设计

### 移动优先

```jsx
// ✅ 默认移动端，使用 min-width 断点
<div className="
  w-full           /* 移动端：100% 宽度 */
  md:w-1/2         /* md及以上：50% 宽度 */
  lg:w-1/3         /* lg及以上：33% 宽度 */
">
  内容
</div>
```

### 响应式工具类

```jsx
<div className="
  p-4              /* 移动端：小内边距 */
  md:p-6           /* md及以上：中等内边距 */
  lg:p-8           /* lg及以上：大内边距 */
">
  响应式内边距
</div>

<button className="
  text-sm           /* 移动端：小字体 */
  md:text-base      /* md及以上：基础字体 */
  lg:text-lg        /* lg及以上：大字体 */
">
  响应式字体
</button>
```

---

## 🎯 组件模式

### 按钮组件

```jsx
// 基础按钮
<button className="
  px-4 py-2
  rounded-md
  font-medium
  transition-colors
  bg-blue-600
  text-white
  hover:bg-blue-700
  active:bg-blue-800
  disabled:bg-gray-400
  disabled:cursor-not-allowed
">
  点击我
</button>

// 按钮变体
<button className="btn-primary">主要按钮</button>
<button className="btn-secondary">次要按钮</button>
<button className="btn-ghost">幽灵按钮</button>
```

### 卡片组件

```jsx
<div className="
  bg-white
  rounded-lg
  shadow-md
  p-6
  hover:shadow-lg
  transition-shadow
">
  <h3 className="text-xl font-semibold mb-2">卡片标题</h3>
  <p className="text-gray-600">卡片内容...</p>
</div>
```

### 表单输入

```jsx
<div className="space-y-4">
  <div>
    <label htmlFor="email" className="block text-sm font-medium mb-1">
      邮箱
    </label>
    <input
      type="email"
      id="email"
      className="
        w-full
        px-3 py-2
        border border-gray-300
        rounded-md
        focus:outline-none
        focus:ring-2
        focus:ring-blue-500
        focus:border-transparent
      "
      placeholder="you@example.com"
    />
  </div>
</div>
```

---

## 🎭 状态变体

### 悬停状态

```jsx
<button className="
  bg-blue-600
  text-white
  hover:bg-blue-700
  hover:shadow-md
">
  悬停我
</button>
```

### 焦点状态

```jsx
<input className="
  border border-gray-300
  focus:outline-none
  focus:ring-2
  focus:ring-blue-500
  focus:border-transparent
" />
```

### 活动状态

```jsx
<button className="
  bg-blue-600
  active:bg-blue-800
  active:scale-95
  transition-transform
">
  点击我
</button>
```

### 禁用状态

```jsx
<button
  disabled
  className="
    bg-gray-400
    text-gray-700
    disabled:bg-gray-300
    disabled:cursor-not-allowed
  "
>
  禁用按钮
</button>
```

---

## 🎨 深色模式

### 配置深色模式

```javascript
// tailwind.config.js
export default {
  darkMode: 'class', // 或 'media'
  // ...
}
```

### 深色模式工具类

```jsx
<div className="
  bg-white
  text-gray-900
  dark:bg-gray-900
  dark:text-gray-100
">
  <h1 className="
    text-2xl
    font-bold
    dark:text-white
  ">
    深色模式标题
  </h1>
  <p className="
    text-gray-600
    dark:text-gray-400
  ">
    深色模式段落
  </p>
</div>
```

### 切换深色模式

```jsx
import { useEffect, useState } from 'react'

export function DarkModeToggle() {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [isDark])

  return (
    <button
      onClick={() => setIsDark(!isDark)}
      className="
        px-4 py-2
        rounded-md
        bg-gray-200
        dark:bg-gray-800
        text-gray-900
        dark:text-gray-100
      "
    >
      {isDark ? '浅色模式' : '深色模式'}
    </button>
  )
}
```

---

## 📋 最佳实践

### 组件提取

```jsx
// ❌ 避免：重复的工具类
<div className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">按钮1</div>
<div className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">按钮2</div>

// ✅ 推荐：提取为组件类
@layer components {
  .btn {
    @apply bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700;
  }
}

<div className="btn">按钮1</div>
<div className="btn">按钮2</div>
```

### 语义化命名

```jsx
// ✅ 使用有意义的类名
<div className="product-card">
  <h3 className="product-title">产品名称</h3>
  <p className="product-description">产品描述</p>
</div>

// 配合 @apply
@layer components {
  .product-card {
    @apply bg-white rounded-lg shadow-md p-6;
  }
  .product-title {
    @apply text-xl font-semibold mb-2;
  }
}
```

### 移动优先

```jsx
// ✅ 好的做法：默认移动端，逐步增强
<div className="w-full md:w-1/2 lg:w-1/3">
  响应式布局
</div>

// ❌ 避免：从桌面端开始
<div className="lg:w-1/3 md:w-1/2 w-full">
  难以维护
</div>
```

---

## ⚠️ 常见陷阱

### 避免的陷阱

```jsx
// ❌ 陷阱1：过度使用 arbitrary values
<div className="top-[123px] left-[456px]">位置</div>

// ✅ 正确做法：使用配置的间距
<div className="top-32 left-96">位置</div>

// ❌ 陷阱2：内联样式和 Tailwind 混用
<div style={{ padding: '1rem' }} className="p-4">重复</div>

// ✅ 正确做法：只使用 Tailwind
<div className="p-4">一致</div>

// ❌ 陷阱3：动态拼接类名
<div className={`text-${color}-600`}>动态颜色</div>

// ✅ 正确做法：使用完整的类名
<div className={color === 'blue' ? 'text-blue-600' : 'text-red-600'}>
  动态颜色
</div>
```

---

## 📋 功能总览

### 核心功能

| 功能 | 说明 | 详细文档 |
|------|------|----------|
| **设计令牌** | 颜色、间距、断点系统 | [查看详情](tailwind-guide.md#设计令牌系统) |
| **自定义配置** | 颜色、字体、动画 | [查看详情](tailwind-guide.md#自定义配置) |
| **性能优化** | JIT模式、清理样式 | [查看详情](tailwind-guide.md#性能优化) |
| **常用插件** | 表单、排版插件 | [查看详情](tailwind-guide.md#常用插件) |

---

## 📋 检查清单

### 配置

- [ ] 内容路径正确配置
- [ ] 设计令牌自定义
- [ ] 深色模式配置
- [ ] 必要的插件安装

### 使用

- [ ] 使用移动优先断点
- [ ] 组件样式提取到 @layer components
- [ ] 避免内联样式
- [ ] 使用完整的类名而非动态拼接

### 性能

- [ ] 启用 JIT 模式
- [ ] 清理未使用的样式
- [ ] 生产构建优化

---

## 🔗 相关资源

### 官方文档

- [Tailwind CSS 官方文档](https://tailwindcss.com/docs)
- [Tailwind UI 组件库](https://tailwindui.com/)

### 工具

- **Headwind UI**: 免费组件库
- **Tailwind Shades**: 颜色生成器
- **Tailwind CSS IntelliSense**: VSCode 插件

---

## 🔗 相关文档

- [完整配置指南](tailwind-guide.md) - 设计令牌、自定义配置、性能优化
- [React最佳实践](./react.md)
- [Vue最佳实践](./vue.md)
- [Svelte最佳实践](./svelte.md)
- [设计Token方法论](../methodology/design-tokens.md)

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
