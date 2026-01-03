# Frontend Design Templates - 测试用例

> 🧪 模板完整性验证测试套件

---

## 📋 测试说明

本目录包含 Frontend Design Templates 的完整测试用例，用于验证所有项目模板的配置正确性和功能完整性。

---

## 🚀 快速开始

### 运行所有测试

```bash
python tests/test-cases/test-templates.py
```

### 运行单个模板测试

```bash
# React 模板测试
python tests/test-cases/test-templates.py --template react

# Vue 模板测试
python tests/test-cases/test-templates.py --template vue

# Vanilla 模板测试
python tests/test-cases/test-templates.py --template vanilla
```

### 显示详细输出

```bash
python tests/test-cases/test-templates.py --verbose
```

---

## 📁 测试覆盖

### 文件完整性测试

验证每个模板是否包含所有必需的文件：

- **React**: 13 个必需文件
- **Vue**: 11 个必需文件
- **Vanilla**: 8 个必需文件

### 配置正确性测试

验证配置文件的正确性：

- `package.json` - 依赖和脚本配置
- `tsconfig.json` - TypeScript 编译配置
- `vite.config.ts` - Vite 构建配置
- `README.md` - 文档完整性

---

## 📊 测试结果

### 成功标准

- ✅ 所有必需文件存在
- ✅ 所有配置文件格式正确
- ✅ 必需的脚本命令已配置
- ✅ README 文档包含必需章节

### 失败处理

如果测试失败，请检查：

1. 文件是否存在于正确位置
2. JSON 配置文件格式是否正确
3. 必需的脚本命令是否已配置
4. README 文档是否完整

---

## 🔧 测试维护

### 添加新测试

在 `test-templates.py` 中添加新的测试方法：

```python
def test_new_feature(self, template_dir: Path) -> bool:
    """测试新功能"""
    # 实现测试逻辑
    return True
```

### 更新测试标准

修改 `get_template_files` 方法来更新必需文件列表。

---

## 📚 相关资源

- [Frontend Design Agent Skills](https://github.com/your-org/frontend-design)
- [测试目录](../)

---

## 📄 许可证

MIT License

---

> **维护者**: Frontend Design Agent Skills 项目团队
> **更新日期**: 2025-01-04
