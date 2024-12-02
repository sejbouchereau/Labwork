from comptes import comptes


# Fonction qui demande à l'utilisateur son numéro de compte
def get_account_number():
    """
    Une fonction qui demande à l'utilisateur son numéro de compte.
    Cette fonction se nomme get_account_number
    Cette fonction demande à l'utilisateur son numéro de compte et le retourne sous forme d'Integer (int)
    """
    account_number = int(input("Veuillez entrer votre numéro de compte: "))
    return int(account_number)


# Fonction qui vérifie si un numéro de compte est valide
def is_account_valid(account_number):
    """
    - Écrivez une fonction qui vérifie si un numéro de compte est valide:
    - Cette fonction va avoir comme nom is_account_valid
    - Cette fonction prend en paramètre un numéro de compte (integer)
    - Cette fonction retourne un bool (True ou False)
    """
    if account_number in comptes:
        return True
    else:
        return False


# Fonction qui demande à l'utilisateur son code pin
def get_pin():
    """
    Une fonction qui demande à l'utilisateur son code pin.
    Cette fonction se nomme get_pin
    Cette fonction demande à l'utilisateur son code pin et le retourne sous forme de string.
    """
    pin_code = input("Veuillez entrer votre code PIN: ")
    return pin_code


# Fonction qui vérifie si le code PIN entré par l'utilisateur est correct
def is_pin_valid(account_number, pin_code):
    """
    - Une fonction qui vérifie si le code PIN entré par l'utilisateur est correct.
    - Cette fonction va avoir comme nom is_pin_valid
    - Cette fonction prend en paramètre un numéro de compte (integer) et un code pin (string)
    - Cette fonction retourne un dictionnaire qui correspond aux informations du compte si le code pin est valide
    - Cette fonction retourne None si le code pin est invalide.
    """
    if pin_code == comptes[account_number]['Code PIN']:
        return comptes[account_number]
    else:
        return None


# Fonction qui affiche à l'utilisateur les options de retrait et lui demande son choix
def get_choice():
    """
    Une fonction qui affiche à l'utilisateur les options de retrait et lui demande son choix.
    Cette fonction se nomme get_choice
    Cette fonction retourne le choix de l'utilisateur sour forme d'integer (int).
    """
    choice = int(input(
        "Sélectionnez l'une des options de retrait suivantes:\n1. Retirer 20$\n2. Retirer 50$\n3. Retirer 100$\n4. Retirer un montant personnalisé "))
    return choice


# Fonction qui valide si le retrait est possible
def is_withdrawl_possible(account_details, choice):
    """
    Une fonction qui valide si le retrait est possible.
    Cette fonction s'appelle is_withdrawl_possible
    Cette fonction prend en entrée le compte de l'utilisateur (Un dictionnaire), et le montant du retrait.
    Cette fonction retourne True si l'argent disponible est plus grand égal au montant du retrait.
    Elle retourne False dans le cas contraire.
    """
    solde = int(account_details['Solde'])
    return choice <= solde


# Fonction qui effectue un retrait
def withdrawl(account_details, choice):
    """
    Une fonction qui effectue un retrait.
    Cette fonction s'appelle withdrawl
    Cette fonction prend en entrée le compte de l'utilisateur (Un dictionnaire) et le montant du retrait
    Cette fonction doit vérifier que le solde est assez grand pour effectuer le retrait.
    Sinon elle affiche à l'écran un message d'erreur et retourne le dictionnaire sans avoir effectuer d'opération
    Cette fonction retourne le dictionnaire qui correspond au compte après l'opération
    """
    if is_withdrawl_possible(account_details, choice):
        account_details['Solde'] -= choice
    else:
        print("Solde insuffisant pour effectuer ce retrait.")
    return account_details


# Fonction qui demande à l'utilisateur quel montant il veut retirer
def get_withdrawl_amount():
    """
    Une fonction qui demande à l'utilisateur quel montant il veut retirer.
    Cette fonction se nomme get_withdrawl_amount
    Cette fonction retourne le montant entré sous forme de float.
    """
    amount = float(input("Veuillez entrer le montant que vous désirez retirer: "))
    return amount


# Fonction qui gère les options de retrait
def call_withdrawl(choice, account_details):
    """
    Une fonction qui gère les options de retrait.
    - Cette fonction s'appelle call_withdrawl
    - Cette fonction prend en entrée un chiffre qui correspond à l'option choisie et le dictionnaire qui correspond au compte de l'utilisateur.
    - Si l'utilisateur entre une option valide, on appelle la fonction withdrawl avec le retrait voulu, sinon on affiche une erreur et on appelle return
    """
    if choice == 1:
        return withdrawl(account_details, 20)
    elif choice == 2:
        return withdrawl(account_details, 50)
    elif choice == 3:
        return withdrawl(account_details, 100)
    elif choice == 4:
        amount = get_withdrawl_amount()
        return withdrawl(account_details, amount)
    else:
        print("Erreur: Choix invalide.")
        return account_details


# Fonction qui affiche le solde du compte
def get_account_balance(account_details):
    """
    Une fonction qui affiche à l'utilisateur les options de retrait et lui demande son choix.
    Cette fonction se nomme get_account_balance
    Cette fonction prend en entrée le dictionnaire qui correspond au compte de l'utilisateur.
    Cette fonction retourne le solde d'un utilisateur.
    """
    print(f"Votre solde actuel est de {account_details['Solde']:,}$.")


def main():
    print("Bienvenue à Ahuntsic Bank\n")
    account_number = get_account_number()
    if is_account_valid(account_number):
        pin_code = get_pin()
        account_details = is_pin_valid(account_number, pin_code)
        if account_details:
            while True:
                choice = get_choice()
                account_details = call_withdrawl(choice, account_details)
                get_account_balance(account_details)
                # Demande à l'utilisateur s'il veut continuer ou quitter
                continue_choice = input("Souhaitez-vous effectuer un autre retrait ? (oui/non) ").strip().lower()
                if continue_choice != "oui":
                    break
        else:
            print("Votre code PIN est invalide.")
    else:
        print("Votre numéro de compte n'existe pas dans notre base de données.")

    print("Veuillez passer une bonne journée.")


if __name__ == "__main__":
    main()
