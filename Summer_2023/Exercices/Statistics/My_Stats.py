from collections import Counter
import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
import math
from math import *

observations = pnd.DataFrame({'NOTES': np.array([3, 19, 10, 15, 14, 12, 9, 8, 11, 12,
                                                 11, 12, 13, 11, 14, 16])})
valeurs = observations['NOTES']

print("\n-- NOMBRE D'OBSERVATIONS --")
n = valeurs.count()
print(f"Nombre d'observations: {n}")

print("\n-- MINIMUM --")
valeurs_triees = valeurs.sort_values()
print(f"Valeur minimale: {valeurs_triees[0]}")

print("\n-- MAXIMUM --")
valeurs_triees = valeurs_triees.reset_index(drop=True)  # Réinitialise les index avec les valeurs triées
print(f"Valeur maximale: {valeurs_triees[len(valeurs_triees) - 1]}")

print("\n-- ÉTENDUE --")
valeurs_triees = valeurs_triees.reset_index(drop=True)  # Réinitialise les index avec les valeurs triées
print(f"Étendue: {str(valeurs_triees[len(valeurs_triees) - 1] - valeurs_triees[0])}")

print("\n-- SOMME --")
somme = 0
for i in observations["NOTES"]:
    somme += i
print(f"Somme: {somme}")

# ----------------------------------------------
#               TENDANCE CENTRALE
# ----------------------------------------------

print("\n-- MOYENNE --")


def calculMoyenne(feature):  # La fonction NumPy .mean() retourne également la moyenne
    total = sum(feature)
    moyenne = total / feature.count()
    return round(moyenne, 3)


print(f"Moyenne: {calculMoyenne(valeurs)}")

print("\n-- MÉDIANE --")


def calculMediane(feature):  # La fonction NumPy .median() retourne également la médiane
    feature = observations["NOTES"].sort_values()
    feature = feature.reset_index(drop=True)  # Réinitialise les index avec les valeurs triées
    total = feature.count()
    pair = False
    if total % 2 == 0:
        pair = True
    if pair:
        index = round((total / 2))
        index_python = index - 1
        valeur1 = feature[index_python]
        valeur2 = feature[index_python + 1]
        mediane = round(valeur1 + ((valeur2 - valeur1) / 2))
    else:
        index = round(((total + 1) / 2))
        index_python = index - 1
        mediane = round(feature[index_python])
    return mediane, index


print(f"Médiane: {calculMediane(valeurs)[0]}")

print("\n-- MODE --")


def calculMode(feature):
    mode = Counter(feature)
    return mode


print(f"Mode: {calculMode(valeurs)}")

print("\n-- QUARTILES --")


def calculQuartiles(feature, mediane, rang_mediane):
    sort_feature = feature.sort_values().reset_index(drop=True)  # Réinitialise les index avec les valeurs triées
    q1, q2, q3 = 0, mediane, 0

    resteDivision = rang_mediane % 2  # Calcul Q1
    if resteDivision != 0:
        q1 = sort_feature[int((rang_mediane / 2) + 1) - 1]
    else:
        valeurMin = sort_feature[int((rang_mediane / 2) - 1)]
        valeurMax = sort_feature[int((rang_mediane / 2))]
        q1 = (valeurMin + ((valeurMax - valeurMin) / 2) + valeurMax) / 2

    nbDonnees = len(sort_feature) + 1  # Calcul Q3
    nbDonneesDepuisMediane = nbDonnees - rang_mediane
    resteDivision = nbDonneesDepuisMediane % 2
    if resteDivision != 0:
        q3 = sort_feature[int(rang_mediane + math.ceil(nbDonneesDepuisMediane / 2)) - 1]
    else:
        valeurMinQ3 = sort_feature[int(rang_mediane + (nbDonneesDepuisMediane / 2)) - 1]
        valeurMaxQ3 = sort_feature[int(rang_mediane + (nbDonneesDepuisMediane / 2))]
        q3 = (valeurMinQ3 + ((valeurMaxQ3 - valeurMinQ3) / 2) + valeurMaxQ3) / 2

    return q1, q2, q3


quartiles = calculQuartiles(valeurs, calculMediane(valeurs)[0],
                            calculMediane(valeurs)[1])
qt_1, qt_2, qt_3 = quartiles[0], quartiles[1], quartiles[2]
print(f"Q1: {qt_1}\nQ2: {qt_2}\nQ3: {qt_3}")

print("\n-- INTERQUARTILE --")


def calculInterquartile(features_quartiles):
    premier_quartile = features_quartiles[0]
    troisieme_quartile = features_quartiles[2]
    interquartile = troisieme_quartile - premier_quartile
    return interquartile


print(f"Interquartile: {calculInterquartile(quartiles)}")

print("\n-- VARIANCE --")


def calculVarianceEcartType(feature):
    n = feature.count()
    moyenneArithmetique = feature.mean()
    variance = 0
    c3 = 0
    for valeurObservation in feature:
        x = valeurObservation
        moy = moyenneArithmetique
        c1 = valeurObservation - moyenneArithmetique
        c2 = c1 * c1
        c3 = c3 + c2
    variance = c3 / (n - 1)
    ecartType = sqrt(variance)
    return [variance, ecartType]


print(f"Variance: {round(calculVarianceEcartType(valeurs)[0], 3)}")

print("\n-- ÉCART-TYPE --")

print(f"Écart-type: {round(calculVarianceEcartType(valeurs)[1], 3)}")

print("\n-- CRITÈRE DE TUKEY --")


def critereDeTukey(feature, premier_quartile, troisieme_quartile):  # Retourne les valeurs extrêmes
    valeurs_extremes_inferieures = []
    valeurs_extremes_superieures = []
    sort_feature = feature.sort_values().reset_index(drop=True)  # Réinitialise les index avec les valeurs triées
    interquartile = troisieme_quartile - premier_quartile
    borne_inferieure = premier_quartile - (1.5 * interquartile)
    borne_superieure = troisieme_quartile + (1.5 * interquartile)
    for valeur in feature:
        if valeur < borne_inferieure:
            valeurs_extremes_inferieures.append(valeur)
        if valeur > borne_superieure:
            valeurs_extremes_superieures.append(valeur)
    valeurs_extremes = valeurs_extremes_inferieures + valeurs_extremes_superieures
    return valeurs_extremes


vals_extremes = critereDeTukey(valeurs, quartiles[0], quartiles[2])

print(f"Valeurs extrêmes ({len(vals_extremes)}): {vals_extremes}")


def visualisation(feature, moyenne, mediane, quartile_1, quartile_2, quartile_3):
    plt.subplot(2, 2, 1)
    plt.hist(feature)
    plt.title("Histogramme et moyenne")
    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=1, label=str(moyenne))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 2)
    plt.hist(feature)
    plt.title("Histogramme et medianne")
    plt.axvline(mediane, color='green', linestyle='dashed', linewidth=1, label=str(mediane))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 3)
    plt.hist(feature)
    plt.title("Histogramme et quartiles")
    plt.axvline(quartile_1, color='orange', linestyle='dashed', linewidth=1, label="Ql: " + str(quartile_1))
    plt.axvline(quartile_2, color='orange', linestyle='dashed', linewidth=1, label="Q2: " + str(quartile_2))
    plt.axvline(quartile_3, color='orange', linestyle='dashed', linewidth=1, label="Q3: " + str(quartile_3))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 4)
    plt.boxplot(feature)
    plt.title("Boite à moustaches")

    plt.show()

# Exemple de visualisation du feature avec la libraire matplotlib :
# visualisation(valeurs, calculMoyenne(valeurs), calculMediane(observations["NOTES"])[0], qt_1, qt_2, qt_3)
