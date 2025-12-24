#!/usr/bin/env python3
"""Script to verify project build configuration."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run command and handle errors."""
    print(f"\n{'='*60}")
    print(f"Executing: {description}")
    print(f"Command: {cmd}")
    print(f"{'='*60}\n")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Error: {description}")
        print(result.stderr)
        return False
    else:
        print(f"✅ Success: {description}")
        if result.stdout:
            print(result.stdout)
        return True


def main():
    """Main function."""
    print("Starting project build configuration verification...")
    
    # Check required files
    required_files = [
        "pyproject.toml",
        "README.md",
        "src/python_example_pep/__init__.py",
        "src/python_example_pep/example/example.py",
    ]
    
    print("\nChecking required files...")
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} does not exist")
            return 1
    
    # Check build tool
    if not run_command("python -m pip show build", "Check build tool"):
        print("\nInstalling build tool...")
        if not run_command("python -m pip install build", "Install build"):
            return 1
    
    # Try to build
    if not run_command("python -m build", "Build distribution package"):
        return 1
    
    # Check build artifacts
    dist_dir = Path("dist")
    if dist_dir.exists():
        files = list(dist_dir.glob("*"))
        print(f"\n✅ Build successful! Generated files:")
        for f in files:
            print(f"   - {f.name}")
    else:
        print("\n❌ dist directory does not exist")
        return 1
    
    print("\n" + "="*60)
    print("✅ All verifications passed!")
    print("="*60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
