# E2E 测试

> 📋 **测试范围**: 完整的用户场景和发布流程测试

## 测试文件

### 发布流程测试
- `test_release_package.py` - 完整发布打包流程
- `test_release_verify.py` - 发布验证流程

### 用户场景测试
- `test_skill_installation.py` - 技能安装测试
- `test_skill_usage.py` - 技能使用测试

## 运行测试

```bash
# 运行所有E2E测试
python -m pytest tests/e2e/

# 运行特定测试文件
python -m pytest tests/e2e/test_release_package.py
```

## 测试状态

| 测试文件 | 状态 | 描述 |
|----------|------|------|
| test_release_package.py | ⏳ 待创建 | 发布打包流程 |
| test_release_verify.py | ⏳ 待创建 | 发布验证流程 |
| test_skill_installation.py | ⏳ 待创建 | 技能安装测试 |
| test_skill_usage.py | ⏳ 待创建 | 技能使用测试 |

---

> **最后更新**: 2026-01-05
