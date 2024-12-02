from bank import Banque
from bank_account import CompteBancaire

banque_ahuntsic = Banque()

compte_1 = CompteBancaire("Jean Leloup", 2000, 754211)
compte_2 = CompteBancaire("Lisa Marino", 800, 872663)
compte_3 = CompteBancaire("Mourad Demdar", 9200, 837612)

banque_ahuntsic.ajouterUnCompte(compte_1)
banque_ahuntsic.ajouterUnCompte(compte_2)
banque_ahuntsic.ajouterUnCompte(compte_3)

banque_ahuntsic.creerUnCompte("Joseph Lamine", 2783, 827732)

compte_2.deposer(500)

for compte in banque_ahuntsic.comptes:
    compte.afficher_solde()

banque_ahuntsic.supprimerUnCompte(837612)

for compte in banque_ahuntsic.comptes:
    compte.afficher_solde()
