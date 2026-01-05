# Tailwind CSS 自定义与优化

> 🎨 **Customization & Optimization** - 性能优化、插件、最佳实践

---

## 📖 文档说明

本文档提供 Tailwind CSS 的自定义配置、性能优化和常用插件详解。

**相关文档**：
- [指南总览](tailwind-guide.md) - 设计令牌、自定义配置、主题系统
- [返回主文档](tailwind.md)

---

## ⚡ 性能优化

### JIT 模式

Tailwind CSS 3.0+ 默认使用 JIT（即时）编译，只生成使用的样式。

```javascript
// tailwind.config.js
export default {
  // JIT 默认启用
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  // 可选：配置 JIT 行为
  jit: true,
}
```

### 清理未使用的样式

使用 PurgeCSS 或 Tailwind 的内置清理功能。

```javascript
// tailwind.config.js
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  // 生产环境自动清理
  purge: {
    enabled: process.env.NODE_ENV === 'production',
    content: ['./src/**/*.{js,ts,jsx,tsx}'],
    options: {
      safelist: [
        // 保留特定类名
        'bg-blue-500',
        /^bg-/, // 正则表达式
      ],
    },
  },
}
```

### 使用 @tailwindcss/erase

```bash
# 安装
npm install -D @tailwindcss/erase
```

```javascript
// tailwind.config.js
export default {
  plugins: [
    require('@tailwindcss/erase'),
  ],
}
```

### 生产构建优化

```javascript
// postcss.config.js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    // 添加 CSS 压缩
    ...(process.env.NODE_ENV === 'production'
      ? {
          cssnano: {
            preset: 'default',
          },
        }
      : {}),
  },
}
```

### 优化 CSS 大小

```javascript
// tailwind.config.js
export default {
  // 禁用未使用的核心插件
  corePlugins: {
    preflight: false, // 禁用基础样式重置
  },
  // 自定义 safelist
  safelist: [
    {
      pattern: /bg-/,
      variants: ['hover', 'focus'],
    },
  ],
}
```

---

## 🔧 常用插件

### 表单插件 (@tailwindcss/forms)

```bash
npm install -D @tailwindcss/forms
```

```javascript
// tailwind.config.js
export default {
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

**表单插件功能**：
- 自动美化表单元素
- 统一的表单样式
- 深色模式支持
- 自定义表单样式

### 排版插件 (@tailwindcss/typography)

```bash
npm install -D @tailwindcss/typography
```

```javascript
// tailwind.config.js
export default {
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

```jsx
<article className="prose dark:prose-invert lg:prose-xl">
  <h1>文章标题</h1>
  <p>文章内容...</p>
</article>
```

**排版插件修饰符**：
- `prose-sm`: 小号排版
- `prose-base`: 基础排版
- `prose-lg`: 大号排版
- `prose-xl`: 特大号排版
- `prose-2xl`: 超大号排版
- `dark:prose-invert`: 深色模式
- `prose-headings`: 标题样式
- `prose-h1`: H1 样式

### 容器查询插件 (@tailwindcss/container-queries)

```bash
npm install -D @tailwindcss/container-queries
```

```javascript
// tailwind.config.js
export default {
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
}
```

```jsx
<div className="@container">
  <div className="@lg:text-xl">
    响应式文本
  </div>
</div>
```

### Aspect Ratio 插件 (@tailwindcss/aspect-ratio)

```bash
npm install -D @tailwindcss/aspect-ratio
```

```javascript
// tailwind.config.js
export default {
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

```jsx
<div className="aspect-w-16 aspect-h-9">
  <iframe src="..." />
</div>
```

---

## 🎨 自定义组件样式

### 按钮样式变体

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#3b82f6',
          hover: '#2563eb',
          active: '#1d4ed8',
        },
      },
    },
  },
}
```

```jsx
// 基础按钮
<button className="px-4 py-2 bg-primary text-white rounded hover:bg-primary-hover active:bg-primary-active">
  按钮
</button>

// 大按钮
<button className="px-6 py-3 bg-primary text-white rounded-lg text-lg hover:bg-primary-hover">
  大按钮
</button>
```

### 卡片组件

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      boxShadow: {
        card: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'card-hover': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
    },
  },
}
```

```jsx
<div className="p-6 bg-white rounded-lg shadow-card hover:shadow-card-hover transition-shadow duration-300">
  <h3 className="text-lg font-semibold mb-2">卡片标题</h3>
  <p className="text-gray-600">卡片内容</p>
</div>
```

### 表单输入

```jsx
// 文本输入
<input
  type="text"
  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
  placeholder="请输入..."
/>

// 选择框
<select className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
  <option>选项1</option>
  <option>选项2</option>
</select>
```

---

## 📋 最佳实践

### 1. 使用 @apply 指令

```css
/* components.css */
.btn {
  @apply px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600;
}

.card {
  @apply p-6 bg-white rounded-lg shadow-md;
}
```

### 2. 创建可复用的组件类

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      // 使用 @layer 添加基础样式
      spacing: {
        '128': '32rem',
      },
    },
  },
}
```

```css
/* styles.css */
@layer components {
  .btn-primary {
    @apply px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600;
  }

  .card {
    @apply p-6 bg-white rounded-lg shadow-md;
  }
}
```

### 3. 使用 CSS 变量

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        primary: 'var(--color-primary)',
        secondary: 'var(--color-secondary)',
      },
    },
  },
}
```

```css
/* :root {
  --color-primary: #3b82f6;
  --color-secondary: #6366f1;
} */
```

### 4. 响应式设计

```jsx
// 移动优先
<div className="w-full md:w-1/2 lg:w-1/3">
  响应式布局
</div>

// 响应式显示
<div className="hidden md:block">
  桌面端显示
</div>

// 响应式间距
<div className="p-4 md:p-6 lg:p-8">
  响应式内边距
</div>
```

### 5. 深色模式

```jsx
// 使用深色模式变体
<div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  深色模式支持
</div>

// 使用深色选择器
<div className="dark:bg-gray-800 dark:text-white">
  深色模式专用
</div>
```

### 6. 性能优化

```javascript
// tailwind.config.js
export default {
  // 使用 JIT 模式
  mode: 'jit',
  // 配置内容路径
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  // 生产环境优化
  purge: {
    enabled: process.env.NODE_ENV === 'production',
    content: ['./src/**/*.{js,ts,jsx,tsx}'],
  },
}
```

### 7. 自定义工具类

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      // 自定义间距
      spacing: {
        '128': '32rem',
      },
      // 自定义字体大小
      fontSize: {
        'xxs': '0.625rem',
      },
      // 自定义断点
      screens: {
        '3xl': '1600px',
      },
    },
  },
}
```

### 8. 动态类名

```jsx
// 使用模板字符串
function Button({ variant, size }) {
  const variantClasses = {
    primary: 'bg-blue-500 hover:bg-blue-600',
    secondary: 'bg-gray-500 hover:bg-gray-600',
    danger: 'bg-red-500 hover:bg-red-600',
  }

  const sizeClasses = {
    sm: 'px-2 py-1 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  }

  return (
    <button className={`${variantClasses[variant]} ${sizeClasses[size]} rounded`}>
      按钮
    </button>
  )
}
```

---

## 🔗 相关文档

- [指南总览](tailwind-guide.md) - 设计令牌、自定义配置、主题系统
- [返回主文档](tailwind.md) - Tailwind CSS总览

---

## 🔗 快速导航

- [返回by-framework/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
