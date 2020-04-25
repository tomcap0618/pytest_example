import pytest

from pytest_example.mult import *


def test_mult():
    value = mult(1, 5)
    assert value == 5
