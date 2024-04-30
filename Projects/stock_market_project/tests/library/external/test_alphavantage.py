"""This module tests the alphavantage external api
"""
from stock_market.library.external.alphavantage import AlphaVantage

def test_positive_case():
    """This test case will test the positive i.e. valid symbols
    """
    alpha_api = AlphaVantage()
    data = alpha_api.get_daily_stock(symbol='TATAMOTORS.BSE')
    assert data is not None
