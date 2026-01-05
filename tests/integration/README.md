# 集成测试

> 📋 **测试范围**: 模块间交互和端到端流程测试

## 测试文件

### 工具集成测试
- `test_validate_workflow.py` - 验证工具集成测试
- `test_generate_workflow.py` - 生成工具集成测试

### 跨模块测试
- `test_token_to_theme.py` - Token到主题生成流程
- `test_component_validation.py` - 组件验证流程

## 运行测试

```bash
# 运行所有集成测试
python -m pytest tests/integration/

# 运行特定测试文件
python -m pytest tests/integration/test_validate_workflow.py
```

## 测试状态

| 测试文件 | 状态 | 描述 |
|----------|------|------|
| test_validate_workflow.py | ⏳ 待创建 | 验证工具集成测试 |
| test_generate_workflow.py | ⏳ 待创建 | 生成工具集成测试 |
| test_token_to_theme.py | ⏳ 待创建 | Token到主题生成 |
| test_component_validation.py | ⏳ 待创建 | 组件验证流程 |

---

> **最后更新**: 2026-01-05
