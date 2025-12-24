# 使用示例

本文档展示如何使用项目的各个模块。

> **注意**: 本项目采用多目录模块结构，每个模块位于独立的目录中。

## 示例模块 (example)

```python
from python_example_pep import example

# 问候语
print(example.hello())  # Hello, World!
print(example.hello("Python"))  # Hello, Python!

# 简单计算
result = example.add(2, 3)
print(result)  # 5
```

## 工具函数模块 (utils)

```python
from python_example_pep import utils
from pathlib import Path

# 确保目录存在
dir_path = utils.ensure_dir("./logs/app")
print(dir_path)  # Path 对象

# 获取文件大小
try:
    size = utils.get_file_size("README.md")
    print(f"文件大小: {size} 字节")
except FileNotFoundError:
    print("文件不存在")

# 分割路径
parts = utils.split_path("/usr/local/bin")
print(parts)  # ['usr', 'local', 'bin']

# 规范化路径
normalized = utils.normalize_path("./src")
print(normalized)  # 绝对路径

# 连接路径
joined = utils.join_paths("usr", "local", "bin")
print(joined)  # 'usr/local/bin'
```

## 数据验证模块 (validators)

```python
from python_example_pep import validators

# 验证邮箱
if validators.validate_email("user@example.com"):
    print("邮箱格式正确")

# 验证手机号
if validators.validate_phone("13800138000"):
    print("手机号格式正确")

# 验证 URL
if validators.validate_url("https://www.example.com"):
    print("URL 格式正确")

# 验证字符串长度
if validators.validate_length("hello", min_length=3, max_length=10):
    print("长度符合要求")

# 验证数值范围
if validators.validate_range(5.0, 0.0, 10.0):
    print("数值在范围内")
```

## 计算器模块 (calculator)

```python
from python_example_pep import calculator

# 使用计算器类
calc = calculator.Calculator()

# 基本运算
result1 = calc.add(2, 3)  # 5
result2 = calc.subtract(5, 3)  # 2
result3 = calc.multiply(2, 3)  # 6
result4 = calc.divide(6, 2)  # 3.0
result5 = calc.power(2, 3)  # 8

# 查看计算历史
history = calc.get_history()
for entry in history:
    print(entry)

# 清空历史
calc.clear_history()

# 使用工具函数
numbers = [1, 2, 3, 4, 5]
total = calculator.calculate_sum(numbers)  # 15
average = calculator.calculate_average(numbers)  # 3.0
```

## 日志记录模块 (logger)

```python
from python_example_pep import logger

# 创建日志记录器
log = logger.Logger("my_app", level=logger.LogLevel.INFO)

# 记录不同级别的日志
log.debug("这是调试信息")
log.info("这是信息")
log.warning("这是警告")
log.error("这是错误")
log.critical("这是严重错误")

# 更改日志级别
log.set_level(logger.LogLevel.DEBUG)

# 使用文件日志
file_logger = logger.Logger(
    "file_app",
    level=logger.LogLevel.INFO,
    log_file="./logs/app.log"
)
file_logger.info("这条日志会写入文件")

# 使用便捷函数
app_logger = logger.get_logger("app", level=logger.LogLevel.DEBUG)
app_logger.info("应用启动")
```

## 完整示例

```python
from python_example_pep import calculator, logger, validators

# 创建日志记录器
log = logger.get_logger("calculator_app")

# 验证输入
user_email = "user@example.com"
if not validators.validate_email(user_email):
    log.error(f"无效的邮箱: {user_email}")
    exit(1)

log.info(f"用户邮箱验证通过: {user_email}")

# 使用计算器
calc = calculator.Calculator()
try:
    result = calc.divide(10, 2)
    log.info(f"计算结果: {result}")
except ZeroDivisionError:
    log.error("除数不能为 0")

# 显示计算历史
log.info("计算历史:")
for entry in calc.get_history():
    log.info(f"  {entry}")
```

