# 单元测试

> 📋 **测试范围**: Python 工具脚本的单元测试

## 测试文件

### validate 测试
- `test_check_tokens.py` - Token验证工具测试
- `test_check_accessibility.py` - 无障碍检查工具测试
- `test_check_performance.py` - 性能检查工具测试

### generate 测试
- `test_generate_component.py` - 组件生成器测试
- `test_generate_theme.py` - 主题生成器测试

### utils 测试
- `test_color.py` - 颜色工具测试
- `test_token.py` - Token工具测试
- `test_reporter.py` - 报告工具测试

## 运行测试

```bash
# 运行所有单元测试
python -m pytest tests/unit/

# 运行特定测试文件
python -m pytest tests/unit/test_check_tokens.py

# 查看测试覆盖率
python -m pytest tests/unit/ --cov=scripts --cov-report=html
```

## 测试状态

| 测试文件 | 状态 | 覆盖率 |
|----------|------|--------|
| test_check_tokens.py | ⏳ 待创建 | - |
| test_check_accessibility.py | ⏳ 待创建 | - |
| test_check_performance.py | ⏳ 待创建 | - |
| test_generate_component.py | ⏳ 待创建 | - |
| test_generate_theme.py | ⏳ 待创建 | - |
| test_color.py | ⏳ 待创建 | - |
| test_token.py | ⏳ 待创建 | - |
| test_reporter.py | ⏳ 待创建 | - |

---

> **最后更新**: 2026-01-05
