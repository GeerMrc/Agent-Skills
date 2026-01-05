# 数据展示组件

> 🧩 **Display Components** - Card、Badge、Container、Grid

---

## 📖 文档说明

本文档提供数据展示和布局组件的完整实现示例，包括代码、类型定义和最佳实践。

**相关文档**：
- [用户反馈组件](component-examples-feedback.md) - Toast、Modal、复合组件
- [返回主文档](component-examples.md)
- [基础与表单组件](component-examples-basic-form.md)

---

## 📦 数据展示组件

### Card 组件

**适用场景**：内容卡片容器

**特性**：
- 3种变体：elevated、outlined、flat
- Header 和 Footer 插槽
- 响应式设计

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

**使用示例**：
```tsx
// 基础用法
<Card>
  <p>卡片内容</p>
</Card>

// 带 Header
<Card header={<h2>标题</h2>}>
  <p>内容</p>
</Card>

// 不同变体
<Card variant="outlined">...</Card>
<Card variant="flat">...</Card>
```

---

### Badge 组件

**适用场景**：状态标签、徽章

**特性**：
- 5种变体：default、success、warning、error、info
- 3种尺寸：sm、md、lg

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

**使用示例**：
```tsx
<Badge>默认</Badge>
<Badge variant="success">成功</Badge>
<Badge variant="warning">警告</Badge>
<Badge variant="error">错误</Badge>
<Badge variant="info">信息</Badge>

<Badge size="sm">小</Badge>
<Badge size="md">中</Badge>
<Badge size="lg">大</Badge>
```

---

## 📐 布局组件

### Container 组件

**适用场景**：内容容器，限制最大宽度

**特性**：
- 5种尺寸：sm、md、lg、xl、full
- 自动水平居中
- 响应式内边距

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

---

### Grid 组件

**适用场景**：网格布局

**特性**：
- 响应式列数
- 可配置间距

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

## 💡 使用示例

### 产品卡片网格

```tsx
function ProductGrid() {
  const products = [
    { id: '1', name: '产品A', price: 99, status: 'available' },
    { id: '2', name: '产品B', price: 199, status: 'sale' },
  ];

  return (
    <Container size="xl">
      <Grid cols={3} gap={6}>
        {products.map(product => (
          <Card key={product.id}>
            <Card.Header>
              <h3>{product.name}</h3>
            </Card.Header>
            <div>
              <p>¥{product.price}</p>
              <Badge variant={product.status === 'available' ? 'success' : 'warning'}>
                {product.status}
              </Badge>
            </div>
          </Card>
        ))}
      </Grid>
    </Container>
  );
}
```

---

## 🔗 相关文档

- [用户反馈组件](component-examples-feedback.md) - Toast、Modal、复合组件
- [返回主文档](component-examples.md)
- [基础与表单组件](component-examples-basic-form.md)

---

## 🔗 快速导航

- [返回examples/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.1 (拆分版)
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
