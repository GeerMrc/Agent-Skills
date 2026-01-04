# Frontend Design Agent Skills - 发布工具

> 📦 **自动化发布和验证工具**

---

## 📋 目录结构

```
release/
├── package/              # 打包工具
│   ├── package-skill.py         # 自动打包脚本
│   ├── package-config.json      # 打包配置
│   └── requirements.txt         # 依赖
├── verify/               # 验证工具
│   ├── verify-before-release.py # 发布前验证
│   ├── verify-after-install.py  # 安装后验证
│   ├── test-cases/              # 测试用例
│   ├── expected-output/         # 预期输出
│   └── README.md                # 测试说明
└── output/               # 发布包输出
    └── .gitkeep
```

---

## 🚀 快速开始

### 1. 打包技能包

```bash
cd release/package
python package-skill.py
```

输出：
- `../output/frontend-design-{version}.tar.gz`
- `../output/frontend-design-{version}.zip`

### 2. 发布前验证

```bash
cd ../verify
python verify-before-release.py
```

验证内容：
- SKILL.md 存在且格式正确
- 必需文件存在
- 目录结构符合规范
- 不包含 docs/ 和 tests/

### 3. 安装后验证

用户安装技能包后，运行：

```bash
cd frontend-design
python ../release/verify/verify-after-install.py
```

---

## 📦 发布流程

### 完整流程

```bash
# 1. 打包
cd release/package
python package-skill.py

# 2. 验证
cd ../verify
python verify-before-release.py

# 3. 创建 GitHub Release
# (使用 GitHub MCP 或 Web UI)

# 4. 用户安装后验证
python verify-after-install.py
```

---

## 🔧 配置

### 打包配置

编辑 `package/package-config.json`:

```json
{
  "skill_name": "frontend-design",
  "skill_version": "2.2.0",
  "output_directory": "../output/",

  "exclude_patterns": [
    ".git",
    "docs/",
    "tests/"
  ],

  "required_files": [
    "SKILL.md"
  ]
}
```

---

## 📖 相关文档

- [Agent Skills发布规范](../docs/AGENT_SKILLS_RELEASE_SPEC.md)
- [开发流程规范](../docs/DEVELOPMENT_WORKFLOW.md)

---

> **最后更新**: 2026-01-04
> **维护者**: Frontend Design Agent Skills 项目团队
