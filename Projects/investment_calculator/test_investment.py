"""This module will have tests

"""
from calculators.lumpsum import returns as lumpsum_returns
from calculators.sip import returns as sip_returns

def test_lumpsum():
    """This function tests lumpsum
    """
    assert(lumpsum_returns(1000, 0, 15) == 1000)


def test_sip():
    """This function tests sip
    """
    assert(sip_returns(1000, 0, 2) == 24000)
