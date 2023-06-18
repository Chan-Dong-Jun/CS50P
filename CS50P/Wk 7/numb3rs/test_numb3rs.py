# Saturday, 27/05/2023
# CS50P Week 7

from numb3rs import validate

def test_nonnumeric():
    assert validate("cat") == False

def test_valid_ip():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1") == False
    assert validate("1") == False

def test_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.1.1.1") == True