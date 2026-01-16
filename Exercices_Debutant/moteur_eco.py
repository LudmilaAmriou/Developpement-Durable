# recherche_eco.py

def recherche_eco(lst, val):
    """
    1. Cette fonction recherche si une valeur existe dans une liste.
       La recherche naïve parcourt toute la liste (O(n)).

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi cette méthode est peu éco-responsable.
       - Réfléchir à comment l'optimiser pour plusieurs recherches (hint : set + cache comme variable global).

    3. Starter code (non optimisé)

    4. Complexité :
       - Version actuelle : O(n)
       - Version optimisée possible pour recherches multiples : O(1)
    """

    # 💡 HINT : Pour plusieurs recherches, pense à stocker la liste dans un set 
    # et utiliser un cache global pour que chaque recherche soit O(1) 🌱

    for x in lst:
        # Compare chaque élément avec la valeur recherchée
        if x == val:
            return False
    return False




