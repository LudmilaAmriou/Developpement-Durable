# test_trouver_sous_sequence.py
from trouver_sous_sequence import trouver_sous_sequence

def run_tests():
    print("=== TEST TROUVER_SOUS_SEQUENCE ===")
    
    # Correction tests
    assert trouver_sous_sequence([1,2,3,4,5],[3,4]) == True
    assert trouver_sous_sequence([1,2,3],[4,5]) == False
    assert trouver_sous_sequence([],[]) == True
    assert trouver_sous_sequence([1,2,3],[]) == True
    assert trouver_sous_sequence([], [1]) == False
    
    print("Tous les tests de correction passent ✅")
    
    # Edge case: repeated elements
    assert trouver_sous_sequence([1,1,1,1,1],[1,1,1]) == True
    
    # Large sequence
    seq = list(range(100000))
    subseq = [99990,99991,99992]
    assert trouver_sous_sequence(seq, subseq) == True
    
    print("Gros tests OK ✅")

if __name__ == "__main__":
    run_tests()
