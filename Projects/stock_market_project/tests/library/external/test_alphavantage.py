"""This module tests the alphavantage external api
"""
from stock_market.library.external.alphavantage import AlphaVantage
from stock_market.library.exceptions import WrongSymbolException
import pytest

def test_positive_case():
    """This test case will test the positive i.e. valid symbols
    """
    alpha_api = AlphaVantage()
    data = alpha_api.get_current_stock_price(symbol='TATAMOTORS.BSE')
    assert data is not None
    assert data > 0

def test_negative_case():
    """This test case will test the negative scenario which is 
    wrong symbol
    """
    alpha_api = AlphaVantage()
    with pytest.raises(WrongSymbolException):
        alpha_api.get_current_stock_price(symbol='Xyyyyyyyyyy')
