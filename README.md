# Python Example PEP

一个遵循 PEP 517/518/621 标准的现代 Python 项目示例。

## 特性

- ✅ 遵循 PEP 517/518/621 标准
- ✅ 使用 `pyproject.toml` 管理项目元数据和构建配置
- ✅ 使用 `python -m build` 进行构建（不依赖 setup.py）
- ✅ 使用 `twine` 发布到 PyPI 私库
- ✅ 多模块项目结构（utils, validators, calculator, logger, example）
- ✅ 完整的单元测试覆盖（覆盖率要求 ≥80%）
- ✅ 包含 GitHub Actions 和 GitLab CI 配置

## 项目结构

```
python-example-pep/
├── src/
│   └── python_example_pep/     # 主包
│       ├── __init__.py
│       ├── example/             # 示例模块（独立目录）
│       │   ├── __init__.py
│       │   └── example.py
│       ├── utils/               # 工具函数模块（独立目录）
│       │   ├── __init__.py
│       │   └── utils.py
│       ├── validators/           # 数据验证模块（独立目录）
│       │   ├── __init__.py
│       │   └── validators.py
│       ├── calculator/           # 计算器模块（独立目录）
│       │   ├── __init__.py
│       │   └── calculator.py
│       └── logger/               # 日志记录模块（独立目录）
│           ├── __init__.py
│           └── logger.py
├── tests/                       # 测试目录
│   ├── __init__.py
│   ├── test_example.py
│   ├── test_utils.py
│   ├── test_validators.py
│   ├── test_calculator.py
│   └── test_logger.py
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── .gitlab-ci.yml              # GitLab CI/CD 配置
├── pyproject.toml              # PEP 621 项目元数据和构建配置
├── README.md
├── USAGE.md                    # 使用示例文档
├── .gitignore
├── .pypirc.example             # PyPI 配置示例
├── Makefile                    # 便捷命令
└── verify_build.py             # 构建验证脚本
```

## 模块说明

### example - 示例模块
提供基础的示例函数，包括问候语和简单计算。

### utils - 工具函数模块
提供文件路径处理、目录管理等实用工具函数。

### validators - 数据验证模块
提供邮箱、手机号、URL、字符串长度、数值范围等验证功能。

### calculator - 计算器模块
提供完整的计算器类，支持加减乘除、幂运算，并记录计算历史。

### logger - 日志记录模块
提供灵活的日志记录功能，支持控制台和文件输出，可配置日志级别。

## 安装

### 从源代码安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/python-example-pep.git
cd python-example-pep

# 安装开发依赖
pip install -e ".[dev]"
```

## 开发

### 运行测试

```bash
# 运行所有测试
pytest

# 运行测试并显示覆盖率
pytest --cov=src --cov-report=term-missing

# 生成 HTML 覆盖率报告
pytest --cov=src --cov-report=html
# 然后在浏览器中打开 htmlcov/index.html
```

### 测试覆盖率

项目要求测试覆盖率 ≥80%。运行测试时会自动检查覆盖率：

```bash
pytest
```

如果覆盖率低于 80%，测试将失败。查看详细覆盖率报告：

```bash
# 终端报告
pytest --cov=src --cov-report=term-missing

# HTML 报告
pytest --cov=src --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### 代码格式化

```bash
black src tests
```

### 代码检查

```bash
ruff check src tests
mypy src
```

## 构建

使用 PEP 517 兼容的构建工具（**不使用 setup.py**）：

```bash
# 安装构建工具
pip install build

# 构建分发包（符合 PEP 517 标准）
python -m build
```

构建完成后，会在 `dist/` 目录下生成：
- `*.whl` (wheel 文件)
- `*.tar.gz` (源码分发包)

### 验证构建

运行验证脚本确保一切正常：

```bash
python verify_build.py
```

或使用 Makefile：

```bash
make build
```

## 发布到 PyPI 私库

使用 `twine` 上传到 PyPI 私库（元数据来自 PEP 621 的 `pyproject.toml`）：

```bash
# 安装 twine
pip install twine

# 方法 1: 直接指定仓库 URL
twine upload --repository-url https://your-private-pypi.com/simple/ dist/*
```

### 配置 PyPI 私库

方法 2: 配置 `~/.pypirc` 文件（复制 `.pypirc.example` 并修改）：

```ini
[distutils]
index-servers =
    private

[private]
repository = https://your-private-pypi.com/simple/
username = your_username
password = your_password
```

然后使用：

```bash
twine upload --repository private dist/*
```

或使用 Makefile：

```bash
make upload
```

### 环境变量方式

方法 3: 使用环境变量（推荐用于 CI/CD）：

```bash
export TWINE_USERNAME=your_username
export TWINE_PASSWORD=your_password
export TWINE_REPOSITORY_URL=https://your-private-pypi.com/simple/
twine upload dist/*
```

## CI/CD

### GitHub Actions

项目包含 GitHub Actions 工作流配置（`.github/workflows/ci.yml`），支持：
- 多 Python 版本测试（3.8-3.12）
- 多操作系统测试（Ubuntu, Windows, macOS）
- 自动构建分发包
- 自动发布到 PyPI 私库（可选）

### GitLab CI

项目包含 GitLab CI 配置（`.gitlab-ci.yml`），包含以下阶段：

1. **测试阶段** (`test`)
   - 多 Python 版本测试（3.8-3.12）
   - 代码覆盖率检查（要求 ≥80%）
   - 代码质量检查（ruff, mypy, black）

2. **构建阶段** (`build`)
   - 使用 `python -m build` 构建分发包
   - 生成 wheel 和源码分发包

3. **部署阶段** (`deploy`)
   - 手动触发发布到 PyPI 私库
   - 使用 `twine upload` 上传

#### GitLab CI 环境变量配置

在 GitLab 项目设置中配置以下 CI/CD 变量：

- `PYPI_REPOSITORY_URL`: PyPI 私库 URL（例如：`https://your-private-pypi.com/simple/`）
- `PYPI_USERNAME`: PyPI 用户名
- `PYPI_PASSWORD`: PyPI 密码或 token

配置路径：GitLab 项目 → Settings → CI/CD → Variables

## 许可证

MIT License

## 参考

- [PEP 517](https://peps.python.org/pep-0517/) - 构建系统接口
- [PEP 518](https://peps.python.org/pep-0518/) - 指定构建依赖
- [PEP 621](https://peps.python.org/pep-0621/) - 项目元数据标准

