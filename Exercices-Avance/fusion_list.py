# fusion_listes.py

def fusion_listes(lst1, lst2):
    """
    1. Fusionner deux listes triées en une seule liste triée.
       Actuellement, utilisez une méthode naïve.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier la complexité O(n*m) si vous utilisez des boucles imbriquées.
       - Optimiser pour O(n+m) en comparant les éléments au fur et à mesure.

    3. Starter code (non optimisé) :
       - Ajouter tous les éléments dans une liste puis trier.

    4. Complexité :
       - Version naïve : O((n+m) log(n+m))
       - Version optimisée : O(n+m)

    Exemple :
    fusion_listes([1,3,5],[2,4,6]) -> [1,2,3,4,5,6]
    """
    res = lst1 + lst2
    res.sort()
    return res
