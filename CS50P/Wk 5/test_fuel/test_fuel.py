import pytest
from fuel import convert, gauge

def test_incorrect_int():
    assert convert("3/4") == 75
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_val_err():
    with pytest.raises(ValueError):
        convert("three/four")