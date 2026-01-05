# 基础与表单组件

> 🧩 **Basic & Form Components** - Button、Input、FormField、Select 完整实现

---

## 📖 文档说明

本文档提供基础组件和表单组件的完整实现示例，包括代码、类型定义和最佳实践。

**相关文档**：
- [返回主文档](component-examples.md)
- [数据展示组件](component-examples-display.md) - Card、Badge、Container、Grid
- [用户反馈组件](component-examples-feedback.md) - Toast、Modal、复合组件

---

## 🔘 基础组件

### Button 组件

**适用场景**：用户点击触发操作

**特性**：
- 4种变体：primary、secondary、ghost、danger
- 3种尺寸：sm、md、lg
- 加载状态支持
- 图标支持（左/右）
- 完整类型定义 + ref 转发

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

**使用示例**：
```tsx
// 基础用法
<Button>点击我</Button>

// 不同变体
<Button variant="primary">主要按钮</Button>
<Button variant="secondary">次要按钮</Button>
<Button variant="danger">危险操作</Button>

// 不同尺寸
<Button size="sm">小按钮</Button>
<Button size="md">中等按钮</Button>
<Button size="lg">大按钮</Button>

// 加载状态
<Button isLoading>提交中...</Button>

// 带图标
<Button leftIcon={<Plus />}>添加</Button>
<Button rightIcon={<ArrowRight />}>继续</Button>
```

---

### Input 组件

**适用场景**：用户输入文本

**特性**：
- Label 标签支持
- 错误状态提示
- 左右图标支持
- 自动 ID 生成
- 完整无障碍属性

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

**使用示例**：
```tsx
// 基础用法
<Input placeholder="请输入用户名" />

// 带标签
<Input label="邮箱" type="email" />

// 错误状态
<Input label="密码" error="密码长度至少8位" />

// 带图标
<Input
  label="搜索"
  leftIcon={<Search />}
  placeholder="搜索内容..."
/>
```

---

## 📝 表单组件

### FormField 组件

**适用场景**：表单字段包装器

**特性**：
- 统一的表单字段布局
- Label 标签支持
- 必填标记
- 错误和描述文字

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

**使用示例**：
```tsx
<FormField
  label="用户名"
  required
  description="用于登录的用户名"
>
  <Input placeholder="请输入用户名" />
</FormField>

<FormField
  label="邮箱"
  error="邮箱格式不正确"
>
  <Input type="email" />
</FormField>
```

---

### Select 组件

**适用场景**：下拉选择

**特性**：
- Label 标签支持
- 错误状态
- Options 配置
- Placeholder 支持
- 禁用选项

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

**使用示例**：
```tsx
const options = [
  { value: 'admin', label: '管理员' },
  { value: 'user', label: '普通用户' },
  { value: 'guest', label: '访客', disabled: true },
];

<Select
  label="用户角色"
  options={options}
  placeholder="请选择角色"
/>

<Select
  label="国家"
  options={countryOptions}
  error="请选择一个国家"
/>
```

---

## 💡 组合使用示例

### 登录表单

```tsx
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      await login({ email, password });
    } catch (err) {
      setErrors({ email: '邮箱或密码错误' });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <FormField label="邮箱" required>
        <Input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="your@email.com"
          error={errors.email}
        />
      </FormField>

      <FormField label="密码" required>
        <Input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
        />
      </FormField>

      <Button
        type="submit"
        isLoading={isLoading}
        className="w-full"
      >
        登录
      </Button>
    </form>
  );
}
```

---

## 🔗 相关文档

- [返回主文档](component-examples.md)
- [数据展示组件](component-examples-display.md) - Card、Badge、Container、Grid
- [用户反馈组件](component-examples-feedback.md) - Toast、Modal、复合组件
- [组件状态覆盖](../implementation/component-states.md)

---

> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
