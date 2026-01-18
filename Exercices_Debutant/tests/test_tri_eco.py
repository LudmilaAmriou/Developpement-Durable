from Exercices_Debutant.tri_eco import tri_eco
import time
import random

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Tri Efficace")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    test_cases = [
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([3, 3, 1, 2], [1, 2, 3, 3]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Worst case for bubble sort
    ]
    
    try:
        for input_list, expected in test_cases:
            result = tri_eco(input_list.copy())
            assert result == expected, f"Failed on {input_list}: got {result}, expected {expected}"
        print("   ✅ Correction OK - Le tri fonctionne")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Complexity Analysis - WORST CASE (reversed list)
    print("\n2️⃣ Analyse de complexité (cas le pire - liste inversée)...")
    print("   → Liste triée en ordre décroissant (maximum de swaps)")
    
    sizes = [500, 1000, 2000, 4000]
    times = []
    
    for size in sizes:
        # WORST CASE: Completely reversed list
        # Forces maximum number of comparisons AND swaps for bubble sort!
        test_list = list(range(size, 0, -1))  # [500, 499, 498, ..., 2, 1]
        
        # Measure time (single run - it's already slow enough)
        start = time.perf_counter()
        tri_eco(test_list.copy())
        end = time.perf_counter()
        
        elapsed = end - start
        times.append(elapsed)
        print(f"   Size {size:5d}: {elapsed*1000:8.2f} ms")
    
    # Analyze growth rate
    print("\n3️⃣ Analyse du ratio de croissance...")
    
    ratios = []
    for i in range(len(times) - 1):
        ratio = times[i+1] / times[i]
        size_ratio = sizes[i+1] / sizes[i]
        ratios.append(ratio)
        print(f"   {sizes[i]:4d} → {sizes[i+1]:4d}: temps x{ratio:.2f} (taille x{size_ratio:.1f})")
    
    avg_ratio = sum(ratios) / len(ratios)
    
    # Check absolute performance
    print(f"\n⏱️  Temps absolu ({sizes[-1]} éléments): {times[-1]*1000:.2f} ms")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    # Detect complexity based on growth pattern
    # O(n log n): ratio should be ~2.2 when size doubles
    # O(n²): ratio should be ~4.0 when size doubles
    
    if avg_ratio <= 2.5:
        # Optimal O(n log n) - using efficient sort
        print("✅ TRÈS ÉCOLO - Complexité O(n log n) détectée!")
        print("   → Tu utilises un algorithme de tri efficace")
        print("   → Algorithme optimal!")
        eco_score = 100
        
    elif avg_ratio <= 3.0:
        # Decent but not quite optimal
        print("⚠️  BON MAIS PAS OPTIMAL")
        print("   → Complexité entre O(n log n) et O(n²)")
        print("   → Peut-être insertion sort ou shell sort?")
        eco_score = 70
        
    elif avg_ratio >= 3.5:
        # Quadratic O(n²) - bubble sort, selection sort, etc.
        print("❌ PAS ÉCOLO - Complexité O(n²) détectée!")
        print("   → Algorithme de tri inefficace!")
        print("   → Probablement: bubble sort, selection sort, ou insertion sort")
        print(f"   → Avec {sizes[-1]} éléments: {sizes[-1]**2/1000000:.1f} millions de comparaisons! 😱")
        print()
        print("   💡 Le problème des double boucles:")
        print("      for i in range(n):")
        print("          for j in range(n-i-1):  ← O(n²) ici!")
        eco_score = 30
        
    else:
        print("⚠️  COMPLEXITÉ AMBIGUË")
        print(f"   → Ratio moyen: {avg_ratio:.2f}")
        eco_score = 50
    
    # Additional check: absolute performance
    if times[-1] > 2.0:  # More than 2 seconds for 4000 items
        print(f"\n⚠️  WARNING: BEAUCOUP trop lent!")
        print(f"   → {times[-1]:.2f}s pour seulement {sizes[-1]} éléments")
        print(f"   → Avec 100,000 éléments, ça prendrait {times[-1] * (100000/sizes[-1])**2 / 60:.1f} MINUTES!")
        eco_score = min(eco_score, 20)
    
    elif times[-1] > 0.5:
        print(f"\n⚠️  Lent en pratique")
        print(f"   → {times[-1]*1000:.0f}ms pour {sizes[-1]} éléments")
        eco_score = min(eco_score, 40)
    
    print(f"\n💡 CONSEIL ECO:")
    if eco_score < 80:
        print("   Le problème avec bubble sort:")
        print("   ❌ Double boucle imbriquée = O(n²)")
        print("   ❌ Compare TOUS les éléments avec TOUS les autres")
        print("   ❌ Avec 1000 éléments = 1 million de comparaisons!")
        print()
        print("   Solutions optimales O(n log n):")
        print("   ✅ Implémente merge sort ou quick sort")
        print("   ✅ Avec 1000 éléments = seulement ~10,000 comparaisons")
        print()
    
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Parfait! Tri ultra-optimisé!")
    elif eco_score >= 70:
        print("👍 Bon algorithme, proche de l'optimal")
    elif eco_score >= 40:
        print("⚠️  Fonctionne mais O(n²) est trop lent!")
    else:
        print("📚 Bubble sort n'est PAS éco-responsable!")
    
    return eco_score 

if __name__ == "__main__":
    run_tests()