# test_compte_frequence.py
from compte_frequence import compte_frequence

def run_tests():
    print("=== TEST COMPTE_FREQUENCE ===")
    
    # Correction tests
    assert compte_frequence([1,2,2,3,1]) == {1:2, 2:2, 3:1}
    assert compte_frequence([]) == {}
    assert compte_frequence([5,5,5,5]) == {5:4}
    
    print("Tous les tests de correction passent ✅")
    
    # Edge case: large input
    big_list = [i%100 for i in range(10000)]
    freq = compte_frequence(big_list)
    assert freq[0] == 100
    assert freq[99] == 100
    
    print("Gros tests OK ✅")

if __name__ == "__main__":
    run_tests()
