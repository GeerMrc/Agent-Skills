#!/usr/bin/env python3
"""
模板测试脚本

测试项目模板的完整性和可用性。

用法:
    python tests/test-templates.py                    # 测试所有模板
    python tests/test-templates.py -t react vue      # 测试指定模板
    python tests/test-templates.py -o report.md      # 生成Markdown报告
    python tests/test-templates.py --verbose         # 显示详细输出

> 📅 **创建日期**: 2026-01-04
> 👤 **作者**: Frontend Design Agent Skills 项目团队
"""

import argparse
import sys
from pathlib import Path

# 添加父目录到Python路径
sys.path.insert(0, str(Path(__file__).parent))

from utils.template_tester import TemplateTester
from utils.reporter import TemplateTestReporter


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description="测试项目模板的完整性和可用性",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                    # 测试所有模板
  %(prog)s -t react vue        # 测试指定模板
  %(prog)s -o report.md        # 生成Markdown报告
  %(prog)s --verbose           # 显示详细输出
        """,
    )

    parser.add_argument(
        "-t",
        "--templates",
        nargs="+",
        help="要测试的模板列表（默认测试所有模板）",
    )

    parser.add_argument(
        "-d",
        "--templates-dir",
        default="frontend-design/templates",
        help="模板目录路径（默认: frontend-design/templates）",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="生成报告文件（支持.md和.json格式）",
    )

    parser.add_argument(
        "--output-dir",
        default=".",
        help="报告输出目录（默认: 当前目录）",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="显示详细输出",
    )

    parser.add_argument(
        "--no-cleanup",
        action="store_true",
        help="不清理临时测试目录",
    )

    args = parser.parse_args()

    # 检查模板目录
    templates_dir = Path(args.templates_dir)
    if not templates_dir.exists():
        print(f"❌ 错误: 模板目录不存在: {templates_dir}")
        print(f"请使用 -d 参数指定正确的模板目录")
        sys.exit(1)

    # 创建测试器
    tester = TemplateTester(
        templates_dir=str(templates_dir),
        verbose=args.verbose,
    )

    # 运行测试
    results = tester.test_all_templates(args.templates)

    # 打印摘要
    tester.print_summary()

    # 生成报告
    if results and args.output:
        reporter = TemplateTestReporter(output_dir=args.output_dir)

        print(f"\n{'='*60}")
        print(f"生成报告")
        print(f"{'='*60}\n")

        output_ext = Path(args.output).suffix.lower()

        if output_ext == ".md":
            output_path = reporter.generate_markdown_report(results, args.output)
            print(f"✅ Markdown报告已生成: {output_path}")
        elif output_ext == ".json":
            output_path = reporter.generate_json_report(results, args.output)
            print(f"✅ JSON报告已生成: {output_path}")
        else:
            # 默认生成Markdown
            output_path = reporter.generate_markdown_report(results, args.output)
            print(f"✅ 报告已生成: {output_path}")

    # 清理临时目录
    if not args.no_cleanup:
        tester.cleanup()
    else:
        print(f"\n💡 提示: 临时目录保留在: {tester.temp_dir}")

    # 返回退出码
    if results:
        failed = sum(1 for r in results if r.status == "FAIL")
        sys.exit(0 if failed == 0 else 1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
