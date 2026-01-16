# nettoyer_mails.py

def nettoyer_mails(mails):
    """
    1. Cette fonction supprime les doublons et prépare le filtrage des mails indésirables
       ("spam" ou "pub").

    2. Vos tâches :
       - Lire et comprendre le code.
       - Identifier pourquoi cette méthode est lente.
       - Réfléchir à comment l'optimiser (hint : filtrer "spam"/"pub" et utiliser un set).

    3. Starter code (non optimisé)

    4. Complexité :
       - Version actuelle : O(n^2)
       - Version optimisée possible : O(n)
    """
    res = []
    for mail in mails:
        # Ajoute le mail si pas déjà présent
        if mail not in res:
            if mail != "spam" and mail != "pub":
                res.append(mail)
    return res
