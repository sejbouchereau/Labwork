from bank_account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = []

    def creerUnCompte(self, name, balance, account_number):
        if balance != float(balance):
            raise ValueError("The balance must be of type float.")
        if account_number != int(account_number):
            raise ValueError("The account number must be an integer.")

        account = BankAccount(name, balance, account_number)
        self.accounts.append(account)

    def ajouterUnCompte(self, account):
        if not isinstance(account, BankAccount):
            raise ValueError("The account is not approved.")
        self.accounts.append(account)

    def supprimerUnCompte(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return
        raise ValueError("The account number is not in our database.")
