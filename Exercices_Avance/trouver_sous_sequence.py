# trouver_sous_sequence.py

def trouver_sous_sequence(seq, subseq):
    """
    1. Vérifier si une sous-séquence existe dans une séquence.
       La version naïve parcourt toute la séquence et vérifie chaque fenêtre.

    2. Vos tâches :
       - Ajouter des commentaires.
       - Identifier la complexité O(n*m).
       - Réfléchir à une optimisation possible (ex: sliding window).

    3. Starter code (non optimisé) :
       - Boucle pour chaque position et comparaison avec subseq.

    Exemple :
    trouver_sous_sequence([1,2,3,4,5],[3,4]) -> True
    trouver_sous_sequence([1,2,3],[4,5]) -> False
    """
    n = len(seq)
    m = len(subseq)
    for i in range(n - m + 1):
        if seq[i:i+m] == subseq:
            return True
    return False
