#!/usr/bin/env python3
"""
Frontend Design Agent Skills - 发布包验证测试

验证技能包目录结构符合 Agent Skills 开放标准规范。
"""

import os
import sys
import tarfile
import zipfile
from pathlib import Path
from typing import List, Tuple


class ReleasePackageValidator:
    """发布包验证器"""

    # Agent Skills 规范要求的目录结构
    REQUIRED_FILES = ["SKILL.md"]

    ALLOWED_ROOT_FILES = [
        "SKILL.md",           # 必需
        "LICENSE",            # 可选
        "README.md",          # 可选
        "CHANGELOG.md",       # 可选
        "CONTRIBUTING.md",    # 可选
        ".gitignore",         # 可选
    ]

    ALLOWED_ROOT_DIRS = [
        "scripts",            # 可选 - 可执行代码
        "references",         # 可选 - 详细文档
        "templates",          # 可选 - 项目模板
        "tests",              # 可选 - 测试文件
        "docs",               # 可选 - 额外文档
    ]

    # 不应在发布包根目录的开发过程文档
    DEV_FILES_THAT_SHOULD_BE_IN_DOCS = [
        "TASK.md",
        "FRONTEND-DESIGN-DEVELOPMENT-PLAN.md",
        "MIGRATION_GUIDE.md",
        "PRE_RELEASE_AUDIT_REPORT.md",
        "QUALITY_VALIDATION_REPORT.md",
        "RELEASE_NOTES.md",
        "ARCHITECTURE.md",
        "API.md",
        "DEVELOPMENT_WORKFLOW.md",
        "AGENT_SKILLS_RELEASE_SPEC.md",
    ]

    def __init__(self, package_path: str):
        """
        初始化验证器

        Args:
            package_path: 技能包根目录路径
        """
        self.package_path = Path(package_path).resolve()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed_checks: List[str] = []

    def log(self, message: str, level: str = "info"):
        """记录日志"""
        prefix = {
            "error": "❌",
            "warning": "⚠️",
            "success": "✅",
            "info": "ℹ️",
        }.get(level, "  ")
        print(f"{prefix} {message}")

    def validate(self) -> bool:
        """
        执行完整验证

        Returns:
            bool: 验证是否通过
        """
        self.log(f"开始验证 Agent Skills 发布包: {self.package_path}", "info")
        self.log("=" * 60, "info")

        # 1. 验证必需文件
        self._validate_required_files()

        # 2. 验证根目录文件
        self._validate_root_files()

        # 3. 验证根目录目录
        self._validate_root_dirs()

        # 4. 验证 SKILL.md 格式
        self._validate_skill_md()

        # 5. 验证开发文档位置
        self._validate_dev_docs_location()

        # 输出结果
        self.log("=" * 60, "info")
        return self._print_results()

    def _validate_required_files(self):
        """验证必需文件存在"""
        self.log("检查必需文件...", "info")
        for filename in self.REQUIRED_FILES:
            file_path = self.package_path / filename
            if file_path.exists():
                self.passed_checks.append(f"必需文件存在: {filename}")
                self.log(f"  {filename} 存在", "success")
            else:
                self.errors.append(f"缺少必需文件: {filename}")
                self.log(f"  {filename} 不存在", "error")

    def _validate_root_files(self):
        """验证根目录文件符合规范"""
        self.log("检查根目录文件...", "info")
        for item in self.package_path.iterdir():
            if item.is_file():
                if item.name not in self.ALLOWED_ROOT_FILES:
                    self.warnings.append(
                        f"根目录包含非标准文件: {item.name}"
                    )
                    self.log(f"  非标准文件: {item.name}", "warning")

        allowed_files = ", ".join(self.ALLOWED_ROOT_FILES)
        self.log(f"  允许的文件: {allowed_files}", "info")
        self.passed_checks.append("根目录文件验证完成")

    def _validate_root_dirs(self):
        """验证根目录目录符合规范"""
        self.log("检查根目录目录...", "info")
        for item in self.package_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                if item.name not in self.ALLOWED_ROOT_DIRS:
                    self.errors.append(
                        f"根目录包含非标准目录: {item.name}"
                    )
                    self.log(f"  非标准目录: {item.name}", "error")

        allowed_dirs = ", ".join(self.ALLOWED_ROOT_DIRS)
        self.log(f"  允许的目录: {allowed_dirs}", "info")
        self.passed_checks.append("根目录目录验证完成")

    def _validate_skill_md(self):
        """验证 SKILL.md 格式"""
        self.log("检查 SKILL.md 格式...", "info")
        skill_md_path = self.package_path / "SKILL.md"

        if not skill_md_path.exists():
            return

        with open(skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split("\n")

        # 检查 YAML frontmatter
        if not content.startswith("---"):
            self.errors.append("SKILL.md 缺少 YAML frontmatter（必须以 --- 开头）")
            self.log("  缺少 YAML frontmatter", "error")
            return

        # 检查必需的 YAML 字段
        yaml_end = content.find("---", 3)
        if yaml_end == -1:
            self.errors.append("SKILL.md YAML frontmatter 未正确闭合")
            self.log("  YAML frontmatter 未闭合", "error")
            return

        yaml_content = content[3:yaml_end].strip()
        required_fields = ["name:", "description:"]
        for field in required_fields:
            if field not in yaml_content:
                self.errors.append(f"SKILL.md 缺少必需字段: {field}")
                self.log(f"  缺少字段: {field}", "error")

        # 检查文件长度（社区黄金标准 ≤ 200 行）
        if len(lines) > 200:
            self.warnings.append(
                f"SKILL.md 超过 200 行（当前 {len(lines)} 行），建议精简"
            )
            self.log(f"  文件过长: {len(lines)} 行", "warning")

        self.log(f"  SKILL.md 格式验证通过", "success")
        self.passed_checks.append("SKILL.md 格式验证完成")

    def _validate_dev_docs_location(self):
        """验证开发文档位置正确"""
        self.log("检查开发文档位置...", "info")

        # 检查根目录是否有开发文档
        dev_docs_in_root = []
        for doc_name in self.DEV_FILES_THAT_SHOULD_BE_IN_DOCS:
            if (self.package_path / doc_name).exists():
                dev_docs_in_root.append(doc_name)

        if dev_docs_in_root:
            self.errors.append(
                f"开发文档应在 docs/ 目录: {', '.join(dev_docs_in_root)}"
            )
            for doc in dev_docs_in_root:
                self.log(f"  {doc} 应在 docs/ 目录", "error")
        else:
            self.log("  开发文档位置正确", "success")
            self.passed_checks.append("开发文档位置验证完成")

    def _print_results(self) -> bool:
        """打印验证结果"""
        self.log("验证结果:", "info")
        print()

        if self.passed_checks:
            self.log(f"通过 ({len(self.passed_checks)}):", "success")
            for check in self.passed_checks:
                print(f"  ✓ {check}")
            print()

        if self.warnings:
            self.log(f"警告 ({len(self.warnings)}):", "warning")
            for warning in self.warnings:
                print(f"  ! {warning}")
            print()

        if self.errors:
            self.log(f"错误 ({len(self.errors)}):", "error")
            for error in self.errors:
                print(f"  ✗ {error}")
            print()

        # 判断是否通过（允许有警告，但不允许有错误）
        passed = len(self.errors) == 0

        if passed:
            self.log("验证通过! ✅", "success")
        else:
            self.log("验证失败! ❌", "error")

        return passed


def create_test_package(source_dir: Path, output_dir: Path):
    """
    创建测试用的发布包（zip 和 tar.gz）

    Args:
        source_dir: 源目录
        output_dir: 输出目录
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    package_name = "frontend-design-skill"

    # 创建 zip 包
    zip_path = output_dir / f"{package_name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for item in source_dir.rglob("*"):
            if item.is_file() and ".git" not in str(item):
                arcname = f"{package_name}/{item.relative_to(source_dir)}"
                zipf.write(item, arcname)

    print(f"✅ 创建 ZIP 包: {zip_path}")

    # 创建 tar.gz 包
    tar_path = output_dir / f"{package_name}.tar.gz"
    with tarfile.open(tar_path, "w:gz") as tarf:
        for item in source_dir.rglob("*"):
            if item.is_file() and ".git" not in str(item):
                arcname = f"{package_name}/{item.relative_to(source_dir)}"
                tarf.add(item, arcname)

    print(f"✅ 创建 TAR.GZ 包: {tar_path}")


def main():
    """主函数"""
    # 获取脚本所在目录的父目录（技能包根目录）
    script_dir = Path(__file__).parent.resolve()
    package_dir = script_dir.parent

    print("=" * 70)
    print("Frontend Design Agent Skills - 发布包验证测试")
    print("=" * 70)
    print()

    # 执行验证
    validator = ReleasePackageValidator(str(package_dir))
    passed = validator.validate()

    print()

    # 如果验证通过，创建测试包
    if passed:
        print("创建测试发布包...")
        test_output_dir = script_dir / "release-packages"
        create_test_package(package_dir, test_output_dir)
        print()

        # 验证创建的包
        print("验证创建的发布包...")
        for pkg in test_output_dir.glob("*"):
            print(f"  📦 {pkg.name}: {pkg.stat().st_size} bytes")
    else:
        print("❌ 验证未通过，不创建测试包")

    print()
    print("=" * 70)

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
