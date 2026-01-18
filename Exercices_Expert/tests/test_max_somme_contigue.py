# test_max_somme_contigue.py

from Exercices_Expert.max_somme_contigue import max_somme_contigue
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Maximum Subarray (Kadane)")
    print("="*50)

    # 1️⃣ Test de correction
    print("\n1️⃣ Test de correction...")
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1,2,3,4,5], 15),
        ([-1,-2,-3,-4], -1),
        ([3,-1,2,-1,4], 7),
        ([0,0,0,0], 0),
        ([5], 5),
        ([], 0),
    ]
    
    for lst, expected in test_cases:
        result = max_somme_contigue(lst)
        assert result == expected, f"❌ Correction échouée pour {lst}: got {result}, expected {expected}"
    print("   ✅ Correction OK")

    # 2️⃣ Test de performance - force failure for O(n²/n³)
    print("\n2️⃣ Test de performance (O(n) attendu)...")
    
    # Large list that kills quadratic/cubic
    n = 10000  # big enough to blow up O(n²)
    large_input = [(-1)**i * i for i in range(1, n+1)]
    
    start = time.perf_counter()
    try:
        max_somme_contigue(large_input)
        duration = time.perf_counter() - start
    except MemoryError:
        print("❌ Algorithme NON optimisé - trop lent/mémoire insuffisante")
        return
    except RecursionError:
        print("❌ Algorithme NON optimisé - récursion trop profonde")
        return

    print(f"   ⏱️ Temps sur {n} éléments : {duration:.4f}s")
    
    # Threshold: anything >0.2s is considered non-optimal
    if duration < 0.05:
        print("✅ TRÈS ÉCOLO - Algorithme O(n) détecté !")
        eco_score = 100
    elif duration < 0.2:
        print("⚠️ MOYENNEMENT ÉCOLO - Algorithme correct mais pas optimal")
        eco_score = 70
    else:
        print("❌ PAS ÉCOLO - Algorithme naïf détecté (O(n²/n³))")
        eco_score = 30

    # 3️⃣ Conseils éco
    print("\n3️⃣ CONSEILS ÉCO-CODING:")
    if eco_score < 100:
        print("   💡 Astuce:")
        print("      - Utilise l'algorithme de Kadane O(n):")
        print("        max_current = max_global = lst[0]")
        print("        for i in range(1,len(lst)):")
        print("            max_current = max(lst[i], max_current + lst[i])")
        print("            max_global = max(max_global, max_current)")
        print("        return max_global")
        print("      - Pas de double boucle ni sum() répétitif !")
        print("      - Gain énorme sur la vitesse et l'énergie !")

    print("\n" + "="*50)
    print(f"🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Excellent! Algorithme très écolo!")
    elif eco_score >= 70:
        print("👍 Correct mais peut être optimisé")
    else:
        print("📚 Améliore ton code pour qu'il soit plus éco-responsable")

    return eco_score

if __name__ == "__main__":
    run_tests()
