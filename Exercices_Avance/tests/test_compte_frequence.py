from Exercices_Avance.compte_frequence import compte_frequence
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Compte Fréquence")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    test_cases = [
        ([1, 2, 2, 3, 1], {1: 2, 2: 2, 3: 1}),
        (['a', 'b', 'a', 'c', 'b', 'a'], {'a': 3, 'b': 2, 'c': 1}),
        ([1], {1: 1}),
        ([], {}),
        ([5, 5, 5, 5], {5: 4}),
        ([1, 2, 3, 4, 5], {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
    ]
    
    try:
        for input_list, expected in test_cases:
            result = compte_frequence(input_list)
            assert result == expected, f"Failed on {input_list}: got {result}, expected {expected}"
        print("   ✅ Correction OK")
        print("   → Compte correctement les fréquences")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Complexity Analysis - O(n²) vs O(n)
    print("\n2️⃣ Analyse de complexité...")
    print("   → Test avec différents patterns de données")
    
    sizes = [1000, 2000, 4000, 8000]
    times = []
    
    for size in sizes:
        # WORST CASE for lst.count(): Many unique elements
        # Each element appears only once, so count() scans entire list every time
        test_list = list(range(size))  # All unique
        
        # Measure time
        measurements = []
        for _ in range(3):
            start = time.perf_counter()
            compte_frequence(test_list)
            end = time.perf_counter()
            measurements.append(end - start)
        
        median_time = sorted(measurements)[1]
        times.append(median_time)
        print(f"   Size {size:5d}: {median_time*1000:8.2f} ms")
    
    # Analyze growth rate
    print("\n3️⃣ Analyse du ratio de croissance...")
    
    ratios = []
    for i in range(len(times) - 1):
        ratio = times[i+1] / times[i]
        size_ratio = sizes[i+1] / sizes[i]
        ratios.append(ratio)
        print(f"   {sizes[i]:5d} → {sizes[i+1]:5d}: temps x{ratio:.2f} (taille x{size_ratio:.1f})")
    
    avg_ratio = sum(ratios) / len(ratios)
    
    # Check absolute performance
    print(f"\n⏱️  Temps absolu ({sizes[-1]} éléments): {times[-1]*1000:.2f} ms")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    # Detect complexity based on growth pattern
    if avg_ratio <= 2.3:
        # Linear O(n) - optimal with dict or Counter
        print("✅ TRÈS ÉCOLO - Complexité O(n) détectée!")
        print("   → Tu utilises probablement un dict avec compteur")
        print("   → Ou Counter de collections")
        print("   → Algorithme optimal!")
        eco_score = 100
        
    elif avg_ratio <= 3.0:
        # Slightly suboptimal
        print("⚠️  PRESQUE OPTIMAL")
        print("   → Complexité proche de O(n)")
        eco_score = 75
        
    elif avg_ratio >= 3.5:
        # Quadratic O(n²) - using lst.count()
        print("❌ PAS ÉCOLO - Complexité O(n²) détectée!")
        print("   → Problème: lst.count(x) parcourt TOUTE la liste!")
        print("   → À chaque élément unique, count() scanne les n éléments")
        print(f"   → Avec {sizes[-1]} éléments: {sizes[-1]**2/1000000:.1f} millions de comparaisons! 😱")
        eco_score = 30
        
    else:
        print("⚠️  COMPLEXITÉ AMBIGUË")
        print(f"   → Ratio moyen: {avg_ratio:.2f}")
        eco_score = 50
    
    # Additional performance check
    if times[-1] > 1.0:  # More than 1 second
        print(f"\n⚠️  WARNING: Trop lent en pratique!")
        print(f"   → {times[-1]:.2f}s pour {sizes[-1]} éléments")
        print(f"   → Avec 100,000 éléments, ça prendrait {times[-1] * (100000/sizes[-1])**2 / 60:.1f} MINUTES!")
        eco_score = min(eco_score, 20)
    
    elif times[-1] > 0.5:
        print(f"\n⚠️  Lent pour des grandes listes")
        print(f"   → {times[-1]*1000:.0f}ms pour {sizes[-1]} éléments")
        eco_score = min(eco_score, 40)
    
    print(f"\n💡 CONSEIL ECO:")
    if eco_score < 80:
        print("   Le problème avec lst.count():")
        print("   → Pire cas (tous uniques): n × n = O(n²)")
        print()
        print("   Solutions optimales O(n):")
        print()
        print("   💡 Solution 1: Dict avec compteur manuel")
        print()
        print("   💡 Solution 2: Dict avec get()")
        print()
        print("   💡 Solution 3: Counter (le plus simple!)")
        print()
        print("   Toutes ces solutions: O(n)")
        print("   → Parcourt la liste UNE SEULE FOIS")
        print(f"   → Avec {sizes[-1]} éléments: {sizes[-1]} ops vs {sizes[-1]**2//1000000}M ops!")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Parfait! Comptage ultra-optimisé!")
    elif eco_score >= 70:
        print("👍 Bon travail! Proche de l'optimal")
    elif eco_score >= 40:
        print("⚠️  Fonctionne mais O(n²) est trop lent!")
    else:
        print("📚 As tu laissé lst.count() dans la boucle?!")
    
    return eco_score

if __name__ == "__main__":
    run_tests()