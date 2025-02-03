# Vérifie si une sous-chaîne donnée est un palindrome. Args: chaine_caracteres (str): La sous-chaîne à vérifier.
def is_palindrome(chaine_caracteres):
    # Returns: bool: True si la sous-chaîne est un palindrome, sinon False.
    return chaine_caracteres == chaine_caracteres[::-1]


def min_palindrome_partition_forward(s):

    length = len(s)
    palindrome_cuts = []  # Liste pour stocker les points de coupure palindrome

    start_index = 0  # Index de départ pour la recherche de palindrome
    while start_index < length:
        end_index = length - 1  # Index de fin pour la recherche de palindrome
        while end_index >= start_index:
            if is_palindrome(s[start_index:end_index + 1]):
                palindrome_cuts.append(s[start_index:end_index + 1])
                start_index = end_index + 1
                break
            end_index -= 1
        else:
            start_index += 1

    return len(palindrome_cuts), palindrome_cuts


def min_palindrome_partition_backward(s):

    length = len(s)
    palindrome_cuts = []  # Liste pour stocker les points de coupure palindrome

    end_index = length - 1  # Index de fin pour la recherche de palindrome
    while end_index >= 0:
        start_index = 0  # Index de départ pour la recherche de palindrome
        while start_index <= end_index:
            if is_palindrome(s[start_index:end_index + 1]):
                palindrome_cuts.append(s[start_index:end_index + 1])
                end_index = start_index - 1
                break
            start_index += 1
        else:
            end_index -= 1

    return len(palindrome_cuts), palindrome_cuts


# Exemple d'utilisation
input_string = "asasses"
num_cuts_forward, cuts_made_forward = min_palindrome_partition_forward(
    input_string)
num_cuts_backward, cuts_made_backward = min_palindrome_partition_backward(
    input_string)

coupures_forward = num_cuts_forward - 1
coupures_backward = num_cuts_backward - 1

print("Parcours du début à la fin :")
print("Le nombre de coupures nécessaires :", coupures_forward)
print(f"Coupures de chaînes de caractères faites: {cuts_made_forward}")

print("\nParcours de la fin au début :")
print("Le nombre de coupures nécessaires :", coupures_backward)
print(f"Coupures de chaînes de caractères faites: {cuts_made_backward}")
