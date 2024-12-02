"""
1.
Créez une classe Date qui représente une date (jour, mois, année).
Ajoutez des méthodes pour afficher la date au format jour/mois/année et pour déterminer si l'année est bissextile.
afficher_date -> jour/mois/annee
is_annee_bissextile
Testez votre classe en créant une instance de Date et en affichant la date et si l'année est bissextile.
"""
from math import pi
from typing import List

"""
- Si le jour n'est pas un chiffre entre 1 et 31, levez une ValueError
"""


class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        if 1 <= int(self.jour) <= 31:
            self.mois = mois
            self.annee = annee
        else:
            raise ValueError('Le jour doit être compris entre 1 et 31')

    def afficher_date(self):
        print(f"{self.jour}/{self.mois}/{self.annee}")

    def is_annee_bissextile(self):
        if self.annee % 4 == 0:
            return True
        else:
            return False


# exemple = Date(6, "Avril", 2023)
# exemple.afficher_date()
# exemple.is_annee_bissextile()


"""
Écrire une fonction qui demande à l'utilisateur d'entrer un jour, un mois, une année et qui retourne un objet Date. 
Le nom de la fonction est ask_for_date()

-- Cette fonction peut retourner une erreur à trois endroits.
    -- jour = int(input)
    -- annee = int(input)
    -- return Date(jour, mois, annee)
--
    Si une erreur est levée:
    Je veux afficher à l'écran: Vous avez entré une valeur invalide et aussi l'erreur retournée. 
"""


def ask_for_date():
    try:
        jour = int(input('Entrez un jour: '))
        mois = input('Entrez un mois: ')
        annee = int(input('Entrez une année: '))

        return Date(jour, mois, annee)
    except Exception as e:
        print(f"Vous avez entré une valeur invalide. Voici l'erreur retournée: {e}")


date = ask_for_date()

if date.is_annee_bissextile():
    print("L'année entrée est bissextile.")

hier = Date(5, 'avril', 2023)
demain = Date(7, 'avril', 2023)
hier.afficher_date()
date.afficher_date()
demain.afficher_date()

"""
Créez une classe Livre qui représente un livre avec un titre, un auteur et un prix.
Ajoutez une méthode pour retourner le titre du livre
Ajoutez une méthode pour retourner l'auteur du livre et 
une méthode pour vérifier si le livre est en promotion 
(c'est-à-dire si le prix est inférieur à un prix donné en paramètre).
"""

"""
Dans la méthode is_livre_en_promotion:
    -- Si le prix donné en paramètre est supérieur à 35$ 
    -- Levez une ValueError qui dit: Un prix de promotion ne peut être supérieur à 35$
"""


class Livre:
    def __init__(self, titre, auteur, prix):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def afficher_titre(self):
        print(self.titre)

    def get_titre(self):
        return self.titre

    def get_auteur(self):
        return self.auteur

    def is_livre_en_promotion(self, prix):
        if prix > self.prix:
            raise ValueError("Un prix de promotion ne peut être supérieur au prix de l'article")
        return self.prix > prix


book = Livre("Moby Dick", "Jules Verne", 60)

"""
Je veux demander à l'utilisateur d'entrer un prix de promotion
Et je veux afficher Wouhouu! si le livre le tour du monde en 80 jours est en promotion

-- Si ce programme retourne une ValueError, affichez à l'écran: Vous avez entrer une valeur invalide, suivie de l'erreur retournée
"""

try:
    prix_promo = int(input("Entrez le prix de promotion: "))
    if book.is_livre_en_promotion(prix_promo):
        print("Wouhouu vous sauvez de précieux billets!")
    else:
        print("Le livre n'est pas en promotion")
except ValueError as e:
    print(f"Vous avez entrer une valeur invalide: {e}")

print(f"Merci de votre achat: {book.get_titre()} par {book.get_auteur()}.")

"""
Créez une classe Etudiant qui représente un étudiant
avec un nom: str, un prénom:str , une date de naissance: Date et une liste de notes: List[int]. 
Ajoutez des méthodes pour 
calculer la moyenne des notes de l'étudiant et
pour afficher son nom et 
pour afficher sa moyenne.
"""


class Etudiant:
    def __init__(self, prenom: str, nom: str, date_de_naissance: Date, liste_notes: List[int]):
        self.prenom = prenom
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.liste_notes = liste_notes

    def calculer_moyenne(self):
        return sum(self.liste_notes) / len(self.liste_notes)

    def afficher_nom(self):
        print(f"{self.prenom} {self.nom}")

    def afficher_moyenne(self):
        print(self.calculer_moyenne())


"""
Je veux créer un objet avec comme prénom Jonathan comme nom Joseph comme date de naissance le 12 aout 1980 et comme notes 
[80, 79, 90, 58, 72]
"""

jonathan = Etudiant('Jonathan', 'Joseph', Date(10, "Juillet", 2000), [80, 79, 90, 58, 72])
jonathan.afficher_moyenne(), jonathan.date_de_naissance.afficher_date()

"""
Créez une classe Cercle qui a un attribut : le rayon.
Ajoutez une méthode pour calculer et retourner la surface pi*r^2 et une autre méthode pour calculer la circonférence 2*pi*r.
"""


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return pi * (self.rayon ** 2)

    def calculer_circonference(self):
        return 2 * pi * self.rayon


cercle_1 = Cercle(10)
cercle_2 = Cercle(34)

print(int(cercle_1.calculer_circonference()))
print(int(cercle_2.calculer_circonference()))

"""
Créez une classe JeuDeCartes qui a deux attributs : 
la liste des cartes et 
une carte est représentée par un objet de la classe Carte
qui a 2 attributs: 
-- La valeur (Chiffre entre 1 et 13)
-- La couleur (Pique, Trèfle, Coeur, Carreau)
-- Une méthode afficher_carte: 
    Ex. "4 de Carreau"
la liste de joueurs. 
Liste de string: 

Ajoutez des méthodes pour distribuer les cartes et afficher les cartes des joueurs.

"""


class Carte:
    def __init__(self, valeur, couleur):
        if valeur < 1 or valeur > 13:
            raise ValueError("La carte doit avoir une valeur comprise entre 1 et 13")
        self.valeur = valeur
        self.couleur = couleur

    def afficher_carte(self):
        print(f"{self.valeur} de {self.couleur}")


class JeuDeCartes:
    """
    Un jeu de cartes contient toujours 52 cartes
    1 à 2 de chaque couleur
    """

    def __init__(self, liste_des_joueurs):
        self.liste_de_cartes = [Carte(1, 'Pique'), Carte(2, 'Pique'), Carte(1, 'Coeur'), Carte(2, 'Coeur'),
                                Carte(1, 'Trefle'), Carte(2, 'Trefle'), Carte(1, 'Carreau'), Carte(2, 'Carreau')]
        self.liste_des_joueurs = liste_des_joueurs

    def distribuer_cartes(self):
        """
        Retourner un dictionnaire
        {
        {Joueur1: [Carte(1, 'Pique'), Carte(2, 'Pique')]}
        {Joueur2: [Carte(1, 'Coeur'), Carte(2, 'Coeur')]}
        {Joueur3: [Carte(1, 'Trefle'), Carte(2, 'Trefle')]}
        {Joueur4: [Carte(1, 'Carreau'), Carte(2, 'Carreau')]}
        }
        """
        dictionnaire = {}
        """
        1. Trouver le nombre de cartes à donner à chaque joueur.
        -- Garder en mémoire un compteur qui compte ou on est rendu dans le paquet de cartes
        2. Boucler sur les joueurs.
        3. Lui donner le nombre de cartes qu'on veut. 
        """
        nb_de_cartes_par_joueur = int(len(self.liste_de_cartes) / len(self.liste_des_joueurs))
        cartes_distribuees = 0
        for j in self.liste_des_joueurs:
            position_dans_la_liste_de_cartes = cartes_distribuees + nb_de_cartes_par_joueur
            dictionnaire.update({j: self.liste_de_cartes[cartes_distribuees:position_dans_la_liste_de_cartes]})
            cartes_distribuees += nb_de_cartes_par_joueur

        return dictionnaire

    def afficher_cartes_des_joueurs(self):
        distribution = self.distribuer_cartes()
        for item in distribution:
            cartes = distribution[item]
            print(f"Joueur: {item}")
            print("Cartes:")
            for carte in cartes:
                carte.afficher_carte()


liste_des_joueurs = ['Joueur1', 'Joueur2', 'Joueur3', 'Joueur4']
jeu_de_carte = JeuDeCartes(liste_des_joueurs)
jeu_de_carte.afficher_cartes_des_joueurs()
