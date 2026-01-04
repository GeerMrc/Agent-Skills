#!/usr/bin/env python3
"""
模板测试报告生成器

生成格式化的模板测试报告，支持多种输出格式。

> 📅 **创建日期**: 2026-01-04
> 👤 **作者**: Frontend Design Agent Skills 项目团队
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List

from .template_tester import TestResult


class TemplateTestReporter:
    """
    模板测试报告生成器

    生成多种格式的测试报告：
    - 终端输出（彩色文本）
    - Markdown文件
    - JSON文件
    """

    def __init__(self, output_dir: str = "."):
        """
        初始化报告生成器

        Args:
            output_dir: 报告输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_terminal_report(self, results: List[TestResult]) -> str:
        """
        生成终端格式的报告

        Args:
            results: 测试结果列表

        Returns:
            格式化的报告字符串
        """
        lines = []
        lines.append("=" * 60)
        lines.append("模板测试报告")
        lines.append("=" * 60)
        lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")

        # 统计
        total = len(results)
        passed = sum(1 for r in results if r.status == "PASS")
        failed = sum(1 for r in results if r.status == "FAIL")
        skipped = sum(1 for r in results if r.status == "SKIP")

        lines.append("测试摘要")
        lines.append("-" * 60)
        lines.append(f"总计: {total} | ✅ 通过: {passed} | ❌ 失败: {failed} | ⏭️ 跳过: {skipped}")

        if total > 0:
            pass_rate = (passed / total) * 100
            lines.append(f"通过率: {pass_rate:.1f}%")

        # 总耗时
        total_install_time = sum(r.install_time for r in results)
        total_build_time = sum(r.build_time for r in results)
        lines.append(f"总耗时: 安装 {total_install_time:.1f}s + 构建 {total_build_time:.1f}s")

        lines.append("")

        # 详细结果
        lines.append("详细结果")
        lines.append("-" * 60)

        for result in results:
            status_icon = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️"}.get(result.status, "❓")
            lines.append(f"{status_icon} {result.template_name}: {result.status}")

            if result.status == "PASS":
                lines.append(f"   安装: {result.install_time:.1f}s | 构建: {result.build_time:.1f}s | 输出: {result.build_size / (1024*1024):.2f}MB")
            elif result.status == "FAIL":
                lines.append(f"   错误: {result.error_message[:80]}...")

        lines.append("")

        # 失败详情
        failed_results = [r for r in results if r.status == "FAIL"]
        if failed_results:
            lines.append("失败详情")
            lines.append("-" * 60)
            for result in failed_results:
                lines.append(f"❌ {result.template_name}")
                lines.append(f"   {result.error_message}")
                lines.append("")

        return "\n".join(lines)

    def generate_markdown_report(
        self,
        results: List[TestResult],
        output_file: str = "template-test-report.md",
    ) -> str:
        """
        生成Markdown格式的报告

        Args:
            results: 测试结果列表
            output_file: 输出文件名

        Returns:
            输出文件路径
        """
        output_path = self.output_dir / output_file

        lines = []
        lines.append("# 模板测试报告")
        lines.append("")
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")

        # 统计
        total = len(results)
        passed = sum(1 for r in results if r.status == "PASS")
        failed = sum(1 for r in results if r.status == "FAIL")
        skipped = sum(1 for r in results if r.status == "SKIP")

        lines.append("## 测试摘要")
        lines.append("")
        lines.append("| 指标 | 数量 |")
        lines.append("|------|------|")
        lines.append(f"| 总计 | {total} |")
        lines.append(f"| ✅ 通过 | {passed} |")
        lines.append(f"| ❌ 失败 | {failed} |")
        lines.append(f"| ⏭️ 跳过 | {skipped} |")

        if total > 0:
            pass_rate = (passed / total) * 100
            lines.append(f"| **通过率** | **{pass_rate:.1f}%** |")

        lines.append("")

        # 详细结果表格
        lines.append("## 详细结果")
        lines.append("")
        lines.append("| 模板 | 状态 | 安装时间 | 构建时间 | 输出大小 |")
        lines.append("|------|------|----------|----------|----------|")

        for result in results:
            status_icon = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️"}.get(result.status, "❓")

            if result.status == "PASS":
                size_mb = f"{result.build_size / (1024*1024):.2f}MB"
                lines.append(f"| {result.template_name} | {status_icon} {result.status} | {result.install_time:.1f}s | {result.build_time:.1f}s | {size_mb} |")
            elif result.status == "FAIL":
                lines.append(f"| {result.template_name} | {status_icon} {result.status} | - | - | - |")
            else:
                lines.append(f"| {result.template_name} | {status_icon} {result.status} | - | - | - |")

        lines.append("")

        # 失败详情
        failed_results = [r for r in results if r.status == "FAIL"]
        if failed_results:
            lines.append("## 失败详情")
            lines.append("")

            for result in failed_results:
                lines.append(f"### ❌ {result.template_name}")
                lines.append("")
                lines.append(f"```\n{result.error_message}\n```")
                lines.append("")

        # 写入文件
        content = "\n".join(lines)
        output_path.write_text(content, encoding="utf-8")

        return str(output_path)

    def generate_json_report(
        self,
        results: List[TestResult],
        output_file: str = "template-test-report.json",
    ) -> str:
        """
        生成JSON格式的报告

        Args:
            results: 测试结果列表
            output_file: 输出文件名

        Returns:
            输出文件路径
        """
        output_path = self.output_dir / output_file

        # 统计
        total = len(results)
        passed = sum(1 for r in results if r.status == "PASS")
        failed = sum(1 for r in results if r.status == "FAIL")
        skipped = sum(1 for r in results if r.status == "SKIP")

        # 构建报告数据
        report = {
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "skipped": skipped,
                "pass_rate": (passed / total * 100) if total > 0 else 0,
            },
            "results": [
                {
                    "template_name": r.template_name,
                    "status": r.status,
                    "install_time": r.install_time,
                    "build_time": r.build_time,
                    "build_size": r.build_size,
                    "error_message": r.error_message,
                    "logs": r.logs,
                }
                for r in results
            ],
        }

        # 写入文件
        output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

        return str(output_path)
