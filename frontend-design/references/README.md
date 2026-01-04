# References 文档导航

> 📚 **渐进式披露核心** - 按需加载的详细参考文档

---

## 📖 文档组织说明

本目录包含Frontend Design Agent Skills的详细参考文档，采用**渐进式披露架构**，每个文档200-300行，按需读取。

### 架构原则

1. **第一层**：SKILL.md（≤200行）- 入口点和导航地图
2. **第二层**：references/README.md（本文件）- 文档总览和导航
3. **第三层**：*.md详细文档（200-300行/文件）- 具体实现指导

---

## 🗂️ 目录导航

### 🔬 方法论文档（methodology/）

核心设计方法论，指导系统性设计思维：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [Design Token方法论](methodology/design-tokens.md) | 核心设计令牌系统 | 182行 | ✅ DONE |
| [令牌工作流](methodology/token-workflow.md) | 令牌开发流程 | 260行 | ✅ DONE |
| [系统化方法](methodology/systematic-approach.md) | 完整设计系统 | 360行 | ✅ DONE |

**何时读取**：
- 理解设计系统基础时
- 学习Design Token方法论时
- 建立设计令牌系统时

---

### 🔨 实现指南（implementation/）

具体实现指导，覆盖完整的开发流程：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [组件状态覆盖](implementation/component-states.md) | 8种状态完整覆盖（主文档） | 230行 | ✅ DONE |
| └─ [交互状态详解](implementation/component-states-interactive.md) | Default/Hover/Active/Focus | 310行 | ✅ DONE |
| └─ [功能状态详解](implementation/component-states-functional.md) | 功能状态总览（主文档） | 252行 | ✅ DONE |
| └─ [Disabled状态](implementation/component-states-disabled.md) | 禁用状态详解 | 405行 | ✅ DONE |
| └─ [Loading状态](implementation/component-states-loading.md) | 加载状态总览（主文档，3份子文档） | 240行 | ✅ DONE |
| └─ [Loading视觉与交互](implementation/component-states-loading-visual.md) | 视觉设计、交互行为、无障碍 | 357行 | ✅ DONE |
| └─ [Loading加载模式](implementation/component-states-loading-patterns.md) | 4种加载模式完整实现 | 650行 | ✅ DONE |
| └─ [Empty & Error状态](implementation/component-states-empty-error.md) | 空/错误状态详解 | 661行 | ✅ DONE |
| [无障碍指南](implementation/accessibility.md) | WCAG AA标准 | 280行 | ✅ DONE |
| [响应式设计](implementation/responsive-design.md) | 移动优先 | 290行 | ✅ DONE |
| [性能优化](implementation/performance-optimization.md) | 性能最佳实践（主文档） | 218行 | ✅ DONE |
| └─ [渲染优化](implementation/performance-rendering.md) | 加载+运行时+构建优化 | 277行 | ✅ DONE |
| └─ [资源优化](implementation/performance-resources.md) | 图片+网络优化 | 236行 | ✅ DONE |
| └─ [监控测试](implementation/performance-monitoring.md) | 测试+监控+检查清单 | 278行 | ✅ DONE |
| [SEO指南](implementation/seo-best-practices.md) | 搜索引擎优化 | 535行 | ✅ DONE |

**何时读取**：
- 实现具体功能时
- 解决技术问题时
- 查找最佳实践时

---

### 🎨 美学指导（aesthetics/）

设计美学指导，确保视觉质量：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [设计方向](aesthetics/design-directions.md) | 5种设计方向模板（主文档） | 232行 | ✅ DONE |
| └─ [现代风格详解](aesthetics/design-directions-modern.md) | Brutalist、Retro-Futuristic | 480行 | ✅ DONE |
| └─ [表现风格详解](aesthetics/design-directions-expressive.md) | Luxury、Playful总览（主文档） | 293行 | ✅ DONE |
| └─ [Luxury风格](aesthetics/design-directions-luxury.md) | 奢华风格详解 | 525行 | ✅ DONE |
| └─ [Playful风格](aesthetics/design-directions-playful.md) | 俏皮风格详解 | 634行 | ✅ DONE |
| └─ [编辑风格详解](aesthetics/design-directions-editorial.md) | Editorial | 350行 | ✅ DONE |
| [排版指南](aesthetics/typography.md) | 字体选择与排版 | 280行 | ✅ DONE |
| [色彩理论](aesthetics/color-theory.md) | 色彩系统 | 270行 | ✅ DONE |
| [反模式](aesthetics/anti-patterns.md) | 避免常见错误 | 290行 | ✅ DONE |

**何时读取**：
- 设计UI界面时
- 选择字体和配色时
- 避免设计陷阱时

---

### ✅ 质量保证（quality/）

质量标准和检查清单：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [质量清单](quality/checklist.md) | 完整检查清单 | 402行 | ✅ DONE |
| [审查标准](quality/review-criteria.md) | 代码审查标准 | 280行 | ✅ DONE |
| [测试策略](quality/testing-strategy.md) | 测试方法 | 280行 | ✅ DONE |

**何时读取**：
- 代码审查时
- 质量检查时
- 准备发布时

---

### 💡 示例文档（examples/）

实用示例和最佳实践：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [组件示例](examples/component-examples.md) | 组件示例总览（主文档，2份子文档） | 239行 | ✅ DONE |
| └─ [基础与表单组件](examples/component-examples-basic-form.md) | Button、Input、FormField、Select | 330行 | ✅ DONE |
| └─ [数据展示与反馈组件](examples/component-examples-display-feedback.md) | Card、Badge、Toast、Modal、Layout | 430行 | ✅ DONE |
| [布局示例](examples/layout-examples.md) | 布局示例 | 280行 | ✅ DONE |
| [动画示例](examples/animation-examples.md) | 动画示例 | 270行 | ✅ DONE |

**何时读取**：
- 学习示例时
- 寻找灵感时
- 实现类似功能时

---

### 🛠️ 框架特定（by-framework/）

特定框架的最佳实践：

| 文档 | 说明 | 行数 | 状态 |
|------|------|------|------|
| [React](by-framework/react.md) | React最佳实践（主文档，1份子文档） | 485行 | ✅ DONE |
| └─ [完整实现指南](by-framework/react-guide.md) | Context、表单、测试 | 560行 | ✅ DONE |
| [Vue](by-framework/vue.md) | Vue最佳实践（主文档，1份子文档） | 577行 | ✅ DONE |
| └─ [完整实现指南](by-framework/vue-guide.md) | 状态管理、路由、测试 | 580行 | ✅ DONE |
| [Svelte](by-framework/svelte.md) | Svelte最佳实践 | 644行 | ✅ DONE |
| [Angular](by-framework/angular.md) | Angular最佳实践（主文档，1份子文档） | 527行 | ✅ DONE |
| └─ [完整实现指南](by-framework/angular-guide.md) | 依赖注入、路由、表单、测试 | 620行 | ✅ DONE |
| [Tailwind](by-framework/tailwind.md) | Tailwind最佳实践（主文档，1份子文档） | 265行 | ✅ DONE |
| └─ [完整配置指南](by-framework/tailwind-guide.md) | 设计令牌、自定义配置、性能优化 | 380行 | ✅ DONE |
| [CSS Modules](by-framework/css-modules.md) | CSS Modules指南 | 280行 | ✅ DONE |
| [Styled Components](by-framework/styled-components.md) | Styled Components总览（主文档，1份子文档） | 294行 | ✅ DONE |
| └─ [完整实现指南](by-framework/styled-components-guide.md) | 安装、配置、高级用法、测试、性能优化 | 582行 | ✅ DONE |

**何时读取**：
- 使用特定框架时
- 配置开发环境时
- 解决框架特定问题时

---

## 📖 使用指南

### 如何使用渐进式披露架构

1. **从SKILL.md开始** - 了解技能概览和核心理念
2. **查阅本README.md** - 找到需要的文档类别
3. **读取具体文档** - 获取200-300行的详细指导
4. **按需深入** - 只加载需要的文档到上下文

### 文档命名规范

- 使用`kebab-case`（小写字母+连字符）
- 清晰表达文档内容
- 保持命名一致性

### 文档大小限制

- SKILL.md：≤200行
- references/*.md：200-300行
- 确保快速加载和高效阅读

---

## 🔗 快速导航

- [返回SKILL.md](../SKILL.md)
- [查看任务追踪](../TASK.md)
- [查看开发计划](../FRONTEND-DESIGN-DEVELOPMENT-PLAN.md)

---

> **最后更新**: 2026-01-04
> **维护者**: 项目团队
