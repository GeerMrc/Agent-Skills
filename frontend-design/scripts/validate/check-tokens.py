#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Token 验证工具

验证Design Token的命名规范、格式和结构完整性。

用法:
    python check-tokens.py <token-file>
    python check-tokens.py <token-file> --format json
    python check-tokens.py <token-file> --output report.md

示例:
    python check-tokens.py tokens.json
    python check-tokens.py tokens.json --format markdown --output report.md
"""

import sys
import argparse
import json
from pathlib import Path
from typing import Dict, Any

# 添加父目录到路径以导入共享模块
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.token import TokenValidator, ValidationResult
from utils.reporter import Reporter


def load_tokens(file_path: Path) -> Dict[str, Any]:
    """
    加载Token文件

    Args:
        file_path: Token文件路径

    Returns:
        Token字典
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        if file_path.suffix == '.json':
            return json.load(f)
        else:
            # 尝试解析为JSON
            return json.load(f)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='验证Design Token的命名规范和结构',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s tokens.json                    # 文本格式输出
  %(prog)s tokens.json --format json      # JSON格式输出
  %(prog)s tokens.json --format markdown --output report.md
        """
    )

    parser.add_argument(
        'token_file',
        type=Path,
        help='Token文件路径 (JSON格式)'
    )

    parser.add_argument(
        '--format', '-f',
        choices=['text', 'json', 'markdown'],
        default='text',
        help='输出格式 (默认: text)'
    )

    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='输出文件路径 (可选)'
    )

    parser.add_argument(
        '--strict',
        action='store_true',
        help='严格模式: 警告也视为错误'
    )

    args = parser.parse_args()

    # 检查文件存在
    if not args.token_file.exists():
        print(f"❌ 错误: 文件不存在 - {args.token_file}", file=sys.stderr)
        return 1

    # 加载Token
    try:
        tokens = load_tokens(args.token_file)
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析错误: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ 文件读取错误: {e}", file=sys.stderr)
        return 1

    # 验证Token
    result = TokenValidator.validate_token_structure(tokens)

    # 严格模式
    if args.strict and result.warning_count > 0:
        result.is_valid = False

    # 生成报告
    report = Reporter.format_token_report(result, args.format)

    # 输出报告
    if args.output:
        Reporter.save_report(report, args.output)
        print(f"📄 报告已保存到: {args.output}")
    else:
        print(report)

    # 打印摘要
    Reporter.print_summary(result)

    # 返回状态码
    return 0 if result.is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
