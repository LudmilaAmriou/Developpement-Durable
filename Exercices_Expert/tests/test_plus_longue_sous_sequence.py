from Exercices_Expert.plus_longue_sous_sequence import plus_long_sous_sequence
import time

def run_tests():
    print("="*50)
    print("🧪 ECO-CODING TESTS - Plus Longue Sous-Séquence Croissante")
    print("="*50)

    # 1️⃣ Test de correction
    print("\n1️⃣ Test de correction...")
    small_tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0,1,0,3,2,3], 4),
        ([1,2,3,4,5], 5),
        ([5,4,3,2,1], 1),
        ([3,10,2,1,20], 3),
    ]
    try:
        for lst, expected in small_tests:
            result = plus_long_sous_sequence(lst)
            assert result == expected, f"❌ Correction échouée pour {lst}"
        print("   ✅ Correction OK")
    except AssertionError as e:
        print(f"   ❌ Erreur: {e}")
        return

    # 2️⃣ Test de performance (détection O(2^n))
    print("\n2️⃣ Test de performance (détection O(2^n))...")
    test_input = list(range(6000, 0, -1))  # 25 éléments: naïf O(2^n) explosera
    start = time.perf_counter()
    try:
        plus_long_sous_sequence(test_input)
        duration = time.perf_counter() - start
    except RecursionError:
        duration = float('inf')
        print("   ⚠️ Algorithme naïf détecté - récursion trop profonde !")

    print(f"   ⏱️ Temps sur 25 éléments : {duration:.4f}s")

    # 3️⃣ Analyse du code et conseils écolo
    print("\n3️⃣ Analyse du code et conseils...")
    if duration > 0.5:
        print("   ⚠️ Trop lent ! Algorithme NON optimisé (O(2^n) ou DP O(n²))")
        print("   💡 Conseil : utiliser Patience Sorting / DP + Binary Search → O(n log n)")
        eco_score = 30
    elif duration > 0.01:
        print("   ⚠️ Moyen : probablement DP O(n²)")
        print("   💡 Conseil : convertir en O(n log n) avec bisect / patience sorting")
        eco_score = 70
    else:
        print("   ✅ Très écolo : probablement O(n log n)")
        print("   💡 Tu utilises patience sorting ou binary search correctement")
        eco_score = 100

    # 4️⃣ Résultat final
    print("\n" + "="*50)
    print("📊 RÉSULTAT FINAL")
    print("="*50)
    print(f"🌱 ECO-SCORE: {eco_score}/100")

    if eco_score >= 90:
        print("🏆 Excellent! Algorithme optimal détecté")
    elif eco_score >= 70:
        print("👍 Correct mais peut être plus rapide")
    else:
        print("📚 Besoin d’optimisation !")

    return eco_score 

if __name__ == "__main__":
    run_tests()
