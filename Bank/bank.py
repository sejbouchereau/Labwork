from bank_account import CompteBancaire

class Banque:
    def __init__(self):
        self.comptes = []
    
    def creerUnCompte(self, nom, solde, numero_de_compte):
        if solde != float(solde):
            raise ValueError("Le solde doit être de type float.")
        if numero_de_compte != int(numero_de_compte):
            raise ValueError("Le numéro de compte doit être un entier.")
    
        compte = CompteBancaire(nom, solde, numero_de_compte)
        self.comptes.append(compte)
    
    def ajouterUnCompte(self, compte):
        if not isinstance(compte, CompteBancaire):
            raise ValueError("Le compte n'est pas approuvé.")
        self.comptes.append(compte)
    
    def supprimerUnCompte(self, numero_de_compte):
        for compte in self.comptes:
            if compte.numero_de_compte == numero_de_compte:
                self.comptes.remove(compte)
                return
        raise ValueError("Le numéro de compte n'est pas dans notre base de données.")