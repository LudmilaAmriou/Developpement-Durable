# test_fusion_listes.py
from fusion_list import fusion_listes

def run_tests():
    print("=== TEST FUSION_LISTES ===")
    
    # Correction tests
    assert fusion_listes([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
    assert fusion_listes([], [1,2,3]) == [1,2,3]
    assert fusion_listes([1,2,3], []) == [1,2,3]
    assert fusion_listes([], []) == []
    assert fusion_listes([1,2,2],[2,3]) == [1,2,2,2,3]
    
    print("Tous les tests de correction passent ✅")
    
    # Large test (performance hint)
    big1 = list(range(0,5000,2))  # 0,2,4,...
    big2 = list(range(1,5001,2))  # 1,3,5,...
    result = fusion_listes(big1, big2)
    assert result == list(range(5000)), "Erreur sur gros test !"
    print("Gros test OK ✅")

if __name__ == "__main__":
    run_tests()
