"""Tests for the calculator module."""

import pytest

from calculator import add, divide, multiply, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    # 这个测试目前会失败——divide() 还没有处理除零情况。
    # 这就是我们要在 Issue #1 里修复的 bug。
    with pytest.raises(ValueError):
        divide(1, 0)
