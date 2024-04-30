"""This module will have helper classes and functions to
get the responses from alphavantage
"""

import requests


class AlphaVantage:
    """This class will have methods to fetch the stock prices"""

    API_URL = "https://www.alphavantage.co/query"

    FUNCTIONS = {"Daily": "TIME_SERIES_DAILY"}

    def __init__(self):
        # hardcoding
        self.api_key = "LWEQTRKW8PJ0O1NQ"

    def _get_last_stock_session_price(self, response):
        """This method gives the stock price of last trading session
        """
        stock_history = response['Time Series (Daily)']
        last_trading_date = list(stock_history.keys())[0]
        return last_trading_date["4. close"]



    def get_daily_stock(self, symbol):
        """This function will get daily stock value
        of the symbol passed

        Returns:
          Close price of the last trading session
        """
        endpoint_url = f"{AlphaVantage.API_URL}?function={AlphaVantage.FUNCTIONS['Daily']}&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(endpoint_url, timeout=15)
        # if the status is okay
        if response.status_code == 200:
            return self._get_last_stock_session_price(response.json())
        return None
