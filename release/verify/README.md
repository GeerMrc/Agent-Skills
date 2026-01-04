# Frontend Design Templates - 测试套件

> 🧪 模板完整性验证和测试基准

---

## 📋 测试说明

本目录包含 Frontend Design Templates 的测试基准和发布验证工具。

**注意**: 测试用例代码已移动到项目根目录的 `tests/test-cases/` 目录。

---

## 📁 目录结构

**项目根目录结构**:
```
project-root/
├── tests/                   # 测试代码目录（与docs/、release/同级）
│   └── test-cases/          # 测试用例
│       ├── test-templates.py   # 模板测试脚本
│       └── README.md           # 测试用例文档
└── release/                 # 发布工具目录
    └── verify/
        ├── test/                    # 技能测试工具
        │   └── test-skill.py       # 技能完整性测试
        ├── expected-output/        # 测试基准
        │   ├── template-test-baseline.json  # 基准配置
        │   └── README.md           # 基准文档
        ├── verify-before-release.py  # 发布前验证
        └── verify-after-install.py   # 安装后验证
```

---

## 🚀 快速开始

### 运行模板测试

```bash
# 从项目根目录运行
python tests/test-cases/test-templates.py
```

### 运行单个模板测试

```bash
# React 模板
python tests/test-cases/test-templates.py --template react

# Vue 模板
python tests/test-cases/test-templates.py --template vue

# Vanilla 模板
python tests/test-cases/test-templates.py --template vanilla
```

### 显示详细输出

```bash
python tests/test-cases/test-templates.py --verbose
```

---

## 📊 测试覆盖

### 文件完整性测试

验证每个模板是否包含所有必需的文件：

| 模板 | 必需文件数 |
|------|-----------|
| React | 13 |
| Vue | 11 |
| Vanilla | 8 |

### 配置正确性测试

- `package.json` - 依赖和脚本配置
- `tsconfig.json` - TypeScript 编译配置
- `vite.config.ts` - Vite 构建配置
- `README.md` - 文档完整性

---

## 📈 测试结果

### 成功标准

- ✅ 所有必需文件存在
- ✅ 所有配置文件格式正确
- ✅ 必需的脚本命令已配置
- ✅ README 文档包含必需章节

### 最新测试结果

```
总计: 3/3 模板测试通过
✅ 所有模板测试通过! 🎉
```

---

## 🔄 测试维护

### 更新测试基准

1. 修改 `expected-output/template-test-baseline.json`
2. 运行测试验证变更
3. 提交更新

### 添加新测试

在 `test-cases/test-templates.py` 中添加新的测试方法。

---

## 📚 相关资源

- [Frontend Design Agent Skills](https://github.com/your-org/frontend-design)
- [项目模板](../templates/)

---

## 📄 许可证

MIT License

---

> **维护者**: Frontend Design Agent Skills 项目团队
> **更新日期**: 2025-01-04
