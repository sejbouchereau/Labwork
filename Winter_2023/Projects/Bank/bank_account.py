class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = str(name)
        self.balance = int(balance)
        self.account_number = int(account_number)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Amount exceeds account balance.")
        self.balance -= amount

    def display_balance(self):
        print(f"Account balance: {self.balance}$")
