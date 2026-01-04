# 系统化方法

> 🏗️ **构建完整设计系统** - 从Tokens到组件

---

## 📖 核心概念

系统化方法提供了一个完整的框架，用于构建可扩展、可维护的设计系统。它从Design Token开始，逐步构建组件、模式和页面。

**核心原则**：
- Tokens优先：所有设计决策从Token开始
- 原子设计：从原子到页面的层级结构
- 一致性：统一的视觉语言
- 可扩展性：支持未来需求

---

## 🎯 设计系统层级

### 5层结构

```
┌─────────────────────────────────────┐
│    5. Pages（页面）                  │  完整的用户界面
├─────────────────────────────────────┤
│    4. Templates（模板）              │  页面结构
├─────────────────────────────────────┤
│    3. Organisms（有机体）            │  复杂组件（表单、导航）
├─────────────────────────────────────┤
│    2. Molecules（分子）              │  简单组件（按钮组、卡片）
├─────────────────────────────────────┤
│    1. Atoms（原子）                  │  基础元素（按钮、输入框）
├─────────────────────────────────────┤
│    0. Design Tokens（设计令牌）      │  基础构件
└─────────────────────────────────────┘
```

---

## 📐 第0层：Design Tokens

**基础构件** - 所有设计决策的起点

**Token类别**：
- 颜色系统
- 间距系统
- 字体系统
- 阴影系统
- 圆角系统
- 动画系统

**示例**：
```css
:root {
  --color-primary: oklch(0.7 0.15 250);
  --spacing-md: 1rem;
  --font-size-base: 1rem;
}
```

---

## 🔲 第1层：Atoms（原子）

**基础UI元素** - 不可分割的最小单元

**示例**：
- 按钮（Button）
- 输入框（Input）
- 标签（Label）
- 图标（Icon）

**原子设计原则**：
- 使用Token定义样式
- 支持多种状态（default/hover/active/disabled等）
- 可组合成更复杂的组件

**示例**：
```tsx
// Button Atom
import { designTokens } from '@/tokens';

export function Button({ variant = 'primary', children }) {
  return (
    <button
      style={{
        background: designTokens.color[variant],
        padding: designTokens.spacing.sm,
        // ...其他样式
      }}
    >
      {children}
    </button>
  );
}
```

---

## 🔷 第2层：Molecules（分子）

**简单组件** - 由多个原子组成

**示例**：
- 搜索框（Search Input = Input + Button）
- 表单字段（Form Field = Label + Input + Error）
- 卡片（Card = Image + Title + Description）

**分子设计原则**：
- 组合多个原子
- 实现基础交互
- 保持职责单一

**示例**：
```tsx
// SearchBox Molecule
export function SearchBox({ onSearch }) {
  return (
    <div className="search-box">
      <Input placeholder="搜索..." />
      <Button onClick={onSearch}>搜索</Button>
    </div>
  );
}
```

---

## 🧬 第3层：Organisms（有机体）

**复杂组件** - 由多个分子和原子组成

**示例**：
- 导航栏（Navigation Bar）
- 表单（Form）
- 列表（List）
- 模态框（Modal）

**有机体设计原则**：
- 处理复杂交互
- 管理内部状态
- 可独立使用

**示例**：
```tsx
// NavigationBar Organism
export function NavigationBar() {
  return (
    <nav className="navbar">
      <Logo />
      <NavigationLinks />
      <SearchBox />
      <UserMenu />
    </nav>
  );
}
```

---

## 📄 第4层：Templates（模板）

**页面结构** - 定义页面布局

**示例**：
- 页面模板（Page Template）
- 文章模板（Article Template）
- 产品页面模板（Product Template）

**模板设计原则**：
- 不包含实际内容
- 使用占位内容
- 定义布局结构

**示例**：
```tsx
// ArticlePage Template
export function ArticlePageTemplate() {
  return (
    <div className="article-page">
      <Header />
      <main>
        <ArticleHeader />
        <ArticleContent />
        <ArticleFooter />
      </main>
      <Sidebar />
      <Footer />
    </div>
  );
}
```

---

## 📱 第5层：Pages（页面）

**完整界面** - 实际的页面实现

**示例**：
- 首页
- 文章详情页
- 产品列表页

**页面设计原则**：
- 组合多个模板和组件
- 包含实际内容
- 实现完整功能

---

## 🔄 开发流程

### 1. 定义Tokens

```
设计系统基础
├── 颜色系统
├── 间距系统
├── 字体系统
└── ...其他Token
```

### 2. 创建Atoms

```
基础组件
├── Button
├── Input
├── Label
└── ...其他原子
```

### 3. 组合Molecules

```
简单组件
├── SearchBox (Input + Button)
├── FormField (Label + Input + Error)
└── ...其他分子
```

### 4. 构建Organisms

```
复杂组件
├── NavigationBar (Logo + Links + SearchBox)
├── Form (多个FormField)
└── ...其他有机体
```

### 5. 设计Templates

```
页面模板
├── PageTemplate
├── ArticleTemplate
└── ...其他模板
```

### 6. 实现Pages

```
实际页面
├── HomePage
├── ArticlePage
└── ...其他页面
```

---

## ✅ 最佳实践

### 1. Token优先

**所有样式从Token开始**：
```tsx
// ✅ 好的做法
<Button style={{ background: tokens.color.primary }} />

// ❌ 不好的做法
<Button style={{ background: '#3B82F6' }} />
```

### 2. 组件组合

**优先组合而非修改**：
```tsx
// ✅ 好的做法：组合组件
<Card>
  <CardHeader title="标题" />
  <CardBody>内容</CardBody>
  <CardFooter>
    <Button>操作</Button>
  </CardFooter>
</Card>

// ❌ 不好的做法：创建新的复杂组件
<ComplexCardWithButton />
```

### 3. 文档化

**记录组件使用方式**：
```tsx
/**
 * Button组件
 *
 * @param variant - 按钮变体（primary/secondary/ghost）
 * @param size - 按钮大小（sm/md/lg）
 * @param disabled - 是否禁用
 *
 * @example
 * <Button variant="primary" size="md">
 *   点击我
 * </Button>
 */
```

### 4. 测试

**测试所有层级**：
```tsx
// Atoms测试
describe('Button', () => {
  it('should render with primary variant', () => {
    // ...
  });
});

// Molecules测试
describe('SearchBox', () => {
  it('should call onSearch when button clicked', () => {
    // ...
  });
});
```

---

## 📚 相关文档

- [Design Token方法论](./design-tokens.md) - Token基础
- [令牌工作流](./token-workflow.md) - Token开发流程
- [组件示例](../examples/component-examples.md) - 组件示例

---

## 🔗 快速导航

- [返回methodology/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ⏳ IN_PROGRESS (框架已完成，待完善详细内容)
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
