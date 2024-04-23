"""This module will have tests

"""
from calculators.lumpsum import lumpsum

def test_lumpsum():
    """This function tests lumpsum
    """
    assert(lumpsum(1000, 0, 15) == 1000)