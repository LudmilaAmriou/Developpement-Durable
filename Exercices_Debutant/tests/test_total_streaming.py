from Exercices_Debutant.total_streaming import somme_streaming
import time

def count_operations(func, data):
    """
    Count actual operations by instrumenting the function.
    Since we can't modify the student's code directly,
    we'll measure and compare with optimal solution.
    """
    pass

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Somme Streaming")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([10, -5, 3, -2], 6),
        ([0, 0, 0], 0),
        ([-1, -2, -3], -6),
        ([100], 100),
        ([], 0),
    ]
    
    try:
        for data, expected in test_cases:
            result = somme_streaming(data)
            assert result == expected, f"Failed: somme_streaming({data}) = {result}, expected {expected}"
        print("   ✅ Correction OK")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Check if they filter negatives (eco optimization mentioned in docstring)
    print("\n2️⃣ Test d'optimisation écologique...")
    print("   → Vérification: filtres-tu les valeurs négatives inutiles?")
    
    # Test with many negatives
    test_negatives = [-1, -2, -3, 5, -10, -20, 8, -5]
    result = somme_streaming(test_negatives)
    expected_naive = sum(test_negatives)  # -28
    expected_optimized = sum([x for x in test_negatives if x > 0])  # 13
    
    if result == expected_optimized:
        print("   ✅ Optimisation détectée: tu filtres les négatifs!")
        filters_negatives = True
        eco_boost = 50
    elif result == expected_naive:
        print("   ⚠️  Pas d'optimisation: tu additionnes les négatifs inutilement")
        filters_negatives = False
        eco_boost = 0
    else:
        print(f"   ❌ Résultat inattendu: {result}")
        return
    
    # Test 3: Built-in vs manual loop comparison
    print("\n3️⃣ Comparaison avec Python built-in sum()...")
    
    # Large dataset
    large_data = list(range(-50000, 50000))  # 100,000 elements
    
    # Student's solution
    start = time.perf_counter()
    for _ in range(10):
        result_student = somme_streaming(large_data)
    time_student = time.perf_counter() - start
    
    # Optimal solution with sum()
    start = time.perf_counter()
    for _ in range(10):
        result_builtin = sum(large_data)
    time_builtin = time.perf_counter() - start
    
    # Optimal with filter (if applicable)
    start = time.perf_counter()
    for _ in range(10):
        result_filtered = sum(x for x in large_data if x > 0)
    time_filtered = time.perf_counter() - start
    
    print(f"   Student solution:  {time_student*1000:.2f} ms")
    print(f"   Python sum():      {time_builtin*1000:.2f} ms")
    print(f"   sum() + filter:    {time_filtered*1000:.2f} ms")
    
    overhead = time_student / time_builtin
    print(f"\n   📊 Ton code est {overhead:.2f}x plus lent que sum()")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    eco_score = 50  # Base score for correctness
    
    # Score for using built-in
    if overhead <= 1.5:
        print("✅ TRÈS ÉCOLO - Tu utilises sum() ou équivalent!")
        print("   → Code Pythonic et optimisé")
        eco_score += 40
    elif overhead <= 3.0:
        print("⚠️  CORRECT mais pas optimal")
        print("   → Boucle manuelle détectée")
        print("   → sum() est ~2x plus rapide (implémenté en C)")
        eco_score += 20
    else:
        print("❌ INEFFICACE")
        print("   → Beaucoup trop lent comparé à sum()")
        eco_score += 0
    
    # Score for filtering negatives
    if filters_negatives:
        print("\n✅ BONUS: Tu filtres les valeurs négatives!")
        print("   → Économise des opérations inutiles")
        print("   → Dans un contexte streaming, c'est intelligent")
        eco_score += eco_boost
    else:
        print("\n⚠️  ATTENTION: Tu additionnes les valeurs négatives")
        print("   → Dans le contexte 'streaming', c'est du gaspillage")
        print("   → Les viewers négatifs n'existent pas!")
        print("   → Conseil: filtre avec 'if x > 0'")
    
    # Check if they used sum()
    print(f"\n💡 CONSEIL ECO:")
    if overhead > 1.5:
        print("   Optimisations possibles:")
        print("      → Il existe une fonction Python implémentée en C (beaucoup plus rapide)")
        print()
    
    if not filters_negatives:
        print("   Filtre les valeurs inutiles (contexte streaming)")
        print("      → Dans le streaming, valeurs négatives = erreur de capteur")
        print()
    
    if overhead <= 1.5 and filters_negatives:
        print("   🏆 Code parfait!")
        print("   → return sum(x for x in donnees if x > 0)")
    
    print(f"\n🌱 ECO-SCORE: {min(eco_score, 100)}/100")
    
    if eco_score >= 90:
        print("🏆 Excellent! Code ultra-optimisé!")
    elif eco_score >= 70:
        print("👍 Bon travail!")
    elif eco_score >= 50:
        print("⚠️  Fonctionne mais peut être amélioré")
    else:
        print("📚 Revois les built-ins Python et le filtrage")
    
    return eco_score >= 60

if __name__ == "__main__":
    run_tests()