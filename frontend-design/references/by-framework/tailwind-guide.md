# Tailwind CSS 指南总览

> 🎨 **Core Configuration** - 设计令牌、自定义配置、主题系统

---

## 📖 文档说明

本文档提供 Tailwind CSS 的核心配置指南，包括设计令牌系统、自定义配置和主题系统。

**相关文档**：
- [自定义与优化](tailwind-guide-customization.md) - 性能优化、插件、最佳实践
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
          500: 'oklch(0.60 0.19 250)',
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
        // 中性色
        neutral: {
          50: 'oklch(0.98 0.005 250)',
          100: 'oklch(0.96 0.008 250)',
          200: 'oklch(0.92 0.01 250)',
          300: 'oklch(0.85 0.015 250)',
          400: 'oklch(0.70 0.02 250)',
          500: 'oklch(0.55 0.025 250)',
          600: 'oklch(0.45 0.025 250)',
          700: 'oklch(0.35 0.02 250)',
          800: 'oklch(0.25 0.015 250)',
          900: 'oklch(0.15 0.01 250)',
        },
        // 功能色
        info: 'oklch(0.6 0.2 250)',
        success: 'oklch(0.7 0.2 145)',
        warning: 'oklch(0.75 0.15 85)',
        danger: 'oklch(0.6 0.22 25)',
      },
    },
  },
}
```

### 间距系统

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      spacing: {
        '0': '0',
        'px': '1px',
        '0.5': '0.125rem',
        '1': '0.25rem',
        '2': '0.5rem',
        '3': '0.75rem',
        '4': '1rem',
        '5': '1.25rem',
        '6': '1.5rem',
        '7': '1.75rem',
        '8': '2rem',
        '9': '2.25rem',
        '10': '2.5rem',
        '12': '3rem',
        '16': '4rem',
        '20': '5rem',
        '24': '6rem',
        '32': '8rem',
        '40': '10rem',
        '48': '12rem',
        '56': '14rem',
        '64': '16rem',
      },
    },
  },
}
```

### 排版系统

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'serif'],
        mono: ['Fira Code', 'Monaco', 'monospace'],
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '1' }],
        '6xl': ['3.75rem', { lineHeight: '1' }],
        '7xl': ['4.5rem', { lineHeight: '1' }],
        '8xl': ['6rem', { lineHeight: '1' }],
        '9xl': ['8rem', { lineHeight: '1' }],
      },
      fontWeight: {
        'thin': '100',
        'extralight': '200',
        'light': '300',
        'normal': '400',
        'medium': '500',
        'semibold': '600',
        'bold': '700',
        'extrabold': '800',
        'black': '900',
      },
      letterSpacing: {
        'tighter': '-0.05em',
        'tight': '-0.025em',
        'normal': '0',
        'wide': '0.025em',
        'wider': '0.05em',
        'widest': '0.1em',
      },
    },
  },
}
```

### 动画系统

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      animation: {
        // 淡入淡出
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
        // 内阴影
        'inner-lg': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.1)',
        // 柔和阴影
        'soft': '0 2px 8px rgba(0, 0, 0, 0.05)',
        'soft-lg': '0 8px 16px rgba(0, 0, 0, 0.08)',
        // 彩色阴影
        'primary': '0 4px 12px rgba(59, 130, 246, 0.3)',
        'success': '0 4px 12px rgba(16, 185, 129, 0.3)',
        'warning': '0 4px 12px rgba(245, 158, 11, 0.3)',
        'danger': '0 4px 12px rgba(239, 68, 68, 0.3)',
      },
    },
  },
}
```

### 边框半径

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      borderRadius: {
        '4xl': '2rem',
        '5xl': '2.5rem',
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
    extend: {
      screens: {
        'xs': '480px',
        '3xl': '1600px',
        // 自定义断点范围
        'sm': {'min': '640px', 'max': '767px'},
        'md': {'min': '768px', 'max': '1023px'},
        'lg': {'min': '1024px', 'max': '1279px'},
        'xl': {'min': '1280px', 'max': '1535px'},
        '2xl': {'min': '1536px'},
      },
    },
  },
}
```

### Z-index 层级

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      zIndex: {
        '60': '60',
        '70': '70',
        '80': '80',
        '90': '90',
        '100': '100',
      },
    },
  },
}
```

---

## 🎨 主题系统

### 深色模式

```javascript
// tailwind.config.js
export default {
  darkMode: 'class', // 或 'media'
}
```

```html
<!-- 手动切换深色模式 -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    <!-- 内容 -->
  </body>
</html>
```

### 主题变体

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        // 亮色主题
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        },
        // 深色主题
        dark: {
          bg: '#0f172a',
          fg: '#f1f5f9',
          primary: '#60a5fa',
        },
      },
    },
  },
}
```

---

## 🔗 相关文档

- [自定义与优化](tailwind-guide-customization.md) - 性能优化、插件、最佳实践
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
