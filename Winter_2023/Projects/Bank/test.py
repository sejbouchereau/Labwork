from bank import Bank
from bank_account import BankAccount

ahuntsic_bank = Bank()

account_1 = BankAccount("Jean Leloup", 2000, 754211)
account_2 = BankAccount("Lisa Marino", 800, 872663)
account_3 = BankAccount("Mourad Demdar", 9200, 837612)

ahuntsic_bank.ajouterUnCompte(account_1)
ahuntsic_bank.ajouterUnCompte(account_2)
ahuntsic_bank.ajouterUnCompte(account_3)

ahuntsic_bank.creerUnCompte("Joseph Lamine", 2783, 827732)

account_2.deposit(500)

for account in ahuntsic_bank.accounts:
    account.display_balance()

ahuntsic_bank.supprimerUnCompte(837612)

for account in ahuntsic_bank.accounts:
    account.display_balance()
