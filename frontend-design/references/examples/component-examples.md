# 组件示例

> 🧩 **Component Examples** - 实用的 React 组件模式

---

## 📖 文档说明

本文档提供常用 React 组件的完整示例，涵盖基础组件、表单组件、布局组件等。

**目标读者**: React 开发者
**文档长度**: 约290行
**阅读时间**: 约16分钟

---

## 🎯 组件设计原则

### 组件设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **单一职责** | 组件只做一件事 | Button 只处理按钮逻辑 |
| **可复用** | 通过 props 定制 | Button 可变 size、variant |
| **可组合** | 小组件组合成大组件 | Form = Input + Label + Error |
| **类型安全** | 使用 TypeScript | Props 有明确的类型 |

---

## 🔘 基础组件

### Button 组件

```tsx
// Button.tsx
import { forwardRef } from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      children,
      variant = 'primary',
      size = 'md',
      isLoading = false,
      leftIcon,
      rightIcon,
      disabled,
      className = '',
      ...props
    },
    ref
  ) => {
    const baseStyles = 'inline-flex items-center justify-center gap-2 rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50';

    const variantStyles = {
      primary: 'bg-blue-600 text-white hover:bg-blue-700',
      secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
      ghost: 'bg-transparent text-gray-900 hover:bg-gray-100',
      danger: 'bg-red-600 text-white hover:bg-red-700',
    };

    const sizeStyles = {
      sm: 'h-8 px-3 text-sm',
      md: 'h-10 px-4 text-base',
      lg: 'h-12 px-6 text-lg',
    };

    return (
      <button
        ref={ref}
        className={`${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading && <Spinner size="sm" />}
        {!isLoading && leftIcon && leftIcon}
        {children}
        {!isLoading && rightIcon && rightIcon}
      </button>
    );
  }
);

Button.displayName = 'Button';
```

### Input 组件

```tsx
// Input.tsx
import { forwardRef } from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      label,
      error,
      leftIcon,
      rightIcon,
      className = '',
      id,
      ...props
    },
    ref
  ) => {
    const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`;

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            {label}
          </label>
        )}
        <div className="relative">
          {leftIcon && (
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              {leftIcon}
            </div>
          )}
          <input
            ref={ref}
            id={inputId}
            className={`
              w-full rounded-md border border-gray-300 px-3 py-2
              focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500
              disabled:bg-gray-100 disabled:cursor-not-allowed
              ${leftIcon ? 'pl-10' : ''}
              ${rightIcon ? 'pr-10' : ''}
              ${error ? 'border-red-500 focus:border-red-500 focus:ring-red-500' : ''}
              ${className}
            `}
            {...props}
          />
          {rightIcon && (
            <div className="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              {rightIcon}
            </div>
          )}
        </div>
        {error && (
          <p className="mt-1 text-sm text-red-600">{error}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';
```

---

## 📝 表单组件

### FormField 组件

```tsx
// FormField.tsx
import { ReactNode } from 'react';

interface FormFieldProps {
  label?: string;
  error?: string;
  required?: boolean;
  description?: string;
  children: ReactNode;
}

export function FormField({
  label,
  error,
  required,
  description,
  children,
}: FormFieldProps) {
  return (
    <div className="space-y-1">
      {label && (
        <label className="block text-sm font-medium text-gray-700">
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      {children}
      {description && (
        <p className="text-sm text-gray-500">{description}</p>
      )}
      {error && (
        <p className="text-sm text-red-600">{error}</p>
      )}
    </div>
  );
}
```

### Select 组件

```tsx
// Select.tsx
import { forwardRef } from 'react';

interface SelectOption {
  value: string;
  label: string;
  disabled?: boolean;
}

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string;
  error?: string;
  options: SelectOption[];
  placeholder?: string;
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
  (
    {
      label,
      error,
      options,
      placeholder,
      className = '',
      ...props
    },
    ref
  ) => {
    return (
      <div className="w-full">
        {label && (
          <label className="block text-sm font-medium text-gray-700 mb-1">
            {label}
          </label>
        )}
        <select
          ref={ref}
          className={`
            w-full rounded-md border border-gray-300 px-3 py-2
            focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500
            disabled:bg-gray-100 disabled:cursor-not-allowed
            ${error ? 'border-red-500' : ''}
            ${className}
          `}
          {...props}
        >
          {placeholder && (
            <option value="">{placeholder}</option>
          )}
          {options.map((option) => (
            <option
              key={option.value}
              value={option.value}
              disabled={option.disabled}
            >
              {option.label}
            </option>
          ))}
        </select>
        {error && (
          <p className="mt-1 text-sm text-red-600">{error}</p>
        )}
      </div>
    );
  }
);

Select.displayName = 'Select';
```

---

## 📦 数据展示组件

### Card 组件

```tsx
// Card.tsx
import { ReactNode } from 'react';

interface CardProps {
  header?: ReactNode;
  footer?: ReactNode;
  children: ReactNode;
  variant?: 'elevated' | 'outlined' | 'flat';
}

export function Card({
  header,
  footer,
  children,
  variant = 'elevated',
}: CardProps) {
  const variantStyles = {
    elevated: 'shadow-md',
    outlined: 'border border-gray-200',
    flat: '',
  };

  return (
    <div className={`bg-white rounded-lg ${variantStyles[variant]}`}>
      {header && (
        <div className="px-6 py-4 border-b border-gray-200">
          {header}
        </div>
      )}
      <div className="px-6 py-4">{children}</div>
      {footer && (
        <div className="px-6 py-4 border-t border-gray-200">
          {footer}
        </div>
      )}
    </div>
  );
}
```

### Badge 组件

```tsx
// Badge.tsx
import { ReactNode } from 'react';

interface BadgeProps {
  children: ReactNode;
  variant?: 'default' | 'success' | 'warning' | 'error' | 'info';
  size?: 'sm' | 'md' | 'lg';
}

export function Badge({
  children,
  variant = 'default',
  size = 'md',
}: BadgeProps) {
  const variantStyles = {
    default: 'bg-gray-100 text-gray-800',
    success: 'bg-green-100 text-green-800',
    warning: 'bg-yellow-100 text-yellow-800',
    error: 'bg-red-100 text-red-800',
    info: 'bg-blue-100 text-blue-800',
  };

  const sizeStyles = {
    sm: 'px-2 py-0.5 text-xs',
    md: 'px-2.5 py-0.5 text-sm',
    lg: 'px-3 py-1 text-base',
  };

  return (
    <span
      className={`inline-flex items-center rounded-full font-medium ${variantStyles[variant]} ${sizeStyles[size]}`}
    >
      {children}
    </span>
  );
}
```

---

## 🔔 反馈组件

### Toast 组件

```tsx
// Toast.tsx
import { useEffect } from 'react';
import { X } from 'lucide-react';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
  onClose: () => void;
}

export function Toast({
  message,
  type = 'info',
  duration = 3000,
  onClose,
}: ToastProps) {
  useEffect(() => {
    const timer = setTimeout(onClose, duration);
    return () => clearTimeout(timer);
  }, [duration, onClose]);

  const typeStyles = {
    success: 'bg-green-500',
    error: 'bg-red-500',
    warning: 'bg-yellow-500',
    info: 'bg-blue-500',
  };

  return (
    <div className="fixed bottom-4 right-4 z-50 animate-slide-up">
      <div className={`${typeStyles[type]} text-white px-4 py-3 rounded-lg shadow-lg flex items-center gap-3`}>
        <span>{message}</span>
        <button
          onClick={onClose}
          className="hover:bg-white/20 rounded p-1 transition-colors"
        >
          <X size={16} />
        </button>
      </div>
    </div>
  );
}
```

### Modal 组件

```tsx
// Modal.tsx
import { useEffect } from 'react';
import { X } from 'lucide-react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: ReactNode;
}

export function Modal({ isOpen, onClose, title, children }: ModalProps) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50"
        onClick={onClose}
      />

      {/* Modal */}
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? 'modal-title' : undefined}
        className="relative bg-white rounded-lg shadow-xl max-w-md w-full mx-4 animate-fade-in"
      >
        {/* Header */}
        {title && (
          <div className="flex items-center justify-between p-6 border-b">
            <h2 id="modal-title" className="text-lg font-semibold">
              {title}
            </h2>
            <button
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600 transition-colors"
            >
              <X size={20} />
            </button>
          </div>
        )}

        {/* Body */}
        <div className="p-6">
          {children}
        </div>
      </div>
    </div>
  );
}
```

---

## 📐 布局组件

### Container 组件

```tsx
// Container.tsx
import { ReactNode } from 'react';

interface ContainerProps {
  children: ReactNode;
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  className?: string;
}

export function Container({
  children,
  size = 'lg',
  className = '',
}: ContainerProps) {
  const sizeStyles = {
    sm: 'max-w-screen-sm',
    md: 'max-w-screen-md',
    lg: 'max-w-screen-lg',
    xl: 'max-w-screen-xl',
    full: 'max-w-full',
  };

  return (
    <div className={`mx-auto px-4 ${sizeStyles[size]} ${className}`}>
      {children}
    </div>
  );
}
```

### Grid 组件

```tsx
// Grid.tsx
import { ReactNode } from 'react';

interface GridProps {
  children: ReactNode;
  cols?: 1 | 2 | 3 | 4 | 6 | 12;
  gap?: number;
  className?: string;
}

export function Grid({
  children,
  cols = 3,
  gap = 4,
  className = '',
}: GridProps) {
  return (
    <div
      className={`grid grid-cols-1 md:grid-cols-${cols} gap-${gap} ${className}`}
    >
      {children}
    </div>
  );
}
```

---

## 🎭 复合组件示例

### UserCard 组件

```tsx
// UserCard.tsx
import { Card } from './Card';
import { Badge } from './Badge';
import { Button } from './Button';

interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
  avatar?: string;
}

interface UserCardProps {
  user: User;
  onEdit?: (user: User) => void;
  onDelete?: (userId: string) => void;
}

export function UserCard({ user, onEdit, onDelete }: UserCardProps) {
  const roleColors = {
    admin: 'success',
    user: 'info',
    guest: 'default',
  } as const;

  return (
    <Card>
      <div className="flex items-start gap-4">
        {/* Avatar */}
        <div className="w-12 h-12 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold">
          {user.name.charAt(0).toUpperCase()}
        </div>

        {/* Content */}
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-1">
            <h3 className="font-semibold">{user.name}</h3>
            <Badge variant={roleColors[user.role]} size="sm">
              {user.role}
            </Badge>
          </div>
          <p className="text-sm text-gray-600">{user.email}</p>
        </div>
      </div>

      {/* Actions */}
      <Card.Footer className="flex gap-2 justify-end">
        {onEdit && (
          <Button
            variant="secondary"
            size="sm"
            onClick={() => onEdit(user)}
          >
            编辑
          </Button>
        )}
        {onDelete && (
          <Button
            variant="danger"
            size="sm"
            onClick={() => onDelete(user.id)}
          >
            删除
          </Button>
        )}
      </Card.Footer>
    </Card>
  );
}
```

---

## 📋 组件检查清单

### 设计

- [ ] 单一职责
- [ ] Props 有明确的类型
- [ ] 可复用和可组合
- [ ] 支持 ref 转发

### 样式

- [ ] 使用设计令牌
- [ ] 支持变体和尺寸
- [ ] 响应式设计
- [ ] 深色模式支持

### 可访问性

- [ ] 适当的 ARIA 属性
- [ ] 键盘导航支持
- [ ] 焦点管理
- [ ] 屏幕阅读器友好

### 测试

- [ ] 单元测试覆盖
- [ ] Props 变体测试
- [ ] 交互测试
- [ ] 可访问性测试

---

## 💡 最佳实践总结

1. **组件拆分**：保持组件小而专注
2. **类型安全**：使用 TypeScript 定义 Props
3. **可复用性**：通过 props 支持多种变体
4. **可访问性**：确保键盘和屏幕阅读器支持
5. **测试覆盖**：为每个组件编写测试

---

## 🔗 相关资源

### 工具

- ** Bit**: 组件开发和分享平台
- ** Storybook**: 组件文档和开发环境
- ** React Cosmos**: 组件开发工具

### 文档

- [React 组件模式](https://reactpatterns.com/)
- [组件设计最佳实践](https://www.patterns.dev/)

---

> **文档版本**: v1.0
> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills Team
