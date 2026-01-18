from Exercices_Debutant.nettoyer_mails import nettoyer_mails
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Nettoyage d'Emails")
    print("="*50)
    
    # Test 1: Correctness - Basic functionality
    print("\n1️⃣ Test de correction...")
    test_mails = ['alice@mail.com', 'spam', 'bob@mail.com', 'alice@mail.com', 'pub', 'charlie@mail.com']
    expected = ['alice@mail.com', 'bob@mail.com', 'charlie@mail.com']
    result = nettoyer_mails(test_mails)
    
    try:
        assert set(result) == set(expected), f"Got {result}, expected {expected}"
        assert len(result) == len(expected), "Doublons non supprimés!"
        assert 'spam' not in result, "Spam pas filtré!"
        assert 'pub' not in result, "Pub pas filtré!"
        print("   ✅ Correction OK")
        print(f"   Input:  {test_mails}")
        print(f"   Output: {result}")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Edge cases
    print("\n2️⃣ Test des cas limites...")
    try:
        assert nettoyer_mails([]) == []
        assert nettoyer_mails(['spam', 'pub']) == []
        assert nettoyer_mails(['test@mail.com']) == ['test@mail.com']
        assert nettoyer_mails(['a@m.com', 'a@m.com', 'a@m.com']) == ['a@m.com']
        print("   ✅ Cas limites OK")
    except AssertionError:
        print("   ❌ Erreur sur les cas limites!")
        return
    
    # Test 3: Complexity Detection - The critical test!
    print("\n3️⃣ Analyse de complexité (O(n²) vs O(n))...")
    
    sizes = [2000, 4000, 8000, 16000]
    times = []
    
    for size in sizes:
        # WORST CASE: All unique emails (no early returns)
        # This forces the O(n²) behavior!
        test_list = []
        for i in range(size):
            if i % 50 == 0:
                test_list.append('spam')
            elif i % 50 == 1:
                test_list.append('pub')
            else:
                # ALL UNIQUE emails to maximize comparisons
                test_list.append(f'unique_user_{i}@mail.com')
        
        # Measure time (multiple runs for accuracy)
        measurements = []
        for _ in range(3):
            start = time.perf_counter()
            nettoyer_mails(test_list)
            end = time.perf_counter()
            measurements.append(end - start)
        
        median_time = sorted(measurements)[1]
        times.append(median_time)
        print(f"   Size {size:5d}: {median_time*1000:.2f} ms")
    
    # Analyze growth rate
    print("\n4️⃣ Analyse du ratio de croissance...")
    
    ratios = []
    for i in range(len(times) - 1):
        ratio = times[i+1] / times[i]
        size_ratio = sizes[i+1] / sizes[i]
        ratios.append(ratio)
        print(f"   {sizes[i]} → {sizes[i+1]}: temps x{ratio:.2f} (taille x{size_ratio:.1f})")
    
    avg_ratio = sum(ratios) / len(ratios)
    
    # Check absolute performance
    print(f"\n⏱️  Temps absolu ({sizes[-1]} emails): {times[-1]*1000:.2f} ms")
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    # Detect complexity based on growth pattern
    # For O(n): ratio should be ~2 (doubling size doubles time)
    # For O(n²): ratio should be ~4 (doubling size quadruples time)
    
    if avg_ratio <= 2.3:
        # Linear O(n) - optimal with set
        print("✅ TRÈS ÉCOLO - Complexité O(n) détectée!")
        print("   → Tu utilises probablement un set pour déduplication")
        print("   → Algorithme optimal!")
        eco_score = 100
        
    elif avg_ratio <= 3.0:
        # Slightly suboptimal but acceptable
        print("⚠️  PRESQUE OPTIMAL")
        print("   → Complexité proche de O(n)")
        print("   → Peut-être quelques opérations en trop?")
        eco_score = 75
        
    elif avg_ratio >= 3.5:
        # Quadratic O(n²) detected!
        print("❌ PAS ÉCOLO - Complexité O(n²) détectée!")
        print("   → Problème: 'if mail not in res' est O(n)")
        print("   → Chaque vérification parcourt toute la liste!")
        print(f"   → Avec {sizes[-1]} emails = {sizes[-1]**2/1000000:.1f} millions de comparaisons! 😱")
        eco_score = 40
        
    else:
        # Ambiguous
        print("⚠️  COMPLEXITÉ AMBIGUË")
        print("   → Pas clair si O(n) ou O(n²)")
        print(f"   → Ratio moyen: {avg_ratio:.2f} (attendu: 2 pour O(n), 4 pour O(n²))")
        eco_score = 60
    
    # Additional performance check
    if times[-1] > 1.0:  # More than 1 second for 16000 items
        print(f"\n⚠️  WARNING: Trop lent en pratique!")
        print(f"   → {times[-1]:.2f}s pour {sizes[-1]} emails")
        print(f"   → Imagine avec 1 million d'emails...")
        eco_score = min(eco_score, 30)
    
    print(f"\n💡 CONSEIL ECO:")
    if eco_score < 80:
        print("   Le problème dans ton code:")
        print("   ❌ 'if mail not in res' parcourt TOUTE la liste res")
        print("   ❌ Avec n emails, tu fais n×n/2 comparaisons = O(n²)")
        print()
        print("   La solution optimale:")
        print("   ✅ Utilise un set pour tracker les emails déjà vus")
        print("   ✅ 'if mail not in seen_set' est O(1) au lieu de O(n)")
        print("   ✅ Total: O(n) au lieu de O(n²)")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Parfait! Code ultra-optimisé!")
    elif eco_score >= 70:
        print("👍 Bon travail! Proche de l'optimal")
    elif eco_score >= 40:
        print("⚠️  Fonctionne mais beaucoup trop lent!")
    else:
        print("📚 Revois les structures de données (set vs list)")
    
    return eco_score

if __name__ == "__main__":
    run_tests()