# tri_eco.py

def tri_eco(lst):
    """
    1. Cette fonction implémente un tri naïf (bubble sort) pour trier une liste.
       Elle est actuellement inefficace et peu éco-responsable.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi cette méthode est lente.
       - Réfléchir à comment l'optimiser.

    3. Starter code (non optimisé)

    4. Complexité :
       - Version actuelle : O(n^2)
       - Version optimisée possible : O(n log n)

    NOTE : Ne pas écrire la version optimisée pour l'instant.
    """
    n = len(lst)
    # Boucle externe : parcourir tous les éléments
    for i in range(n):
        # Boucle interne : comparer chaque élément avec le suivant
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # Échanger si l'ordre est incorrect
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
