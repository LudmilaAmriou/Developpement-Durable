from Exercices_Debutant.moteur_eco import recherche_eco
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Recherche Optimisée")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    lst = ['Google', 'Ecosia', 'Qwant']
    try:
        assert recherche_eco(lst, 'Ecosia') == True
        assert recherche_eco(lst, 'Qwant') == True
        assert recherche_eco(lst, 'Bing') == False
        assert recherche_eco([], 'Test') == False
        print("   ✅ Correction OK")
    except AssertionError:
        print("   ❌ Erreur de correction!")
        return
    
    # Test 2: Single search complexity (your current code should pass this)
    print("\n2️⃣ Test de recherche unique...")
    test_list = ['A'] * 10000 + ['B']
    
    start = time.perf_counter()
    for _ in range(3):
        recherche_eco(test_list, 'B')
    single_time = time.perf_counter() - start
    
    print(f"   ⏱️  3 recherches: {single_time*1000:.2f} ms")
    
    # Test 3: MULTIPLE SEARCHES - This is where optimization matters!
    print("\n3️⃣ Test de recherches MULTIPLES (vraie vie!)...")
    print("   → Scénario: 1000 recherches sur une liste de 10,000 moteurs")
    
    # Large list of search engines
    engines = [f'Engine_{i}' for i in range(10000)]
    search_queries = ['Engine_500', 'Engine_5000', 'Engine_9999', 'NotFound'] * 250  # 1000 searches
    
    # Measure time for 1000 searches
    start = time.perf_counter()
    for query in search_queries:
        recherche_eco(engines, query)
    multi_time = time.perf_counter() - start
    
    print(f"   ⏱️  1000 recherches: {multi_time*1000:.2f} ms")
    
    # Test 4: Complexity analysis
    print("\n4️⃣ Analyse de complexité...")
    
    # Compare with optimal solution (using set)
    engines_set = set(engines)
    
    start = time.perf_counter()
    for query in search_queries:
        query in engines_set  # O(1) lookup
    optimal_time = time.perf_counter() - start
    
    print(f"   ⏱️  Solution optimale (set): {optimal_time*1000:.2f} ms")
    
    efficiency_ratio = multi_time / optimal_time
    print(f"   📊 Ton code est {efficiency_ratio:.0f}x plus lent que l'optimal")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    # Determine if they used set optimization
    if efficiency_ratio < 5:
        # They probably used set or similar optimization
        print("✅ TRÈS ÉCOLO - Optimisation détectée!")
        print("   → Tu utilises probablement un set ou dict")
        print("   → Complexité O(1) par recherche")
        eco_score = 100
    elif efficiency_ratio < 50:
        print("⚠️  MOYENNEMENT ÉCOLO")
        print("   → Recherche linéaire basique détectée")
        print("   → Fonctionne mais pas optimal pour recherches multiples")
        eco_score = 60
    else:
        print("❌ PAS ÉCOLO pour recherches multiples!")
        print("   → Algorithme O(n) répété = O(n×m) total")
        print("   → Conseil: convertis la liste en set!")
        eco_score = 30
    
    print(f"\n💡 CONSEIL ECO:")
    if eco_score < 80:
        print("   Pour recherches multiples, pense à:")
        print("   1. Convertir la liste en set UNE FOIS")
        print("   2. Utiliser 'in' sur le set (O(1) au lieu de O(n))")
        print("   3. Exemple: moteurs_set = set(lst)")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 80:
        print("🏆 Excellent! Code optimisé pour le monde réel!")
    elif eco_score >= 60:
        print("👍 Fonctionnel mais peut être BEAUCOUP plus rapide")
    else:
        print("📚 Relis la consigne sur l'optimisation avec set")
    
    return eco_score

if __name__ == "__main__":
    run_tests()