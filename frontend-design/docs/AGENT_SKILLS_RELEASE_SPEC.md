# Agent Skills 技能包发布规范

> 📋 **文档版本**: v1.0
> 📅 **创建日期**: 2025-01-04
> 🎯 **适用范围**: Agent Skills 技能包的创建、验证、打包和发布

---

## 📖 文档说明

### 文档目的
本文档基于官方 [Agent Skills 规范](https://agentskills.io/specification) 和 [Anthropic 官方文档](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)，定义了技能包的完整发布流程和规范要求。

### 规范来源
- **官方规范**: [agentskills.io/specification](https://agentskills.io/specification)
- **官方仓库**: [github.com/anthropics/skills](https://github.com/anthropics/skills)
- **发布日期**: 2025年12月18日（Agent Skills 作为开放标准正式发布）

---

## 🎯 关键概念区分

### ⚠️ GitHub 仓库 vs 发布的技能包

> **重要**: 必须明确区分两个不同的概念

| 概念 | 定义 | 内容 | 用途 |
|------|------|------|------|
| **GitHub 仓库** | 版本控制的代码仓库 | 所有文件 + docs/ + 开发文档 | 开发管理、版本控制、协作 |
| **发布的技能包** | 打包分发的技能文件 | 只包含技能运行所需文件 | AI Agent 使用技能 |

### GitHub 仓库结构（完整）

```
Agent-Skills/                    # GitHub 仓库根目录
├── README.md                    # 仓库总览
├── CHANGELOG.md                 # 变更日志
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # 许可证
├── .gitignore                   # 仓库级忽略配置
├── release/                     # 🆕 发布管理目录（仅在仓库中）
│   ├── package/                 # 🆕 打包工具
│   │   ├── package-skill.py     # 🆕 自动打包脚本
│   │   └── requirements.txt     # 🆕 依赖
│   ├── verify/                  # 🆕 验证工具
│   │   ├── verify-before-release.py  # 🆕 发布前验证
│   │   └── verify-after-install.py   # 🆕 安装后验证
│   └── output/                  # 🆕 发布包输出（.gitignore）
├── docs/                        # ✅ 开发文档目录（仅在仓库中）
│   ├── README.md                # 🆕 文档导航索引
│   ├── DEVELOPMENT_WORKFLOW.md  # 开发流程规范
│   ├── API.md                   # API 文档
│   ├── TASK.md                  # 任务追踪
│   └── AGENT_SKILLS_RELEASE_SPEC.md
├── frontend-design/             # 技能包目录
│   ├── SKILL.md                 # 必需
│   ├── LICENSE
│   ├── README.md
│   ├── CHANGELOG.md
│   ├── scripts/
│   ├── references/
│   └── templates/
└── .git/                        # Git 版本控制
```

### 发布的技能包内容（精简）

> **关键**: 发布的技能包**不包含** `docs/` 和 `tests/` 目录

```
frontend-design/                 # 发布的技能包
├── SKILL.md                     # ✅ 必需
├── LICENSE                      # ✅ 可选
├── README.md                    # ✅ 可选
├── CHANGELOG.md                 # ✅ 可选
├── scripts/                     # ✅ 可选 - 技能运行所需的脚本
│   ├── check-tokens.py
│   ├── check-accessibility.py
│   ├── generate-theme.py
│   └── ...
├── references/                  # ✅ 可选 - 技能参考文档
│   ├── methodology/
│   ├── by-framework/
│   └── quality/
├── templates/                   # ✅ 可选 - 项目模板
│   ├── react/
│   ├── vue/
│   └── vanilla/
└── assets/                      # ✅ 可选 - 静态资源
```

### ❌ 不应包含在发布包中的内容

以下内容**只在 GitHub 仓库中**，**不包含在发布的技能包**中：

| 目录/文件 | 原因 |
|-----------|------|
| `release/` | 发布和验证工具，开发管理用 |
| `docs/` | 开发文档，给开发者看的，不是技能运行所需 |
| `tests/` | 测试和验证工具，开发管理用 |
| `TASK.md` | 任务追踪，开发管理用 |
| `FRONTEND-DESIGN-DEVELOPMENT-PLAN.md` | 开发计划 |
| `PRE_RELEASE_AUDIT_REPORT.md` | 审计报告 |
| `QUALITY_VALIDATION_REPORT.md` | 验证报告 |
| `RELEASE_NOTES.md` | 发布说明 |
| `MIGRATION_GUIDE.md` | 迁移指南 |
| `ARCHITECTURE.md` | 架构文档 |
| `API.md` | API 文档 |
| `DEVELOPMENT_WORKFLOW.md` | 开发流程规范 |
| `AGENT_SKILLS_RELEASE_SPEC.md` | 发布规范文档 |
| `.git/` | Git 版本控制 |

### 📦 技能包打包时的排除规则

创建发布包时，必须排除以下内容：

```python
# 打包时排除的目录和文件
EXCLUDE_PATTERNS = [
    '.git/',                    # Git 版本控制
    '.gitignore',               # Git 配置
    'release/',                 # 🆕 发布和验证工具
    'docs/',                    # ⚠️ 开发文档（关键！）
    'tests/',                   # 🆕 测试和验证工具
    '*.md',                     # 只保留必需的 MD 文件
]

# 只包含的 MD 文件
INCLUDE_MD_ONLY = [
    'SKILL.md',                 # 必需
    'README.md',                # 可选
    'CHANGELOG.md',             # 可选
    'CONTRIBUTING.md',          # 可选
]
```

---

## 🏗️ 技能包目录结构

### 最小结构

一个技能包是一个包含 `SKILL.md` 文件的目录：

```
skill-name/
└── SKILL.md          # 必需
```

### 完整结构

```
skill-name/
├── SKILL.md          # 必需 - 技能入口文件
├── LICENSE           # 可选 - 许可证文件
├── README.md         # 可选 - 技能说明文档
├── scripts/          # 可选 - 可执行代码
│   ├── validate/     # 验证工具
│   ├── generate/     # 生成工具
│   └── utils/        # 共享模块
├── references/       # 可选 - 详细文档
│   ├── methodology/  # 方法论文档
│   ├── by-framework/ # 框架特定文档
│   └── quality/      # 质量指南
├── templates/        # 可选 - 项目模板
│   ├── react/
│   ├── vue/
│   └── vanilla/
├── assets/           # 可选 - 静态资源
│   ├── images/
│   ├── fonts/
│   └── data/
└── tests/            # 可选 - 测试文件
    ├── unit/
    └── integration/
```

---

## 📄 SKILL.md 格式规范

### YAML Frontmatter（必需）

```yaml
---
name: skill-name
description: A clear description of what this skill does and when to use it.
license: MIT
metadata:
  author: your-name
  version: "1.0.0"
---
```

### 字段规范

| 字段 | 必需 | 约束 |
|------|------|------|
| `name` | ✅ 是 | 最多64字符。仅允许小写字母、数字和连字符。不能以连字符开头或结尾。 |
| `description` | ✅ 是 | 最多1024字符。非空。描述技能的功能和使用场景。 |
| `license` | ❌ 否 | 许可证名称或引用打包的许可证文件。 |
| `compatibility` | ❌ 否 | 最多500字符。指示环境要求（预期产品、系统包、网络访问等）。 |
| `metadata` | ❌ 否 | 用于额外元数据的任意键值映射。 |
| `allowed-tools` | ❌ 否 | 技能可以使用的预批准工具的空格分隔列表（实验性）。 |

#### `name` 字段规范

- **长度**: 1-64 字符
- **允许字符**: Unicode 小写字母数字字符和连字符（`a-z` 和 `-`）
- **禁止**:
  - 不能以 `-` 开头或结尾
  - 不能包含连续连字符（`--`）
  - 必须与父目录名称匹配

**有效示例**:
```yaml
name: frontend-design
name: pdf-processing
name: code-reviewer
```

**无效示例**:
```yaml
name: Frontend-Design  # ❌ 大写字母不允许
name: -pdf            # ❌ 不能以连字符开头
name: pdf--processing # ❌ 连续连字符不允许
```

#### `description` 字段规范

- **长度**: 1-1024 字符
- **内容要求**: 应描述技能的功能和使用场景
- **最佳实践**: 包含有助于代理识别相关任务的特定关键词

**好的示例**:
```yaml
description: Create distinctive, production-grade frontend interfaces using Design Token methodology, OKLCH color system, and 8-state component patterns. Use when building user interfaces, design systems, or when the user mentions frontend design, UI/UX, or component development.
```

**差的示例**:
```yaml
description: Helps with frontend design.  # ❌ 太简单，缺少关键词
```

#### `license` 字段规范

- **推荐**: 保持简短（许可证名称或打包的许可证文件名称）

**示例**:
```yaml
license: MIT
license: Apache-2.0
license: Proprietary. LICENSE.txt has complete terms
```

#### `compatibility` 字段规范

- **长度**: 如果提供，最多500字符
- **使用场景**: 仅在技能有特定环境要求时包含
- **内容**: 可以指示预期产品、必需的系统包、网络访问需求等

**示例**:
```yaml
compatibility: Designed for Claude Code (or similar products)
compatibility: Requires git, docker, jq, and access to the internet
compatibility: Requires Python 3.8+, Node.js 18+, and npm
```

#### `metadata` 字段规范

- **格式**: 从字符串键到字符串值的映射
- **用途**: 客户端可以使用它来存储 Agent Skills 规范未定义的额外属性
- **建议**: 使键名合理唯一以避免意外冲突

**示例**:
```yaml
metadata:
  author: maric
  version: "2.2.0"
  category: development
  tags: frontend,design,ui,ux
```

#### `allowed-tools` 字段规范（实验性）

- **格式**: 预批准运行的工具的空格分隔列表
- **注意**: 实验性功能。代理实现之间的支持可能有所不同

**示例**:
```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read Write
```

### Markdown 主体内容

Frontmatter 之后的 Markdown 主体包含技能指令。没有格式限制。编写任何有助于代理有效执行任务的内容。

**推荐的章节结构**:
```markdown
# 技能名称

## 概述
简要描述技能的核心功能和使用场景。

## 使用场景
列出触发此技能的典型场景。

## 核心功能
- 功能1
- 功能2
- 功能3

## 使用指南
分步骤说明如何使用此技能。

## 示例
提供输入输出示例。

## 注意事项
列出常见边缘情况和注意事项。

## 相关资源
- [详细指南](references/guide.md)
- [API 文档](references/api.md)
```

---

## 📁 可选目录规范

### scripts/ 目录

包含代理可以运行的可执行代码。脚本应该：
- 自包含或清楚记录依赖关系
- 包含有用的错误消息
- 优雅地处理边缘情况

**支持的语言**（取决于代理实现）：
- Python (推荐用于复杂逻辑)
- Bash (推荐用于系统操作)
- JavaScript/Node.js (推荐用于 Web 相关)

**目录结构示例**:
```
scripts/
├── validate/
│   ├── check-tokens.py
│   └── check-accessibility.py
├── generate/
│   ├── generate-component.py
│   └── generate-theme.py
└── utils/
    ├── color.py
    ├── token.py
    └── reporter.py
```

### references/ 目录

包含代理可以按需阅读的其他文档：
- `REFERENCE.md` - 详细技术参考
- `FORMS.md` - 表单模板或结构化数据格式
- 特定领域文件（`finance.md`、`legal.md` 等）

**保持单个参考文件聚焦**。代理按需加载这些文件，因此较小的文件意味着更少的上下文使用。

**目录结构示例**:
```
references/
├── README.md              # 导航文档
├── methodology/
│   ├── design-tokens.md
│   ├── component-states.md
│   └── design-directions.md
├── by-framework/
│   ├── react.md
│   ├── vue.md
│   ├── svelte.md
│   └── angular.md
└── quality/
    ├── checklist.md
    ├── performance.md
    └── seo-best-practices.md
```

### templates/ 目录

包含静态资源：
- 模板（文档模板、配置模板）
- 图像（图表、示例）
- 数据文件（查找表、模式）

**目录结构示例**:
```
templates/
├── react/
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── src/
├── vue/
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
└── vanilla/
    ├── package.json
    └── src/
```

### assets/ 目录

包含静态资源文件：
- 图像（图表、示例、图标）
- 字体
- 数据文件（JSON、YAML 配置）

**目录结构示例**:
```
assets/
├── images/
│   ├── architecture-diagram.png
│   └── component-states.png
├── fonts/
│   └── inter/
└── data/
    ├── color-palettes.json
    └── token-sets.yaml
```

### tests/ 目录

包含测试文件和基准配置：
- 单元测试
- 集成测试
- 测试基准配置

**目录结构示例**:
```
tests/
├── unit/
│   └── test-validators.py
├── integration/
│   └── test-workflow.py
└── baselines/
    └── test-baseline.json
```

---

## 🔄 渐进式披露原则

### 三层披露架构

技能应结构化为高效使用上下文：

1. **元数据层** (~100 tokens):
   - 所有技能的 `name` 和 `description` 字段在启动时加载
   - 代理使用此信息决定何时激活技能

2. **指令层** (< 5000 tokens 推荐):
   - 技能激活时加载完整的 `SKILL.md` 主体
   - 包含核心指令和使用指南

3. **资源层** (按需):
   - 文件（如 `scripts/`、`references/` 或 `assets/` 中的文件）仅在需要时加载
   - 代理可以选择性地探索这些资源

### 行数限制

- **SKILL.md**: 建议保持在 **500 行**以下
- **最佳实践**: 将详细参考材料移至单独的文件

### 上下文效率

```
启动时: 所有技能的 name + description (~100 tokens/技能)
     ↓
激活时: 完整 SKILL.md (~1000-5000 tokens)
     ↓
执行时: 按需加载 scripts/references/assets (按需)
```

---

## 🔗 文件引用规范

### 相对路径引用

在技能中引用其他文件时，使用从技能根目录开始的相对路径：

```markdown
## 详细指南

参见 [参考指南](references/REFERENCE.md) 了解详细信息。

运行提取脚本:
```bash
python scripts/extract.py
```

使用项目模板:
```bash
cp -r templates/react ./my-project
```
```

### 引用深度限制

- **从 SKILL.md 开始**: 保持文件引用仅一级深度
- **避免**: 深度嵌套的引用链（如 A → B → C → D）

**好的示例**:
```
SKILL.md → references/guide.md
SKILL.md → scripts/tool.py
```

**避免的示例**:
```
SKILL.md → references/guide.md → references/details.md → references/api.md
```

---

## ✅ 技能包验证

### 官方验证工具

使用 `skills-ref` 参考库验证技能：

```bash
skills-ref validate ./my-skill
```

### 验证检查项

| 检查项 | 说明 |
|--------|------|
| SKILL.md 存在 | 必需文件存在 |
| Frontmatter 有效 | YAML 格式正确 |
| name 字段有效 | 符合命名规范 |
| description 字段有效 | 非空且在长度限制内 |
| 目录名称匹配 | skill-name/ 与 name 字段一致 |

### 自定义验证脚本

可以创建自定义验证脚本：

```python
#!/usr/bin/env python3
"""技能包验证脚本"""

import os
import sys
import yaml
from pathlib import Path

def validate_skill(skill_path: Path) -> bool:
    """验证技能包结构"""
    # 检查 SKILL.md 存在
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print("❌ SKILL.md 不存在")
        return False

    # 解析 YAML frontmatter
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content.startswith('---'):
            print("❌ 缺少 YAML frontmatter")
            return False

        # 提取 frontmatter
        _, frontmatter, _ = content.split('---', 2)
        try:
            metadata = yaml.safe_load(frontmatter)
        except yaml.YAMLError as e:
            print(f"❌ YAML 解析错误: {e}")
            return False

    # 验证必需字段
    if 'name' not in metadata:
        print("❌ 缺少 name 字段")
        return False

    if 'description' not in metadata:
        print("❌ 缺少 description 字段")
        return False

    # 验证 name 格式
    name = metadata['name']
    if not name.islower() or '--' in name or name.startswith('-') or name.endswith('-'):
        print(f"❌ name 格式无效: {name}")
        return False

    # 验证目录名称匹配
    if skill_path.name != name:
        print(f"❌ 目录名称与 name 不匹配: {skill_path.name} != {name}")
        return False

    # 验证 description 长度
    description = metadata['description']
    if len(description) > 1024:
        print(f"❌ description 超过 1024 字符")
        return False

    # 验证 SKILL.md 行数
    with open(skill_md, 'r', encoding='utf-8') as f:
        lines = len(f.readlines())
        if lines > 500:
            print(f"⚠️  SKILL.md 超过 500 行 ({lines} 行)")

    print("✅ 技能包验证通过")
    return True

if __name__ == '__main__':
    skill_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    success = validate_skill(skill_path)
    sys.exit(0 if success else 1)
```

---

## 📦 技能包打包

### ZIP 打包格式

技能包可以打包为 `.zip` 文件进行分发：

```bash
# 使用 Python 脚本打包（来自官方示例）
python scripts/package_skill.py path/to/skill-folder

# 指定输出目录
python scripts/package_skill.py path/to/skill-folder ./dist

# 输出: my-skill.zip 或 dist/my-skill.zip
```

### 打包脚本示例

```python
#!/usr/bin/env python3
"""技能包打包脚本"""

import zipfile
from pathlib import Path

def package_skill(skill_path: Path, output_dir: Path = None) -> Path:
    """打包技能包为 ZIP 文件"""
    skill_path = skill_path.resolve()

    if output_dir is None:
        output_dir = skill_path.parent
    else:
        output_dir = output_dir.resolve()

    zip_name = f"{skill_path.name}.zip"
    output_path = output_dir / zip_name

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in skill_path.rglob('*'):
            if file.is_file() and '.git' not in file.parts:
                arcname = file.relative_to(skill_path.parent)
                zipf.write(file, arcname)

    print(f"✅ 技能包已打包: {output_path}")
    return output_path

if __name__ == '__main__':
    import sys
    skill_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    package_skill(skill_path, output_dir)
```

---

## 🚀 技能包发布流程

### 1. 准备发布

#### 1.1 版本号规范

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

```
major.minor.patch

例如: 2.2.0
- major: 重大版本更新（破坏性变更）
- minor: 次要版本更新（新功能，向后兼容）
- patch: 补丁版本（问题修复，向后兼容）
```

#### 1.2 更新 CHANGELOG.md

```markdown
## [2.2.0] - 2025-01-04

### Added
- ✅ 新功能1
- ✅ 新功能2

### Changed
- 🔄 功能改进

### Fixed
- 🐛 问题修复
```

### 2. Git 标签和提交

#### 2.1 创建 Git 标签

```bash
# 创建带注释的标签
git tag -a v2.2.0 -m "Release v2.2.0 - Phase 5 完成"

# 推送标签到远端
git push origin v2.2.0
```

#### 2.2 提交规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)：

```
type(scope): subject

type:
  feat: 新功能
  fix: 问题修复
  docs: 文档更新
  style: 代码格式
  refactor: 代码重构
  test: 测试相关
  chore: 构建/工具

示例:
feat(templates): add React project template
fix(scripts): fix f-string syntax error
docs(release): add release notes for v2.2.0
```

### 3. GitHub Release

#### 3.1 创建 Release

通过 GitHub MCP 或 Web UI 创建 Release：

```markdown
# Release v2.2.0

## 新功能
- 完整的 API 文档（docs/API.md - 938行）
- 贡献指南（CONTRIBUTING.md - 617行）
- 迁移指南（MIGRATION_GUIDE.md - 607行）
- 发布说明（RELEASE_NOTES.md - 492行）

## 破坏性变更
无

## 升级指南
从 v2.1.2 升级：
```bash
git pull origin main
git checkout v2.2.0
```

## 完整变更日志
参见 [CHANGELOG.md](CHANGELOG.md)
```

#### 3.2 附加资产

可以附加以下资产到 Release：
- 技能包 ZIP 文件
- 验证报告
- 质量指标

### 4. 多技能仓库结构

如果在一个仓库中管理多个技能包（如 `Agent-Skills` 仓库）：

```
Agent-Skills/
├── README.md              # 仓库总览
├── frontend-design/       # 技能包1
│   ├── SKILL.md
│   ├── scripts/
│   ├── references/
│   └── templates/
├── backend-api/           # 技能包2
│   ├── SKILL.md
│   └── scripts/
└── data-science/          # 技能包3
    ├── SKILL.md
    └── references/
```

#### 4.1 仓库级 README.md

```markdown
# Agent-Skills

> AI Agent 技能包集合

## 技能包列表

| 技能包 | 版本 | 描述 |
|--------|------|------|
| [frontend-design](./frontend-design/) | v2.2.0 | 创建独特、生产级的前端界面 |
| [backend-api](./backend-api/) | v1.0.0 | 后端 API 开发技能 |
| [data-science](./data-science/) | v1.0.0 | 数据科学和机器学习 |

## 安装

在 Claude Code 中：

```bash
/plugin marketplace add your-username/Agent-Skills
```

选择要安装的技能包。

## 开发

每个技能包都是独立的，遵循 [Agent Skills 规范](https://agentskills.io/specification)。

## 贡献

欢迎贡献！请参见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 许可证

MIT
```

---

## 📋 技能包质量检查清单

### 发布前检查

- [ ] **SKILL.md 规范**
  - [ ] YAML frontmatter 完整
  - [ ] name 字段符合规范
  - [ ] description 清晰且包含关键词
  - [ ] 行数 ≤ 500 行
  - [ ] Markdown 格式正确

- [ ] **目录结构**
  - [ ] scripts/ 目录包含可执行脚本
  - [ ] references/ 目录包含详细文档
  - [ ] templates/ 目录包含项目模板
  - [ ] tests/ 目录包含测试文件

- [ ] **代码质量**
  - [ ] 所有脚本语法正确
  - [ ] 错误处理完整
  - [ ] 文档字符串完整

- [ ] **文档完整性**
  - [ ] README.md 存在且完整
  - [ ] CHANGELOG.md 更新
  - [ ] LICENSE 文件包含

- [ ] **Git 规范**
  - [ ] 提交遵循 Conventional Commits
  - [ ] Git 标签创建
  - [ ] GitHub Release 创建

- [ ] **验证测试**
  - [ ] 官方验证脚本通过
  - [ ] 单元测试通过
  - [ ] 集成测试通过

---

## 🔗 参考资源

### 官方文档

- [Agent Skills 规范](https://agentskills.io/specification)
- [Agent Skills 官方网站](https://agentskills.io)
- [Anthropic 官方博客](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic Skills GitHub](https://github.com/anthropics/skills)

### 相关标准

- [语义化版本 (Semantic Versioning)](https://semver.org/lang/zh-CN/)
- [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)
- [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)

### 工具和资源

- [Claude Code 文档](https://code.claude.com/docs/en/skills)
- [VS Code Agent Skills 集成](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

---

## 📝 附录

### A. 完整的 SKILL.md 示例

```markdown
---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces using Design Token methodology, OKLCH color system, and 8-state component patterns. Use when building user interfaces, design systems, or when the user mentions frontend design, UI/UX, or component development.
license: MIT
metadata:
  author: maric
  version: "2.2.0"
  tags: frontend,design,ui,ux,tokens
---

# Frontend Design Agent Skills

> 创建独特、生产级前端界面的专业技能包

## 概述

此技能包提供完整的前端设计方法论，包括：
- Design Token 设计系统
- OKLCH 现代色彩空间
- 8种组件状态完整覆盖
- 多框架支持（React/Vue/Svelte/Angular）

## 使用场景

- 构建用户界面组件
- 创建设计系统
- 实现 Design Token
- 前端性能优化
- 无障碍功能实现

## 核心功能

- Design Token 验证和生成
- 组件状态完整覆盖（8种状态）
- 主题生成（light/dark）
- 无障碍检查（WCAG AA）
- 性能分析和优化

## 工具脚本

### 验证工具
- `check-tokens.py` - Design Token 验证
- `check-accessibility.py` - 无障碍检查
- `check-performance.py` - 性能分析

### 生成工具
- `generate-component.py` - 组件生成
- `generate-theme.py` - 主题生成

### 测试工具
- `test-skill.py` - 技能完整性验证

## 项目模板

提供三种完整的项目模板：
- React 模板（Vite + React 18 + TypeScript）
- Vue 模板（Vite + Vue 3.4 + TypeScript）
- Vanilla 模板（Vite + TypeScript）

## 快速开始

```bash
# 验证 Design Token
python scripts/check-tokens.py tokens/

# 生成组件
python scripts/generate-component.py Button --framework react

# 生成主题
python scripts/generate-theme.py my-theme --colors modern
```

## 相关文档

- [API 文档](docs/API.md)
- [方法论](references/methodology/)
- [框架指南](references/by-framework/)
- [质量指南](references/quality/)

## 最佳实践

1. **渐进式披露**: 使用三层架构组织内容
2. **OKLCH 优先**: 使用 OKLCH 色彩空间而非 RGB/HSL
3. **状态完整**: 覆盖所有8种组件状态
4. **无障碍**: 遵循 WCAG AA 标准
5. **性能**: 优化 Core Web Vitals

## 版本历史

参见 [CHANGELOG.md](CHANGELOG.md) 获取完整版本历史。

## 许可证

MIT License - 详见 [LICENSE](LICENSE)
```

### B. 项目结构验证脚本

```python
#!/usr/bin/env python3
"""技能包项目结构验证"""

import os
import sys
from pathlib import Path
from typing import Dict, List

# 必需文件和目录
REQUIRED_ITEMS = {
    'SKILL.md': 'file',
    'LICENSE': 'file',
    'README.md': 'file',
    'CHANGELOG.md': 'file',
}

# 可选目录
OPTIONAL_DIRS = [
    'scripts',
    'references',
    'templates',
    'assets',
    'tests',
    'docs',
]

def validate_structure(skill_path: Path) -> Dict[str, List[str]]:
    """验证项目结构"""
    results = {
        'required': [],
        'optional': [],
        'missing': [],
        'extra': [],
    }

    # 检查必需项
    for item, item_type in REQUIRED_ITEMS.items():
        path = skill_path / item
        if path.exists():
            results['required'].append(item)
        else:
            results['missing'].append(item)

    # 检查可选项
    for dir_name in OPTIONAL_DIRS:
        path = skill_path / dir_name
        if path.exists():
            results['optional'].append(dir_name)

    # 列出额外文件/目录
    for item in skill_path.iterdir():
        if item.name not in REQUIRED_ITEMS and item.name not in OPTIONAL_DIRS:
            if not item.name.startswith('.'):
                results['extra'].append(item.name)

    return results

def print_report(results: Dict[str, List[str]]) -> None:
    """打印验证报告"""
    print("=== 技能包结构验证 ===\n")

    print(f"✅ 必需项 ({len(results['required'])}/{len(REQUIRED_ITEMS)}):")
    for item in results['required']:
        print(f"   - {item}")

    if results['missing']:
        print(f"\n❌ 缺失项 ({len(results['missing'])}):")
        for item in results['missing']:
            print(f"   - {item}")

    if results['optional']:
        print(f"\n📁 可选项 ({len(results['optional'])}):")
        for item in results['optional']:
            print(f"   - {item}/")

    if results['extra']:
        print(f"\n📦 额外项 ({len(results['extra'])}):")
        for item in results['extra']:
            item_type = "DIR" if (Path.cwd() / item).is_dir() else "FILE"
            print(f"   - {item} ({item_type})")

if __name__ == '__main__':
    skill_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    results = validate_structure(skill_path)
    print_report(results)

    # 如果缺失必需项，返回错误
    sys.exit(1 if results['missing'] else 0)
```

---

> **最后更新**: 2025-01-04
> **维护者**: Frontend Design Agent Skills 项目团队
> **规范版本**: Agent Skills v1.0 (2025-12-18)
