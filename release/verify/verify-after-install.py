#!/usr/bin/env python3
"""
Frontend Design Agent Skills - 安装后验证脚本

验证技能包已正确安装并符合 Agent Skills 规范。
"""

import os
import sys
from pathlib import Path


def verify_installation():
    """验证安装"""
    print("=" * 70)
    print("Frontend Design Agent Skills - 安装验证")
    print("=" * 70)
    print()

    # 获取当前目录（技能包根目录）
    skill_path = Path.cwd()

    # 检查必需文件
    required_files = ["SKILL.md"]
    missing_files = []

    print("必需文件检查:")
    for filename in required_files:
        file_path = skill_path / filename
        if file_path.exists():
            print(f"  ✅ {filename} 存在")
        else:
            print(f"  ❌ {filename} 不存在")
            missing_files.append(filename)

    print()

    # 检查可选文件
    optional_files = [
        "LICENSE",
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md"
    ]

    print("可选文件检查:")
    for filename in optional_files:
        file_path = skill_path / filename
        if file_path.exists():
            print(f"  ✅ {filename}")
        else:
            print(f"  ⚠️  {filename} 不存在（可选）")

    print()

    # 检查目录
    optional_dirs = ["scripts", "references", "templates", "assets"]

    print("可选目录检查:")
    for dirname in optional_dirs:
        dir_path = skill_path / dirname
        if dir_path.exists() and dir_path.is_dir():
            print(f"  ✅ {dirname}/")
        else:
            print(f"  ⚠️  {dirname}/ 不存在（可选）")

    print()

    # 检查不应存在的内容
    print("排除内容检查:")
    exclude_items = ["docs", "tests", "release-packages"]

    clean = True
    for item_name in exclude_items:
        item_path = skill_path / item_name
        if item_path.exists():
            print(f"  ❌ {item_name} 不应存在于发布包中")
            clean = False
        else:
            print(f"  ✅ {item_name} 不存在（正确）")

    print()
    print("=" * 70)

    if missing_files:
        print("❌ 验证失败 - 缺少必需文件")
        return False

    if not clean:
        print("❌ 验证失败 - 发布包包含不应存在的内容")
        return False

    print("✅ 验证通过 - 技能包安装正确")
    print("=" * 70)
    return True


if __name__ == "__main__":
    success = verify_installation()
    sys.exit(0 if success else 1)
