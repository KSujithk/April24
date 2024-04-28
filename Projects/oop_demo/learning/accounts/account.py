"""This module will have Bank Account
"""


class BankAccount:
    """
    This class will have basic Bank Account Functionality
    """

    def __init__(
        self, account_number: str, name: str, initial_deposit: float = 0
    ) -> None:
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

    def account_type(self):
        """
        This method will return the account_type

        Returns:
          "Savings" for Savings Account
          "Current" for Current Account
          None for others
        """
        if isinstance(self,SavingsAccount):
            return "Savings"
        elif isinstance(self, CurrentAccount):
            return "Current"
        return None


class SavingsAccount(BankAccount):
    """This class represents the Savings Account Structure"""

    def withdraw(self, amount):
        """
        This method is overriden to implement non negative balances
        """
        if self.balance - amount < 0:
            # dont allow this transaction
            # fail this
            print("This transaction is not allowed")
            return
        return super().withdraw(amount)

    def deposit(self, amount):
        """
        This method stops the user to deposit more than 10 lakhs
        """
        if amount > 1000000:
            print("Not allowed")
            return
        return super().deposit(amount)


class CurrentAccount(BankAccount):
    """This represents the Current Account"""
