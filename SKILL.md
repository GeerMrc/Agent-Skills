---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use when building web components, pages, applications, or styling/beautifying any web UI. Generates creative, polished code following Design Token methodology and progressive disclosure architecture.
license: MIT
---

# Frontend Design Agent Skills

> 📋 **版本**: v2.0.0
> 🎯 **目标**: 符合Agent Skills最佳实践，功能超越GLM原版

---

## 🎯 核心理念

本技能采用**渐进式披露三层架构（PDA Pattern）**，提供高质量的前端设计指导：

1. **极简入口点** - SKILL.md ≤ 200行（社区黄金标准）
2. **按需加载** - references/ 详细文档按需读取
3. **技术栈灵活** - 支持多框架（React/Vue/Svelte/Angular）
4. **设计优先** - Design Token方法论优先

---

## 🚀 快速开始

### 触发模式（Trigger Patterns）

**必须使用本技能的场景**：

- **网站开发**：用户请求任何网站、Web应用或Web组件开发
- **设计风格**：用户提及设计风格："现代"、"高级"、"极简"、"暗色模式"、"SaaS风格"
- **UI构建**：构建仪表板、落地页、管理面板或任何Web UI
- **设计改进**：用户要求"让它更好看"或"改进设计"
- **组件库**：创建组件库或设计系统
- **框架指定**：用户指定框架：React、Vue、Svelte、Next.js、Nuxt等
- **设计转换**：将设计/模型转换为代码
- **工具指定**：用户提及：Tailwind CSS、shadcn/ui、Material-UI、Chakra UI等

**触发关键词**：
- "构建一个网站/应用/组件"
- "创建一个仪表板/落地页"
- "为...设计一个UI"
- "让它变得现代/简洁/高级"
- "用...来设计这个"

**不要用于**：
- 后端API开发
- 纯逻辑/算法实现
- 非视觉代码任务

### 设计思维流程

在编写代码前，按以下步骤思考：

1. **理解上下文** - 用途是什么？谁使用？技术约束？
2. **选择美学方向** - 选择大胆、独特的设计风格（brutalist、retro-futuristic、luxury、playful、editorial等）
3. **确定核心差异** - 什么是令人难忘的？
4. **实现高质量代码** - 生产级、视觉震撼、细节精致

**关键原则**：
- 选择清晰的概念方向，精确执行
- 大胆的极繁主义和精致的极简主义都可行
- 关键是有意性，不是强度

### 技术栈默认值

**默认技术栈**（如未指定）：
- 框架：React + TypeScript
- 样式：Tailwind CSS
- 主题：CSS自定义属性（light/dark模式）

**支持的替代方案**：
- 框架：Vue、Svelte、Angular、vanilla HTML/CSS
- 样式：CSS Modules、SCSS、Styled Components、Emotion
- 组件库：MUI、Ant Design、Chakra UI、Headless UI

---

## 📚 文档导航

### 核心方法论文档

| 文档 | 说明 |
|------|------|
| [Design Token方法论](references/methodology/design-tokens.md) | 核心设计令牌系统 |
| [令牌工作流](references/methodology/token-workflow.md) | 令牌开发流程 |
| [系统化方法](references/methodology/systematic-approach.md) | 完整设计系统 |

### 实现指南

| 文档 | 说明 |
|------|------|
| [组件状态覆盖](references/implementation/component-states.md) | 8种状态完整覆盖 |
| [无障碍指南](references/implementation/accessibility.md) | WCAG AA标准 |
| [响应式设计](references/implementation/responsive-design.md) | 移动优先 |
| [性能优化](references/implementation/performance.md) | 性能最佳实践 |
| [SEO指南](references/implementation/seo-best-practices.md) | 搜索引擎优化 |

### 美学指导

| 文档 | 说明 |
|------|------|
| [设计方向](references/aesthetics/design-directions.md) | 5种设计方向模板 |
| [排版指南](references/aesthetics/typography.md) | 字体选择与排版 |
| [色彩理论](references/aesthetics/color-theory.md) | 色彩系统 |
| [反模式](references/aesthetics/anti-patterns.md) | 避免常见错误 |

### 质量保证

| 文档 | 说明 |
|------|------|
| [质量清单](references/quality/checklist.md) | 完整检查清单 |
| [审查标准](references/quality/review-criteria.md) | 代码审查标准 |
| [测试策略](references/quality/testing-strategy.md) | 测试方法 |

### 框架特定

| 文档 | 说明 |
|------|------|
| [React](references/by-framework/react.md) | React最佳实践 |
| [Vue](references/by-framework/vue.md) | Vue最佳实践 |
| [Svelte](references/by-framework/svelte.md) | Svelte最佳实践 |
| [Angular](references/by-framework/angular.md) | Angular最佳实践 |
| [Tailwind](references/by-framework/tailwind.md) | Tailwind配置 |

---

## 🎨 前端美学指南

### 核心原则

1. **排版** - 选择独特、美观的字体，避免Inter/Roboto/Arial等通用字体
2. **色彩与主题** - 使用CSS变量，主色调+强烈强调色
3. **动效** - 使用动画实现微交互和页面加载效果
4. **空间构图** - 非对称布局、重叠、对角线流动
5. **背景与细节** - 渐变网格、噪点纹理、几何图案

### 禁止事项

❌ 通用AI美学：
- 滥用的字体系列（Inter、Roboto、Arial）
- 陈词滥调的配色方案（特别是白色背景上的紫色渐变）
- 可预测的布局和组件模式
- 缺乏上下文特定性的千篇一律设计

✅ 正确做法：
- 每个设计都应该是独特的
- 在浅色和深色主题、不同字体、不同美学之间变化
- 避免收敛到通用选择（如Space Grotesk）

---

## 🔧 工具与脚本

### 验证工具
- `scripts/validate/check-tokens.py` - Token验证
- `scripts/validate/check-accessibility.py` - 无障碍检查
- `scripts/validate/check-performance.py` - 性能检查

### 生成工具
- `scripts/generate/generate-theme.py` - 主题生成
- `scripts/generate/generate-component.py` - 组件生成
- `scripts/generate/export-tokens.py` - Token导出

### 测试工具
- `scripts/test/test-skill.py` - 技能测试

---

## 📦 项目模板

提供预配置的项目模板：
- `templates/react/` - React项目模板
- `templates/vue/` - Vue项目模板
- `templates/vanilla/` - 原生HTML/CSS/JS模板

---

## ✅ 质量标准

- 代码覆盖率 > 80%
- WCAG AA 无障碍标准
- 移动优先响应式设计
- 性能优化（LCP < 2.5s）
- SEO最佳实践

---

## 📖 更多文档

- [开发流程规范](docs/DEVELOPMENT_WORKFLOW.md)
- [贡献指南](docs/CONTRIBUTING.md)
- [架构说明](docs/ARCHITECTURE.md)
- [API文档](docs/API.md)
- [迁移指南](docs/MIGRATION_GUIDE.md)

---

> **版本**: v2.0.0 | **状态**: 🚀 Active Development
