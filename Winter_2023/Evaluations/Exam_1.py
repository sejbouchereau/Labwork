"""
Question 1. 
"""
from math import *

# TODO Répondez à la question 1 ci-dessous

# a) Faux
# b) Vrai
# c) Faux
# d) Vrai
# e) Vrai
# f) Vrai
# g) Vrai
# h) Faux

"""
Question 2:
"""

# TODO Répondez à la question 2 ci-dessous


def est_triangle(a, b, c):
    if min(a, b, c) <= 0:
        raise ValueError("Les valeurs doivent être des entiers positifs.")
    return a + b > c


print(est_triangle(1, 2, 3))

"""
Question 3:
"""

# TODO Répondez à la question 3 ci-dessous


class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        self.longueur = int(longueur)
        self.largeur = int(largeur)

    def aire(self):
        aire = (self.longueur * self.largeur)
        return aire

    def perimetre(self):
        perimetre = (self.longueur * 2) + (self.largeur * 2)
        return perimetre

    def est_carre(self):
        if self.longueur == self.largeur:
            return True
        else:
            return False


rec = Rectangle(2, 4)
print(rec.aire())
print(rec.perimetre())
print(rec.est_carre())

"""
Question 4
"""

# TODO Répondez à la question 4 ci-dessous


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, autre_point):
        return sqrt((self.x - autre_point.x) ** 2 + (self.y - autre_point.y) ** 2)

    def deplacer(self, deplacement_x, deplacement_y):
        self.x += deplacement_x
        self.y += deplacement_y

    def afficher_position(self):
        return f"({self.x},{self.y})"


p1 = Point(1, 4)
p2 = Point(1, 5)

print(f"Distance p1-p2 est de: {p1.distance(p2)}")

p1.deplacer(0, 1)

print(f"Après le déplacement, la distance p1-p2 est de: {p1.distance(p2)}")

print(f"La position de p1: {p1.afficher_position()}")
print(f"La position de p2: {p2.afficher_position()}")
