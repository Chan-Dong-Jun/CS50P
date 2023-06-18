from project import check_input, define_word, parser
import pytest

def test_check_input():
    with pytest.raises(SystemExit):
        check_input(["project.py"])

def test_define_word():
    with pytest.raises(TypeError):
        define_word()
    assert define_word("") == None
    define_word("happy")

def test_parser():
    with pytest.raises(TypeError):
        parser("1234")
    with pytest.raises(IndexError):
        parser([])
    with pytest.raises(KeyError):
        parser({})