"""This module will have functions to get the stock prices
"""
from stock_market.library.external.alphavantage import AlphaVantage

def get_bse_stock_price(symbol):
    """This function will get the stock price

    Raises WrongSymbolException if the symbol is wrong
    """
    alpha_api = AlphaVantage()
    price = alpha_api.get_current_stock_price(symbol=f"{symbol}.BSE")
    return price
    