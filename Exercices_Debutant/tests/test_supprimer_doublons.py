from Exercices_Debutant.supprimer_doublons import supprimer_doublons
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Suppression Doublons")
    print("="*50)
    
    # Test 1: Correctness - basic functionality
    print("\n1️⃣ Test de correction...")
    test_cases = [
        (['a.txt', 'b.txt', 'a.txt', 'c.txt'], ['a.txt', 'b.txt', 'c.txt']),
        (['x', 'x', 'x'], ['x']),
        (['a', 'b', 'c'], ['a', 'b', 'c']),
        ([], []),
        (['z'], ['z']),
    ]
    
    try:
        for input_list, expected in test_cases:
            result = supprimer_doublons(input_list)
            assert result == expected, f"Failed on {input_list}: got {result}, expected {expected}"
        print("   ✅ Correction OK")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Order preservation (critical for this exercise)
    print("\n2️⃣ Test de préservation de l'ordre...")
    test_order = ['z', 'a', 'z', 'b', 'a', 'c']
    result_order = supprimer_doublons(test_order)
    expected_order = ['z', 'a', 'b', 'c']  # First occurrence kept
    
    try:
        assert result_order == expected_order, f"Order not preserved: {result_order}"
        print("   ✅ Ordre préservé correctement")
    except AssertionError as e:
        print(f"   ❌ {e}")
        return
    
    # Test 3: Complexity Detection - O(n²) vs O(n)
    print("\n3️⃣ Analyse de complexité...")
    print("   → Test avec beaucoup de doublons (pire cas)")
    
    sizes = [1000, 2000, 4000, 8000]
    times = []
    
    for size in sizes:
        # WORST CASE: Maximum unique files (no early duplicates to skip)
        # This forces EVERY iteration to scan the full growing list
        test_list = []
        for i in range(size):
            # Each file is unique, so every 'if f not in res' scans all of res
            test_list.append(f'unique_file_{i}.txt')
        
        # Measure time
        measurements = []
        for _ in range(3):
            start = time.perf_counter()
            supprimer_doublons(test_list)
            end = time.perf_counter()
            measurements.append(end - start)
        
        median_time = sorted(measurements)[1]
        times.append(median_time)
        print(f"   Size {size:5d}: {median_time*1000:8.2f} ms")
    
    # Analyze growth rate
    print("\n4️⃣ Analyse du ratio de croissance...")
    
    ratios = []
    for i in range(len(times) - 1):
        ratio = times[i+1] / times[i]
        size_ratio = sizes[i+1] / sizes[i]
        ratios.append(ratio)
        print(f"   {sizes[i]:5d} → {sizes[i+1]:5d}: temps x{ratio:.2f} (taille x{size_ratio:.1f})")
    
    avg_ratio = sum(ratios) / len(ratios)
    
    # Check absolute performance
    print(f"\n⏱️  Temps absolu ({sizes[-1]} fichiers): {times[-1]*1000:.2f} ms")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    # Detect complexity based on growth pattern
    if avg_ratio <= 2.3:
        # Linear O(n) - optimal with set or dict
        print("✅ TRÈS ÉCOLO - Complexité O(n) détectée!")
        print("   → Tu utilises probablement dict ou set")
        print("   → Algorithme optimal tout en préservant l'ordre!")
        eco_score = 100
        
    elif avg_ratio <= 3.0:
        # Slightly suboptimal
        print("⚠️  PRESQUE OPTIMAL")
        print("   → Complexité proche de O(n)")
        print("   → Peut-être quelques opérations en trop?")
        eco_score = 75
        
    elif avg_ratio >= 3.5:
        # Quadratic O(n²) detected!
        print("❌ PAS ÉCOLO - Complexité O(n²) détectée!")
        print("   → Problème: 'if f not in res' parcourt toute la liste!")
        print("   → À chaque itération, Python scanne res du début à la fin")
        print(f"   → Avec {sizes[-1]} fichiers: {sizes[-1]**2/1000000:.1f} millions de comparaisons! 😱")
        print()
        eco_score = 30
        
    else:
        print("⚠️  COMPLEXITÉ AMBIGUË")
        print(f"   → Ratio moyen: {avg_ratio:.2f}")
        eco_score = 50
    
    # Additional performance check
    if times[-1] > 0.8:  # More than 800ms for 8000 unique files
        print(f"\n⚠️  WARNING: Trop lent en pratique!")
        print(f"   → {times[-1]:.2f}s pour {sizes[-1]} fichiers")
        print(f"   → Avec 100,000 fichiers, ça prendrait {times[-1] * (100000/sizes[-1])**2 / 60:.1f} MINUTES!")
        eco_score = min(eco_score, 20)
    
    elif times[-1] > 0.3:
        print(f"\n⚠️  Lent pour des grandes listes")
        print(f"   → {times[-1]*1000:.0f}ms pour {sizes[-1]} fichiers")
        eco_score = min(eco_score, 35)
    
    print(f"\n💡 CONSEIL ECO:")
    if eco_score < 80:
        print("   Le problème avec ton code:")
        print("   ❌ 'if f not in res' sur une liste est O(n)")
        print("   ❌ Pour chaque fichier, tu scannes toute la liste res")
        print("   ❌ Complexité totale: O(n × n) = O(n²)")
        print()
        print("   Solutions optimales O(n):")
        print()
        print("   💡 Solution 1: Set pour tracker (le plus simple)")
        print()
        print("   💡 Solution 2: dict.fromkeys() (Pythonic)")
        print("        → dict garde l'ordre en Python 3.7+")
        print("        → Une seule ligne!")
        print()
        print("   Gain: O(n) vs O(n²)")
        print("   → Avec 10,000 fichiers: 10,000 ops vs 100 millions!")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Parfait! Déduplication ultra-optimisée!")
    elif eco_score >= 70:
        print("👍 Bon travail! Proche de l'optimal")
    elif eco_score >= 40:
        print("⚠️  Fonctionne mais O(n²) est trop lent!")
    else:
        print("📚 Utilise un set ou dict pour O(1) lookup!")
    
    return eco_score >= 60

if __name__ == "__main__":
    run_tests()