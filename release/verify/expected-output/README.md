# Frontend Design Templates - Expected Output

> 📊 测试基准配置和预期输出

---

## 📋 说明

本目录包含 Frontend Design Templates 的测试基准配置，用于验证模板的正确性和一致性。

---

## 📁 文件说明

### template-test-baseline.json

测试基准配置文件，包含：

- **模板定义**: 每个模板的详细配置
- **必需文件列表**: 验证文件完整性
- **预期脚本**: 验证 package.json 配置
- **验证规则**: 自动化测试规则

---

## 🚀 使用方法

### 加载基准配置

```python
import json

with open('tests/expected-output/template-test-baseline.json', 'r') as f:
    baseline = json.load(f)

# 访问模板配置
react_config = baseline['templates']['react']
```

### 验证模板

```python
def verify_template(template_name, template_dir):
    baseline = load_baseline()
    config = baseline['templates'][template_name]

    # 验证文件
    for file in config['file_list']:
        assert (template_dir / file).exists()

    # 验证配置
    # ...
```

---

## 📊 基准配置结构

```json
{
  "templates": {
    "<template-name>": {
      "name": "模板名称",
      "framework": "框架名称",
      "version": "框架版本",
      "build_tool": "构建工具",
      "language": "编程语言",
      "required_files": 文件数量,
      "file_list": ["文件列表"],
      "expected_scripts": {"脚本": "命令"},
      "expected_dependencies": {"依赖": "版本"}
    }
  },
  "validation_rules": {
    "package_json": {...},
    "tsconfig_json": {...},
    "vite_config": {...},
    "readme": {...}
  }
}
```

---

## 🔄 更新基准

当模板配置变更时，需要更新基准文件：

1. 更新 `template-test-baseline.json`
2. 运行测试验证
3. 提交变更

---

## 📚 相关资源

- [测试用例](../../../../tests/test-cases/)
- [Frontend Design Agent Skills](https://github.com/your-org/frontend-design)

---

## 📄 许可证

MIT License

---

> **维护者**: Frontend Design Agent Skills 项目团队
> **更新日期**: 2025-01-04
