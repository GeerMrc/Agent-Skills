#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技能测试工具

验证SKILL.md完整性、文档导航链接和结构规范。

用法:
    python test-skill.py
    python test-skill.py --format json

示例:
    python test-skill.py
    python test-skill.py --format markdown --output skill-test-report.md
"""

import sys
import argparse
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class TestIssue:
    """测试问题"""
    level: str  # 'error', 'warning', 'info'
    category: str  # 'structure', 'navigation', 'content', 'format'
    location: str
    message: str
    suggestion: Optional[str] = None


@dataclass
class TestResult:
    """测试结果"""
    total_tests: int
    passed: int
    failed: int
    warnings: int
    issues: List[TestIssue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return self.failed == 0


class SkillTester:
    """技能测试器"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.skill_file = project_root / "SKILL.md"
        self.references_dir = project_root / "references"
        self.issues: List[TestIssue] = []

    def run_all_tests(self) -> TestResult:
        """
        运行所有测试

        Returns:
            测试结果
        """
        self.issues = []
        tests = 0
        passed = 0

        # 1. 检查SKILL.md存在
        tests += 1
        if self._test_skill_file_exists():
            passed += 1

        # 2. 检查SKILL.md行数
        tests += 1
        if self._test_skill_line_count():
            passed += 1

        # 3. 检查必需章节
        tests += 1
        if self._test_required_sections():
            passed += 1

        # 4. 检查文档导航
        tests += 1
        if self._test_documentation_links():
            passed += 1

        # 5. 检查references目录结构
        tests += 1
        if self._test_references_structure():
            passed += 1

        # 6. 检查文档行数限制
        tests += 1
        if self._test_document_line_limits():
            passed += 1

        # 7. 检查文档README文件
        tests += 1
        if self._test_readme_files():
            passed += 1

        # 8. 检查示例文档
        tests += 1
        if self._test_example_documents():
            passed += 1

        failed = sum(1 for i in self.issues if i.level == 'error')
        warnings = sum(1 for i in self.issues if i.level == 'warning')

        return TestResult(
            total_tests=tests,
            passed=passed,
            failed=failed,
            warnings=warnings,
            issues=self.issues
        )

    def _test_skill_file_exists(self) -> bool:
        """检查SKILL.md存在"""
        if not self.skill_file.exists():
            self.issues.append(TestIssue(
                level='error',
                category='structure',
                location='SKILL.md',
                message='SKILL.md文件不存在',
                suggestion='创建SKILL.md作为技能入口点'
            ))
            return False
        return True

    def _test_skill_line_count(self) -> bool:
        """检查SKILL.md行数"""
        if not self.skill_file.exists():
            return True

        lines = len(self.skill_file.read_text(encoding='utf-8').split('\n'))

        if lines > 200:
            self.issues.append(TestIssue(
                level='error',
                category='structure',
                location='SKILL.md',
                message=f'SKILL.md行数过多: {lines}行 (要求≤200行)',
                suggestion='使用渐进式披露架构，将详细内容移至references/目录'
            ))
            return False

        if lines > 180:
            self.issues.append(TestIssue(
                level='warning',
                category='structure',
                location='SKILL.md',
                message=f'SKILL.md接近行数限制: {lines}行',
                suggestion='考虑将部分内容移至references/目录'
            ))

        return True

    def _test_required_sections(self) -> bool:
        """检查必需章节"""
        if not self.skill_file.exists():
            return True

        content = self.skill_file.read_text(encoding='utf-8')
        required_sections = [
            '## 🎯 核心理念',
            '## 🚀 快速开始',
            '## 📚 文档导航',
            '## 🎨 前端美学指南',
            '## 🔧 工具与脚本',
        ]

        missing = []
        for section in required_sections:
            if section not in content:
                missing.append(section)

        if missing:
            for section in missing:
                self.issues.append(TestIssue(
                    level='error',
                    category='content',
                    location='SKILL.md',
                    message=f'缺少必需章节: {section}',
                    suggestion='添加该章节到SKILL.md'
                ))
            return False

        return True

    def _test_documentation_links(self) -> bool:
        """检查文档导航链接"""
        if not self.skill_file.exists():
            return True

        content = self.skill_file.read_text(encoding='utf-8')

        # 检查references文档链接
        doc_links = re.findall(r'\[([^\]]+)\]\((references/[^)]+)\)', content)
        broken_links = []

        for title, link in doc_links:
            target_path = self.project_root / link
            if not target_path.exists():
                broken_links.append(f'{title} -> {link}')

        if broken_links:
            for link in broken_links:
                self.issues.append(TestIssue(
                    level='error',
                    category='navigation',
                    location='SKILL.md',
                    message=f'文档链接失效: {link}',
                    suggestion='创建目标文档或更新链接路径'
                ))
            return False

        return True

    def _test_references_structure(self) -> bool:
        """检查references目录结构"""
        if not self.references_dir.exists():
            self.issues.append(TestIssue(
                level='error',
                category='structure',
                location='references/',
                message='references目录不存在',
                suggestion='创建references/目录并组织文档'
            ))
            return False

        required_subdirs = [
            'methodology',
            'implementation',
            'aesthetics',
            'quality',
            'examples',
            'by-framework'
        ]

        missing = []
        for subdir in required_subdirs:
            if not (self.references_dir / subdir).exists():
                missing.append(subdir)

        if missing:
            for subdir in missing:
                self.issues.append(TestIssue(
                    level='warning',
                    category='structure',
                    location=f'references/{subdir}',
                    message=f'缺少子目录: {subdir}',
                    suggestion=f'创建references/{subdir}/目录'
                ))

        return len(missing) == 0

    def _test_document_line_limits(self) -> bool:
        """检查文档行数限制"""
        if not self.references_dir.exists():
            return True

        issues_found = False

        for doc_file in self.references_dir.rglob('*.md'):
            if doc_file.name == 'README.md':
                max_lines = 200  # README允许200行
            else:
                max_lines = 400  # 其他文档允许400行

            lines = len(doc_file.read_text(encoding='utf-8').split('\n'))

            if lines > max_lines:
                self.issues.append(TestIssue(
                    level='warning',
                    category='content',
                    location=str(doc_file.relative_to(self.project_root)),
                    message=f'文档行数过多: {lines}行 (建议≤{max_lines}行)',
                    suggestion='拆分文档或使用渐进式披露架构'
                ))
                issues_found = True

        return not issues_found

    def _test_readme_files(self) -> bool:
        """检查README文件"""
        if not self.references_dir.exists():
            return True

        missing_readme = []

        # 检查各子目录的README
        for subdir in ['methodology', 'implementation', 'aesthetics', 'quality', 'by-framework']:
            readme_path = self.references_dir / subdir / 'README.md'
            if not readme_path.exists():
                missing_readme.append(f'references/{subdir}/README.md')

        if missing_readme:
            for readme in missing_readme:
                self.issues.append(TestIssue(
                    level='info',
                    category='structure',
                    location=readme,
                    message='缺少README.md导航文件',
                    suggestion='创建README.md提供该目录的文档导航'
                ))

        return len(missing_readme) == 0

    def _test_example_documents(self) -> bool:
        """检查示例文档"""
        examples_dir = self.references_dir / 'examples'

        if not examples_dir.exists():
            self.issues.append(TestIssue(
                level='info',
                category='content',
                location='references/examples/',
                message='examples目录不存在',
                suggestion='创建examples/目录并添加示例文档'
            ))
            return False

        required_examples = [
            'component-examples.md',
            'layout-examples.md',
            'animation-examples.md'
        ]

        missing = []
        for example in required_examples:
            if not (examples_dir / example).exists():
                missing.append(example)

        if missing:
            for example in missing:
                self.issues.append(TestIssue(
                    level='info',
                    category='content',
                    location=f'references/examples/{example}',
                    message=f'缺少示例文档: {example}',
                    suggestion='创建示例文档以帮助用户理解最佳实践'
                ))

        return len(missing) == 0


def format_report(result: TestResult, output_format: str = 'text') -> str:
    """格式化报告"""
    if output_format == 'json':
        import json
        return json.dumps({
            'is_valid': result.is_valid,
            'total_tests': result.total_tests,
            'passed': result.passed,
            'failed': result.failed,
            'warnings': result.warnings,
            'issues': [
                {
                    'level': i.level,
                    'category': i.category,
                    'location': i.location,
                    'message': i.message,
                    'suggestion': i.suggestion
                }
                for i in result.issues
            ]
        }, ensure_ascii=False, indent=2)

    elif output_format == 'markdown':
        lines = [
            "# 技能测试报告\n",
            f"**状态**: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"**测试**: {result.passed}/{result.total_tests} 通过",
            f"**失败**: {result.failed}",
            f"**警告**: {result.warnings}\n"
        ]

        if result.issues:
            lines.append("## 问题列表\n")

            # 按类别分组
            by_category: Dict[str, List[TestIssue]] = {}
            for issue in result.issues:
                by_category.setdefault(issue.category, []).append(issue)

            for category, issues in by_category.items():
                lines.append(f"### {category.title()}\n")
                for issue in issues:
                    emoji = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}.get(issue.level, '⚪')
                    lines.append(f"#### {emoji} `{issue.location}`")
                    lines.append(f"{issue.message}")
                    if issue.suggestion:
                        lines.append(f"**建议**: {issue.suggestion}")
                    lines.append("")

        return "\n".join(lines)

    else:  # text
        lines = [
            "=" * 60,
            "技能测试报告",
            "=" * 60,
            f"状态: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"测试: {result.passed}/{result.total_tests} 通过",
            f"失败: {result.failed}",
            f"警告: {result.warnings}",
            ""
        ]

        if result.issues:
            lines.append("问题列表:")
            lines.append("-" * 40)

            by_category: Dict[str, List[TestIssue]] = {}
            for issue in result.issues:
                by_category.setdefault(issue.category, []).append(issue)

            for category, issues in by_category.items():
                lines.append(f"\n【{category.upper()}】")
                for issue in issues:
                    emoji = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}.get(issue.level, '⚪')
                    lines.append(f"\n{emoji} [{issue.level.upper()}] {issue.location}")
                    lines.append(f"    {issue.message}")
                    if issue.suggestion:
                        lines.append(f"    💡 {issue.suggestion}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='验证Frontend Design Agent Skills完整性',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--project-root', type=Path, default=Path.cwd(), help='项目根目录')
    parser.add_argument('--format', '-f', choices=['text', 'json', 'markdown'], default='text')
    parser.add_argument('--output', '-o', type=Path, help='输出文件路径')

    args = parser.parse_args()

    tester = SkillTester(args.project_root)
    result = tester.run_all_tests()

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
    print(f"\n🧪 技能测试 - {status}")
    print(f"   测试: {result.passed}/{result.total_tests} | "
          f"失败: {result.failed} | 警告: {result.warnings}")

    return 0 if result.is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
