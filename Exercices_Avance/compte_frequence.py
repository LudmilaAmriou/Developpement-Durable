# compte_frequence.py

def compte_frequence(lst):
    """
    1. Compter la fréquence de chaque élément d'une liste.
       La version naïve utilise lst.count() pour chaque élément.

    2. Vos tâches :
       - Ajouter des commentaires.
       - Identifier la complexité O(n^2).
       - Réfléchir à une optimisation possible (dict ... Counter).

    3. Starter code (non optimisé) :
       - Boucle et lst.count() pour chaque élément unique.

    Exemple :
    compte_frequence([1,2,2,3,1]) -> {1:2, 2:2, 3:1}
    """
    res = {}
    for x in lst:
        if x not in res:
            res[x] = lst.count(x)
    return res
