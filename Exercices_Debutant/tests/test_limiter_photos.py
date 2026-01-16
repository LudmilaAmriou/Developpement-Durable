from Exercices_Debutant.limiter_photos import limiter_photos
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Limiter Photos")
    print("="*50)
    
    # Test 1: Correctness
    print("\n1️⃣ Test de correction...")
    test_cases = [
        # (input, expected_output)
        (list(range(10)), list(range(10))),  # Less than 1000
        (list(range(1500)), list(range(500, 1500))),  # More than 1000
        (list(range(1000)), list(range(1000))),  # Exactly 1000
        ([], []),  # Empty
        (['photo_1', 'photo_2', 'photo_3'], ['photo_1', 'photo_2', 'photo_3']),
    ]
    
    try:
        for photos, expected in test_cases:
            result = limiter_photos(photos.copy())
            assert result == expected, f"Failed: got {len(result)} photos, expected {len(expected)}"
            if len(expected) > 0:
                assert result == expected, f"Content mismatch"
        print("   ✅ Correction OK")
        print("   → Garde bien les 1000 dernières photos")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # Test 2: Edge case - exactly 1000
    print("\n2️⃣ Test du cas limite (exactement 1000)...")
    test_1000 = list(range(1000))
    result_1000 = limiter_photos(test_1000)
    assert len(result_1000) == 1000 and result_1000 == test_1000
    print("   ✅ OK - Garde toutes les photos si <= 1000")
    
    # Test 3: Performance comparison - This is the KEY test!
    print("\n3️⃣ Comparaison de performance (loop vs slicing)...")
    
    # Create large photo list
    large_photos = [f'photo_{i}.jpg' for i in range(100000)]
    
    # Test student's solution multiple times
    print("   → Test avec 100,000 photos (garde les 1000 dernières)")
    
    times_student = []
    for _ in range(100):  # Run many times for accurate measurement
        photos_copy = large_photos  # Don't copy, just reference
        start = time.perf_counter()
        result = limiter_photos(photos_copy)
        end = time.perf_counter()
        times_student.append(end - start)
    
    time_student = sorted(times_student)[50]  # Median
    
    # Compare with optimal slicing solution
    times_optimal = []
    for _ in range(100):
        photos_copy = large_photos  # Don't copy, just reference
        start = time.perf_counter()
        result_optimal = photos_copy[-1000:]  # Slicing
        end = time.perf_counter()
        times_optimal.append(end - start)
    
    time_optimal = sorted(times_optimal)[50]  # Median
    
    print(f"   Student solution:  {time_student*1000000:.2f} µs")
    print(f"   Slicing optimal:   {time_optimal*1000000:.2f} µs")
    
    overhead = time_student / time_optimal
    print(f"\n   📊 Ton code est {overhead:.1f}x plus lent que slicing")
    
    # Test 4: Check if they're using slicing
    print("\n4️⃣ Détection de la méthode utilisée...")
    
    # Heuristic: slicing is MUCH faster than loop
    # Both use slicing, so overhead should be ~1.0
    if overhead <= 1.5:
        print("   ✅ SLICING DÉTECTÉ!")
        print("   → Tu utilises photos[-1000:] ou équivalent")
        uses_slicing = True
    elif overhead <= 3.0:
        print("   ⚠️  OPTIMISÉ mais probablement pas pur slicing")
        print("   → Peut-être list comprehension?")
        uses_slicing = False
    else:
        print("   ❌ BOUCLE MANUELLE détectée")
        print("   → Tu copies élément par élément avec un for")
        uses_slicing = False
    
    # Final scoring
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    
    eco_score = 50  # Base for correctness
    
    # Score based on method used
    if uses_slicing:
        print("✅ TRÈS ÉCOLO - Utilise le slicing Python!")
        print("   → Slicing est implémenté en C (ultra-rapide)")
        print("   → Code lisible: photos[-1000:]")
        print("   → Une seule ligne!")
        eco_score = 100
    elif overhead <= 5.0:
        print("⚠️  CORRECT mais pas optimal")
        print("   → List comprehension ou autre méthode")
        print("   → Fonctionne mais plus lent que slicing")
        eco_score = 70
    else:
        print("❌ PAS ÉCOLO - Boucle manuelle inefficace")
        print("   → Copies élément par élément avec for loop")
        print(f"   → {overhead:.0f}x plus lent que slicing!")
        eco_score = 40
    
    # Performance penalty
    if overhead > 10.0:
        print(f"\n⚠️  WARNING: Beaucoup trop lent!")
        print(f"   → {overhead:.0f}x plus lent que la solution optimale")
        eco_score = min(eco_score, 30)
    
    print(f"\n💡 CONSEIL ECO:")
    if not uses_slicing:
        print("   Le problème avec la boucle:")
        print("   ❌ for i in range(n-1000, n):")
        print("      ❌ res.append(photos[i])")
        print("   → Python doit:")
        print("     • Itérer 1000 fois (overhead Python)")
        print("     • Calculer l'index à chaque fois")
        print("     • Appeler append() 1000 fois")
        print("     • Gérer la croissance de la liste")
        print()
        print("   La solution optimale:")
        print("   → Une seule ligne!")
        print("   → Implémenté en C (ultra-rapide)")
        print("   → Crée la nouvelle liste en une seule opération")
        print()
        print(f"  → Gain: {overhead:.0f}x plus rapide = {overhead:.0f}x moins d'énergie!")
    else:
        print("   🏆 Code parfait!")
        print("   → Le slicing Python est la méthode optimale")
        print("   → Simple, lisible, et ultra-rapide")
    
    print(f"\n🌱 ECO-SCORE: {eco_score}/100")
    
    if eco_score >= 90:
        print("🏆 Excellent! Utilisation parfaite du slicing!")
    elif eco_score >= 70:
        print("👍 Bon travail, mais une autre solution serait meilleur")
    elif eco_score >= 40:
        print("⚠️  Fonctionne mais très inefficace")
    else:
        print("📚 Tu peux faire mieux!")
    
    return eco_score >= 60

if __name__ == "__main__":
    run_tests()