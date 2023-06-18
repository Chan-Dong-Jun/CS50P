# Sunday, 28/05/2023
# CS50P Week 7

from working import convert
import pytest

def test_nonsensensical_input():
    with pytest.raises(ValueError):
        convert("cat")

def test_range():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")

def test_correct_output():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"