# 迁移指南

> 📖 **版本**: v2.2.0
> 📅 **更新日期**: 2025-01-04

---

## 📑 目录

- [概述](#概述)
- [从 GLM v1.0 迁移](#从-glm-v10-迁移)
- [从 v2.0.x 升级](#从-v20x-升级)
- [Design Token 迁移](#design-token-迁移)
- [框架迁移指南](#框架迁移指南)
- [常见问题](#常见问题)

---

## 概述

本指南帮助您从旧版本迁移到 Frontend Design Agent Skills v2.2.0。

### 迁移路径

```
GLM v1.0 (原始版本)
    │
    └─▶ v2.0.0 (重构版本)
            │
            ├─▶ v2.1.0 (Phase 2 完成)
            │
            ├─▶ v2.1.1 (Phase 3 完成)
            │
            ├─▶ v2.1.2 (Phase 4 完成)
            │
            └─▶ v2.2.0 (Phase 5 完成 - 当前版本)
```

### 版本对比

| 特性 | GLM v1.0 | v2.0.0 | v2.2.0 |
|------|----------|--------|--------|
| SKILL.md 行数 | 980 行 | 175 行 | 193 行 |
| 上下文效率 | 基准 | 11.4x ↑ | 11.4x ↑ |
| 标准化程度 | 40% | 95% | 95% |
| 框架支持 | React/TS | React/Vue/Svelte/TS | +Angular |
| 工具脚本 | ❌ | ❌ | ✅ 6个工具 |
| 项目模板 | ❌ | ❌ | ✅ 3个模板 |
| OKLCH 支持 | ❌ | ❌ | ✅ 完整支持 |

---

## 从 GLM v1.0 迁移

### 主要变化

#### 1. 文档结构重组

**GLM v1.0**:
```
GLM-SKILL.md (980行，单一文件)
```

**v2.2.0**:
```
SKILL.md (193行，入口点)
├── references/README.md (导航)
├── methodology/ (方法论)
│   ├── design-tokens.md
│   ├── component-states.md
│   └── design-directions.md
├── frameworks/ (框架指南)
│   ├── react.md
│   ├── vue.md
│   ├── svelte.md
│   └── angular.md
├── quality/ (质量指南)
│   ├── checklist.md
│   ├── accessibility.md
│   ├── performance.md
│   └── seo.md
└── scripts/ (工具脚本)
    ├── validate/
    ├── generate/
    └── test/
```

#### 2. 渐进式披露架构

采用 **Progressive Disclosure Architecture (PDA)** 模式：

- **第1层**: SKILL.md - 快速概览（<200行）
- **第2层**: references/README.md - 分类导航
- **第3层**: 具体文档 - 详细内容

#### 3. 技术栈升级

| 特性 | GLM v1.0 | v2.2.0 |
|------|----------|--------|
| 色彩系统 | RGB/HSL | OKLCH |
| 状态覆盖 | 5种 | 8种 |
| 框架 | 仅 React | React/Vue/Svelte/Angular |
| 工具 | 无 | 6个Python工具 |
| 模板 | 无 | 3个项目模板 |

### 迁移步骤

#### 步骤1: 备份现有配置

```bash
# 备份现有的 GLM-SKILL.md
cp GLM-SKILL.md GLM-SKILL.md.backup

# 备份现有的 Design Tokens
cp tokens.json tokens.json.backup
```

#### 步骤2: 安装新版本

```bash
# 克隆新版本仓库
git clone https://github.com/your-org/frontend-design.git
cd frontend-design

# 或者如果您是从源码升级
git pull origin main
```

#### 步骤3: 迁移 Design Tokens

**RGB/HSL 转 OKLCH**:

旧格式 (GLM v1.0):
```json
{
  "color-primary": "#3B82F6",
  "color-secondary": "#10B981"
}
```

新格式 (v2.2.0):
```json
{
  "color-primary": "oklch(0.65 0.19 250)",
  "color-secondary": "oklch(0.65 0.15 160)"
}
```

**使用转换工具**:

```bash
# 使用提供的转换脚本
python scripts/convert-tokens.py tokens.json.backup --format oklch --output tokens.json
```

#### 步骤4: 更新组件状态

GLM v1.0 支持 5 种状态，v2.2.0 支持全部 8 种状态：

**新增状态**:
- `loading` - 加载状态
- `empty` - 空状态
- `error` - 错误状态

**更新组件**:

```css
/* GLM v1.0 */
.button {
  /* 5种状态: default, hover, active, focus, disabled */
}

/* v2.2.0 */
.button {
  /* 8种状态: default, hover, active, focus, disabled, loading, empty, error */
}
```

#### 步骤5: 更新导入路径

**GLM v1.0**:
```typescript
import { designTokens } from '@/GLM-SKILL';
```

**v2.2.0**:
```typescript
import { designTokens } from '@/tokens';
```

#### 步骤6: 验证迁移

```bash
# 验证 Design Tokens
python scripts/validate/check-tokens.py tokens.json

# 验证组件状态覆盖
python scripts/validate/check-accessibility.py src/components/

# 运行测试套件
npm test
```

### 迁移检查清单

- [ ] 备份现有文件
- [ ] 安装 v2.2.0
- [ ] 转换 Design Tokens 为 OKLCH
- [ ] 更新组件状态（8种状态）
- [ ] 更新导入路径
- [ ] 验证 Tokens 格式
- [ ] 验证无障碍性
- [ ] 运行测试套件
- [ ] 更新文档

---

## 从 v2.0.x 升级

### v2.0.0 → v2.1.0

**新增功能**:
- ✅ 组件状态覆盖指南（8种状态）
- ✅ 5种设计方向模板
- ✅ 质量检查清单
- ✅ 多框架支持（Vue、Svelte、Angular）
- ✅ 性能优化指南
- ✅ SEO最佳实践

**迁移步骤**:

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 更新依赖（如果需要）
# npm install

# 3. 验证现有 Tokens
python scripts/validate/check-tokens.py tokens.json

# 4. 查看新增文档
cat references/methodology/component-states.md
cat references/quality/checklist.md
```

**破坏性变更**: 无

---

### v2.1.0 → v2.1.1

**新增功能**:
- ✅ 6个Python工具脚本
- ✅ Design Token 验证工具
- ✅ 无障碍检查工具
- ✅ 性能检查工具
- ✅ 主题生成工具
- ✅ 组件生成工具

**迁移步骤**:

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 设置 Python 环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装依赖（如果有 requirements.txt）
# pip install -r requirements.txt

# 4. 测试工具
python scripts/validate/check-tokens.py tokens.json
```

**破坏性变更**: 无

---

### v2.1.1 → v2.1.2

**新增功能**:
- ✅ 3个完整项目模板（React、Vue、Vanilla）
- ✅ 完整测试套件
- ✅ 模板完整性验证

**迁移步骤**:

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 测试模板
cd templates/react
npm install
npm run build

# 3. 运行模板测试
cd ../..
python scripts/test/test-templates.py
```

**破坏性变更**: 无

---

### v2.1.2 → v2.2.0

**新增功能**:
- ✅ 完整 API 文档（docs/API.md）
- ✅ 贡献指南（CONTRIBUTING.md）
- ✅ 迁移指南（MIGRATION_GUIDE.md）
- ✅ 发布说明准备

**迁移步骤**:

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 查看新文档
cat docs/API.md
cat CONTRIBUTING.md
cat MIGRATION_GUIDE.md

# 3. 无需代码更改，仅文档更新
```

**破坏性变更**: 无

---

## Design Token 迁移

### 色彩系统迁移

#### RGB/HSL 转 OKLCH

**为什么使用 OKLCH？**

- **感知均匀性**: OKLCH 提供更一致的颜色感知
- **更广色域**: 支持更丰富的颜色空间
- **更好对比度**: 更准确的可访问性计算
- **未来标准**: CSS Color Level 4 规范

**转换示例**:

| RGB | HSL | OKLCH |
|-----|-----|-------|
| `#3B82F6` | `hsl(217, 91%, 60%)` | `oklch(0.65 0.19 250)` |
| `#10B981` | `hsl(160, 84%, 39%)` | `oklch(0.65 0.15 160)` |
| `#EF4444` | `hsl(0, 79%, 60%)` | `oklch(0.63 0.24 25)` |

**手动转换**:

使用在线工具:
- [OKLCH Color Picker](https://oklch.com)
- [Color.js Converter](https://colorjs.io/apps/)

**使用转换脚本**:

```bash
python scripts/convert/rgb-to-oklch.py tokens.json --output tokens-new.json
```

#### Token 命名规范

**旧命名** (不推荐):
```json
{
  "primaryBlue": "#3B82F6",
  "primary_red": "#EF4444"
}
```

**新命名** (推荐):
```json
{
  "color-primary": "oklch(0.65 0.19 250)",
  "color-error": "oklch(0.63 0.24 25)"
}
```

**命名规则**:
- 使用小写字母和连字符
- 语义化命名（primary, secondary, error）
- 避免具体颜色名（blue, red）

### Token 类别迁移

#### 间距 Token

**旧格式**:
```json
{
  "spacing-xs": "4px",
  "spacing-sm": "8px",
  "spacing-md": "16px"
}
```

**新格式** (推荐使用 rem):
```json
{
  "spacing-xs": "0.25rem",
  "spacing-sm": "0.5rem",
  "spacing-md": "1rem"
}
```

#### 字体 Token

**旧格式**:
```json
{
  "font-base": "16px",
  "font-h1": "32px"
}
```

**新格式**:
```json
{
  "font-size-base": "1rem",
  "font-size-h1": "2rem",
  "font-weight-normal": "400",
  "font-weight-bold": "700"
}
```

### Token 验证

使用提供的验证工具确保 Token 符合规范：

```bash
# 验证 Token 格式
python scripts/validate/check-tokens.py tokens.json

# 详细输出
python scripts/validate/check-tokens.py tokens.json --format markdown --output report.md

# 严格模式
python scripts/validate/check-tokens.py tokens.json --strict
```

**验证规则**:
- ✅ Token 命名使用小写字母和连字符
- ✅ 颜色 Token 使用 OKLCH 格式
- ✅ 间距 Token 使用 rem 或 px 单位
- ✅ 必需类别完整（color, spacing, font, shadow, radius）

---

## 框架迁移指南

### React → Vue

**组件对比**:

```typescript
// React
import { useState } from 'react';

export function Button({ variant = 'primary', onClick }) {
  const [loading, setLoading] = useState(false);

  return (
    <button className={`btn btn-${variant}`} onClick={onClick}>
      {loading ? 'Loading...' : 'Click'}
    </button>
  );
}
```

```vue
<!-- Vue -->
<script setup lang="ts">
import { ref } from 'vue';

interface Props {
  variant?: string;
  onClick?: () => void;
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary'
});

const loading = ref(false);
</script>

<template>
  <button :class="['btn', `btn-${variant}`]" @click="onClick">
    {{ loading ? 'Loading...' : 'Click' }}
  </button>
</template>
```

### React → Svelte

```typescript
// React
export function Button({ variant = 'primary', children }) {
  return <button className={`btn btn-${variant}`}>{children}</button>;
}
```

```svelte
<!-- Svelte -->
<script lang="ts">
export let variant: string = 'primary';
</script>

<button class="btn btn-{variant}">
  <slot />
</button>
```

### 框架特定资源

- [React → Vue 指南](https://vuejs.org/guide/extras/composition-api-faq.html)
- [React → Svelte 指南](https://svelte.dev/docs#run-time-component-options)
- [React → Angular 指南](https://angular.io/guide/architecture)

---

## 常见问题

### Q1: 迁移后原有代码还能工作吗？

**A**: 是的，但可能需要小幅调整：
- 更新导入路径
- 转换 Token 格式
- 添加新的组件状态

### Q2: OKLCH 是否被所有浏览器支持？

**A**: 现代浏览器（Chrome 111+, Firefox 113+, Safari 15.4+）都已支持。对于旧浏览器，可以使用降级方案：

```css
.button {
  background: #3B82F6; /* 降级 */
  background: oklch(0.65 0.19 250); /* 现代浏览器 */
}
```

### Q3: 如何处理自定义的 Token？

**A**: 您可以保留自定义 Token，但建议：
1. 按照命名规范重命名
2. 验证格式正确性
3. 添加到项目的 token 文件中

### Q4: 迁移需要多长时间？

**A**: 取决于项目规模：
- 小型项目（<50 组件）: 1-2 天
- 中型项目（50-200 组件）: 3-5 天
- 大型项目（>200 组件）: 1-2 周

### Q5: 是否可以分阶段迁移？

**A**: 可以，建议的迁移顺序：
1. 阶段1: 更新文档和工具
2. 阶段2: 转换 Design Tokens
3. 阶段3: 更新组件状态
4. 阶段4: 添加新功能（性能、SEO等）

### Q6: 迁移过程中遇到问题怎么办？

**A**:
1. 查看本文档的相关章节
2. 查阅 API 文档 (`docs/API.md`)
3. 在 GitHub Issues 提问
4. 联系项目维护者

---

## 获取帮助

### 资源链接

- [API 文档](./docs/API.md)
- [贡献指南](./CONTRIBUTING.md)
- [开发规范](./docs/DEVELOPMENT_WORKFLOW.md)
- [任务追踪](./TASK.md)

### 报告问题

如果您在迁移过程中遇到问题：

1. **搜索现有 Issues**: [GitHub Issues](https://github.com/your-org/frontend-design/issues)
2. **创建新 Issue**: 包含详细的错误信息和复现步骤
3. **Pull Request**: 如果您有解决方案，欢迎提交 PR

---

## 变更日志

完整的变更记录请查看 [CHANGELOG.md](./CHANGELOG.md)。

---

> **最后更新**: 2025-01-04
> **维护者**: Frontend Design Agent Skills 项目团队
