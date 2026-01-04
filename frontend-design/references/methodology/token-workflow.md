# 令牌工作流

> ⚙️ **从设计到代码** - Token开发完整流程

---

## 📖 核心概念

Design Token工作流定义了从设计到代码的完整流程，确保设计决策能够准确、高效地转化为可维护的代码。

**核心目标**：
- 同步设计工具和代码中的Token
- 自动化Token导出和转换
- 确保Token版本一致性
- 支持多平台（Web、iOS、Android）

---

## 🔄 工作流程

### 阶段1：设计定义

**在设计工具中创建Token**（Figma、Sketch等）

1. **创建Token变量**
   - 在设计工具中定义颜色、间距、字体等
   - 使用语义化命名
   - 组织Token层级结构

2. **应用Token到设计**
   - 将设计值替换为Token引用
   - 确保所有设计元素使用Token
   - 创建Token样式指南

### 阶段2：Token提取

**从设计工具导出Token**

1. **使用设计工具插件**
   - Figma Tokens插件
   - Style Dictionary
   - Diez

2. **导出格式**
   ```json
   {
     "color": {
       "primary": {
         "value": "#3B82F6",
         "type": "color"
       }
     },
     "spacing": {
       "medium": {
         "value": "16px",
         "type": "dimension"
       }
     }
   }
   ```

### 阶段3：Token转换

**转换为代码格式**

**输出目标**：
- CSS自定义属性（CSS Variables）
- Sass/SCSS变量
- JavaScript/TypeScript对象
- JSON配置文件

### 阶段4：代码集成

**在代码中使用Token**

1. **导入Token文件**
2. **应用Token到组件**
3. **测试Token一致性**
4. **提交版本控制**

### 阶段5：维护和更新

**持续维护Token**

1. **设计变更** → 更新设计工具中的Token
2. **重新导出** → 生成新的Token文件
3. **代码更新** → 同步到代码库
4. **测试验证** → 确保变更正确
5. **版本发布** → 发布新版本

---

## 🛠️ 工具和自动化

### Style Dictionary

**功能**：将设计Token转换为多种格式

**配置示例**：
```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{
        "destination": "variables.css",
        "format": "css/variables"
      }]
    },
    "js": {
      "transformGroup": "js",
      "buildPath": "build/js/",
      "files": [{
        "destination": "tokens.js",
        "format": "javascript/es6"
      }]
    }
  }
}
```

### Figma Tokens插件

**功能**：在Figma中管理和导出Token

**特性**：
- 创建和组织Token
- 导出多种格式
- 同步到代码仓库

### 自定义脚本

**Token验证脚本**：
```python
# scripts/validate/check-tokens.py
import json

def validate_tokens(tokens):
    """验证Token的完整性和格式"""
    required_categories = ['color', 'spacing', 'typography']
    for category in required_categories:
        if category not in tokens:
            raise ValueError(f"Missing category: {category}")
    return True

# 使用
with open('tokens.json') as f:
    tokens = json.load(f)
validate_tokens(tokens)
```

---

## 📋 最佳实践

### 1. 版本控制

**Token文件应该纳入版本控制**：
- Git追踪所有Token变更
- 使用语义化版本
- 记录变更日志

### 2. 自动化

**建立CI/CD流程**：
```yaml
# .github/workflows/tokens.yml
name: Token Sync
on: [push]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Export Tokens
        run: npm run export-tokens
      - name: Validate Tokens
        run: npm run validate-tokens
```

### 3. 文档化

**保持Token文档同步**：
- 记录Token用途
- 提供使用示例
- 标记废弃Token

### 4. 测试

**测试Token一致性**：
```javascript
// tests/tokens.test.js
describe('Design Tokens', () => {
  it('should have all required categories', () => {
    expect(tokens).toHaveProperty('color');
    expect(tokens).toHaveProperty('spacing');
  });

  it('should use valid color values', () => {
    expect(tokens.color.primary).toMatch(/^#[0-9A-F]{6}$/i);
  });
});
```

---

## 🔄 工作流示例

### 完整流程示例

**场景**：更新主色调

1. **设计更新**
   - 在Figma中更新`color-primary` Token值
   - 应用到所有使用该Token的组件

2. **导出Token**
   ```bash
   npm run export-tokens
   ```

3. **验证变更**
   ```bash
   npm run validate-tokens
   ```

4. **测试**
   ```bash
   npm test
   ```

5. **提交**
   ```bash
   git add tokens/
   git commit -m "feat(tokens): update primary color"
   ```

---

## 📚 相关文档

- [Design Token方法论](./design-tokens.md) - Token基础概念
- [系统化方法](./systematic-approach.md) - 设计系统构建
- [组件状态覆盖](../implementation/component-states.md) - 组件状态管理

---

## 🔗 快速导航

- [返回methodology/](./README.md)
- [返回references/](../README.md)
- [返回SKILL.md](../../SKILL.md)

---

> **状态**: ⏳ IN_PROGRESS (框架已完成，待完善详细内容)
> **最后更新**: 2025-01-03
> **维护者**: 项目团队
