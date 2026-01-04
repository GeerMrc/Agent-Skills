# -*- coding: utf-8 -*-
"""
报告生成工具模块

提供格式化的验证报告输出功能。
"""

import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class ReportSection:
    """报告章节"""
    title: str
    status: str  # 'pass', 'fail', 'warning'
    details: List[str]
    suggestions: List[str] = None

    def __post_init__(self):
        if self.suggestions is None:
            self.suggestions = []


class Reporter:
    """报告生成器"""

    @staticmethod
    def format_token_report(result, output_format: str = 'text') -> str:
        """
        格式化Token验证报告

        Args:
            result: ValidationResult对象
            output_format: 输出格式 ('text', 'json', 'markdown')

        Returns:
            格式化报告
        """
        if output_format == 'json':
            return Reporter._to_json(result)
        elif output_format == 'markdown':
            return Reporter._to_markdown(result)
        else:
            return Reporter._to_text(result)

    @staticmethod
    def _to_text(result) -> str:
        """生成文本格式报告"""
        lines = [
            "=" * 60,
            "Design Token 验证报告",
            "=" * 60,
            f"状态: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"总Token数: {result.total_tokens}",
            f"错误数: {result.error_count}",
            f"警告数: {result.warning_count}",
            ""
        ]

        if result.errors:
            lines.extend([
                "❌ 错误:",
                "-" * 40
            ])
            for error in result.errors:
                lines.append(f"  [{error.token_name}]")
                lines.append(f"    {error.message}")
                if error.suggestion:
                    lines.append(f"    💡 建议: {error.suggestion}")
                lines.append("")

        if result.warnings:
            lines.extend([
                "⚠️  警告:",
                "-" * 40
            ])
            for warning in result.warnings:
                lines.append(f"  [{warning.token_name}]")
                lines.append(f"    {warning.message}")
                if warning.suggestion:
                    lines.append(f"    💡 建议: {warning.suggestion}")
                lines.append("")

        lines.append("=" * 60)
        return "\n".join(lines)

    @staticmethod
    def _to_markdown(result) -> str:
        """生成Markdown格式报告"""
        lines = [
            "# Design Token 验证报告\n",
            f"**状态**: {'✅ 通过' if result.is_valid else '❌ 失败'}",
            f"**总Token数**: {result.total_tokens}",
            f"**错误数**: {result.error_count}",
            f"**警告数**: {result.warning_count}\n"
        ]

        if result.errors:
            lines.extend([
                "## ❌ 错误\n"
            ])
            for error in result.errors:
                lines.append(f"### `{error.token_name}`")
                lines.append(f"{error.message}")
                if error.suggestion:
                    lines.append(f"**建议**: {error.suggestion}")
                lines.append("")

        if result.warnings:
            lines.extend([
                "## ⚠️ 警告\n"
            ])
            for warning in result.warnings:
                lines.append(f"### `{warning.token_name}`")
                lines.append(f"{warning.message}")
                if warning.suggestion:
                    lines.append(f"**建议**: {warning.suggestion}")
                lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _to_json(result) -> str:
        """生成JSON格式报告"""
        data = {
            "is_valid": result.is_valid,
            "total_tokens": result.total_tokens,
            "error_count": result.error_count,
            "warning_count": result.warning_count,
            "errors": [
                {
                    "level": e.level,
                    "token_name": e.token_name,
                    "message": e.message,
                    "suggestion": e.suggestion
                }
                for e in result.errors
            ],
            "warnings": [
                {
                    "level": w.level,
                    "token_name": w.token_name,
                    "message": w.message,
                    "suggestion": w.suggestion
                }
                for w in result.warnings
            ]
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    @staticmethod
    def save_report(report: str, output_path: Path) -> None:
        """
        保存报告到文件

        Args:
            report: 报告内容
            output_path: 输出路径
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)

    @staticmethod
    def print_summary(result) -> None:
        """
        打印简要摘要

        Args:
            result: ValidationResult对象
        """
        status = "✅ 通过" if result.is_valid else "❌ 失败"
        print(f"\n🎨 Design Token 验证 - {status}")
        print(f"   总Token: {result.total_tokens} | "
              f"错误: {result.error_count} | "
              f"警告: {result.warning_count}")
