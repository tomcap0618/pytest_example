import pytest

from pytest_example.add import *


def test_add():
    value = add(1, 4)
    assert value == 5
