import os
from typing import List

"""
1. Créez une classe Personne qui a les attributs nom, prenom et age.
Assurez-vous que l'âge est un entier positif. 
Sinon on veut lever une erreur
Écrivez une méthode afficher_details qui affiche les détails de la personne.
"""


class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        if age >= 0:
            self.age = age
        else:
            raise ValueError("L'age doit être un entier positif")

    def afficher_details(self):
        print(f"Le nom est {self.nom}, le prénom est {self.prenom}, l'âge est {self.age}")


# Jean = Personne('Doe', 'Jean', 5)
# Jean.afficher_details()

"""
2. Créez une classe CompteBancaire qui a les attributs nom, solde.
Assurez-vous que le solde est un nombres positif.
Écrivez des méthodes pour déposer et retirer de l'argent.
Écrivez une métohode qui affiche le solde de la personne
"""


class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        if solde < 0:
            raise Exception("Le solde doit être supérieur à 0")
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant < self.solde:
            self.solde -= montant
        else:
            raise Exception("Votre solde est insuffisant")

    def afficher(self):
        print(f"Bonjour {self.nom}.\n Votre solde est de {self.solde}")


# compteHakim = CompteBancaire("Hakim", 20)
# #compteHakim.afficher()
# compteHakim.deposer(50)        
# compteHakim.retirer(60)
# compteHakim.afficher()

"""
Créez une classe Rectangle qui a les attributs longueur et largeur.
Assurez-vous que la longueur et la largeur sont des nombres positifs.
Sinon je veux lever une exception
Écrivez une méthode pour calculer l'aire du rectangle. Cette méthode retourne l'aire du rectangle
Écrivez une méthode pour calculer le périmètre du rectangle. Cette méthode retourne le périmètre du rectangle
Écrivez une méthode pour afficher l'aire du rectangle.
Écrivez une méthode pour afficher le périmètre du rectangle.
"""


class Rectangle:
    def __init__(self, longueur, largeur):
        if longueur <= 0 or largeur <= 0:
            raise Exception("La longueur et la largeur doivent être positifs")

        self.longueur = longueur
        self.largeur = largeur

    def calculerAire(self):
        aire = self.longueur * self.largeur
        return aire

    def calculerPerimetre(self):
        perimetre = 2 * self.longueur + 2 * self.largeur
        return perimetre

    def afficherAire(self):
        print(f"L'aire est {self.calculerAire()}")

    def afficherPerimetre(self):
        print(f"Le périmètre est de {self.calculerPerimetre()}")


# rectangle1 = Rectangle(27, 2)
# rectangle1.afficherAire()
# rectangle1.afficherPerimetre()

"""
4. 
    Créez une classe Etudiant qui a les attributs 
    nom: str,
    prenom: str,
    id: int,
    cours: List[str]. 
    Assurez-vous que l'ID est un nombre positif.
    Écrivez une méthode qui ajoute des cours
    Écrivez une méthode qui supprime des cours
    Écrivez une méthode pour afficher les cours suivis.
"""


class Etudiant:
    def __init__(self, nom: str, prenom: str, id: int, cours: List[str]):
        self.nom = nom
        self.prenom = prenom
        if id > 0:
            self.id = id
        else:
            raise ValueError("L'id doit être positif")
        self.cours = cours

    def ajouterCours(self, cours: str):
        self.cours.append(cours)

    def supprimerCours(self, cours: str):
        self.cours.remove(cours)

    def afficherCours(self):
        print("Les cours suivis sont:")
        for c in self.cours:
            print(c)


# Jalil = Etudiant("Zouhair", "Jalil", 2, [])
# Jalil.ajouterCours("Programmation")
# Jalil.ajouterCours("Musique")
# Jalil.ajouterCours("Sciences")
# Jalil.ajouterCours("Linux")

# Jalil.supprimerCours('Musique')
# Jalil.afficherCours()


"""	
    5.Créez une classe Voiture qui a les attributs marque, modele, annee et kilometrage.
    Assurez-vous que l'année et le kilométrage sont des nombres positifs.
    Écrivez une méthode pour afficher les détails de la voiture.
"""


class Voiture:
    def __init__(self, marque: str, modele: str, annee: int, kilometrage: int):
        self.marque = marque
        self.modele = modele
        if annee <= 0 or kilometrage <= 0:
            raise ValueError("L'année doit être positive")
        self.annee = annee
        self.kilometrage = kilometrage

    def afficherDetails(self):
        print(
            f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nKilométrage : {self.kilometrage:,} km\n")


# car_1 = Voiture("Lamborghini", "Gallardo", 2011, 80000)
# car_2 = Voiture("Ferrari", "Enzo", 2001, 24000)
# car_1.afficherDetails(), car_2.afficherDetails()

"""	
    6. Créez une classe Fichier qui a les attributs nom et contenu.
    Écrivez un constructeur qui prend en entrée le nom et le contenu du fichier,
    et une méthode pour afficher le contenu du fichier.
    Écrivez également une méthode pour supprimer le fichier lorsque l'objet est détruit.
"""


class Fichier:
    fichiers = []

    def __init__(self, nom, contenu):
        self.nom = nom
        self.contenu = contenu

    def afficher_contenu(self):
        try:
            with open(self.nom, 'r') as file:
                contenu = file.read()
                print(f"Contenu du fichier {self.nom}:")
                print(contenu)
        except FileNotFoundError:
            print(f"Le fichier {self.nom} n'existe pas.")

    @classmethod
    def creer_fichier(cls, *fichiers):
        for fichier in fichiers:
            if os.path.exists(fichier.nom):
                print(f"Le fichier {fichier.nom} existe déjà.")
            else:
                try:
                    with open(fichier.nom, 'w') as file:
                        file.write(fichier.contenu)
                    cls.fichiers.append(fichier.nom)
                except Exception as e:
                    print(f"Erreur lors de la création du fichier {fichier.nom}: {e}")

    @classmethod
    def afficher_tous(cls):
        print("Liste de tous les fichiers créés:", ', '.join(cls.fichiers))

    def __del__(self):
        try:
            os.remove(self.nom)
            print(f"Le fichier {self.nom} a été supprimé avec succès.")
        except FileNotFoundError:
            print(f"Le fichier {self.nom} n'existe pas.")


# Exemple d’utilisation
fichier1 = Fichier("cat.jpeg", "Image de chat.")
fichier2 = Fichier("different_cat.png", "Image de chat différente")
fichier3 = Fichier("song.mp3", "Différents sons de chats")
Fichier.creer_fichier(fichier1, fichier2, fichier3)
Fichier.afficher_tous()
