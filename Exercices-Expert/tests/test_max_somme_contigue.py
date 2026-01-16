# test_max_somme_contigue.py
from max_somme_contigue import max_somme_contigue

def run_tests():
    print("=== TEST MAX_SOMME_CONTIGUE ===")
    
    # Correction tests
    assert max_somme_contigue([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_somme_contigue([1,2,3,4]) == 10
    assert max_somme_contigue([-1,-2,-3]) == -1
    assert max_somme_contigue([]) == float('-inf')
    
    print("Tous les tests de correction passent ✅")
    
    # Edge case: alternating positive/negative large list
    big_list = [(-1)**i * i for i in range(1000)]
    result = max_somme_contigue(big_list)
    assert isinstance(result, int)
    
    print("Gros tests OK ✅")

if __name__ == "__main__":
    run_tests()
