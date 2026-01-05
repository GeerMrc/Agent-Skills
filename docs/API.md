# Frontend Design Agent Skills - API 文档

> 📖 **文档版本**: v2.2.0（内部开发版本号）
> 📌 **项目版本**: Frontend Design Agent Skills v0.1.1.1 稳定版
> 📅 **更新日期**: 2025-01-04
> 📅 **最后更新**: 2026-01-05
> 👤 **维护者**: 项目团队

> **版本说明**: 本文档使用 v2.2.0 作为内部开发版本号（历史遗留），当前项目稳定版本为 v0.1.1.1

---

## 📑 目录

- [概述](#概述)
- [工具脚本 API](#工具脚本-api)
  - [验证工具](#验证工具)
  - [生成工具](#生成工具)
  - [测试工具](#测试工具)
- [共享模块 API](#共享模块-api)
- [项目模板 API](#项目模板-api)
- [使用示例](#使用示例)

---

## 概述

Frontend Design Agent Skills 提供了一套完整的工具脚本和项目模板，用于快速创建符合 Design Token 规范的前端项目。

### 技术栈

- **Python**: 3.8+ (工具脚本)
- **Node.js**: 18+ (项目模板)
- **框架支持**: React, Vue, Svelte, Angular, Vanilla TypeScript
- **色彩系统**: OKLCH
- **构建工具**: Vite 5+

---

## 工具脚本 API

所有工具脚本位于 `scripts/` 目录下，使用 Python 3.8+ 运行。

### 验证工具

#### check-tokens.py

Design Token 验证工具，检查命名规范和结构完整性。

**用法**:
```bash
python scripts/validate/check-tokens.py <token-file> [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `token_file` | Path | ✅ | Token 文件路径 (JSON 格式) |
| `--format`, `-f` | string | ❌ | 输出格式: `text` (默认), `json`, `markdown` |
| `--output`, `-o` | Path | ❌ | 输出文件路径 |
| `--strict` | flag | ❌ | 严格模式: 警告也视为错误 |

**返回值**:
- `0`: 验证通过
- `1`: 验证失败

**示例**:
```bash
# 基础验证
python scripts/validate/check-tokens.py tokens.json

# JSON 格式输出
python scripts/validate/check-tokens.py tokens.json --format json

# 生成 Markdown 报告
python scripts/validate/check-tokens.py tokens.json --format markdown --output report.md

# 严格模式
python scripts/validate/check-tokens.py tokens.json --strict
```

**验证规则**:
- Token 命名必须使用小写字母、数字和连字符
- 颜色 Token 值必须使用 OKLCH 格式: `oklch(L C H)`
- 间距 Token 建议使用 `rem` 或 `px` 单位
- 必需类别: `color`, `spacing`, `font`, `shadow`, `radius`

---

#### check-accessibility.py

无障碍检查工具，验证 WCAG AA 对比度和 ARIA 属性。

**用法**:
```bash
python scripts/validate/check-accessibility.py <file> [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `file` | Path | ✅ | HTML/组件文件路径 |
| `--format`, `-f` | string | ❌ | 输出格式: `text`, `json`, `markdown` |
| `--output`, `-o` | Path | ❌ | 输出文件路径 |
| `--level` | string | ❌ | WCAG 级别: `AA` (默认), `AAA` |

**返回值**:
- `0`: 检查通过
- `1`: 检查失败

**示例**:
```bash
# 检查 HTML 文件
python scripts/validate/check-accessibility.py index.html

# AAA 级别检查
python scripts/validate/check-accessibility.py index.html --level AAA

# 生成报告
python scripts/validate/check-accessibility.py index.html --format markdown --output a11y-report.md
```

**检查项**:
- 颜色对比度 (WCAG AA: 4.5:1, AAA: 7.0:1)
- ARIA 属性完整性
- 语义化 HTML 标签
- 键盘导航支持
- 屏幕阅读器兼容性

---

#### check-performance.py

性能检查工具，分析代码性能问题。

**用法**:
```bash
python scripts/validate/check-performance.py <file> [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `file` | Path | ✅ | 代码文件路径 |
| `--format`, `-f` | string | ❌ | 输出格式: `text`, `json`, `markdown` |
| `--output`, `-o` | Path | ❌ | 输出文件路径 |
| `--threshold` | number | ❌ | 性能阈值 (默认: 80) |

**返回值**:
- `0`: 性能良好
- `1`: 发现性能问题

**示例**:
```bash
# 检查性能
python scripts/validate/check-performance.py src/components/Button.tsx

# 自定义阈值
python scripts/validate/check-performance.py src/components/Button.tsx --threshold 90
```

**检查项**:
- Bundle 大小分析
- Rendering 性能
- Network 请求优化
- 内存泄漏检测
- 代码分割建议

---

### 生成工具

#### generate-component.py

组件生成工具，生成包含 8 种状态的完整组件代码。

**用法**:
```bash
python scripts/generate/generate-component.py <component-name> [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `component_name` | string | ✅ | 组件名称 (如 Button, Modal) |
| `--framework`, `-f` | string | ❌ | 目标框架: `react` (默认), `vue`, `svelte`, `typescript`, `javascript` |
| `--output`, `-o` | Path | ❌ | 输出目录 |
| `--file` | flag | ❌ | 输出到文件而非控制台 |

**返回值**:
- `0`: 生成成功
- `1`: 生成失败

**示例**:
```bash
# 生成 React 按钮组件
python scripts/generate/generate-component.py Button

# 生成 Vue 模态框组件
python scripts/generate/generate-component.py Modal --framework vue

# 生成并保存到文件
python scripts/generate/generate-component.py Card --framework react --output src/components/

# 生成 TypeScript 类型定义
python scripts/generate/generate-component.py Button --framework typescript
```

**支持的组件类型**:
- `button` - 按钮组件
- `input` - 输入框组件
- `card` - 卡片组件
- `modal` - 模态框组件
- `dropdown` - 下拉菜单组件
- `badge` - 徽章组件
- `tooltip` - 提示框组件
- `switch` - 开关组件

**生成的 8 种状态**:
1. **Default** - 默认状态
2. **Hover** - 悬停状态
3. **Active** - 激活状态
4. **Focus** - 焦点状态
5. **Disabled** - 禁用状态
6. **Loading** - 加载状态
7. **Empty** - 空状态
8. **Error** - 错误状态

---

#### generate-theme.py

主题生成工具，生成亮色/暗色主题配置。

**用法**:
```bash
python scripts/generate/generate-theme.py [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `--type`, `-t` | string | ❌ | 主题类型: `light` (默认), `dark`, `both` |
| `--output`, `-o` | Path | ❌ | 输出目录 (默认: 当前目录) |
| `--format`, `-f` | string | ❌ | 输出格式: `json` (默认), `css`, `scss` |

**返回值**:
- `0`: 生成成功
- `1`: 生成失败

**示例**:
```bash
# 生成亮色主题
python scripts/generate/generate-theme.py --type light

# 生成暗色主题
python scripts/generate/generate-theme.py --type dark

# 生成两种主题
python scripts/generate/generate-theme.py --type both

# 生成 SCSS 格式
python scripts/generate/generate-theme.py --type both --format scss --output src/styles/
```

**主题配置包含**:
- 颜色系统 (OKLCH 格式)
- 间距系统
- 字体系统
- 阴影系统
- 圆角系统
- 断点系统
- 动画系统

---

### 测试工具

#### test-skill.py

技能测试工具，验证 SKILL.md 完整性。

**用法**:
```bash
python release/verify/test/test-skill.py [options]
```

**参数**:
| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `--file`, `-f` | Path | ❌ | SKILL.md 文件路径 (默认: `SKILL.md`) |
| `--max-lines` | number | ❌ | 最大行数限制 (默认: 200) |
| `--verbose`, `-v` | flag | ❌ | 详细输出 |

**返回值**:
- `0`: 测试通过
- `1`: 测试失败

**示例**:
```bash
# 基础测试
python release/verify/test/test-skill.py

# 指定文件
python release/verify/test/test-skill.py --file references/SKILL.md

# 详细输出
python release/verify/test/test-skill.py --verbose
```

**验证项**:
- 文件行数检查 (≤200 行)
- Markdown 格式验证
- 必需章节检查
- 链接有效性验证

---

## 共享模块 API

共享模块位于 `scripts/utils/` 目录，提供可重用的工具类。

### ColorUtils

色彩工具类，提供 OKLCH 色彩空间处理和对比度计算。

**类方法**:

#### `parse_oklch(color_str: str) -> Optional[OKLCHColor]`

解析 OKLCH 颜色字符串。

**参数**:
- `color_str`: OKLCH 颜色字符串 (如 `"oklch(0.7 0.15 250)"`)

**返回**:
- `OKLCHColor` 对象或 `None`

**示例**:
```python
from utils.color import ColorUtils

color = ColorUtils.parse_oklch("oklch(0.7 0.15 250)")
print(color.l)  # 0.7
print(color.c)  # 0.15
print(color.h)  # 250
```

---

#### `is_valid_oklch(color_str: str) -> bool`

验证 OKLCH 格式是否正确。

**参数**:
- `color_str`: 颜色字符串

**返回**:
- `True`: 格式有效
- `False`: 格式无效

**示例**:
```python
from utils.color import ColorUtils

ColorUtils.is_valid_oklch("oklch(0.7 0.15 250)")  # True
ColorUtils.is_valid_oklch("rgb(255, 0, 0)")        # False
```

---

#### `calculate_contrast_ratio(foreground: str, background: str) -> float`

计算对比度比值。

**参数**:
- `foreground`: 前景色
- `background`: 背景色

**返回**:
- 对比度比值 (1.0 - 21.0)

**示例**:
```python
from utils.color import ColorUtils

ratio = ColorUtils.calculate_contrast_ratio(
    "oklch(0.2 0.1 250)",
    "oklch(0.98 0.01 250)"
)
print(ratio)  # ~12.5
```

---

#### `meets_wcag_aa(foreground: str, background: str, large_text: bool = False) -> bool`

检查是否满足 WCAG AA 标准。

**参数**:
- `foreground`: 前景色
- `background`: 背景色
- `large_text`: 是否大文本 (默认: `False`)

**返回**:
- `True`: 满足标准
- `False`: 不满足标准

**示例**:
```python
from utils.color import ColorUtils

ColorUtils.meets_wcag_aa(
    "oklch(0.2 0.1 250)",
    "oklch(0.98 0.01 250)"
)  # True

ColorUtils.meets_wcag_aa(
    "oklch(0.5 0.1 250)",
    "oklch(0.9 0.01 250)",
    large_text=True
)  # True
```

---

#### `meets_wcag_aaa(foreground: str, background: str, large_text: bool = False) -> bool`

检查是否满足 WCAG AAA 标准。

参数和返回值同 `meets_wcag_aa`，但阈值更高。

---

### TokenValidator

Token 验证器，提供命名规范和结构验证功能。

**类方法**:

#### `validate_naming(token_name: str) -> List[str]`

验证 Token 命名规范。

**参数**:
- `token_name`: Token 名称

**返回**:
- 问题列表 (空列表表示无问题)

**示例**:
```python
from utils.token import TokenValidator

TokenValidator.validate_naming("color-primary")  # []
TokenValidator.validate_naming("Color-Primary")  # ["Token名称必须使用小写字母..."]
```

---

#### `validate_token_structure(tokens: Dict[str, Any]) -> ValidationResult`

验证 Token 结构完整性。

**参数**:
- `tokens`: Token 字典

**返回**:
- `ValidationResult` 对象

**示例**:
```python
from utils.token import TokenValidator

tokens = {
    "color-primary": "oklch(0.7 0.15 250)",
    "spacing-sm": "0.25rem"
}

result = TokenValidator.validate_token_structure(tokens)
print(result.is_valid)     # True
print(result.total_tokens)  # 2
print(result.error_count)   # 0
```

---

#### `validate_token_file(file_path: Path) -> ValidationResult`

验证 Token 文件。

**参数**:
- `file_path`: Token 文件路径

**返回**:
- `ValidationResult` 对象

**示例**:
```python
from utils.token import TokenValidator
from pathlib import Path

result = TokenValidator.validate_token_file(Path("tokens.json"))
if result.is_valid:
    print("✅ Token 文件有效")
else:
    print(f"❌ 发现 {result.error_count} 个错误")
```

---

### Reporter

报告生成器，提供格式化的验证报告输出功能。

**类方法**:

#### `format_token_report(result: ValidationResult, output_format: str = 'text') -> str`

格式化 Token 验证报告。

**参数**:
- `result`: `ValidationResult` 对象
- `output_format`: 输出格式 (`text`, `json`, `markdown`)

**返回**:
- 格式化报告字符串

**示例**:
```python
from utils.reporter import Reporter
from utils.token import TokenValidator

tokens = {...}
result = TokenValidator.validate_token_structure(tokens)

# 文本格式
text_report = Reporter.format_token_report(result, 'text')

# Markdown 格式
md_report = Reporter.format_token_report(result, 'markdown')

# JSON 格式
json_report = Reporter.format_token_report(result, 'json')
```

---

#### `save_report(report: str, output_path: Path) -> None`

保存报告到文件。

**参数**:
- `report`: 报告内容
- `output_path`: 输出路径

**示例**:
```python
from utils.reporter import Reporter
from pathlib import Path

report = "..."

Reporter.save_report(report, Path("reports/validation.md"))
```

---

#### `print_summary(result: ValidationResult) -> None`

打印简要摘要。

**参数**:
- `result`: `ValidationResult` 对象

**示例**:
```python
from utils.reporter import Reporter
from utils.token import TokenValidator

tokens = {...}
result = TokenValidator.validate_token_structure(tokens)
Reporter.print_summary(result)

# 输出:
# 🎨 Design Token 验证 - ✅ 通过
#    总Token: 25 | 错误: 0 | 警告: 2
```

---

## 项目模板 API

项目模板位于 `templates/` 目录，提供开箱即用的项目脚手架。

### React 模板

**位置**: `templates/react/`

**技术栈**:
- React 18.2.0
- Vite 5.0.8
- TypeScript 5.2.2
- ESLint 8.55.0

**可用脚本**:
```bash
cd templates/react

# 安装依赖
npm install

# 开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 代码检查
npm run lint

# 类型检查
npm run typecheck
```

**依赖包**:
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.55.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "typescript": "^5.2.2",
    "vite": "^5.0.8"
  }
}
```

---

### Vue 模板

**位置**: `templates/vue/`

**技术栈**:
- Vue 3.4.15
- Vite 5.0.11
- TypeScript 5.3.3
- ESLint 8.56.0

**可用脚本**:
```bash
cd templates/vue

# 安装依赖
npm install

# 开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 代码检查
npm run lint
```

**依赖包**:
```json
{
  "dependencies": {
    "vue": "^3.4.15"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.3",
    "@vue/eslint-config-typescript": "^12.0.0",
    "eslint": "^8.56.0",
    "eslint-plugin-vue": "^9.19.2",
    "typescript": "^5.3.3",
    "vite": "^5.0.11",
    "vue-tsc": "^1.8.27"
  }
}
```

---

### Vanilla 模板

**位置**: `templates/vanilla/`

**技术栈**:
- 原生 JavaScript (ES6+)
- Vite 5.0.8
- TypeScript 5.2.2
- ESLint 8.55.0

**可用脚本**:
```bash
cd templates/vanilla

# 安装依赖
npm install

# 开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 代码检查
npm run lint
```

**依赖包**:
```json
{
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "eslint": "^8.55.0",
    "typescript": "^5.2.2",
    "vite": "^5.0.8"
  }
}
```

---

## 使用示例

### 完整工作流示例

#### 1. 创建新项目

```bash
# 使用 React 模板创建新项目
cp -r templates/react my-app
cd my-app
npm install
npm run dev
```

#### 2. 生成组件

```bash
# 生成按钮组件
python scripts/generate/generate-component.py Button --framework react --output src/components/
```

#### 3. 验证 Design Token

```bash
# 创建 Token 文件
cat > tokens.json << EOF
{
  "color-primary": "oklch(0.7 0.15 250)",
  "spacing-sm": "0.25rem"
}
EOF

# 验证 Token
python scripts/validate/check-tokens.py tokens.json
```

#### 4. 生成主题

```bash
# 生成亮色和暗色主题
python scripts/generate/generate-theme.py --type both --format json --output src/styles/
```

#### 5. 检查无障碍性

```bash
# 检查组件无障碍性
python scripts/validate/check-accessibility.py src/components/Button.tsx --format markdown --output reports/a11y.md
```

---

### 集成到 CI/CD

#### GitHub Actions 示例

```yaml
name: Frontend Design Checks

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Validate Design Tokens
        run: |
          python scripts/validate/check-tokens.py tokens.json --strict

      - name: Check Accessibility
        run: |
          python scripts/validate/check-accessibility.py src/**/*.tsx --format json --output reports/a11y.json

      - name: Check Performance
        run: |
          python scripts/validate/check-performance.py src/**/*.tsx --threshold 80
```

---

### 在代码中使用共享模块

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义验证脚本
"""

import sys
from pathlib import Path

# 添加共享模块路径
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

from utils.color import ColorUtils
from utils.token import TokenValidator, ValidationResult
from utils.reporter import Reporter


def custom_validator(tokens_file: Path) -> ValidationResult:
    """自定义验证逻辑"""

    # 加载并验证 Token
    result = TokenValidator.validate_token_file(tokens_file)

    # 自定义检查: 验证主色调对比度
    if 'color-primary' in result.tokens and 'color-bg' in result.tokens:
        if not ColorUtils.meets_wcag_aa(
            result.tokens['color-primary'],
            result.tokens['color-bg']
        ):
            result.errors.append({
                'level': 'error',
                'message': '主色调与背景色对比度不满足 WCAG AA 标准'
            })

    return result


if __name__ == '__main__':
    result = custom_validator(Path('tokens.json'))

    # 生成报告
    report = Reporter.format_token_report(result, 'markdown')
    Reporter.save_report(report, Path('reports/custom-validation.md'))

    # 打印摘要
    Reporter.print_summary(result)

    sys.exit(0 if result.is_valid else 1)
```

---

## 错误处理

### 常见错误及解决方案

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `FileNotFoundError` | 文件不存在 | 检查文件路径是否正确 |
| `json.JSONDecodeError` | JSON 格式错误 | 验证 JSON 格式是否正确 |
| `ValidationError` | Token 验证失败 | 检查 Token 命名和值是否符合规范 |
| `ModuleNotFoundError` | 模块未找到 | 确保在项目根目录运行，检查 Python 路径 |

### 错误码说明

| 错误码 | 含义 |
|--------|------|
| `0` | 成功 |
| `1` | 一般错误 (文件不存在、格式错误等) |
| `2` | 验证失败 (Token 不符合规范) |
| `3` | 生成失败 (组件/主题生成错误) |

---

## 版本兼容性

### Python 版本

| Python 版本 | 支持状态 |
|-------------|----------|
| 3.8 | ✅ 支持 |
| 3.9 | ✅ 支持 |
| 3.10 | ✅ 支持 |
| 3.11 | ✅ 支持 |
| 3.12 | ✅ 支持 |

### Node.js 版本

| Node.js 版本 | 支持状态 |
|--------------|----------|
| 16.x | ✅ 支持 |
| 18.x | ✅ 推荐 |
| 20.x | ✅ 支持 |

---

## 参考资源

- [项目主页](https://github.com/your-org/frontend-design)
- [开发文档](./DEVELOPMENT_WORKFLOW.md)
- [任务追踪](./TASK.md)
- [变更日志](../frontend-design/CHANGELOG.md)

---

> **最后更新**: 2025-01-04
> **维护者**: Frontend Design Agent Skills 项目团队
