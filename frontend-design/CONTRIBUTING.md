# 贡献指南

> 🤝 感谢您对 Frontend Design Agent Skills 项目的关注！
> 📅 **更新日期**: 2025-01-04

---

## 📑 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发环境搭建](#开发环境搭建)
- [代码规范](#代码规范)
- [工作流程](#工作流程)
- [Pull Request 流程](#pull-request-流程)
- [测试规范](#测试规范)
- [文档规范](#文档规范)
- [获取帮助](#获取帮助)

---

## 行为准则

### 我们的承诺

为了营造开放和友好的环境，我们承诺让每个人都能参与到项目中来，无论其经验水平、性别、性别认同和表达、性取向、残疾、个人外观、体型、种族、民族、年龄、宗教或国籍如何。

### 我们的准则

- **使用包容性语言**
- **尊重不同的观点和经验**
- **优雅地接受建设性批评**
- **专注于对社区最有利的事情**
- **对其他社区成员表示同理心

### 不可接受的行为

- 使用性别化语言或图像，以及不受欢迎的性关注或调情
- 恶意攻击、侮辱/贬损评论，以及个人或政治攻击
- 公开或私下骚扰
- 未经明确许可发布他人的私人信息
- 其他在专业场合可能被合理认为不恰当的行为

### 举报

如果您遇到不可接受的行为，请通过以下方式联系项目维护者：
- GitHub Issues: https://github.com/GeerMrc/Agent-Skills/issues
- Email: maintainers@example.com

---

## 如何贡献

### 贡献类型

我们欢迎各种形式的贡献：

- 🐛 **报告问题**: 发现 bug 或有改进建议
- 💡 **提出功能**: 新功能或增强建议
- 📝 **改进文档**: 修复错别字、改进说明、添加示例
- 🔧 **代码贡献**: 修复 bug、实现新功能、优化性能
- 🧪 **测试用例**: 添加测试覆盖、修复测试问题
- 🎨 **设计改进**: UI/UX 改进、可访问性增强
- 🌍 **国际化**: 翻译文档、添加多语言支持

### 开始贡献

1. **查看开放的问题**: [GitHub Issues](https://github.com/GeerMrc/Agent-Skills/issues)
2. **选择一个任务**: 寻找标记为 `good first issue` 或 `help wanted` 的问题
3. **领取任务**: 在问题下评论表示您正在处理
4. **开始工作**: 按照以下指南设置开发环境

---

## 开发环境搭建

### 前置要求

- **Python**: 3.8 或更高版本
- **Node.js**: 18.0 或更高版本
- **Git**: 2.0 或更高版本
- **文本编辑器**: VS Code（推荐）或您喜欢的编辑器

### 克隆仓库

```bash
# 1. Fork 项目仓库到您的 GitHub 账号
# 2. 克隆您 fork 的仓库
git clone https://github.com/YOUR_USERNAME/frontend-design.git
cd frontend-design

# 3. 添加上游远程仓库
git remote add upstream https://github.com/GeerMrc/Agent-Skills.git

# 4. 验证远程仓库
git remote -v
```

### Python 环境设置

```bash
# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 验证 Python 版本
python --version
```

### Node.js 环境设置

```bash
# 如果您要处理项目模板，需要设置 Node.js
# 验证 Node.js 版本
node --version
npm --version
```

### 安装开发工具

```bash
# 安装 pre-commit hooks（可选但推荐）
pip install pre-commit

# 安装项目依赖（如果有）
# npm install
```

### 配置开发环境

```bash
# 安装 pre-commit hooks
pre-commit install

# 验证安装
pre-commit run --all-files
```

### VS Code 推荐扩展

如果您使用 VS Code，建议安装以下扩展：

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "github.vscode-pull-request-github",
    "yzhang.markdown-all-in-one"
  ]
}
```

---

## 代码规范

### Python 代码规范

我们遵循 [PEP 8](https://peps.python.org/) 风格指南：

```python
# ✅ 正确示例
def validate_token(token_name: str, token_value: str) -> ValidationResult:
    """验证 Design Token 的命名和值。

    Args:
        token_name: Token 名称
        token_value: Token 值

    Returns:
        验证结果对象
    """
    if not token_name:
        return ValidationResult(is_valid=False, errors=["Token 名称不能为空"])

    # ... 验证逻辑
    return ValidationResult(is_valid=True)


# ❌ 错误示例
def validateToken(name,value):
    # 缺少类型注解
    # 缺少文档字符串
    # 参数命名不规范
    pass
```

**关键要求**:
- 使用类型注解（Type Hints）
- 函数必须包含文档字符串（Docstrings）
- 使用小写字母和下划线命名函数和变量
- 类名使用 PascalCase
- 常量使用大写字母和下划线

### TypeScript/JavaScript 代码规范

我们遵循 [Airbnb Style Guide](https://github.com/airbnb/javascript)：

```typescript
// ✅ 正确示例
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
}

export function Button({ variant = 'primary', size = 'md', disabled = false, onClick }: ButtonProps) {
  const handleClick = useCallback(() => {
    if (!disabled && onClick) {
      onClick();
    }
  }, [disabled, onClick]);

  return <button className={`btn btn-${variant} btn-${size}`} onClick={handleClick} disabled={disabled} />;
}
```

**关键要求**:
- 使用 TypeScript 类型注解
- 使用函数式组件和 Hooks（React）
- 组件名使用 PascalCase
- 文件名使用 kebab-case 或 PascalCase

### Git 提交规范

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
type(scope): subject

body

footer
```

**类型（type）**:
- `feat`: 新功能
- `fix`: 问题修复
- `docs`: 文档更新
- `style`: 代码格式调整（不影响功能）
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建工具或辅助工具的变动

**示例**:
```bash
# ✅ 正确示例
git commit -m "feat(tokens): add OKLCH color validation"
git commit -m "fix(accessibility): resolve contrast ratio calculation bug"
git commit -m "docs(api): update ComponentGenerator documentation"

# ❌ 错误示例
git commit -m "update stuff"
git commit -m "fixed bug"
git commit -m "add new feature"
```

### 文档规范

- **Markdown 格式**: 使用标准 Markdown 语法
- **中文文档**: 优先使用中文编写文档
- **代码示例**: 所有公开 API 必须包含使用示例
- **文档位置**:
  - API 文档: `docs/API.md`
  - 开发规范: `docs/DEVELOPMENT_WORKFLOW.md`
  - 任务追踪: `TASK.md`

---

## 工作流程

### 分支策略

我们使用 [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) 分支模型：

```
main (生产环境)
  ├── develop (开发集成)
  │     ├── feature/* (功能分支)
  │     ├── fix/* (修复分支)
  │     └── hotfix/* (紧急修复)
  └── release/* (发布准备)
```

### 分支命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 功能分支 | `feature/<name>` | `feature/design-token-system` |
| 修复分支 | `fix/<issue>-<desc>` | `fix-123-token-validation` |
| 紧急修复 | `hotfix/<version>-<desc>` | `hotfix-2.0.1-critical-bug` |
| 发布分支 | `release/<version>` | `release/2.0.0` |

### 开发流程

```bash
# 1. 保持 main 分支最新
git checkout main
git pull upstream main

# 2. 创建功能分支
git checkout -b feature/your-feature-name

# 3. 进行开发
# ... 编写代码 ...
# ... 添加测试 ...
# ... 更新文档 ...

# 4. 提交代码
git add .
git commit -m "feat(scope): description"

# 5. 推送到您的 fork
git push origin feature/your-feature-name

# 6. 创建 Pull Request
# 在 GitHub 上创建 PR
```

### 同步上游更新

```bash
# 在您的功能分支上
git fetch upstream
git rebase upstream/main

# 如果有冲突，解决冲突后
git add .
git rebase --continue

# 强制推送（谨慎使用）
git push origin feature/your-feature-name --force-with-lease
```

---

## Pull Request 流程

### PR 标题格式

使用 Conventional Commits 格式：

```
type(scope): subject
```

例如:
- `feat(tokens): add OKLCH color validation`
- `fix(accessibility): resolve contrast ratio calculation bug`
- `docs(readme): update installation instructions`

### PR 描述模板

创建 PR 时，请使用以下模板：

```markdown
## 变更类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 破坏性变更
- [ ] 文档更新

## 变更描述
<!-- 简要描述您的变更 -->

## 相关 Issue
<!-- 关联的 Issue 号，例如: Fixes #123 -->

## 变更内容
- [ ] 代码已实现
- [ ] 测试已添加/更新
- [ ] 文档已更新

## 测试
<!-- 描述您如何测试这些变更 -->

## 截图（如适用）
<!-- 添加截图或 GIF 演示 -->

## 检查清单
- [ ] 代码符合项目规范
- [ ] 已通过所有测试
- [ ] 已更新相关文档
- [ ] 无新的警告
- [ ] 已添加测试用例

## 补充说明
<!-- 任何其他信息 -->
```

### PR 审查流程

1. **自动检查**: CI/CD 管道运行测试和代码检查
2. **代码审查**: 至少一名维护者审查您的代码
3. **反馈处理**: 根据反馈进行修改
4. **合并批准**: 审查通过后，维护者将合并您的 PR

### 审查标准

**功能性**:
- [ ] 功能实现正确
- [ ] 边界条件处理
- [ ] 错误处理完善

**代码质量**:
- [ ] 代码可读性
- [ ] 命名规范
- [ ] 注释完整

**测试覆盖**:
- [ ] 单元测试已添加
- [ ] 测试覆盖率 > 80%
- [ ] 边界情况已测试

**文档**:
- [ ] API 文档已更新
- [ ] 使用示例已添加
- [ ] CHANGELOG 已更新（如需要）

---

## 测试规范

### Python 测试

使用 `pytest` 框架：

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_color_utils.py

# 显示详细输出
pytest -v

# 生成覆盖率报告
pytest --cov=scripts --cov-report=html
```

**测试示例**:

```python
# tests/test_color_utils.py
import pytest
from scripts.utils.color import ColorUtils

class TestColorUtils:
    """测试 ColorUtils 类"""

    def test_parse_oklch_valid(self):
        """测试解析有效的 OKLCH 颜色"""
        color = ColorUtils.parse_oklch("oklch(0.7 0.15 250)")
        assert color is not None
        assert color.l == 0.7
        assert color.c == 0.15
        assert color.h == 250

    def test_parse_oklch_invalid(self):
        """测试解析无效的 OKLCH 颜色"""
        color = ColorUtils.parse_oklch("rgb(255, 0, 0)")
        assert color is None

    def test_meets_wcag_aa(self):
        """测试 WCAG AA 标准"""
        result = ColorUtils.meets_wcag_aa(
            "oklch(0.2 0.1 250)",
            "oklch(0.98 0.01 250)"
        )
        assert result is True
```

### JavaScript/TypeScript 测试

使用 `vitest` 框架：

```bash
# 运行所有测试
npm test

# 运行特定测试文件
npm test Button.test.tsx

# 监听模式
npm test -- --watch

# 生成覆盖率报告
npm test -- --coverage
```

**测试示例**:

```typescript
// Button.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders with default props', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button')).toHaveTextContent('Click me');
  });

  it('applies variant class', () => {
    render(<Button variant="primary">Click</Button>);
    expect(screen.getByRole('button')).toHaveClass('btn-primary');
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

### 测试覆盖率要求

- **单元测试覆盖率**: > 80%
- **公共 API**: 必须有测试用例
- **边界条件**: 必须覆盖
- **错误处理**: 必须测试

---

## 文档规范

### 文档更新要求

任何代码变更都必须包含相应的文档更新：

- **新增功能**: 更新 API 文档和使用示例
- **API 变更**: 更新 API 文档
- **破坏性变更**: 更新 CHANGELOG 和迁移指南
- **Bug 修复**: 更新相关文档说明

### 文档编写指南

- **使用中文编写**: 项目文档优先使用中文
- **清晰的标题**: 使用正确的 Markdown 标题层级
- **代码示例**: 所有公共 API 必须包含使用示例
- **截图和图表**: 复杂功能应包含截图或流程图

### 文档位置

| 文档类型 | 位置 | 说明 |
|----------|------|------|
| API 文档 | `docs/API.md` | 所有 API 的详细文档 |
| 开发规范 | `docs/DEVELOPMENT_WORKFLOW.md` | 开发流程和规范 |
| 任务追踪 | `TASK.md` | 项目任务追踪 |
| 变更日志 | `CHANGELOG.md` | 版本变更记录 |
| README | `README.md` | 项目介绍和快速开始 |

---

## 获取帮助

### 沟通渠道

- **GitHub Issues**: 报告问题和功能请求
- **GitHub Discussions**: 一般讨论和问答
- **Pull Requests**: 代码审查和讨论

### 资源链接

- [项目文档](../docs/)
- [API 文档](../docs/API.md)
- [开发规范](../docs/DEVELOPMENT_WORKFLOW.md)
- [任务追踪](../docs/TASK.md)
- [变更日志](CHANGELOG.md)

### 常见问题

**Q: 我该如何选择要处理的问题？**

A: 寻找标记为 `good first issue` 或 `help wanted` 的问题。这些通常是适合新贡献者的问题。

**Q: 我的 PR 没有得到回应怎么办？**

A: 请耐心等待。维护者会尽力及时审查所有 PR。如果一周内没有回应，您可以在 PR 中评论提醒。

**Q: 我可以提交多个功能吗？**

A: 我们建议每个 PR 只包含一个功能或修复。这样可以更容易审查和合并。

**Q: 如何设置本地开发环境？**

A: 请参考上面的"开发环境搭建"章节。如果遇到问题，请创建 Issue 寻求帮助。

---

## 许可证

通过贡献代码，您同意您的贡献将按照项目的 [MIT License](LICENSE) 进行许可。

---

## 致谢

感谢所有贡献者让这个项目变得更好！

**贡献者列表**: [CONTRIBUTORS.md](./CONTRIBUTORS.md)

---

> **最后更新**: 2025-01-04
> **维护者**: Frontend Design Agent Skills 项目团队
