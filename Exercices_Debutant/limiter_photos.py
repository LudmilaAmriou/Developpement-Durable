# limiter_photos.py

def limiter_photos(photos):
    """
    1. Cette fonction garde seulement les 1000 dernières photos.
       La version naïve utilise une boucle pour copier les éléments, ce qui est peu éco-responsable.

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi cette méthode est inefficace.
       - Réfléchir à comment l'optimiser.

    3. Starter code (non optimisé) :
       - Boucle pour copier les 1000 derniers éléments dans une nouvelle liste.

    4. Complexité :
       - Version actuelle : O(k) où k = 1000 si n>1000
       - Version optimisée possible : O(1) pour le slicing
    """
    n = len(photos)
    res = []
    # Boucle pour copier les 1000 dernières photos
    for i in range(max(0, n-1000), n):
        res.append(photos[i])
    return res
