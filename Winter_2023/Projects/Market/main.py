from typing import Dict, List


def get_prices(path) -> Dict[str, float]:
    with open(path, "r") as prix:
        prix = prix.read().split()

        aliments = []
        prices = []

        for element in prix:
            if element.endswith(str("$")):
                prices.append(float(element[:-1]))
            else:
                aliments.append(element)

    dict_prix = dict(zip(aliments, prices))

    return dict_prix


def get_non_taxable(path) -> List[str]:
    '''
    Ici, iplémentez le code qui lit le fichier produits_non_taxable.txt, et qui store dans une liste les produits non taxables dans un format comme
    celui-ci:
    ['pomme', 'orange', 'oignon' ...]
    '''
    with open(path, "r") as notax:
        notax = notax.read().split()

        non_taxable = []

        for element in notax:
            non_taxable.append(element)

    return non_taxable


def get_recette(path) -> Dict[str, int]:
    '''
    Ici, iplémentez le code qui lit le fichier recette.txt, et qui store dans un dictionnaire les quantités pour chaque aliment dans un format comme
    celui-ci:
    {
        "vin": 1,
        "oignon": 2,
        "spaghettis":2,
        ...
    }
    '''
    with open(path, "r") as recette:
        recette = recette.read().split()

        produits = []
        quantité = []

        for element in recette:
            if element.isnumeric():
                quantité.append(element)
            else:
                produits.append(element)

        recette = dict(zip(produits, quantité))

    return recette


def calculate_total_price(prices: dict[str, float], recette: dict[str:int], non_taxable: List[str]):
    '''
    Ici, iplémentez le code qui calcule le prix final de la recette
    Vous devez utiliser les dictionnaires des prix et de la recette et la liste des produits non_taxables
    '''
    prix_total = 0
    for produit, quantite in recette.items():
        if produit not in non_taxable:
            prix = prices[produit] * float(quantite)
            prix_total += round(prix, 2)
        else:
            prix = prices[produit] * float(quantite) * 1.14975
            prix_total += round(prix, 2)
    return round(prix_total, 2)


if __name__ == '__main__':
    prices = get_prices('prix.txt')
    recette = get_recette('recette.txt')
    non_taxable = get_non_taxable('produits_non_taxable.txt')
    print(f"Le prix total de la recette est de {calculate_total_price(prices, recette, non_taxable):,}$")
    print(f"Le dictionnaire des prix :\n{prices}")
    print(f"La recette :\n{recette}")
