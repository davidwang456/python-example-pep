#!/usr/bin/env python3
"""验证项目构建配置的脚本。"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """运行命令并处理错误。"""
    print(f"\n{'='*60}")
    print(f"正在执行: {description}")
    print(f"命令: {cmd}")
    print(f"{'='*60}\n")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ 错误: {description}")
        print(result.stderr)
        return False
    else:
        print(f"✅ 成功: {description}")
        if result.stdout:
            print(result.stdout)
        return True


def main():
    """主函数。"""
    print("开始验证项目构建配置...")
    
    # 检查必要文件
    required_files = [
        "pyproject.toml",
        "README.md",
        "src/python_example_pep/__init__.py",
        "src/python_example_pep/example.py",
    ]
    
    print("\n检查必要文件...")
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} 不存在")
            return 1
    
    # 检查构建工具
    if not run_command("python -m pip show build", "检查 build 工具"):
        print("\n安装 build 工具...")
        if not run_command("python -m pip install build", "安装 build"):
            return 1
    
    # 尝试构建
    if not run_command("python -m build", "构建分发包"):
        return 1
    
    # 检查构建产物
    dist_dir = Path("dist")
    if dist_dir.exists():
        files = list(dist_dir.glob("*"))
        print(f"\n✅ 构建成功！生成的文件:")
        for f in files:
            print(f"   - {f.name}")
    else:
        print("\n❌ dist 目录不存在")
        return 1
    
    print("\n" + "="*60)
    print("✅ 所有验证通过！")
    print("="*60)
    return 0


if __name__ == "__main__":
    sys.exit(main())

