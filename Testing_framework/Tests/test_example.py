import pytest

def somma(a, b):
    return a + b

def test_somma(test_env):
    assert somma(2, 3) == 5