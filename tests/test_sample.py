import pytest
import sys

@pytest.mark.parametrize("text,expected", [
    ("hello", "HELLO"),
    ("bye", "BYE")
])

def test_string(text,expected):
    assert text.upper() == expected

@pytest.mark.parametrize("a,b,expected", [
    (2,2,4),
    (3,3,6)
])

def test_addition(a,b,expected):
    assert a + b == expected

@pytest.mark.skipif(sys.platform == "linux", reason="Skipping on linux")
def test_skip_example():
    return True

@pytest.mark.xfail(reason="Known bug in feature")
def test_expected_failure():
    assert 2 + 2 == 5