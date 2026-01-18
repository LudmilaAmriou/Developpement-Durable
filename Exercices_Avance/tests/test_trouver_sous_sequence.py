from Exercices_Avance.trouver_sous_sequence import trouver_sous_sequence
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Trouver Sous-Séquence")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4], True),
        ([1, 2, 3], [4, 5], False),
        ([1, 2, 3, 4, 5], [1, 2], True),
        ([1, 2, 3, 4, 5], [4, 5], True),
        ([1, 2, 3, 4, 5], [5], True),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([1, 2, 3], [1, 2, 3, 4], False),
        ([], [1], False),
        ([1], [], True),  # Empty subseq is in everything
        ([], [], True),
    ]
    
    try:
        for seq, subseq, expected in test_cases:
            result = trouver_sous_sequence(seq, subseq)
            assert result == expected, f"Failed on {seq}, {subseq}: got {result}, expected {expected}"
        print("   ✅ Correction OK")
        print("   → Détecte correctement les sous-séquences")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Complexity Analysis - O(n×m) vs O(n+m)
    print("\n2️⃣ Analyse de complexité...")
    print("   → Test avec différentes tailles de séquences")
    
    # Test with WORST CASE: subseq at the end
    sizes = [5000, 10000, 20000, 40000]
    subseq_size = 100
    times = []
    
    for size in sizes:
        # WORST CASE: subsequence at the very end
        seq = list(range(size))
        subseq = list(range(size - subseq_size, size))
        
        # Measure time
        measurements = []
        for _ in range(3):
            start = time.perf_counter()
            trouver_sous_sequence(seq, subseq)
            end = time.perf_counter()
            measurements.append(end - start)
        
        median_time = sorted(measurements)[1]
        times.append(median_time)
        print(f"   Size {size:5d} (subseq={subseq_size}): {median_time*1000:8.2f} ms")
    
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
    print(f"\n⏱️  Temps absolu ({sizes[-1]} éléments, subseq {subseq_size}): {times[-1]*1000:.2f} ms")
    
    # Test 3: Compare with optimal solution
    print("\n4️⃣ Comparaison avec solution optimale...")
    
    def trouver_optimal(seq, subseq):
        """Optimal sliding window - compare element by element"""
        if not subseq:
            return True
        if len(subseq) > len(seq):
            return False
        
        m = len(subseq)
        for i in range(len(seq) - m + 1):
            # Compare element by element, stop early if mismatch
            match = True
            for j in range(m):
                if seq[i + j] != subseq[j]:
                    match = False
                    break
            if match:
                return True
        return False
    
    # Test with large sequence
    large_seq = list(range(50000))
    large_subseq = list(range(49900, 50000))  # At the end
    
    # Student's solution
    start = time.perf_counter()
    for _ in range(10):
        result_student = trouver_sous_sequence(large_seq, large_subseq)
    time_student = time.perf_counter() - start
    
    # Optimal
    start = time.perf_counter()
    for _ in range(10):
        result_optimal = trouver_optimal(large_seq, large_subseq)
    time_optimal = time.perf_counter() - start
    
    print(f"   Student solution:  {time_student*1000:.2f} ms")
    print(f"   Optimal (early stop): {time_optimal*1000:.2f} ms")
    
    overhead = time_student / time_optimal
    print(f"\n   📊 Ton code est {overhead:.2f}x plus lent que l'optimal")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    eco_score = 50  # Base for correctness
    
    # Detect based on overhead
    if overhead <= 1.5:
        # Optimal - early stopping
        print("✅ TRÈS ÉCOLO - Algorithme optimal détecté!")
        print("   → Tu utilises probablement une comparaison élément par élément")
        print("   → Avec arrêt précoce en cas de non-correspondance")
        eco_score = 100
        uses_optimal = True
        
    elif overhead <= 2.5:
        # Using slicing - creates copies but not terrible
        print("⚠️  PAS OPTIMAL - Slicing détecté")
        print("   → Tu utilises seq[i:i+m] == subseq")
        print("   → Problème: crée une COPIE de m éléments à chaque itération")
        print(f"   → {overhead:.1f}x plus lent que l'optimal")
        eco_score = 50
        uses_optimal = False
        
    else:
        # Very inefficient
        print("❌ INEFFICACE - Slicing avec overhead important")
        print("   → Tu utilises seq[i:i+m] == subseq")
        print("   → Problème: crée une COPIE de m éléments à chaque itération")
        print(f"   → {overhead:.1f}x plus lent que l'optimal")
        eco_score = 30
        uses_optimal = False
    
    # Performance penalty
    if times[-1] > 1.0:
        print(f"\n⚠️  WARNING: Lent pour grandes séquences")
        print(f"   → {times[-1]:.2f}s pour {sizes[-1]} éléments")
        eco_score = min(eco_score, 50)
    
    print(f"\n💡 CONSEIL ECO:")
    if not uses_optimal:
        print("   La solution optimale: comparaison directe")
        print("   ✅ Pas de copie, compare élément par élément")
        print("   ✅ Arrêt précoce dès qu'un élément diffère")
        print()
        print(f"   Gain: {overhead:.0f}x plus rapide + économie mémoire!")
    else:
        print("   🏆 Code parfait!")
        print("   → Comparaison élément par élément")
        print("   → Arrêt précoce = économie de calculs")
        print("   → Pas de copies inutiles")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Excellent! Recherche ultra-optimisée!")
    elif eco_score >= 70:
        print("👍 Fonctionne bien, optimisation possible")
    else:
        print("📚 Évite les slices dans les boucles!")
    
    return eco_score

if __name__ == "__main__":
    run_tests()