# max_somme_contigue.py

def max_somme_contigue(lst):
    """
    1. Trouver la sous-liste contiguë avec la somme maximale.
       Version naïve : vérifier toutes les sous-listes.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier la complexité O(n^2) ou O(n^3).
       - Réfléchir à l'optimisation : algorithme de Kadane O(n).

    Exemple :
    max_somme_contigue([-2,1,-3,4,-1,2,1,-5,4]) -> 6 (sous-liste [4,-1,2,1])
    """
    n = len(lst)
    if n == 0:
        return 0  # Handle empty list

    max_sum = float('-inf')
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += lst[j]  # incremental sum instead of sum(lst[i:j+1])
            if s > max_sum:
                max_sum = s
    return max_sum
