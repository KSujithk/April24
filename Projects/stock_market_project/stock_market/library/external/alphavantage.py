"""This module will have helper classes and functions to
get the responses from alphavantage
"""

import requests
import urllib
from stock_market.library.exceptions import WrongSymbolException


class AlphaVantage:
    """This class will have methods to fetch the stock prices"""

    API_URL = "https://www.alphavantage.co/query"

    FUNCTIONS = {"Daily": "TIME_SERIES_DAILY"}

    def __init__(self):
        # hardcoding
        self.api_key = "METMGY420KVPIXX3"

    def construct_alphavantage_url(self, symbol, function="TIME_SERIES_INTRADAY"):
        """This method constructs an url"""
        base_url = AlphaVantage.API_URL
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
        }
        url = base_url + "?" + urllib.parse.urlencode(params)
        return url

    def _get_last_stock_session_price(self, response):
        """This method gives the stock price of last trading session"""
        stock_history = response["Time Series (Daily)"]
        last_trading_date = list(stock_history.keys())[0]
        return float(stock_history[last_trading_date]["4. close"])

    def get_current_stock_price(self, symbol):
        """This function will get daily stock value
        of the symbol passed

        Returns:
          Close price of the last trading session

        Raises:
          WrongSymbolException: in the case of invalid symbol
        """
        endpoint_url = self.construct_alphavantage_url(symbol)
        # f"{AlphaVantage.API_URL}?function={AlphaVantage.FUNCTIONS['Daily']}&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(endpoint_url, timeout=15)
        # if the status is okay
        if response.status_code == 200:
            result = response.json()
            if "Error Message" in result:
                raise WrongSymbolException(symbol)

            return self._get_last_stock_session_price(result)
        return None
