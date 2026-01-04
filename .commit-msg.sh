#!/bin/bash
#
# Git commit-msg hook
# 验证提交信息符合 Conventional Commits 规范
#
# 安装方法：
#   cp .commit-msg.sh .git/hooks/commit-msg
#   chmod +x .git/hooks/commit-msg
#

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# 允许的提交类型
ALLOWED_TYPES="feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert"

# Conventional Commits 正则表达式
# 格式: type(scope): subject
PATTERN="^($ALLOWED_TYPES)(\(.+\))?: .{10,50}$"

# 跳过合并提交和回滚提交
if echo "$COMMIT_MSG" | grep -qE "^(Merge|Revert)"; then
    exit 0
fi

# 验证提交信息格式
if ! echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
    echo "❌ 错误: 提交信息不符合 Conventional Commits 规范" >&2
    echo "" >&2
    echo "正确格式:" >&2
    echo "  type(scope): subject" >&2
    echo "" >&2
    echo "允许的类型 (type):" >&2
    echo "  feat     - 新功能" >&2
    echo "  fix      - 问题修复" >&2
    echo "  docs     - 文档更新" >&2
    echo "  style    - 代码格式" >&2
    echo "  refactor - 代码重构" >&2
    echo "  test     - 测试相关" >&2
    echo "  chore    - 构建工具" >&2
    echo "  perf     - 性能优化" >&2
    echo "  ci       - CI配置" >&2
    echo "  build    - 构建系统" >&2
    echo "  revert   - 回滚提交" >&2
    echo "" >&2
    echo "示例:" >&2
    echo "  feat(design-tokens): add OKLCH color system support" >&2
    echo "  fix(auth): resolve token validation error" >&2
    echo "  docs(readme): update installation instructions" >&2
    echo "" >&2
    echo "当前提交信息:" >&2
    echo "  $COMMIT_MSG" >&2
    echo "" >&2
    echo "请修改提交信息后重试。" >&2
    exit 1
fi

echo "✅ 提交信息格式验证通过"
exit 0
