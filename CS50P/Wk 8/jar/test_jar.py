#01/06/2023
#CS50P Week 8
import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(10)
    assert jar.size == 2
