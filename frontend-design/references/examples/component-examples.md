# 组件示例

> 🧩 **Component Examples** - 实用的 React 组件模式

---

## 📖 文档说明

本文档提供常用 React 组件的完整示例，涵盖基础组件、表单组件、布局组件等。

**目标读者**: React 开发者
**文档长度**: ~180行（主文档）
**阅读时间**: 约10分钟

**相关文档**:
- [基础与表单组件](component-examples-basic-form.md) - Button、Input、FormField、Select 完整实现
- [数据展示组件](component-examples-display.md) - Card、Badge、Container、Grid
- [用户反馈组件](component-examples-feedback.md) - Toast、Modal、复合组件

---

## 🎯 组件设计原则

### 设计原则表

| 原则 | 说明 | 示例 |
|------|------|------|
| **单一职责** | 组件只做一件事 | Button 只处理按钮逻辑 |
| **可复用** | 通过 props 定制 | Button 可变 size、variant |
| **可组合** | 小组件组合成大组件 | Form = Input + Label + Error |
| **类型安全** | 使用 TypeScript | Props 有明确的类型 |

---

## 📋 组件分类总览

### 按用途分类

| 分类 | 组件 | 说明 | 详细文档 |
|------|------|------|----------|
| **基础组件** | Button, Input | 最常用的基础交互组件 | [查看详情](component-examples-basic-form.md) |
| **表单组件** | FormField, Select | 表单相关组件 | [查看详情](component-examples-basic-form.md) |
| **数据展示** | Card, Badge | 数据可视化展示组件 | [查看详情](component-examples-display.md) |
| **布局组件** | Container, Grid | 页面布局容器 | [查看详情](component-examples-display.md) |
| **反馈组件** | Toast, Modal | 用户反馈和对话框 | [查看详情](component-examples-feedback.md) |
| **复合组件** | UserCard | 组合多个基础组件 | [查看详情](component-examples-feedback.md) |

### 按复杂度分类

| 复杂度 | 组件 | 代码行数 | 学习难度 |
|--------|------|----------|----------|
| **简单** | Badge, Container | ~30行 | ⭐ |
| **中等** | Button, Input, Card, Toast | ~60行 | ⭐⭐ |
| **复杂** | Modal, Select, UserCard | ~100行 | ⭐⭐⭐ |

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

### 1. 组件拆分

**保持组件小而专注**

```tsx
// ✅ 推荐：单一职责
function Button({ children, onClick }) {
  return <button onClick={onClick}>{children}</button>;
}

// ❌ 避免：职责过多
function ButtonWithForm({ children }) {
  return (
    <div>
      <button>{children}</button>
      <form>{/* 表单逻辑不应该在按钮中 */}</form>
    </div>
  );
}
```

### 2. 类型安全

**使用 TypeScript 定义 Props**

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}
```

### 3. 可复用性

**通过 props 支持多种变体**

```tsx
const variantStyles = {
  primary: 'bg-blue-600 text-white',
  secondary: 'bg-gray-200 text-gray-900',
  ghost: 'bg-transparent text-gray-900',
};
```

### 4. 可访问性

**确保键盘和屏幕阅读器支持**

```tsx
<button
  aria-label="关闭对话框"
  onKeyDown={(e) => e.key === 'Escape' && onClose()}
>
  <X />
</button>
```

### 5. 测试覆盖

**为每个组件编写测试**

```tsx
describe('Button', () => {
  it('should render children', () => {
    render(<Button>点击</Button>);
    expect(screen.getByText('点击')).toBeInTheDocument();
  });

  it('should call onClick when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>点击</Button>);
    fireEvent.click(screen.getByText('点击'));
    expect(handleClick).toHaveBeenCalled();
  });
});
```

---

## 🔗 相关资源

### 工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **Bit** | 组件开发和分享平台 | https://bit.dev |
| **Storybook** | 组件文档和开发环境 | https://storybook.js.org |
| **React Cosmos** | 组件开发工具 | https://reactcosmos.org |

### 文档

| 资源 | 说明 | 链接 |
|------|------|------|
| React 组件模式 | 组件设计模式 | https://reactpatterns.com |
| 组件设计最佳实践 | 现代组件设计 | https://www.patterns.dev |
| React 可访问性 | 无障碍开发指南 | https://react.dev/learn/accessibility |

---

## 🚀 快速开始

### 选择合适的组件

```
需要用户点击？
└─ 使用 [Button](component-examples-basic-form.md#button-组件)

需要用户输入？
└─ 使用 [Input](component-examples-basic-form.md#input-组件)

需要展示数据？
└─ 使用 [Card](component-examples-display.md#card-组件)

需要通知用户？
└─ 使用 [Toast](component-examples-feedback.md#toast-组件)

需要对话框？
└─ 使用 [Modal](component-examples-feedback.md#modal-组件)

需要布局容器？
└─ 使用 [Container](component-examples-display.md#container-组件)
```

---

## 🔗 相关文档

- [基础与表单组件详解](component-examples-basic-form.md)
- [数据展示组件详解](component-examples-display.md) - Card、Badge、Container、Grid
- [用户反馈组件详解](component-examples-feedback.md) - Toast、Modal、复合组件
- [组件状态覆盖](../implementation/component-states.md)
- [Design Token方法论](../methodology/design-tokens.md)

---

## 🔗 快速导航

- [返回examples/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **文档版本**: v2.0
> **最后更新**: 2026-01-05
> **维护者**: Frontend Design Agent Skills Team
