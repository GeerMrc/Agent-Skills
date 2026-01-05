#!/usr/bin/env python3
"""
模板构建测试脚本

测试所有项目模板的构建流程：
1. npm install
2. npm run build
"""

import os
import subprocess
import sys
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "frontend-design" / "templates"

# 模板列表
TEMPLATES = [
    {"name": "React", "path": TEMPLATES_DIR / "react"},
    {"name": "Vue", "path": TEMPLATES_DIR / "vue"},
    {"name": "Vanilla", "path": TEMPLATES_DIR / "vanilla"},
]

def run_command(cmd, cwd):
    """运行命令并返回结果"""
    print(f"  运行: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=300  # 5分钟超时
    )
    return result

def test_template(template):
    """测试单个模板的构建"""
    name = template["name"]
    path = template["path"]

    print(f"\n{'='*60}")
    print(f"测试模板: {name}")
    print(f"路径: {path}")
    print(f"{'='*60}")

    # 检查模板目录是否存在
    if not path.exists():
        print(f"  ❌ 模板目录不存在: {path}")
        return False

    # 检查 package.json 是否存在
    package_json = path / "package.json"
    if not package_json.exists():
        print(f"  ❌ package.json 不存在")
        return False

    # 测试 npm install
    print("\n1️⃣  测试 npm install...")
    result = run_command(["npm", "install"], path)
    if result.returncode != 0:
        print(f"  ❌ npm install 失败")
        print(f"  错误: {result.stderr}")
        return False
    print(f"  ✅ npm install 成功")

    # 测试 npm run build
    print("\n2️⃣  测试 npm run build...")
    result = run_command(["npm", "run", "build"], path)
    if result.returncode != 0:
        print(f"  ❌ npm run build 失败")
        print(f"  错误: {result.stderr}")
        return False
    print(f"  ✅ npm run build 成功")

    print(f"\n  ✅ {name} 模板构建测试通过")
    return True

def main():
    """主函数"""
    print("模板构建测试")
    print("="*60)

    results = []
    for template in TEMPLATES:
        success = test_template(template)
        results.append({
            "name": template["name"],
            "success": success
        })

    # 打印测试结果摘要
    print("\n" + "="*60)
    print("测试结果摘要")
    print("="*60)

    for result in results:
        status = "✅ 通过" if result["success"] else "❌ 失败"
        print(f"  {result['name']}: {status}")

    # 检查是否所有测试都通过
    all_passed = all(r["success"] for r in results)
    if all_passed:
        print("\n✅ 所有模板构建测试通过")
        return 0
    else:
        print("\n❌ 部分模板构建测试失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
