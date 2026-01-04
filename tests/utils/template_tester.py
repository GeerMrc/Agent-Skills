#!/usr/bin/env python3
"""
模板测试器

用于测试项目模板的完整性和可用性。
验证模板可以成功安装依赖和构建项目。

> 📅 **创建日期**: 2026-01-04
> 👤 **作者**: Frontend Design Agent Skills 项目团队
"""

import os
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple


@dataclass
class TestResult:
    """模板测试结果"""

    template_name: str
    status: str  # "PASS" | "FAIL" | "SKIP"
    install_time: float = 0.0
    build_time: float = 0.0
    build_size: int = 0
    error_message: str = ""
    logs: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        """返回测试结果的字符串表示"""
        status_icon = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️"}.get(self.status, "❓")
        return f"{status_icon} {self.template_name}: {self.status}"


class TemplateTester:
    """
    模板测试器

    测试项目模板的完整性和可用性，包括：
    - 依赖安装（npm install）
    - 项目构建（npm run build）
    - 错误处理和日志记录
    """

    def __init__(
        self,
        templates_dir: str,
        temp_dir: Optional[str] = None,
        verbose: bool = True,
    ):
        """
        初始化模板测试器

        Args:
            templates_dir: 模板目录路径
            temp_dir: 临时目录路径（可选，默认使用系统临时目录）
            verbose: 是否显示详细输出
        """
        self.templates_dir = Path(templates_dir)
        self.temp_dir = Path(temp_dir or tempfile.gettempdir()) / "template-tests"
        self.verbose = verbose
        self.results: List[TestResult] = []

        # 确保临时目录存在
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def _log(self, message: str) -> None:
        """记录日志"""
        if self.verbose:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def _check_node_npm(self) -> Tuple[bool, str]:
        """
        检查Node.js和npm是否已安装

        Returns:
            (是否安装, 错误消息)
        """
        try:
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            node_version = result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False, "Node.js未安装，请先安装Node.js"

        try:
            result = subprocess.run(
                ["npm", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            npm_version = result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False, "npm未安装，请先安装npm"

        self._log(f"✅ Node.js: {node_version}, npm: {npm_version}")
        return True, ""

    def _run_command(
        self,
        command: List[str],
        cwd: Path,
        timeout: int = 300,
    ) -> Tuple[bool, str, float]:
        """
        运行命令并返回结果

        Args:
            command: 命令列表
            cwd: 工作目录
            timeout: 超时时间（秒）

        Returns:
            (是否成功, 错误消息, 耗时)
        """
        self._log(f"执行: {' '.join(command)}")

        start_time = time.time()
        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            elapsed = time.time() - start_time

            if result.returncode != 0:
                error_msg = result.stderr or result.stdout or "未知错误"
                return False, error_msg, elapsed

            return True, "", elapsed

        except subprocess.TimeoutExpired:
            return False, f"命令超时（{timeout}秒）", timeout

    def _get_directory_size(self, path: Path) -> int:
        """
        获取目录大小（字节）

        Args:
            path: 目录路径

        Returns:
            目录大小（字节）
        """
        total_size = 0
        try:
            for dirpath, _, filenames in os.walk(path):
                for filename in filenames:
                    filepath = Path(dirpath) / filename
                    if filepath.exists():
                        total_size += filepath.stat().st_size
        except Exception as e:
            self._log(f"⚠️ 计算目录大小失败: {e}")

        return total_size

    def test_template(self, template_name: str) -> TestResult:
        """
        测试单个模板

        Args:
            template_name: 模板名称

        Returns:
            测试结果
        """
        self._log(f"\n{'='*60}")
        self._log(f"开始测试模板: {template_name}")
        self._log(f"{'='*60}")

        result = TestResult(template_name=template_name, status="SKIP")
        template_path = self.templates_dir / template_name

        # 检查模板目录是否存在
        if not template_path.exists():
            result.error_message = f"模板目录不存在: {template_path}"
            result.status = "SKIP"
            self._log(f"⏭️ 跳过: {result.error_message}")
            return result

        # 检查package.json是否存在
        package_json = template_path / "package.json"
        if not package_json.exists():
            result.error_message = f"package.json不存在: {package_json}"
            result.status = "SKIP"
            self._log(f"⏭️ 跳过: {result.error_message}")
            return result

        # 创建临时测试目录
        test_dir = self.temp_dir / template_name
        try:
            if test_dir.exists():
                shutil.rmtree(test_dir)
            shutil.copytree(template_path, test_dir)
        except Exception as e:
            result.error_message = f"复制模板失败: {e}"
            result.status = "FAIL"
            self._log(f"❌ {result.error_message}")
            return result

        try:
            # 步骤1: npm install
            self._log(f"\n📦 步骤 1/2: 安装依赖...")
            success, error, install_time = self._run_command(
                ["npm", "install"],
                cwd=test_dir,
                timeout=600,  # 10分钟超时
            )

            result.install_time = install_time

            if not success:
                result.status = "FAIL"
                result.error_message = f"npm install失败:\n{error}"
                result.logs.append(f"npm install: {error}")
                self._log(f"❌ {result.error_message}")
                return result

            self._log(f"✅ 依赖安装成功 (耗时: {install_time:.1f}秒)")

            # 步骤2: npm run build
            self._log(f"\n🔨 步骤 2/2: 构建项目...")
            success, error, build_time = self._run_command(
                ["npm", "run", "build"],
                cwd=test_dir,
                timeout=300,  # 5分钟超时
            )

            result.build_time = build_time

            if not success:
                result.status = "FAIL"
                result.error_message = f"npm run build失败:\n{error}"
                result.logs.append(f"npm run build: {error}")
                self._log(f"❌ {result.error_message}")
                return result

            # 计算构建输出大小
            dist_dir = test_dir / "dist"
            if dist_dir.exists():
                result.build_size = self._get_directory_size(dist_dir)
                size_mb = result.build_size / (1024 * 1024)
                self._log(f"✅ 构建成功 (耗时: {build_time:.1f}秒, 输出: {size_mb:.2f}MB)")
            else:
                self._log(f"✅ 构建成功 (耗时: {build_time:.1f}秒)")

            result.status = "PASS"
            self._log(f"\n🎉 模板 {template_name} 测试通过!")

        except Exception as e:
            result.status = "FAIL"
            result.error_message = f"测试过程中发生异常: {e}"
            self._log(f"❌ {result.error_message}")

        finally:
            # 清理临时目录
            try:
                if test_dir.exists():
                    shutil.rmtree(test_dir)
                    self._log(f"🧹 已清理临时目录: {test_dir}")
            except Exception as e:
                self._log(f"⚠️ 清理临时目录失败: {e}")

        return result

    def test_all_templates(
        self,
        template_names: Optional[List[str]] = None,
    ) -> List[TestResult]:
        """
        测试所有模板

        Args:
            template_names: 要测试的模板列表（可选，默认测试所有模板）

        Returns:
            测试结果列表
        """
        self._log(f"\n{'='*60}")
        self._log(f"模板测试开始")
        self._log(f"{'='*60}\n")

        # 检查Node.js和npm
        installed, error_msg = self._check_node_npm()
        if not installed:
            self._log(f"❌ {error_msg}")
            self._log(f"\n跳过所有模板测试")
            return []

        # 确定要测试的模板列表
        if template_names is None:
            # 自动发现所有模板
            template_names = []
            if self.templates_dir.exists():
                for item in self.templates_dir.iterdir():
                    if item.is_dir() and (item / "package.json").exists():
                        template_names.append(item.name)

        if not template_names:
            self._log("⚠️ 未找到任何模板")
            return []

        self._log(f"找到 {len(template_names)} 个模板: {', '.join(template_names)}\n")

        # 测试每个模板
        self.results = []
        for template_name in template_names:
            result = self.test_template(template_name)
            self.results.append(result)

        return self.results

    def print_summary(self) -> None:
        """打印测试摘要"""
        self._log(f"\n{'='*60}")
        self._log(f"测试摘要")
        self._log(f"{'='*60}\n")

        if not self.results:
            self._log("无测试结果")
            return

        # 统计
        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "PASS")
        failed = sum(1 for r in self.results if r.status == "FAIL")
        skipped = sum(1 for r in self.results if r.status == "SKIP")

        self._log(f"总计: {total} | 通过: {passed} | 失败: {failed} | 跳过: {skipped}")
        self._log("")

        # 详细结果
        for result in self.results:
            self._log(str(result))
            if result.status == "FAIL":
                self._log(f"  错误: {result.error_message[:100]}...")

        # 通过率
        if total > 0:
            pass_rate = (passed / total) * 100
            self._log(f"\n通过率: {pass_rate:.1f}%")

        # 总耗时
        total_install_time = sum(r.install_time for r in self.results)
        total_build_time = sum(r.build_time for r in self.results)
        self._log(f"总耗时: 安装 {total_install_time:.1f}s + 构建 {total_build_time:.1f}s = {total_install_time + total_build_time:.1f}s")

    def cleanup(self) -> None:
        """清理临时目录"""
        try:
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                self._log(f"🧹 已清理临时测试目录: {self.temp_dir}")
        except Exception as e:
            self._log(f"⚠️ 清理临时目录失败: {e}")
