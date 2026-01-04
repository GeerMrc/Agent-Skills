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
| [Frontend Design](frontend-design/) | v2.2.0 | 创建独特、生产级前端界面的专业技能 | ✅ 已发布 |

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
python frontend-design/scripts/test/test-skill.py
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
