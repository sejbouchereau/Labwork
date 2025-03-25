from accounts import accounts


# Function that asks the user for their account number
def get_account_number():
    """
    A function that asks the user for their account number.
    This function is named get_account_number.
    This function asks the user for their account number and returns it as an integer.
    """
    account_number = int(input("Please enter your account number: "))
    return int(account_number)


# Function that checks if an account number is valid
def is_account_valid(account_number):
    """
    - A function that checks if an account number is valid.
    - This function is named is_account_valid.
    - This function takes an account number (integer) as a parameter.
    - This function returns a boolean (True or False).
    """
    return account_number in accounts


# Function that asks the user for their PIN code
def get_pin():
    """
    A function that asks the user for their PIN code.
    This function is named get_pin.
    This function asks the user for their PIN code and returns it as a string.
    """
    pin_code = input("Please enter your PIN code: ")
    return pin_code


# Function that checks if the entered PIN code is correct
def is_pin_valid(account_number, pin_code):
    """
    - A function that checks if the entered PIN code is correct.
    - This function is named is_pin_valid.
    - This function takes an account number (integer) and a PIN code (string) as parameters.
    - This function returns the account details dictionary if the PIN code is valid.
    - This function returns None if the PIN code is invalid.
    """
    if pin_code == accounts[account_number]['PIN Code']:
        return accounts[account_number]
    else:
        return None


# Function that displays withdrawal options and asks the user for their choice
def get_choice():
    """
    A function that displays withdrawal options and asks the user for their choice.
    This function is named get_choice.
    This function returns the user's choice as an integer.
    """
    choice = int(input(
        "Select one of the following withdrawal options:\n"
        "1. Withdraw $20\n"
        "2. Withdraw $50\n"
        "3. Withdraw $100\n"
        "4. Withdraw a custom amount "
    ))
    return choice


# Function that checks if the withdrawal is possible
def is_withdrawal_possible(account_details, choice):
    """
    A function that checks if the withdrawal is possible.
    This function is named is_withdrawal_possible.
    This function takes the user's account (a dictionary) and the withdrawal amount as input.
    This function returns True if the available balance is greater than or equal to the withdrawal amount.
    It returns False otherwise.
    """
    balance = int(account_details['Balance'])
    return choice <= balance


# Function that performs a withdrawal
def withdrawal(account_details, choice):
    """
    A function that performs a withdrawal.
    This function is named withdrawal.
    This function takes the user's account (a dictionary) and the withdrawal amount as input.
    This function verifies if the balance is sufficient to complete the withdrawal.
    Otherwise, it displays an error message and returns the dictionary without making any changes.
    This function returns the updated account dictionary after the operation.
    """
    if is_withdrawal_possible(account_details, choice):
        account_details['Balance'] -= choice
    else:
        print("Insufficient balance to complete this withdrawal.")
    return account_details


# Function that asks the user for the amount they want to withdraw
def get_withdrawal_amount():
    """
    A function that asks the user for the amount they want to withdraw.
    This function is named get_withdrawal_amount.
    This function returns the entered amount as a float.
    """
    amount = float(input("Please enter the amount you wish to withdraw: "))
    return amount


# Function that handles withdrawal options
def call_withdrawal(choice, account_details):
    """
    A function that handles withdrawal options.
    - This function is named call_withdrawal.
    - This function takes a number corresponding to the selected option and the dictionary containing the user's account details as input.
    - If the user enters a valid option, the function calls withdrawal with the specified amount; otherwise, it displays an error and returns.
    """
    if choice == 1:
        return withdrawal(account_details, 20)
    elif choice == 2:
        return withdrawal(account_details, 50)
    elif choice == 3:
        return withdrawal(account_details, 100)
    elif choice == 4:
        amount = get_withdrawal_amount()
        return withdrawal(account_details, amount)
    else:
        print("Error: Invalid choice.")
        return account_details


# Function that displays the account balance
def get_account_balance(account_details):
    """
    A function that displays the user's account balance.
    This function is named get_account_balance.
    This function takes the user's account dictionary as input.
    This function returns the user's balance.
    """
    print(f"Your current balance is ${account_details['Balance']:,}.")


def main():
    print("Welcome to Ahuntsic Bank\n")
    account_number = get_account_number()
    if is_account_valid(account_number):
        pin_code = get_pin()
        account_details = is_pin_valid(account_number, pin_code)
        if account_details:
            while True:
                choice = get_choice()
                account_details = call_withdrawal(choice, account_details)
                get_account_balance(account_details)
                # Ask the user if they want to continue or exit
                continue_choice = input("Would you like to make another withdrawal? (yes/no) ").strip().lower()
                if continue_choice != "yes":
                    break
        else:
            print("Your PIN code is incorrect.")
    else:
        print("Your account number does not exist in our database.")

    print("Have a great day.")


if __name__ == "__main__":
    main()
