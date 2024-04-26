"""This tests the leap year
"""
from workshop.leapyear import is_leap_year, leap_years

def test_is_leap_year():
    """This functions tests the leap year functionality
    """
    assert is_leap_year(2000)
    assert is_leap_year(1996)
    assert not is_leap_year(2100)
    assert not is_leap_year(1997)


def test_leap_years():
    """ This function tests the leap years
    """
    result = leap_years(1996,2005)
    assert len(result) == 3
    assert result == [1996, 2000, 2004]