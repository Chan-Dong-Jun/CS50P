#01/06/2023
#CS50P Week 8

import pytest

from seasons import convert_mins

def test_nonsensical_output():
    with pytest.raises(SystemExit):
        convert_mins(1999-1-1)
