# Agent-Skills

> 🤖 **AI Agent 技能包集合** - 遵循官方 [Agent Skills 开放标准](https://agentskills.io/specification)

---

## 📋 仓库概述

**Agent-Skills** 是一个 AI Agent 技能包的集合仓库，每个技能包都是一个符合 [Agent Skills 规范](https://agentskills.io/specification) 的独立模块。

### Agent Skills 开放标准

- **发布日期**: 2025-12-18
- **规范来源**: [agentskills.io](https://agentskills.io)
- **核心理念**: 通过可发现文件夹的指令、脚本和资源，为 AI Agent 提供可组合、可扩展的能力

---

## 🎯 技能包列表

| 技能包 | 版本 | 描述 | 状态 |
|--------|------|------|------|
| [Frontend Design](frontend-design/) | v0.1.1.1 | 创建独特、生产级前端界面的专业技能 | ✅ 已发布 |

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
```

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

### 本仓库项目结构

```
Agent-Skills/                    # GitHub 仓库根目录
├── README.md                    # 仓库总览
├── CHANGELOG.md                 # 变更日志
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # 许可证
├── docs/                        # 开发文档目录（仅在仓库中）
│   ├── README.md                # 文档导航索引
│   ├── DEVELOPMENT_WORKFLOW.md  # 开发流程规范
│   ├── API.md                   # API文档
│   ├── TASK.md                  # 任务追踪
│   └── [其他开发文档...]
├── tests/                       # 测试代码目录（仅在仓库中）
│   ├── unit/                    # 单元测试
│   ├── integration/             # 集成测试
│   ├── e2e/                     # E2E测试
│   └── test-cases/              # 测试用例
├── release/                     # 发布管理（仅在仓库中）
│   ├── package/                 # 打包工具
│   ├── verify/                  # 验证工具
│   └── output/                  # 发布包输出
└── frontend-design/             # 技能包目录（纯净的运行时）
    ├── SKILL.md                 # 必需 - 技能入口文件
    ├── LICENSE                  # 可选 - 许可证
    ├── README.md                # 可选 - 技能说明
    ├── CHANGELOG.md             # 可选 - 变更日志
    ├── scripts/                 # 技能运行脚本
    │   ├── validate/            # 验证工具
    │   ├── generate/            # 生成工具
    │   └── utils/               # 共享模块
    ├── references/              # 详细文档
    │   ├── methodology/         # 设计方法论
    │   ├── by-framework/        # 框架指南
    │   └── quality/             # 质量指南
    └── templates/               # 项目模板
        ├── react/               # React模板
        ├── vue/                 # Vue模板
        └── vanilla/             # Vanilla模板
```

---

## 🤝 贡献指南

欢迎贡献新的技能包或改进现有技能包！

详细规范请参考: [docs/AGENT_SKILLS_RELEASE_SPEC.md](docs/AGENT_SKILLS_RELEASE_SPEC.md)

---

## 📖 相关资源

- [Agent Skills 规范](https://agentskills.io/specification)
- [Agent Skills 官方网站](https://agentskills.io)
- [Anthropic 官方博客](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

> **Maintained by**: GeerMrc
> **Based on**: [Agent Skills Open Standard](https://agentskills.io/specification)
