# plus_long_sous_sequence.py

def plus_long_sous_sequence(lst):
    """
    1. Trouver la longueur de la plus longue sous-séquence croissante.
       Version naïve : vérifier toutes les sous-séquences.

    2. Vos tâches :
       - Ajouter des commentaires.
       - Identifier la complexité O(2^n).
       - Réfléchir à l'optimisation : patience sorting O(n log n).

    Exemple :
    plus_long_sous_sequence([10,9,2,5,3,7,101,18]) -> 4 ([2,3,7,101])
    """
    n = len(lst)
    # version naïve : vérifier toutes les sous-séquences
    def toutes_sous_seq(i, prev):
        if i == n:
            return 0
        take = 0
        if lst[i] > prev:
            take = 1 + toutes_sous_seq(i+1, lst[i])
        dont_take = toutes_sous_seq(i+1, prev)
        return max(take, dont_take)
    return toutes_sous_seq(0, float('-inf'))
