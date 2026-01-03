#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
性能检查工具

分析代码性能问题，提供优化建议。

用法:
    python check-performance.py <project-dir>
    python check-performance.py <project-dir> --format json

示例:
    python check-performance.py ./src
    python check-performance.py ./src --format markdown --output perf-report.md
"""

import sys
import argparse
import re
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass, field


@dataclass
class PerformanceIssue:
    """性能问题"""
    level: str  # 'critical', 'warning', 'info'
    category: str  # 'bundle', 'rendering', 'network', 'code'
    file: str
    line: int
    message: str
    suggestion: str


@dataclass
class PerformanceResult:
    """性能检查结果"""
    total_files: int
    total_issues: int
    critical_count: int
    warning_count: int
    issues: List[PerformanceIssue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return self.critical_count == 0


class PerformanceChecker:
    """性能检查器"""

    # 文件扩展名
    CODE_EXTENSIONS = {'.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte'}

    def __init__(self):
        self.issues: List[PerformanceIssue] = []

    def check_directory(self, directory: Path) -> PerformanceResult:
        """
        检查目录性能

        Args:
            directory: 项目目录

        Returns:
            检查结果
        """
        self.issues = []
        files_checked = 0

        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.CODE_EXTENSIONS:
                files_checked += 1
                self._check_file(file_path)

        critical = sum(1 for i in self.issues if i.level == 'critical')
        warning = sum(1 for i in self.issues if i.level == 'warning')

        return PerformanceResult(
            total_files=files_checked,
            total_issues=len(self.issues),
            critical_count=critical,
            warning_count=warning,
            issues=self.issues
        )

    def _check_file(self, file_path: Path):
        """检查单个文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            lines = content.split('\n')

            # 检查各种性能问题
            self._check_imports(file_path, lines)
            self._check_large_components(file_path, lines)
            self._check_missing_keys(file_path, lines)
            self._check_inline_styles(file_path, lines)
            self._check_missing_memo(file_path, lines)
            self._check_large_images(file_path, lines)
            self._check_missing_lazy_loading(file_path, lines)

        except Exception as e:
            self.issues.append(PerformanceIssue(
                level='warning',
                category='code',
                file=str(file_path),
                line=0,
                message=f'文件分析失败: {e}',
                suggestion='检查文件编码和格式'
            ))

    def _check_imports(self, file_path: Path, lines: List[str]):
        """检查import语句"""
        for i, line in enumerate(lines, 1):
            # 检查大型库的完整导入
            large_imports = {
                "from 'lodash'": "lodash",
                "from \"lodash\"": "lodash",
                "from 'moment'": "moment",
                "from \"moment\"": "moment",
            }
            for pattern, lib in large_imports.items():
                if pattern in line:
                    self.issues.append(PerformanceIssue(
                        level='warning',
                        category='bundle',
                        file=str(file_path),
                        line=i,
                        message=f'导入整个{lib}库会增加bundle大小',
                        suggestion=f'使用按需导入: import debounce from \'{lib}/debounce\''
                    ))

            # 检查相对路径导入
            if re.search(r"from\s+['\"]\.\.\/\.\.\/\.\.", line):
                self.issues.append(PerformanceIssue(
                    level='info',
                    category='code',
                    file=str(file_path),
                    line=i,
                    message='深层相对路径导入',
                    suggestion='考虑使用路径别名或绝对路径导入'
                ))

    def _check_large_components(self, file_path: Path, lines: List[str]):
        """检查大型组件"""
        if len(lines) > 300:
            self.issues.append(PerformanceIssue(
                level='warning',
                category='code',
                file=str(file_path),
                line=1,
                message=f'组件过大 ({len(lines)} 行)',
                suggestion='考虑拆分为更小的子组件以提高可维护性和渲染性能'
            ))

    def _check_missing_keys(self, file_path: Path, lines: List[str]):
        """检查缺失的key属性"""
        for i, line in enumerate(lines, 1):
            if '.map(' in line and 'key=' not in line and 'key:' not in line:
                self.issues.append(PerformanceIssue(
                    level='critical',
                    category='rendering',
                    file=str(file_path),
                    line=i,
                    message='列表渲染可能缺少key属性',
                    suggestion='为每个列表项添加唯一的key属性以提高渲染性能'
                ))

    def _check_inline_styles(self, file_path: Path, lines: List[str]):
        """检查内联样式"""
        inline_style_count = 0
        for i, line in enumerate(lines, 1):
            if 'style={{' in line:
                inline_style_count += 1
                if inline_style_count > 3:
                    self.issues.append(PerformanceIssue(
                        level='info',
                        category='rendering',
                        file=str(file_path),
                        line=i,
                        message='多处使用内联样式',
                        suggestion='考虑使用CSS类或styled-components以提高性能'
                    ))
                    break

    def _check_missing_memo(self, file_path: Path, lines: List[str]):
        """检查缺失的memoization"""
        has_use_callback = any('useCallback' in line for line in lines)
        has_use_memo = any('useMemo' in line for line in lines)
        has_memo = any('React.memo' in line or 'memo(' in line for line in lines)

        if (has_use_callback or has_use_memo) and not has_memo:
            self.issues.append(PerformanceIssue(
                level='info',
                category='rendering',
                file=str(file_path),
                line=1,
                message='使用了useCallback/useMemo但组件未使用memo',
                suggestion='考虑用React.memo包装组件以避免不必要的重新渲染'
            ))

    def _check_large_images(self, file_path: Path, lines: List[str]):
        """检查大图片引用"""
        for i, line in enumerate(lines, 1):
            if re.search(r'<img[^>]*(src=).*\.(png|jpg|jpeg)', line, re.IGNORECASE):
                if 'loading=' not in line and 'loading=' not in lines[min(i, len(lines)-1)]:
                    self.issues.append(PerformanceIssue(
                        level='warning',
                        category='network',
                        file=str(file_path),
                        line=i,
                        message='图片可能缺少懒加载',
                        suggestion='添加 loading="lazy" 属性以延迟加载图片'
                    ))

    def _check_missing_lazy_loading(self, file_path: Path, lines: List[str]):
        """检查缺失的代码分割"""
        has_dynamic_import = any('import(' in line for line in lines)

        if not has_dynamic_import and len(lines) > 200:
            self.issues.append(PerformanceIssue(
                level='info',
                category='bundle',
                file=str(file_path),
                line=1,
                message='可能缺少代码分割',
                suggestion='考虑使用动态import()进行路由级或组件级代码分割'
            ))


def format_report(result: PerformanceResult, output_format: str = 'text') -> str:
    """格式化报告"""
    if output_format == 'json':
        import json
        return json.dumps({
            'is_valid': result.is_valid,
            'total_files': result.total_files,
            'total_issues': result.total_issues,
            'critical_count': result.critical_count,
            'warning_count': result.warning_count,
            'issues': [
                {
                    'level': i.level,
                    'category': i.category,
                    'file': i.file,
                    'line': i.line,
                    'message': i.message,
                    'suggestion': i.suggestion
                }
                for i in result.issues
            ]
        }, ensure_ascii=False, indent=2)

    elif output_format == 'markdown':
        lines = [
            "# 性能检查报告\n",
            f"**状态**: {'✅ 通过' if result.is_valid else '⚠️ 需要优化'}",
            f"**检查文件**: {result.total_files}",
            f"**发现问题**: {result.total_issues}",
            f"**严重**: {result.critical_count}",
            f"**警告**: {result.warning_count}\n"
        ]

        if result.issues:
            # 按类别分组
            by_category: Dict[str, List[PerformanceIssue]] = {}
            for issue in result.issues:
                by_category.setdefault(issue.category, []).append(issue)

            for category, issues in by_category.items():
                lines.append(f"## {category.title()}\n")
                for issue in issues:
                    emoji = {'critical': '🔴', 'warning': '🟡', 'info': '⚪'}.get(issue.level, '⚪')
                    lines.append(f"### {emoji} `{Path(issue.file).name}:{issue.line}`")
                    lines.append(f"{issue.message}")
                    lines.append(f"**建议**: {issue.suggestion}")
                    lines.append("")

        return "\n".join(lines)

    else:  # text
        lines = [
            "=" * 60,
            "性能检查报告",
            "=" * 60,
            f"状态: {'✅ 通过' if result.is_valid else '⚠️ 需要优化'}",
            f"检查文件: {result.total_files}",
            f"发现问题: {result.total_issues}",
            f"严重: {result.critical_count}",
            f"警告: {result.warning_count}",
            ""
        ]

        if result.issues:
            lines.append("问题列表:")
            lines.append("-" * 40)

            # 按类别分组
            by_category: Dict[str, List[PerformanceIssue]] = {}
            for issue in result.issues:
                by_category.setdefault(issue.category, []).append(issue)

            for category, issues in by_category.items():
                lines.append(f"\n【{category.upper()}】")
                for issue in issues:
                    emoji = {'critical': '🔴', 'warning': '🟡', 'info': '⚪'}.get(issue.level, '⚪')
                    lines.append(f"\n{emoji} [{issue.level.upper()}] {Path(issue.file).name}:{issue.line}")
                    lines.append(f"    {issue.message}")
                    lines.append(f"    💡 {issue.suggestion}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='检查代码性能问题',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('directory', type=Path, help='项目目录路径')
    parser.add_argument('--format', '-f', choices=['text', 'json', 'markdown'], default='text')
    parser.add_argument('--output', '-o', type=Path, help='输出文件路径')
    parser.add_argument('--exclude', type=str, nargs='+', help='排除的目录', default=['node_modules', 'dist', 'build'])

    args = parser.parse_args()

    if not args.directory.exists():
        print(f"❌ 目录不存在: {args.directory}", file=sys.stderr)
        return 1

    checker = PerformanceChecker()
    result = checker.check_directory(args.directory)

    report = format_report(result, args.format)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📄 报告已保存到: {args.output}")
    else:
        print(report)

    # 摘要
    status = "✅ 通过" if result.is_valid else "⚠️ 需要优化"
    print(f"\n⚡ 性能检查 - {status}")
    print(f"   文件: {result.total_files} | "
          f"问题: {result.total_issues} | "
          f"严重: {result.critical_count}")

    return 0 if result.is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
