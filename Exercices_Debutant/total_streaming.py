# total_streaming.py

def somme_streaming(donnees):
    """
    1. Cette fonction calcule la somme des éléments d'une liste de manière naïve.
       Elle additionne même les valeurs négatives.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi cette méthode est peu éco-responsable.
       - Réfléchir à comment l'optimiser.

    3. Starter code  :
       - Boucle simple pour additionner chaque élément.

    4. Complexité :
       - Version actuelle : O(n)
       - Version optimisée possible : O(n) mais avec moins d'opérations inutiles.
    """
    total = 0
    for x in donnees:
        total += x
    return total
