# Sunday, 28/05/2023
# CS50P Week 7

from um import count

def test_correct_input():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
