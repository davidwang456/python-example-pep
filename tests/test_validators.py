"""数据验证模块的测试。"""

import pytest

from python_example_pep import validators


class TestValidateEmail:
    """测试 validate_email 函数。"""

    def test_valid_emails(self):
        """测试有效的邮箱地址。"""
        valid_emails = [
            "test@example.com",
            "user.name@example.co.uk",
            "user+tag@example.com",
            "user123@test-domain.com",
        ]
        for email in valid_emails:
            assert validators.validate_email(email) is True

    def test_invalid_emails(self):
        """测试无效的邮箱地址。"""
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "user@",
            "user@.com",
            "user@com",
            "",
        ]
        for email in invalid_emails:
            assert validators.validate_email(email) is False


class TestValidatePhone:
    """测试 validate_phone 函数。"""

    def test_valid_phones(self):
        """测试有效的手机号码。"""
        valid_phones = [
            "13800138000",
            "15912345678",
            "18600000000",
            "19912345678",
        ]
        for phone in valid_phones:
            assert validators.validate_phone(phone) is True

    def test_invalid_phones(self):
        """测试无效的手机号码。"""
        invalid_phones = [
            "123456",
            "12345678901",
            "01234567890",
            "1380013800",
            "abc12345678",
            "",
        ]
        for phone in invalid_phones:
            assert validators.validate_phone(phone) is False


class TestValidateUrl:
    """测试 validate_url 函数。"""

    def test_valid_urls(self):
        """测试有效的 URL。"""
        valid_urls = [
            "https://www.example.com",
            "http://example.com",
            "https://subdomain.example.com/path",
            "http://example.com:8080/path?query=1",
        ]
        for url in valid_urls:
            assert validators.validate_url(url) is True

    def test_invalid_urls(self):
        """测试无效的 URL。"""
        invalid_urls = [
            "not-a-url",
            "www.example.com",
            "ftp://example.com",
            "",
        ]
        for url in invalid_urls:
            assert validators.validate_url(url) is False


class TestValidateLength:
    """测试 validate_length 函数。"""

    def test_valid_lengths(self):
        """测试有效的长度。"""
        assert validators.validate_length("hello", min_length=3, max_length=10) is True
        assert validators.validate_length("hi", min_length=2) is True
        assert validators.validate_length("test", max_length=10) is True

    def test_invalid_lengths(self):
        """测试无效的长度。"""
        assert validators.validate_length("hi", min_length=3) is False
        assert validators.validate_length("very long text", max_length=5) is False

    def test_edge_cases(self):
        """测试边界情况。"""
        assert validators.validate_length("", min_length=0) is True
        assert validators.validate_length("", min_length=1) is False

    def test_invalid_parameters(self):
        """测试无效参数。"""
        with pytest.raises(ValueError):
            validators.validate_length("test", min_length=-1)

        with pytest.raises(ValueError):
            validators.validate_length("test", min_length=10, max_length=5)


class TestValidateRange:
    """测试 validate_range 函数。"""

    def test_valid_ranges(self):
        """测试有效的范围。"""
        assert validators.validate_range(5.0, 0.0, 10.0) is True
        assert validators.validate_range(0.0, 0.0, 10.0) is True
        assert validators.validate_range(10.0, 0.0, 10.0) is True

    def test_invalid_ranges(self):
        """测试无效的范围。"""
        assert validators.validate_range(15.0, 0.0, 10.0) is False
        assert validators.validate_range(-1.0, 0.0, 10.0) is False

    def test_invalid_parameters(self):
        """测试无效参数。"""
        with pytest.raises(ValueError):
            validators.validate_range(5.0, 10.0, 0.0)

