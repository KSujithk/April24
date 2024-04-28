"""This module will have Bank Account
"""

class BankAccount:
    """
    This class will have basic Bank Account Functionality
    """
    def __init__(self, account_number:str,name:str, initial_deposit:float = 0) -> None:
        """
        This method initializes the object with initial values
        """
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def withdraw(self, amount):
        """
        This method withdraw amount
        """
        self.balance -= amount

    def deposit(self, amount):
        """
        This method deposits amount
        """
        self.balance += amount
