# 20/05/2023
# CS50P Week 5

from plates import is_valid

def test_start_alpha():
    assert is_valid("123") == False

def test_length():
    assert is_valid("CS500000000") == False

def test_alphanum():
    assert is_valid("PI3.14") == False

def test_zero_placement():
    assert is_valid("CS05") == False

def number_placement():
    assert is_valid("CS9EP") == False
    assert is_valid("CSEP9") == True