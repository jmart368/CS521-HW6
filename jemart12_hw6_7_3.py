"""
Homework Problem # 7.3
Description: Test the Account class from Account.py
"""

from Account import Account

if __name__ == "__main__":
    """
    Test program that creates an Account object with an:
    account id = 1122,
    balance = $20,000,
    annual interest rate = 4.5%
    """
    # set the test parameters
    account_1 = Account(1122, 20000.00, 4.5)
    # withdrawal amount = 2500
    account_1.withdraw(2500)
    # deposit amount = 3000
    account_1.deposit(3000)

    print('ID:', account_1.get_id())
    print('Balance:', format(account_1.get_balance(), "0,.2f"))
    print('Monthly interest rate:', account_1.get_monthly_interest_rate())
    print('Monthly interest:', round(account_1.get_monthly_interest(), 2))
