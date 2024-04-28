"""
This test cases will be arround bank account
"""

from learning.accounts.account import BankAccount, SavingsAccount, CurrentAccount
from learning.accounts.exception import HighDepositException, NegativeBalanceException
import pytest


def test_bankaccount_basics():
    """
    This method checks the
        account creation
        depositing the amount
        withdrawing the amount
    """
    account_my = BankAccount(account_number="x12345", name="LT", initial_deposit=10000)
    # checking if the balance is same as initial deposit
    assert account_my.balance == 10000
    # deposit 1000 more and check blance
    account_my.deposit(1000)
    assert account_my.balance == 11000

    # withdraw 5000 and check balance
    account_my.withdraw(5000)
    assert account_my.balance == 6000


def test_savings_account():
    """
    This method will test savings account
    """
    my_savings_account = SavingsAccount(
        account_number="x12345", name="LT", initial_deposit=5000
    )
    assert my_savings_account.account_type() == "Savings"
    assert my_savings_account.balance == 5000
    # try withdrawing more than account balance,
    # the balance should not change
    # todo: This operation should result in error
    with pytest.raises(NegativeBalanceException):
        my_savings_account.withdraw(6000)

    assert my_savings_account.balance == 5000

    my_savings_account.deposit(1000)
    assert my_savings_account.balance == 6000
    # now withdraw valid balance,it should be allowed
    my_savings_account.withdraw(6000)
    assert my_savings_account.balance == 0
    with pytest.raises(HighDepositException):
        my_savings_account.deposit(1100000)
    assert my_savings_account.balance == 0


@pytest.mark.parametrize(
    "initial_deposit,account_number,name",
    [
        (10000, "x1234", "LT"),
        (20000, "x1234", "LT"),
        (30000, "x1234", "LT"),
        (40000, "x1234", "LT"),
        (50000, "x1234", "LT"),
    ],
)
def test_current_account(initial_deposit, account_number, name):
    """
    Testing current account
    """
    my_current_account = CurrentAccount(
        account_number=account_number, name=name, initial_deposit=initial_deposit
    )
    # check for the type
    assert my_current_account.account_type() == "Current"
    # withdraw more than deposited amount
    current_balance = my_current_account.balance

    my_current_account.withdraw(current_balance + 10000)

    assert my_current_account.balance == -10000

    # try depositing 50lakhs
    amount = 5000000
    my_current_account.deposit(amount)
    assert my_current_account.balance == amount - 10000
