class CompteBancaire:
    def __init__(self, nom, solde, numero_de_compte):
        self.nom = str(nom)
        self.solde = int(solde)
        self.numero_de_compte = int(numero_de_compte)
    
    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise ValueError("Montant supérieur au solde du compte.")
        self.solde -= montant

    def afficher_solde(self):
        print(f"Solde au compte : {self.solde}$")
