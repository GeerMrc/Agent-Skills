# Agent-Skills

> 🤖 **AI Agent 技能包集合** - 遵循官方 [Agent Skills 开放标准](https://agentskills.io/specification)

---

## 📋 仓库概述

**Agent-Skills** 是一个 AI Agent 技能包的集合仓库，每个技能包都是一个符合 [Agent Skills 规范](https://agentskills.io/specification) 的独立模块，可以为 AI Agent（如 Claude Code）提供专业化的领域能力。

### Agent Skills 开放标准

- **发布日期**: 2025-12-18
- **规范来源**: [agentskills.io](https://agentskills.io)
- **核心理念**: 通过可发现文件夹的指令、脚本和资源，为 AI Agent 提供可组合、可扩展的能力

---

## 🎯 技能包列表

| 技能包 | 版本 | 描述 | 状态 |
|--------|------|------|------|
| [Frontend Design](#frontend-design) | v0.1.1.1 | 创建独特、生产级前端界面的专业技能 | ✅ 已发布 |

---

## 🚀 快速开始

### 在 Claude Code 中安装

```bash
# 添加市场插件
/plugin marketplace add GeerMrc/Agent-Skills

# 选择并安装技能包
# 浏览并安装: frontend-design
```

### 本地使用

```bash
# 克隆仓库
git clone https://github.com/GeerMrc/Agent-Skills.git
cd Agent-Skills

# 验证技能包
python release/verify/test/test-skill.py

# 验证安装（发布包）
cd frontend-design
python ../release/verify/verify-after-install.py
```

### 从发布包安装

```bash
# 1. 从 GitHub Release 下载发布包
# 2. 解压到目标位置
unzip frontend-design-0.1.1.1.zip

# 3. 验证安装
cd frontend-design
python ../release/verify/verify-after-install.py
```

---

## 📦 技能包详情

### Frontend Design

创建独特、生产级前端界面的专业技能包。

**核心功能**:
- Design Token 设计方法论
- OKLCH 现代色彩系统
- 8种组件状态完整覆盖
- 多框架支持（React/Vue/Svelte/Angular）
- 完整的工具脚本和项目模板

**技术栈**:
- Python 3.8+ 工具脚本
- TypeScript 5.x 类型定义
- Vite 5.x 构建工具

**项目结构**:
```
frontend-design/
├── SKILL.md              # 技能入口（193行）
├── LICENSE               # 许可证
├── README.md             # 技能说明
├── CHANGELOG.md          # 变更日志
├── scripts/              # 10个Python工具脚本
│   ├── validate/         # Token/无障碍/性能验证
│   ├── generate/         # 组件/主题生成
│   └── utils/            # 共享模块
├── references/           # 详细文档
│   ├── methodology/      # 设计方法论
│   ├── by-framework/     # 框架指南
│   └── quality/          # 质量指南
└── templates/            # 项目模板
    ├── react/            # Vite + React 18 + TS
    ├── vue/              # Vite + Vue 3.4 + TS
    └── vanilla/          # Vite + TypeScript
```

**快速使用**:
```bash
# 验证 Design Token
python frontend-design/scripts/validate/check-tokens.py tokens/

# 生成组件
python frontend-design/scripts/generate/generate-component.py Button --framework react

# 生成主题
python frontend-design/scripts/generate/generate-theme.py my-theme --colors modern

# 技能完整性测试
python release/verify/test/test-skill.py
```

**详细信息**: 查看 [Frontend Design README](frontend-design/README.md)

---

## 📚 Agent Skills 规范

### 技能包目录结构

```
skill-name/
├── SKILL.md              # 必需 - 技能入口文件
├── LICENSE               # 可选 - 许可证
├── README.md             # 可选 - 技能说明
├── scripts/              # 可选 - 可执行代码
├── references/           # 可选 - 详细文档
├── templates/            # 可选 - 项目模板
├── assets/               # 可选 - 静态资源
└── tests/                # 可选 - 测试文件
```

### SKILL.md 格式

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

**字段规范**:
| 字段 | 必需 | 约束 |
|------|------|------|
| `name` | ✅ | 最多64字符，小写字母、数字和连字符 |
| `description` | ✅ | 最多1024字符，描述功能和使用场景 |
| `license` | ❌ | 许可证名称或文件引用 |
| `compatibility` | ❌ | 环境要求（最多500字符） |
| `metadata` | ❌ | 额外元数据的键值映射 |

### 渐进式披露原则

技能包应遵循三层披露架构：

1. **元数据层** (~100 tokens): `name` + `description` 在启动时加载
2. **指令层** (< 5000 tokens): 完整 `SKILL.md` 在激活时加载
3. **资源层** (按需): `scripts/`、`references/`、`assets/` 按需加载

---

## 🤝 贡献指南

欢迎贡献新的技能包或改进现有技能包！

### 添加新技能包

1. Fork 本仓库
2. 创建技能包目录：`your-skill-name/`
3. 创建 `SKILL.md` 文件（符合规范）
4. 添加必要的 `scripts/`、`references/` 等
5. 提交 Pull Request

### 技能包要求

- ✅ SKILL.md 符合 [官方规范](https://agentskills.io/specification)
- ✅ YAML frontmatter 完整（name + description 必需）
- ✅ 遵循渐进式披露原则
- ✅ 包含 README.md 说明文档
- ✅ 包含 LICENSE 文件

详细规范请参考: [docs/AGENT_SKILLS_RELEASE_SPEC.md](docs/AGENT_SKILLS_RELEASE_SPEC.md)

---

## 📖 相关资源

### 官方文档
- [Agent Skills 规范](https://agentskills.io/specification)
- [Agent Skills 官方网站](https://agentskills.io)
- [Anthropic 官方博客](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic Skills GitHub](https://github.com/anthropics/skills)

### 相关标准
- [语义化版本 (Semantic Versioning)](https://semver.org/lang/zh-CN/)
- [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)
- [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 🔄 版本历史

### v0.1.1 (2026-01-04)
- ✅ 首个稳定版发布
- ✅ 包含 Frontend Design 技能包 v0.1.1

---

> **Maintained by**: GeerMrc
> **Based on**: [Agent Skills Open Standard](https://agentskills.io/specification)
