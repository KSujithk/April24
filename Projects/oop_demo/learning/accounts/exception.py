"""This module defines exceptions for Accounts
"""


class NegativeBalanceException(Exception):
    """
    This exception will be raised when the user
    has a negative balance
    """


class HighDepositException(Exception):
    """
    This exception represents high deposits
    """
