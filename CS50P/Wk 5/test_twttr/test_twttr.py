# 20/05/2023
# CS50P Week 5

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"

def test_vowel():
    assert shorten("aeiou") == ""

def test_upper_vowel():
    assert shorten("AEIOU") == ""

def test_punctuation():
    assert shorten("!.,") == "!.,"

def test_upper():
    assert shorten("HELLO") == "HLL"

def test_number():
    assert shorten("123") == "123"