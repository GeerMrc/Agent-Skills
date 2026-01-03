#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
无障碍检查工具

检查颜色对比度、ARIA属性、语义化HTML等无障碍问题。

用法:
    python check-accessibility.py <html-file>
    python check-accessibility.py <html-file> --format json

示例:
    python check-accessibility.py index.html
    python check-accessibility.py index.html --format markdown --output a11y-report.md
"""

import sys
import argparse
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

# 添加父目录到路径以导入共享模块
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.color import ColorUtils
from utils.reporter import Reporter


@dataclass
class A11yIssue:
    """无障碍问题"""
    level: str  # 'critical', 'serious', 'moderate', 'minor'
    category: str  # 'contrast', 'aria', 'semantic', 'keyboard', 'other'
    element: str
    message: str
    suggestion: Optional[str] = None
    line: Optional[int] = None


@dataclass
class A11yResult:
    """无障碍检查结果"""
    total_checks: int
    passed: int
    issues: List[A11yIssue] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for i in self.issues if i.level == 'critical')

    @property
    def serious_count(self) -> int:
        return sum(1 for i in self.issues if i.level == 'serious')

    @property
    def is_valid(self) -> bool:
        return self.critical_count == 0


class AccessibilityChecker:
    """无障碍检查器"""

    def __init__(self):
        self.issues: List[A11yIssue] = []

    def check_html(self, html_content: str) -> A11yResult:
        """
        检查HTML无障碍问题

        Args:
            html_content: HTML内容

        Returns:
            检查结果
        """
        self.issues = []
        checks = 0
        passed = 0

        # 1. 检查图片alt属性
        checks += 1
        img_issues = self._check_images(html_content)
        if not img_issues:
            passed += 1
        self.issues.extend(img_issues)

        # 2. 检查链接文本
        checks += 1
        link_issues = self._check_links(html_content)
        if not link_issues:
            passed += 1
        self.issues.extend(link_issues)

        # 3. 检查表单标签
        checks += 1
        form_issues = self._check_forms(html_content)
        if not form_issues:
            passed += 1
        self.issues.extend(form_issues)

        # 4. 检查标题层级
        checks += 1
        heading_issues = self._check_headings(html_content)
        if not heading_issues:
            passed += 1
        self.issues.extend(heading_issues)

        # 5. 检查按钮
        checks += 1
        button_issues = self._check_buttons(html_content)
        if not button_issues:
            passed += 1
        self.issues.extend(button_issues)

        # 6. 检查颜色对比度 (简化版)
        checks += 1
        contrast_issues = self._check_contrast(html_content)
        if not contrast_issues:
            passed += 1
        self.issues.extend(contrast_issues)

        return A11yResult(
            total_checks=checks,
            passed=passed,
            issues=self.issues
        )

    def _check_images(self, html: str) -> List[A11yIssue]:
        """检查图片alt属性"""
        issues = []
        lines = html.split('\n')

        for i, line in enumerate(lines, 1):
            # 查找img标签
            for match in re.finditer(r'<img[^>]*>', line, re.IGNORECASE):
                img_tag = match.group(0)
                # 检查是否有alt属性
                if not re.search(r'\balt\s*=', img_tag, re.IGNORECASE):
                    issues.append(A11yIssue(
                        level='critical',
                        category='aria',
                        element='img',
                        message='图片缺少alt属性',
                        suggestion='添加描述性alt文本，装饰性图片使用alt=""',
                        line=i
                    ))
                # 检查alt是否为空但有意义
                elif re.search(r'\balt\s*=\s*["\']["\']', img_tag, re.IGNORECASE):
                    # 检查是否应该是装饰性图片
                    if re.search(r'\b(decorative|bg|background)\b', img_tag, re.IGNORECASE):
                        pass  # 装饰性图片可以有空alt
                    else:
                        issues.append(A11yIssue(
                            level='moderate',
                            category='aria',
                            element='img',
                            message='图片alt属性为空，但可能需要描述',
                            suggestion='如果图片传达信息，请添加描述性alt文本',
                            line=i
                        ))

        return issues

    def _check_links(self, html: str) -> List[A11yIssue]:
        """检查链接文本"""
        issues = []
        lines = html.split('\n')

        for i, line in enumerate(lines, 1):
            for match in re.finditer(r'<a[^>]*>(.*?)</a>', line, re.IGNORECASE | re.DOTALL):
                link_text = match.group(1).strip()
                link_text_clean = re.sub(r'<[^>]+>', '', link_text).strip()

                # 检查空链接
                if not link_text_clean:
                    issues.append(A11yIssue(
                        level='serious',
                        category='semantic',
                        element='a',
                        message='链接没有文本内容',
                        suggestion='添加描述性链接文本或aria-label',
                        line=i
                    ))

                # 检查"点击这里"类型链接
                elif re.search(r'^(click|点击|here|这里|more|更多)$', link_text_clean, re.IGNORECASE):
                    issues.append(A11yIssue(
                        level='moderate',
                        category='semantic',
                        element='a',
                        message='链接文本不具描述性',
                        suggestion='使用描述性链接文本，如"查看用户指南"而非"点击这里"',
                        line=i
                    ))

                # 检查是否只有URL作为文本
                elif re.match(r'^https?://', link_text_clean):
                    issues.append(A11yIssue(
                        level='minor',
                        category='semantic',
                        element='a',
                        message='链接文本是URL',
                        suggestion='使用有意义的描述文本代替URL',
                        line=i
                    ))

        return issues

    def _check_forms(self, html: str) -> List[A11yIssue]:
        """检查表单标签关联"""
        issues = []
        lines = html.split('\n')

        for i, line in enumerate(lines, 1):
            # 检查input字段
            for match in re.finditer(r'<input[^>]*>', line, re.IGNORECASE):
                input_tag = match.group(0)

                # 检查是否有id但没有label
                has_id = bool(re.search(r'\bid\s*=\s*["\']([^"\']+)["\']', input_tag, re.IGNORECASE))
                has_aria_label = bool(re.search(r'\baria-label\s*=', input_tag, re.IGNORECASE))
                has_aria_labelledby = bool(re.search(r'\baria-labelledby\s*=', input_tag, re.IGNORECASE))

                if has_id and not (has_aria_label or has_aria_labelledby):
                    # 简化检查 - 实际需要检查关联的label
                    issues.append(A11yIssue(
                        level='serious',
                        category='aria',
                        element='input',
                        message='input字段可能有未关联的label',
                        suggestion='确保每个input都有对应的label，使用for/id关联或aria-label',
                        line=i
                    ))

                # 检查必填字段
                is_required = bool(re.search(r'\brequired\b', input_tag, re.IGNORECASE))
                has_aria_required = bool(re.search(r'\baria-required\s*=\s*["\']?true["\']?', input_tag, re.IGNORECASE))

                if is_required and not has_aria_required:
                    issues.append(A11yIssue(
                        level='moderate',
                        category='aria',
                        element='input',
                        message='必填字段缺少aria-required属性',
                        suggestion='添加 aria-required="true" 以改善屏幕阅读器体验',
                        line=i
                    ))

        return issues

    def _check_headings(self, html: str) -> List[A11yIssue]:
        """检查标题层级"""
        issues = []
        heading_pattern = re.compile(r'<h([1-6])[^>]*>(.*?)</h\1>', re.IGNORECASE | re.DOTALL)
        previous_level = 0

        for match in heading_pattern.finditer(html):
            level = int(match.group(1))
            text = re.sub(r'<[^>]+>', '', match.group(2)).strip()

            # 检查是否跳级
            if previous_level > 0 and level > previous_level + 1:
                issues.append(A11yIssue(
                    level='moderate',
                    category='semantic',
                    element=f'h{level}',
                    message=f'标题层级跳级: h{previous_level} → h{level}',
                    suggestion='标题应按顺序递增，不要跳级'
                ))

            # 检查空标题
            if not text:
                issues.append(A11yIssue(
                    level='serious',
                    category='semantic',
                    element=f'h{level}',
                    message='标题没有文本内容',
                    suggestion='添加描述性标题文本'
                ))

            previous_level = level

        return issues

    def _check_buttons(self, html: str) -> List[A11yIssue]:
        """检查按钮"""
        issues = []
        lines = html.split('\n')

        for i, line in enumerate(lines, 1):
            # 检查button元素
            for match in re.finditer(r'<button[^>]*>(.*?)</button>', line, re.IGNORECASE | re.DOTALL):
                button_text = re.sub(r'<[^>]+>', '', match.group(1)).strip()

                if not button_text:
                    issues.append(A11yIssue(
                        level='critical',
                        category='aria',
                        element='button',
                        message='按钮没有文本内容',
                        suggestion='添加按钮文本或aria-label属性',
                        line=i
                    ))

            # 检查作为按钮使用的div/a
            for match in re.finditer(r'<(div|a)[^>]*role\s*=\s*["\']?button["\']?[^>]*>', line, re.IGNORECASE):
                issues.append(A11yIssue(
                    level='serious',
                    category='semantic',
                    element=match.group(1),
                    message='非button元素用作按钮',
                    suggestion='优先使用<button>元素，或确保有正确的role、键盘事件和aria属性',
                    line=i
                ))

        return issues

    def _check_contrast(self, html: str) -> List[A11yIssue]:
        """检查颜色对比度 (简化版)"""
        issues = []

        # 检查CSS中的颜色定义
        color_matches = re.finditer(
            r'color:\s*oklch\([^)]+\);\s*background(?:-color)?:\s*oklch\([^)]+\);',
            html
        )

        for match in color_matches:
            # 简化处理 - 实际需要完整解析CSS
            colors = re.findall(r'oklch\(([^)]+)\)', match.group(0))
            if len(colors) >= 2:
                fg = f"oklch({colors[0]})"
                bg = f"oklch({colors[1]})"
                ratio = ColorUtils.calculate_contrast_ratio(fg, bg)

                if ratio < 4.5:
                    issues.append(A11yIssue(
                        level='critical',
                        category='contrast',
                        element='css',
                        message=f'颜色对比度不足: {ratio:.2f}:1 (要求 4.5:1)',
                        suggestion='调整前景色或背景色以提高对比度'
                    ))

        return issues


def format_report(result: A11yResult, output_format: str = 'text') -> str:
    """格式化报告"""
    if output_format == 'json':
        import json
        return json.dumps({
            'is_valid': result.is_valid,
            'total_checks': result.total_checks,
            'passed': result.passed,
            'critical_issues': result.critical_count,
            'serious_issues': result.serious_count,
            'issues': [
                {
                    'level': i.level,
                    'category': i.category,
                    'element': i.element,
                    'message': i.message,
                    'suggestion': i.suggestion,
                    'line': i.line
                }
                for i in result.issues
            ]
        }, ensure_ascii=False, indent=2)

    elif output_format == 'markdown':
        lines = [
            "# 无障碍检查报告\n",
            f"**状态**: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"**检查项**: {result.passed}/{result.total_checks} 通过",
            f"**严重问题**: {result.critical_count}",
            f"**重要问题**: {result.serious_count}\n"
        ]

        if result.issues:
            lines.append("## 问题列表\n")
            for issue in result.issues:
                emoji = {'critical': '🔴', 'serious': '🟠', 'moderate': '🟡', 'minor': '⚪'}
                lines.append(f"### {emoji.get(issue.level, '⚪')} {issue.level.upper()}: {issue.element}")
                if issue.line:
                    lines.append(f"**行**: {issue.line}")
                lines.append(f"{issue.message}")
                if issue.suggestion:
                    lines.append(f"**建议**: {issue.suggestion}")
                lines.append("")

        return "\n".join(lines)

    else:  # text
        lines = [
            "=" * 60,
            "无障碍检查报告",
            "=" * 60,
            f"状态: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"检查项: {result.passed}/{result.total_checks} 通过",
            f"严重问题: {result.critical_count}",
            f"重要问题: {result.serious_count}",
            ""
        ]

        if result.issues:
            lines.append("问题列表:")
            lines.append("-" * 40)
            for issue in result.issues:
                emoji = {'critical': '🔴', 'serious': '🟠', 'moderate': '🟡', 'minor': '⚪'}
                lines.append(f"\n{emoji.get(issue.level, '⚪')} [{issue.level.upper()}] {issue.element}")
                if issue.line:
                    lines.append(f"    行: {issue.line}")
                lines.append(f"    {issue.message}")
                if issue.suggestion:
                    lines.append(f"    💡 {issue.suggestion}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='检查HTML无障碍问题',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('html_file', type=Path, help='HTML文件路径')
    parser.add_argument('--format', '-f', choices=['text', 'json', 'markdown'], default='text')
    parser.add_argument('--output', '-o', type=Path, help='输出文件路径')

    args = parser.parse_args()

    if not args.html_file.exists():
        print(f"❌ 文件不存在: {args.html_file}", file=sys.stderr)
        return 1

    with open(args.html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    checker = AccessibilityChecker()
    result = checker.check_html(html_content)

    report = format_report(result, args.format)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📄 报告已保存到: {args.output}")
    else:
        print(report)

    # 摘要
    status = "✅ 通过" if result.is_valid else "❌ 失败"
    print(f"\n♿ 无障碍检查 - {status}")
    print(f"   检查: {result.passed}/{result.total_checks} | "
          f"严重: {result.critical_count} | 重要: {result.serious_count}")

    return 0 if result.is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
