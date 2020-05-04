"""
Homework Problem # 12.3
Description: ATM machine games testing Account.py
"""


import sys

from Account import Account


def test_atm():
    """
    Test function for Account using ATM scenario
    """
    # creates 10 accounts in a list with the ids 0, 1, ..., 9
    account_list = [Account(x) for x in range(0, 10)]

    def enter_id():
        """
        Prompts user for an ID# from 0-9 (inclusive)
        Returns user ID.
        """
        while True:
            try:
                user_id = int(input('Please enter an ID from 0-9: '))

                if user_id in range(0, 10):
                    return user_id
                else:
                    print('Input not in range 0-9. Try again.')
                    continue

            except ValueError:
                print('Could not convert input to int. Try again.')
                continue

    def display_menu():
        """
        Displays ATM menu options
        """
        print('\nMain menu')
        print('\n1: Check balance')
        print('2: Withdraw')
        print('3: Deposit')
        print('4: Exit menu')
        print('5: Exit ATM')

    def enter_menu_option():
        """
        Prompts user for menu option, number between 1-4 (inclusive)
        Returns menu_option
        """
        while True:
            try:
                menu_option = int(input('Enter your selection: '))

                if menu_option in range(1, 6):
                    return menu_option
                else:
                    print('Not a menu option. Try again.')
                    continue
            except ValueError:
                print('Not a correct value. Try again.')
                continue

    def menu_output(user_id, menu_option):
        """
        Performs one of 4 actions to specified account, depending on
        the chosen menu option.
        """
        # option 1: Prints account balance
        if menu_option == 1:
            print('The balance is',
                  format(account_list[user_id].get_balance(), '0.2f'))

        # option 2: Withdraws from account
        elif menu_option == 2:
            while True:
                try:
                    withdraw_amount = float(
                        input('Enter an amount to withdraw: '))

                    if withdraw_amount >= 0:
                        break
                    else:
                        print('Invalid withdrawal amount.')
                        continue

                except ValueError:
                    print('Not a valid input. Try again.')
                    continue

            account_list[user_id].withdraw(withdraw_amount)

        # deposits money into account
        elif menu_option == 3:
            while True:
                try:
                    deposit_amount = float(
                        input('Enter an amount to deposit: '))

                    if deposit_amount >= 0:
                        break
                    else:
                        print('Invalid deposit amount.')
                        continue

                except ValueError:
                    print('Not a valid input. Try again.')
                    continue
            account_list[user_id].deposit(deposit_amount)

        # run_atm() called to prompt a new account id
        elif menu_option == 4:
            print('')
            run_atm()

        elif menu_option == 5:
            print('Exiting ATM. Goodbye.')
            sys.exit()

    def run_atm():
        """
        Prompts user for account id each time it is called.
        Menu displayed, and user prompted to choose a menu option.
        Action corresponding to menu option is completed.
        """
        account_id = enter_id()
        while True:

            display_menu()
            menu_choice = enter_menu_option()
            menu_output(account_id, menu_choice)

    run_atm()


if __name__ == "__main__":
    test_atm()
