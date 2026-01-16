# test_plus_long_sous_sequence.py
from plus_longue_sous_sequence import plus_long_sous_sequence

def run_tests():
    print("=== TEST PLUS_LONG_SOUS_SEQUENCE ===")
    
    # Correction tests
    assert plus_long_sous_sequence([10,9,2,5,3,7,101,18]) == 4
    assert plus_long_sous_sequence([]) == 0
    assert plus_long_sous_sequence([1,2,3,4,5]) == 5
    assert plus_long_sous_sequence([5,4,3,2,1]) == 1
    assert plus_long_sous_sequence([2,2,2,2]) == 1
    
    print("Tous les tests de correction passent ✅")
    
    # Edge case: repeated elements in long list
    big_list = [i%100 for i in range(200)]
    result = plus_long_sous_sequence(big_list)
    assert result <= 100
    
    print("Gros tests OK ✅")

if __name__ == "__main__":
    run_tests()
