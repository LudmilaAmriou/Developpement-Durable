# 🌱 Développement Durable – Exercices Python

Bienvenue dans le projet **Développement Durable en Python** !  
L'objectif : apprendre à coder **correctement** tout en adoptant des pratiques **éco-responsables** — un code **lisible**, **optimisé** et peu énergivore.

---

## 📁 Structure du projet

Exercices_Debutant/
│
├─ limiter_photos.py
├─ nettoyer_mails.py
├─ supprimer_doublons.py
├─ moteur_eco.py
├─ tri_eco.py
├─ total_streaming.py
└─ tests/
├─ test_limiter_photos.py
├─ test_nettoyer_mails.py
└─ ...

Exercices_Avance/
│
├─ compte_frequence.py
├─ trouver_sous_sequence.py
└─ tests/
├─ test_compte_frequence.py
├─ test_trouver_sous_sequence.py
└─ ...

Exercices_Expert/
│
├─ plus_longue_sous_sequence.py
├─ max_somme_contigue.py
└─ tests/
├─ test_plus_longue_sous_sequence.py
├─ test_max_somme_contigue.py
└─ ...

- **Exercices_Debutant** : bases de Python et optimisation simple.
- **Exercices_Avance** : algorithmes intermédiaires et structures de données.
- **Exercices_Expert** : algorithmes complexes et optimisation critique.
- **tests/** : scripts de test pour **correction** et **performance**.

---

## 🌱 Principes Éco-Coding

1. **Réduire la complexité algorithmique**

   - Évitez les boucles imbriquées inutiles (O(n²), O(2^n)).
   - Utilisez `set`, `dict`, ou algorithmes optimisés (`merge`, `binary search`, Kadane).

2. **Éviter les calculs répétitifs**

   - Stockez les résultats intermédiaires (cache, memoization).
   - Exemple :
     ```python
     moteurs_set = set(lst)  # Convertir une fois pour O(1) par recherche
     ```

3. **Exploiter les fonctions Python natives**

   - Slicing :
     ```python
     photos[-1000:]  # Ultra-rapide vs boucle for
     ```
   - Fonctions intégrées (`max`, `sum`, `Counter`, `bisect`) sont optimisées en C.

4. **Mesurer la performance**
   - Comparez votre fonction à une solution optimale pour détecter si votre code est linéaire, polynomial ou exponentiel.

---

## 📌 Exercices Débutant

### 1️⃣ `limiter_photos.py`

- **Objectif** : garder les 1000 dernières photos.
- **Optimisation** : slicing → O(1)
- **Test clé** : performance sur 100,000 photos.

### 2️⃣ `nettoyer_mails.py`

- **Objectif** : supprimer doublons et mails `"spam"`/`"pub"`.
- **Optimisation** : set pour suppression de doublons en O(n).

### 3️⃣ `supprimer_doublons.py`

- **Objectif** : supprimer doublons en conservant l'ordre.
- **Optimisation** : set + liste → O(n)

### 4️⃣ `compte_frequence.py`

- **Objectif** : compter la fréquence des éléments.
- **Optimisation** : `dict` ou `Counter` → O(n)

### 5️⃣ `fusion_listes.py`

- **Objectif** : fusionner deux listes triées.
- **Optimisation** : merge type O(n+m) plutôt que concat + sort O((n+m)log(n+m))

---

## 📌 Exercices Expert

### 1️⃣ `plus_longue_sous_sequence.py`

- **Objectif** : longueur de la plus longue sous-séquence croissante (LIS)
- **Version naïve** : récursion brute O(2^n) → très lente
- **Version optimale** : patience sorting + binary search → O(n log n)

### 2️⃣ `max_somme_contigue.py`

- **Objectif** : sous-liste contiguë avec somme maximale
- **Version naïve** : tester toutes les sous-listes O(n² ou n³)
- **Version optimale** : **Algorithme de Kadane** O(n)

---

## 🧪 Tests

Chaque fonction est accompagnée d’un script de test :

1. **Correction** : résultats attendus pour cas simples et limites.
2. **Performance** : comparer à une solution optimale.
3. **Détection de méthode** : slicing, set, DP, naïf.

---

## 💡 Conseils pour les étudiants

- Toujours mesurer la **complexité** du code.
- Préférez **structures natives optimisées** (set, dict, bisect, slicing).
- Pour plusieurs recherches ou filtres, utilisez **cache/memoization**.
- Testez votre code sur de **grandes entrées** avant soumission.
- Le but : **correct + rapide + éco-responsable** !

---

## 🌱 Score Éco

Chaque exercice a un **éco-score** basé sur :

- ✅ **Correction** : le code fonctionne correctement
- ⚡ **Performance** : le code est rapide et proche de l’optimal
- 🏆 **Méthode** : utilise les techniques Python optimales (`set`, slicing, DP, binary search`)

**Score** : 0 → 100

- 100 = solution optimale
- 60-90 = correcte mais peut être optimisée
- <60 = solution naïve / peu éco-responsable

---

## 🔧 Remarques

- Ne jamais inclure des fichiers `.py` comme objets dans le code.
- Chaque fonction doit passer les tests **sans modifier le test**.
