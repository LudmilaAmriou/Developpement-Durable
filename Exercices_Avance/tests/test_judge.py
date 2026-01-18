#!/usr/bin/env python3
"""
JUGE GLOBAL - Exercices Avancé
Exécute tous les tests et calcule le score écologique moyen
Génère un rapport Markdown
"""

import sys
import importlib
from datetime import datetime

# Liste des tests Avancé
AVANCE_TESTS = [
    'Exercices_Avance.tests.test_fusion_listes',
    'Exercices_Avance.tests.test_trouver_sous_sequence',
]

def generate_markdown_report(results, avg_score, passed):
    """Génère un rapport Markdown"""
    
    # Détermination de la note
    if avg_score >= 90:
        grade = "A+"
        badge = "🏆"
        badge_color = "brightgreen"
        comment = "EXCELLENT! Code ultra-optimisé!"
    elif avg_score >= 80:
        grade = "A"
        badge = "🌟"
        badge_color = "green"
        comment = "Très bon travail! Quelques optimisations possibles"
    elif avg_score >= 70:
        grade = "B"
        badge = "👍"
        badge_color = "yellowgreen"
        comment = "Bon niveau, continue d'optimiser"
    elif avg_score >= 60:
        grade = "C"
        badge = "⚠️"
        badge_color = "yellow"
        comment = "Passable - Beaucoup d'améliorations nécessaires"
    elif avg_score >= 50:
        grade = "D"
        badge = "😬"
        badge_color = "orange"
        comment = "Insuffisant - Revois les algorithmes"
    else:
        grade = "F"
        badge = "💀"
        badge_color = "red"
        comment = "ÉCHEC - Algorithmes catastrophiques!"
    
    # Génération du Markdown
    md = f"""# Rapport Éco-Coding - Exercices Avancé

![Score](https://img.shields.io/badge/Score-{int(avg_score)}%25-{badge_color}?style=for-the-badge)
![Grade](https://img.shields.io/badge/Note-{grade.replace('+', '%2B')}-{badge_color}?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-{'VALIDÉ' if passed else 'ÉCHOUÉ'}-{'success' if passed else 'critical'}?style=for-the-badge)

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Niveau:** Avancé  
**Moyenne:** {avg_score:.1f}/100  
**Note:** {grade}

---

## Résultat Global

> {comment}

**Validation:** {"Exercices VALIDÉS" if passed else "Exercices NON VALIDÉS"}

---

## Scores Détaillés

| Exercice | Score | Status | Barre de Progression |
|----------|-------|--------|---------------------|
"""
    
    # Ajout de chaque exercice
    for exercise, score in results.items():
        status = "OK" if score >= 60 else "FAIL"
        filled = int(score / 5)
        bar = "█" * filled + "░" * (20 - filled)
        md += f"| `{exercise}` | **{score:.0f}/100** | {status} | {bar} |\n"
    
    md += """
---

## 🌱 Impact Écologique

"""
    
    if avg_score >= 80:
        md += """### ✅ Excellent Impact!
Ton code économise beaucoup d'énergie! Continue comme ça! 🌍
- Algorithmes optimaux utilisés
- Faible consommation CPU
- Empreinte carbone minimale
"""
    elif avg_score >= 60:
        md += """### ⚠️ Impact Modéré
Ton code fonctionne mais peut être plus efficace.
- Quelques algorithmes à optimiser
- Consommation CPU moyenne
- Chaque optimisation = moins d'énergie consommée 💡
"""
    else:
        md += """### ❌ Impact Élevé!
Ton code gaspille BEAUCOUP d'énergie!
- Algorithmes inefficaces détectés
- Forte consommation CPU
- Empreinte carbone importante 🏭
- **ACTION REQUISE:** Optimise tes algorithmes!
"""
    
    md += """
---

## Exercices par Score

"""
    
    # Groupement par score
    excellent = [k for k, v in results.items() if v >= 90]
    good = [k for k, v in results.items() if 70 <= v < 90]
    passable = [k for k, v in results.items() if 60 <= v < 70]
    failing = [k for k, v in results.items() if v < 60]
    
    if excellent:
        md += "### Excellent (≥90)\n"
        for ex in excellent:
            md += f"- `{ex}` ({results[ex]:.0f}/100)\n"
        md += "\n"
    
    if good:
        md += "### Bon (70-89)\n"
        for ex in good:
            md += f"- `{ex}` ({results[ex]:.0f}/100)\n"
        md += "\n"
    
    if passable:
        md += "### Passable (60-69)\n"
        for ex in passable:
            md += f"- `{ex}` ({results[ex]:.0f}/100)\n"
        md += "\n"
    
    if failing:
        md += "### À Refaire (<60)\n"
        for ex in failing:
            md += f"- `{ex}` ({results[ex]:.0f}/100) - **OPTIMISATION REQUISE**\n"
        md += "\n"
    
    md += """
---

## Recommandations

"""
    
    if avg_score < 60:
        md += """### Priorité: Revoir les algorithmes avancés
1. Étudie les algorithmes classiques (merge, binary search, etc.)
2. Identifie les complexités O(n²) et O(n×m)
3. Exploite les propriétés des données (déjà trié, etc.)
4. Pense "divide and conquer" et optimisations

"""
    elif avg_score < 80:
        md += """### Améliorations possibles
1. Optimise les exercices avec score < 80
2. Compare ton code avec les solutions optimales
3. Cherche les optimisations O(n) vs O(n log n)
4. Évite les copies inutiles et les slicing en boucle

"""
    else:
        md += """### Continue sur ta lancée!
1. Excellent niveau atteint!
2. Tu maîtrises les algorithmes avancés!
3. Prêt pour le niveau Expert!
4. Tu contribues à un code plus écologique!

"""
    
    md += """---

## Prochaines Étapes

"""
    
    if passed:
        md += """- Exercices Avancé validés!
- Tu peux passer aux **Exercices Expert**
- Ou améliorer tes scores existants pour viser le 100/100
- Le niveau Expert te mettra face aux algorithmes les plus complexes!
"""
    else:
        md += """- Retravaille les exercices avec score < 60
- Retente le test une fois optimisé
- Objectif: Moyenne ≥ 60/100
"""
    
    md += f"""
---

<div align="center">

**Rapport généré automatiquement le {datetime.now().strftime('%d/%m/%Y à %H:%M')}**  
🌱 *Code écologique = Planète préservée* 🌍


</div>
"""
    
    return md

def run_all_tests():
    """Exécute tous les tests et collecte les scores"""
    print("="*70)
    print(" JUGE GLOBAL - EXERCICES AVANCÉ - ÉCO-CODING")
    print("="*70)
    print()
    
    results = {}
    total_score = 0
    
    for test_module_name in AVANCE_TESTS:
        exercise_name = test_module_name.split('.')[-1].replace('test_', '')
        
        print(f"\n{'='*70}")
        print(f" TEST: {exercise_name}")
        print(f"{'='*70}\n")
        
        try:
            test_module = importlib.import_module(test_module_name)
            score = test_module.run_tests()
            results[exercise_name] = score
            total_score += score
            print(f"\n {exercise_name}: {score}/100")
            
        except Exception as e:
            print(f"\n{exercise_name}: ERREUR - {e}")
            results[exercise_name] = 0
    
    # Calcul de la moyenne
    num_tests = len(AVANCE_TESTS)
    avg_score = total_score / num_tests if num_tests > 0 else 0
    
    # Rapport console
    print("\n" + "="*70)
    print("RAPPORT FINAL")
    print("="*70)
    print()
    
    print("Scores par exercice:")
    for exercise, score in results.items():
        status = "✅" if score >= 60 else "❌"
        bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
        print(f"  {status} {exercise:30s} [{bar}] {score:3.0f}/100")
    
    print()
    print(f"Score total: {total_score:.0f}/{num_tests * 100}")
    print(f"Moyenne:     {avg_score:.1f}/100")
    print()
    
    # Détermination de la note
    if avg_score >= 90:
        grade, emoji = "A+", "🏆"
        comment = "EXCELLENT! Code ultra-optimisé!"
    elif avg_score >= 80:
        grade, emoji = "A", "🌟"
        comment = "Très bon travail!"
    elif avg_score >= 70:
        grade, emoji = "B", "👍"
        comment = "Bon niveau"
    elif avg_score >= 60:
        grade, emoji = "C", "⚠️"
        comment = "Passable"
    elif avg_score >= 50:
        grade, emoji = "D", "😬"
        comment = "Insuffisant"
    else:
        grade, emoji = "F", "💀"
        comment = "ÉCHEC"
    
    print("="*70)
    print(f"{emoji} NOTE FINALE: {grade} ({avg_score:.1f}/100)")
    print(f"{emoji} {comment}")
    print("="*70)
    print()
    
    passed = avg_score >= 60
    
    if passed:
        print("VALIDATION: Exercices validés")
        print(f"   → {len([s for s in results.values() if s >= 60])}/{num_tests} exercices au-dessus de 60/100")
    else:
        print("VALIDATION: Exercices NON validés")
        print(f"   → Moyenne insuffisante ({avg_score:.1f}/100)")
        print(f"   → Minimum requis: 60/100")
    
    print()
    
    # Impact écologique
    print("🌱 IMPACT ÉCOLOGIQUE:")
    if avg_score >= 80:
        print("   Ton code économise beaucoup d'énergie!")
        print("   Continue comme ça!")
    elif avg_score >= 60:
        print("   Ton code fonctionne mais peut être plus efficace")
        print("   Chaque optimisation = moins d'énergie consommée")
    else:
        print("   Ton code gaspille BEAUCOUP d'énergie!")
        print("   Algorithmes inefficaces = forte empreinte carbone")
    
    print()
    
    # Génération du rapport Markdown
    print("Génération du rapport...")
    report_md = generate_markdown_report(results, avg_score, passed)
    
    report_filename = "ECO_REPORT_AVANCE.md"
    try:
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report_md)
        print(f"Rapport généré: {report_filename}")
        print(f"   → Ouvre ce fichier pour voir ton rapport détaillé!")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport: {e}")
    
    print()
    print("="*70)
    
    return 0 if passed else 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)