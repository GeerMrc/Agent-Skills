# Tailwind CSS 完整指南

> 🎨 **Advanced Configuration & Optimization** - 设计令牌、自定义配置、性能优化

---

## 📖 文档说明

本文档提供 Tailwind CSS 的高级配置和优化细节，包括设计令牌系统、自定义配置、性能优化和常用插件等内容。

**相关文档**：
- [返回主文档](tailwind.md)

---

## 🎨 设计令牌系统

### 使用 OKLCH 颜色

OKLCH 是一种更现代的颜色空间，提供更好的感知均匀性。

```javascript
// tailwind.config.js
import colors from 'tailwindcss-oklch-text/colors'

export default {
  theme: {
    extend: {
      colors: {
        // 使用 OKLCH 颜色空间
        primary: {
          light: 'oklch(0.6 0.2 250)',
          DEFAULT: 'oklch(0.5 0.2 250)',
          dark: 'oklch(0.4 0.2 250)',
        },
        // 语义化颜色
        success: 'oklch(0.7 0.2 145)',
        warning: 'oklch(0.75 0.15 85)',
        error: 'oklch(0.6 0.22 25)',
      },
    },
  },
}
```

### 颜色系统设计

#### 单色系（Monochromatic）

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        blue: {
          50: 'oklch(0.97 0.01 250)',
          100: 'oklch(0.94 0.02 250)',
          200: 'oklch(0.88 0.04 250)',
          300: 'oklch(0.81 0.08 250)',
          400: 'oklch(0.70 0.14 250)',
          500: 'oklch(0.60 0.19 250)',  // 主色
          600: 'oklch(0.55 0.22 250)',
          700: 'oklch(0.48 0.24 250)',
          800: 'oklch(0.41 0.23 250)',
          900: 'oklch(0.34 0.20 250)',
          950: 'oklch(0.25 0.15 250)',
        },
      },
    },
  },
}
```

#### 语义化颜色

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        // 基础颜色
        primary: {
          DEFAULT: 'oklch(0.60 0.19 250)',
          foreground: 'oklch(0.98 0.01 250)',
        },
        secondary: {
          DEFAULT: 'oklch(0.65 0.15 180)',
          foreground: 'oklch(0.98 0.01 180)',
        },
        // 功能颜色
        background: 'oklch(1 0 0)',
        foreground: 'oklch(0.15 0.02 250)',
        // 状态颜色
        destructive: {
          DEFAULT: 'oklch(0.6 0.22 25)',
          foreground: 'oklch(0.98 0.01 25)',
        },
        muted: {
          DEFAULT: 'oklch(0.96 0.01 250)',
          foreground: 'oklch(0.50 0.02 250)',
        },
        accent: {
          DEFAULT: 'oklch(0.96 0.01 250)',
          foreground: 'oklch(0.15 0.02 250)',
        },
        border: 'oklch(0.90 0.01 250)',
        input: 'oklch(0.90 0.01 250)',
        ring: 'oklch(0.60 0.19 250)',
      },
    },
  },
}
```

### 自定义间距

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      spacing: {
        // 添加更大的间距
        '128': '32rem',
        '144': '36rem',
        '160': '40rem',
        // 添加精确间距
        '13': '3.25rem',
        '15': '3.75rem',
        '17': '4.25rem',
        // 添加小数间距
        '0.5': '0.125rem',
        '1.5': '0.375rem',
        '2.5': '0.625rem',
        '3.5': '0.875rem',
      },
    },
  },
}
```

### 断点系统

```javascript
// tailwind.config.js
export default {
  theme: {
    screens: {
      'xs': '475px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
      // 添加自定义断点
      '3xl': '1920px',
      // 添加特定设备断点
      'tablet': '640px',
      'laptop': '1024px',
      'desktop': '1280px',
    },
  },
}
```

### 字体系统

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: [
          'Inter',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          'Segoe UI',
          'Roboto',
          'sans-serif',
        ],
        serif: [
          'Merriweather',
          'Georgia',
          'Cambria',
          'Times New Roman',
          'Times',
          'serif',
        ],
        mono: [
          'Fira Code',
          'SF Mono',
          'Monaco',
          'Cascadia Code',
          'Roboto Mono',
          'Courier New',
          'monospace',
        ],
      },
      fontSize: {
        // 添加更多字体大小选项
        'xxs': '0.625rem',
        '3xl': '2.5rem',
        '4xl': '3rem',
        '5xl': '4rem',
      },
      letterSpacing: {
        // 添加字间距选项
        'tighter': '-0.05em',
        'wide': '0.05em',
        'wider': '0.1em',
      },
      lineHeight: {
        // 添加行高选项
        '0.75': '0.75',
        '1.25': '1.25',
      },
    },
  },
}
```

---

## 🔧 自定义配置

### 自定义颜色

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',  // 主色
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
          950: '#082f49',
        },
      },
    },
  },
}
```

### 自定义字体

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'serif'],
        mono: ['Fira Code', 'monospace'],
        display: ['Cal Sans', 'sans-serif'],
      },
      fontWeight: {
        // 添加更多字重选项
        'extralight': 200,
        'medium': 500,
        'semibold': 600,
        'extrabold': 800,
      },
    },
  },
}
```

### 自定义动画

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      animation: {
        // 淡入动画
        'fade-in': 'fadeIn 0.3s ease-out',
        'fade-out': 'fadeOut 0.3s ease-in',
        // 滑动动画
        'slide-up': 'slideUp 0.3s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
        'slide-left': 'slideLeft 0.3s ease-out',
        'slide-right': 'slideRight 0.3s ease-out',
        // 缩放动画
        'scale-in': 'scaleIn 0.2s ease-out',
        'scale-out': 'scaleOut 0.2s ease-in',
        // 旋转动画
        'spin-slow': 'spin 3s linear infinite',
        'spin-fast': 'spin 0.5s linear infinite',
        'bounce-slow': 'bounce 2s infinite',
        // 弹跳动画
        'bounce-in': 'bounceIn 0.5s ease-out',
        // 抖动动画
        'shake': 'shake 0.5s ease-in-out',
        // 脉冲动画
        'pulse-fast': 'pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeOut: {
          '0%': { opacity: '1' },
          '100%': { opacity: '0' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideLeft: {
          '0%': { transform: 'translateX(10px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideRight: {
          '0%': { transform: 'translateX(-10px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.9)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        scaleOut: {
          '0%': { transform: 'scale(1)', opacity: '1' },
          '100%': { transform: 'scale(0.9)', opacity: '0' },
        },
        bounceIn: {
          '0%': { transform: 'scale(0.3)', opacity: '0' },
          '50%': { transform: 'scale(1.05)' },
          '70%': { transform: 'scale(0.9)' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        shake: {
          '0%, 100%': { transform: 'translateX(0)' },
          '10%, 30%, 50%, 70%, 90%': { transform: 'translateX(-5px)' },
          '20%, 40%, 60%, 80%': { transform: 'translateX(5px)' },
        },
      },
      transitionDuration: {
        '400': '400ms',
        '600': '600ms',
        '800': '800ms',
      },
      transitionTimingFunction: {
        'bounce-in': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
        'bounce-out': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
    },
  },
}
```

### 自定义阴影

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      boxShadow: {
        // 添加自定义阴影
        'sm': '0 1px 2px 0 rgb(0 0 0 / 0.05)',
        'inner-lg': 'inset 0 2px 4px 0 rgb(0 0 0 / 0.06)',
        'color': '0 10px 15px -3px var(--tw-shadow-color)',
        'color-lg': '0 20px 25px -5px var(--tw-shadow-color)',
      },
    },
  },
}
```

### 自定义圆角

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      borderRadius: {
        // 添加更多圆角选项
        '4xl': '2rem',
        '5xl': '2.5rem',
      },
    },
  },
}
```

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

### 优化构建体积

1. **使用动态类名**

```jsx
// ✅ 好：使用完整的类名
<div className={condition ? 'text-blue-600' : 'text-red-600'}>内容</div>

// ❌ 坏：动态拼接类名
<div className={`text-${color}-600`}>内容</div>
```

2. **避免使用任意值**

```jsx
// ✅ 好：使用配置的间距
<div className="p-4">内容</div>

// ❌ 坏：使用任意值
<div className="p-[1.234rem]">内容</div>
```

3. **使用 CSS 变量**

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
/* src/index.css */
:root {
  --color-primary: #0ea5e9;
  --color-secondary: #6366f1;
}
```

### 使用 content 选项

```javascript
// tailwind.config.js
export default {
  content: [
    './pages/**/*.{html,js}',
    './components/**/*.{html,js}',
    './app/**/*.{html,js}',
    './src/**/*.{html,js,ts,jsx,tsx}',
  ],
}
```

---

## 🧩 常用插件

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
  <img src="/image.jpg" alt="16:9 图片" />
</div>
```

### 自定义插件

```javascript
// plugins/custom-buttons.js
export default function({ addComponents, theme }) {
  addComponents({
    '.btn': {
      padding: `${theme('spacing.2')} ${theme('spacing.4')}`,
      borderRadius: theme('borderRadius.md'),
      fontWeight: theme('fontWeight.medium'),
      transitionProperty: theme('transitionProperty.colors'),
      transitionDuration: theme('transitionDuration.150'),
    },
    '.btn-primary': {
      backgroundColor: theme('colors.blue.600'),
      color: theme('colors.white'),
      '&:hover': {
        backgroundColor: theme('colors.blue.700'),
      },
    },
    '.btn-secondary': {
      backgroundColor: theme('colors.gray.200'),
      color: theme('colors.gray.900'),
      '&:hover': {
        backgroundColor: theme('colors.gray.300'),
      },
    },
  })
}
```

```javascript
// tailwind.config.js
import customButtons from './plugins/custom-buttons'

export default {
  plugins: [
    customButtons,
  ],
}
```

---

## 📋 最佳实践总结

### 1. 设计令牌

- 使用 OKLCH 颜色空间
- 定义语义化颜色
- 创建一致的间距系统
- 配置响应式断点

### 2. 自定义配置

- 扩展而非覆盖默认配置
- 使用语义化命名
- 保持配置简洁
- 复用设计令牌

### 3. 性能优化

- 启用 JIT 模式
- 清理未使用的样式
- 优化构建体积
- 使用 CSS 变量

### 4. 插件使用

- 选择必要的插件
- 配置插件选项
- 创建自定义插件
- 避免插件冲突

---

## 🔗 相关文档

- [返回主文档](tailwind.md)
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

> **文档版本**: v1.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
