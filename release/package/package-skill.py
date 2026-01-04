#!/usr/bin/env python3
"""
Frontend Design Agent Skills - 自动打包脚本

自动创建符合 Agent Skills 规范的发布包。
"""

import os
import sys
import json
import tarfile
import zipfile
from pathlib import Path
from datetime import datetime


def load_config(config_path: Path) -> dict:
    """加载打包配置"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def should_exclude(file_path: Path, exclude_patterns: list) -> bool:
    """检查文件是否应该被排除"""
    # 转换为相对路径用于检查
    path_str = str(file_path)

    for pattern in exclude_patterns:
        # 检查路径的任何部分
        if pattern in file_path.parts:
            return True
        # 检查文件名模式
        if pattern.startswith('*') and file_path.name.endswith(pattern.lstrip('*')):
            return True
        # 精确匹配
        if file_path.name == pattern or file_path.suffix == pattern:
            return True

    return False


def create_tar_package(source_dir: Path, output_path: Path,
                       config: dict) -> None:
    """创建 tar.gz 包"""
    exclude_patterns = config['exclude_patterns']
    skill_name = config['skill_name']

    with tarfile.open(output_path, "w:gz") as tarf:
        for item in source_dir.rglob("*"):
            if item.is_file() and not should_exclude(item.relative_to(source_dir), exclude_patterns):
                arcname = f"{skill_name}/{item.relative_to(source_dir)}"
                tarf.add(item, arcname)

    print(f"✅ 创建 TAR.GZ 包: {output_path}")


def create_zip_package(source_dir: Path, output_path: Path,
                       config: dict) -> None:
    """创建 zip 包"""
    exclude_patterns = config['exclude_patterns']
    skill_name = config['skill_name']

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in source_dir.rglob("*"):
            if item.is_file() and not should_exclude(item.relative_to(source_dir), exclude_patterns):
                arcname = f"{skill_name}/{item.relative_to(source_dir)}"
                zipf.write(item, arcname)

    print(f"✅ 创建 ZIP 包: {output_path}")


def main():
    """主函数"""
    # 路径配置
    script_dir = Path(__file__).parent.resolve()
    config_path = script_dir / "package-config.json"
    output_dir = script_dir.parent / "output"

    # 技能包源目录
    skill_dir = script_dir.parent.parent / "frontend-design"

    # 检查配置文件
    if not config_path.exists():
        print(f"❌ 配置文件不存在: {config_path}")
        sys.exit(1)

    # 检查技能包目录
    if not skill_dir.exists():
        print(f"❌ 技能包目录不存在: {skill_dir}")
        sys.exit(1)

    # 加载配置
    config = load_config(config_path)

    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)

    # 版本信息
    version = config.get('skill_version', 'latest')

    print("=" * 70)
    print("Frontend Design Agent Skills - 打包工具")
    print("=" * 70)
    print(f"技能包: {config['skill_name']}")
    print(f"版本: {version}")
    print(f"源目录: {skill_dir}")
    print(f"输出目录: {output_dir}")
    print()

    # 创建发布包
    tar_name = f"{config['skill_name']}-{version}.tar.gz"
    zip_name = f"{config['skill_name']}-{version}.zip"

    tar_path = output_dir / tar_name
    zip_path = output_dir / zip_name

    create_tar_package(skill_dir, tar_path, config)
    create_zip_package(skill_dir, zip_path, config)

    print()
    print("=" * 70)
    print("✅ 打包完成!")
    print(f"📦 TAR.GZ: {tar_path} ({tar_path.stat().st_size:,} bytes)")
    print(f"📦 ZIP: {zip_path} ({zip_path.stat().st_size:,} bytes)")
    print()
    print("下一步: 运行验证脚本")
    print(f"  cd ../verify && python verify-before-release.py")
    print("=" * 70)


if __name__ == "__main__":
    main()
