"""
This test cases will be arround bank account
"""
from learning.accounts.account import BankAccount

def test_bankaccount_basics():
    """
    This method checks the 
        account creation
        depositing the amount 
        withdrawing the amount
    """
    account_my = BankAccount(
        account_number="x12345",
        name="LT",
        initial_deposit=10000)
    # checking if the balance is same as initial deposit
    assert account_my.balance == 10000
    # deposit 1000 more and check blance
    account_my.deposit(1000)
    assert account_my.balance == 11000

    # withdraw 5000 and check balance
    account_my.withdraw(5000)
    assert account_my.balance == 6000
