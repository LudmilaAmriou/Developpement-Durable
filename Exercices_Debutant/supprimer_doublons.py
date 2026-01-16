# supprimer_doublons.py

def supprimer_doublons(fichiers):
    """
    1. Cette fonction supprime les doublons dans une liste tout en conservant l'ordre.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi c'est peu éco-responsable.
       - Réfléchir à comment l'optimiser.

    3. Starter code (non optimisé).

    4. Complexité :
       - Version actuelle : O(n^2)
       - Version optimisée possible : O(n)
    """
    res = []
    for f in fichiers:
        if f not in res:
            res.append(f)
    return res
