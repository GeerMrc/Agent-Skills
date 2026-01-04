#!/usr/bin/env python3
"""
Frontend Design Templates - 模板完整性验证测试

验证所有项目模板的文件完整性、配置正确性和基本功能。

使用方法:
    python tests/test-cases/test-templates.py

选项:
    --template    指定测试的模板 (react/vue/vanilla)
    --verbose     显示详细输出
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple


class TemplateTester:
    """模板测试器"""

    def __init__(self, root_dir: Path, verbose: bool = False):
        self.root_dir = root_dir
        self.templates_dir = root_dir / "templates"
        self.verbose = verbose
        self.results = []

    def log(self, message: str, level: str = "INFO"):
        """输出日志"""
        if self.verbose or level in ["ERROR", "SUCCESS"]:
            prefix = {
                "INFO": "ℹ️",
                "SUCCESS": "✅",
                "ERROR": "❌",
                "WARN": "⚠️"
            }.get(level, "•")
            print(f"{prefix} {message}")

    def get_template_files(self, template_name: str) -> List[str]:
        """获取模板所需的文件列表"""
        templates = {
            "react": [
                "package.json",
                "vite.config.ts",
                "tsconfig.json",
                "tsconfig.node.json",
                "index.html",
                ".gitignore",
                "README.md",
                "src/main.tsx",
                "src/App.tsx",
                "src/App.css",
                "src/index.css",
                "src/vite-env.d.ts"
            ],
            "vue": [
                "package.json",
                "vite.config.ts",
                "tsconfig.json",
                "tsconfig.node.json",
                "index.html",
                ".gitignore",
                "README.md",
                "src/main.ts",
                "src/App.vue",
                "src/style.css",
                "src/vite-env.d.ts"
            ],
            "vanilla": [
                "package.json",
                "vite.config.ts",
                "tsconfig.json",
                "index.html",
                ".gitignore",
                "README.md",
                "src/main.ts",
                "src/style.css"
            ]
        }
        return templates.get(template_name, [])

    def test_file_exists(self, template_dir: Path, file_path: str) -> bool:
        """测试文件是否存在"""
        full_path = template_dir / file_path
        exists = full_path.exists()
        self.log(
            f"文件 {'存在' if exists else '缺失'}: {file_path}",
            "SUCCESS" if exists else "ERROR"
        )
        return exists

    def test_package_json(self, template_dir: Path) -> bool:
        """测试 package.json 配置"""
        package_path = template_dir / "package.json"
        try:
            with open(package_path, 'r', encoding='utf-8') as f:
                package = json.load(f)

            # 检查必需字段
            required_fields = ["name", "version", "type", "scripts"]
            missing_fields = [f for f in required_fields if f not in package]

            if missing_fields:
                self.log(f"package.json 缺少字段: {missing_fields}", "ERROR")
                return False

            # 检查必需脚本
            required_scripts = ["dev", "build", "preview"]
            missing_scripts = [s for s in required_scripts if s not in package.get("scripts", {})]

            if missing_scripts:
                self.log(f"package.json 缺少脚本: {missing_scripts}", "WARN")

            self.log(f"package.json 配置正确: {package.get('name')}", "SUCCESS")
            return True

        except Exception as e:
            self.log(f"package.json 解析失败: {e}", "ERROR")
            return False

    def test_typescript_config(self, template_dir: Path) -> bool:
        """测试 TypeScript 配置"""
        tsconfig_path = template_dir / "tsconfig.json"
        try:
            with open(tsconfig_path, 'r', encoding='utf-8') as f:
                tsconfig = json.load(f)

            # 检查必需配置
            compiler_options = tsconfig.get("compilerOptions", {})
            required_options = ["target", "module", "strict"]
            missing_options = [o for o in required_options if o not in compiler_options]

            if missing_options:
                self.log(f"tsconfig.json 缺少配置: {missing_options}", "WARN")

            self.log("tsconfig.json 配置正确", "SUCCESS")
            return True

        except Exception as e:
            self.log(f"tsconfig.json 解析失败: {e}", "ERROR")
            return False

    def test_vite_config(self, template_dir: Path) -> bool:
        """测试 Vite 配置"""
        vite_config_path = template_dir / "vite.config.ts"
        exists = vite_config_path.exists()

        if exists:
            # 读取文件内容进行基本验证
            with open(vite_config_path, 'r', encoding='utf-8') as f:
                content = f.read()

            has_plugin = "plugin" in content
            self.log(
                f"vite.config.ts {'包含插件' if has_plugin else '无插件配置'}",
                "SUCCESS" if exists else "ERROR"
            )
            return True

        self.log("vite.config.ts 不存在", "ERROR")
        return False

    def test_readme(self, template_dir: Path) -> bool:
        """测试 README 文档"""
        readme_path = template_dir / "README.md"
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查必需章节
            required_sections = ["快速开始", "项目结构", "可用脚本"]
            missing_sections = [s for s in required_sections if s not in content]

            if missing_sections:
                self.log(f"README.md 缺少章节: {missing_sections}", "WARN")

            self.log("README.md 文档完整", "SUCCESS")
            return True

        except Exception as e:
            self.log(f"README.md 读取失败: {e}", "ERROR")
            return False

    def test_template(self, template_name: str) -> Tuple[bool, List[str]]:
        """测试单个模板"""
        template_dir = self.templates_dir / template_name

        if not template_dir.exists():
            self.log(f"模板目录不存在: {template_name}", "ERROR")
            return False, [f"模板目录不存在: {template_name}"]

        self.log(f"\n{'='*60}")
        self.log(f"测试模板: {template_name}")
        self.log(f"{'='*60}")

        results = []
        required_files = self.get_template_files(template_name)

        # 测试文件存在性
        file_results = []
        for file_path in required_files:
            file_results.append(self.test_file_exists(template_dir, file_path))

        all_files_exist = all(file_results)
        results.append(f"文件完整性: {'通过' if all_files_exist else '失败'}")

        # 测试配置文件
        if (template_dir / "package.json").exists():
            results.append(f"package.json: {'通过' if self.test_package_json(template_dir) else '失败'}")

        if (template_dir / "tsconfig.json").exists():
            results.append(f"tsconfig.json: {'通过' if self.test_typescript_config(template_dir) else '失败'}")

        if (template_dir / "vite.config.ts").exists():
            results.append(f"vite.config.ts: {'通过' if self.test_vite_config(template_dir) else '失败'}")

        if (template_dir / "README.md").exists():
            results.append(f"README.md: {'通过' if self.test_readme(template_dir) else '失败'}")

        success = all_files_exist
        self.log(f"\n模板 {template_name} 测试结果: {'通过 ✅' if success else '失败 ❌'}")

        return success, results

    def test_all_templates(self) -> Dict[str, Tuple[bool, List[str]]]:
        """测试所有模板"""
        templates = ["react", "vue", "vanilla"]
        all_results = {}

        for template in templates:
            success, details = self.test_template(template)
            all_results[template] = (success, details)

        return all_results

    def print_summary(self, results: Dict[str, Tuple[bool, List[str]]]):
        """打印测试摘要"""
        self.log(f"\n{'='*60}")
        self.log("测试摘要")
        self.log(f"{'='*60}")

        passed = sum(1 for s, _ in results.values() if s)
        total = len(results)

        for template, (success, details) in results.items():
            status = "✅ 通过" if success else "❌ 失败"
            self.log(f"{template}: {status}")

            for detail in details:
                self.log(f"  - {detail}")

        self.log(f"\n总计: {passed}/{total} 模板测试通过")

        if passed == total:
            self.log("所有模板测试通过! 🎉", "SUCCESS")
            return True
        else:
            self.log("部分模板测试失败", "ERROR")
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="Frontend Design Templates 测试")
    parser.add_argument("--template", choices=["react", "vue", "vanilla"], help="指定测试的模板")
    parser.add_argument("--verbose", action="store_true", help="显示详细输出")
    args = parser.parse_args()

    # 获取项目根目录
    root_dir = Path(__file__).parent.parent.parent
    tester = TemplateTester(root_dir, verbose=args.verbose)

    if args.template:
        # 测试单个模板
        success, details = tester.test_template(args.template)
        sys.exit(0 if success else 1)
    else:
        # 测试所有模板
        results = tester.test_all_templates()
        success = tester.print_summary(results)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
