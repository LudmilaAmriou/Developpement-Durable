# 🌱 Développement Durable – Exercices Python

Bienvenue dans le projet **Développement Durable en Python** !  
L'objectif : apprendre à coder **correctement** tout en adoptant des pratiques **éco-responsables** — un code **lisible**, **optimisé** et peu énergivore.

---

## 📁 Structure du projet

```
Exercices_Debutant/
├── limiter_photos.py
├── nettoyer_mails.py
├── supprimer_doublons.py
├── moteur_eco.py
├── tri_eco.py
├── total_streaming.py
└── tests/
    ├── test_judge.py
    ├── test_nettoyer_mails.py
    ├── test_nettoyer_mails.py
    └── ...

Exercices_Avance/
├── trouver_sous_sequence.py
├── compte_frequence.py
└── tests/
    └── ...

Exercices_Expert/
├── plus_longue_sous_sequence.py
├── max_somme_contigue.py
└── tests/
    └── ...
```

### Description des dossiers

- **Exercices_Debutant** : bases de Python et optimisation simple
- **Exercices_Avance** : algorithmes intermédiaires et structures de données
- **Exercices_Expert** : algorithmes complexes et optimisation critique
- **tests/** : scripts de test pour **correction** et **performance**

---

## 🌱 Principes Éco-Coding

### 1. Réduire la complexité algorithmique

Évitez les boucles imbriquées inutiles (O(n²), O(2^n)). Utilisez `set`, `dict`, ou algorithmes optimisés (`merge`, `binary search`, Kadane).

### 2. Éviter les calculs répétitifs

Stockez les résultats intermédiaires (cache, memoization).

**Exemple :**

```python
data_set = set(lst)  # Convertir une fois pour O(1) par recherche
```

### 3. Exploiter les fonctions Python natives

**Slicing :**

```python
liste[-n:]  # Ultra-rapide vs boucle for
```

Les fonctions intégrées (`max`, `sum`, `Counter`, `bisect`) sont optimisées en C.

### 4. Mesurer la performance

Comparez votre fonction à une solution optimale pour détecter si votre code est linéaire, polynomial ou exponentiel.

---

## 📌 Exercices par Niveau

### Exercices Débutant

#### 1️⃣ `limiter_photos.py`

- **Objectif** : garder les 1000 dernières photos

#### 2️⃣ `nettoyer_mails.py`

- **Objectif** : supprimer doublons et mails `"spam"`/`"pub"`

#### 3️⃣ `supprimer_doublons.py`

- **Objectif** : supprimer doublons en conservant l'ordre

### Exercices Avancé

#### 1️⃣ `compte_frequence.py`

- **Objectif** : compter la fréquence des éléments

#### 2️⃣ `trouver_sous_sequence.py`

- **Objectif** : Identifier une sous-séquence spécifique dans une liste

### Exercices Expert

#### 1️⃣ `plus_longue_sous_sequence.py`

- **Objectif** : longueur de la plus longue sous-séquence croissante (LIS)

#### 2️⃣ `max_somme_contigue.py`

- **Objectif** : sous-liste contiguë avec somme maximale

---

## 🧪 Lancer les Tests

### Exécution locale

Pour tester votre code localement avant de soumettre :

```bash
# Tester un exercice spécifique
python -m Exercices_Debutant.tests.test_limiter_photos
python -m Exercices_Debutant.tests.test_nettoyer_mails
python -m Exercices_Expert.tests.test_plus_longue_sous_sequence

# Tester tous les exercices d'un niveau
python -m pytest Exercices_Debutant/tests/
python -m pytest Exercices_Expert/tests/
```

### Validation automatique

Chaque exercice est évalué sur trois critères :

1. **Correction** : résultats attendus pour cas simples et limites
2. **Performance** : comparaison avec une solution optimale
3. **Détection de méthode** : utilisation de slicing, set, DP, binary search, etc.

---

## ⚠️ Règles Importantes

### Fichiers protégés

> **Les fichiers suivants ne doivent PAS être modifiés :**

- ❌ Tous les fichiers dans `tests/`
- ❌ `.github/workflows/` (configuration CI/CD)
- ❌ Fichiers de configuration du projet

**Attention :** Toute modification de ces fichiers est automatiquement détectée et invalidera votre soumission.

### Rapports automatiques

- Un **rapport de score** est généré automatiquement après chaque soumission
- Le rapport inclut votre **éco-score** détaillé (0-100)
- Vous recevez un feedback sur la correction, performance et méthodologie
- Les rapports sont consultables dans l'interface du projet

---

## 🌱 Score Éco

Chaque exercice reçoit un **éco-score** basé sur :

| Critère            | Description                               |
| ------------------ | ----------------------------------------- |
| ✅ **Correction**  | Le code fonctionne correctement           |
| ⚡ **Performance** | Le code est rapide et proche de l'optimal |
| 🏆 **Méthode**     | Utilise les techniques Python optimales   |

### Barème

| Score     | Signification                        |
| --------- | ------------------------------------ |
| **100**   | Solution optimale                    |
| **60-90** | Correcte mais peut être optimisée    |
| **<60**   | Solution naïve / peu éco-responsable |

---

## 💡 Conseils pour Réussir

- Toujours mesurer la **complexité** de votre code
- Préférez les **structures natives optimisées** (set, dict, bisect, slicing)
- Pour plusieurs recherches ou filtres, utilisez **cache/memoization**
- Testez votre code sur de **grandes entrées** avant soumission
- Utilisez les tests locaux pour valider votre solution
- Le but : **correct + rapide + éco-responsable** !

---

## 🚀 Workflow de Travail

1. **Lire** la description de l'exercice
2. **Implémenter** votre solution
3. **Tester localement** avec `python -m Exercices_xxx.tests.test_xxx`
4. **Optimiser** si nécessaire
5. **Soumettre** votre code
6. **Consulter** le rapport automatique généré
7. **Améliorer** selon les retours

---

## 🔧 Remarques Techniques

- Ne jamais inclure des fichiers `.py` comme objets dans le code
- Chaque fonction doit passer les tests **sans modifier le test**
- Respectez les signatures de fonctions fournies
- Commentez votre code pour expliquer vos choix d'optimisation

---

## 🎁 BONUS : Mesurer l'Impact Carbone

### CodeCarbon - Mesurez les émissions de votre code

Pour aller plus loin dans l'éco-responsabilité, utilisez **CodeCarbon** pour mesurer l'empreinte carbone de vos algorithmes !

#### Installation

```bash
pip install codecarbon
```

#### Utilisation basique

```python
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# Votre code ici
resultat = ma_fonction(grandes_donnees)

emissions = tracker.stop()
print(f"Émissions CO2: {emissions} kg")
```

#### Avec décorateur (recommandé)

```python
from codecarbon import track_emissions

@track_emissions
def ma_fonction_optimisee(data):
    # Votre algorithme
    return resultat

# Les émissions sont automatiquement enregistrées dans emissions.csv
ma_fonction_optimisee(mes_donnees)
```

#### Comparer deux approches

```python
from codecarbon import EmissionsTracker

# Approche naïve
tracker = EmissionsTracker()
tracker.start()
resultat1 = algorithme_naif(data)
emissions_naif = tracker.stop()

# Approche optimisée
tracker = EmissionsTracker()
tracker.start()
resultat2 = algorithme_optimise(data)
emissions_optimise = tracker.stop()

print(f"Naïf: {emissions_naif:.6f} kg CO2")
print(f"Optimisé: {emissions_optimise:.6f} kg CO2")
print(f"Réduction: {(1 - emissions_optimise/emissions_naif)*100:.1f}%")
```

#### Exemple avec les exercices

```python
from codecarbon import EmissionsTracker
from Exercices_Expert.plus_longue_sous_sequence import plus_longue_sous_sequence

# Tester sur de grandes données
data = list(range(10000, 0, -1))

tracker = EmissionsTracker()
tracker.start()
resultat = plus_longue_sous_sequence(data)
emissions = tracker.stop()

print(f"Longueur LIS: {resultat}")
print(f"Émissions: {emissions:.6f} kg CO2")
```

### Pourquoi mesurer ?

- **Visualiser** l'impact réel de vos optimisations
- **Comparer** différentes approches algorithmiques
- **Sensibiliser** à l'impact environnemental du code
- **Documenter** vos choix d'optimisation avec des données concrètes

> 💡 **Astuce** : Ajoutez CodeCarbon à vos tests de performance pour voir la différence entre O(n) et O(n²) en termes d'émissions !

---

**Bon courage et codez responsable !** 🌍💻
