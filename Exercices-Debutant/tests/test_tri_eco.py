from tri_eco import tri_eco
import time, random

def run_tests():
    # Test correction
    assert tri_eco([3,1,2]) == [1,2,3]
    assert tri_eco([]) == []
    assert tri_eco([5,5,2]) == [2,5,5]

    # Test efficacité
    big_list = [random.randint(0,10000) for _ in range(10000)]
    start = time.time()
    tri_eco(big_list)
    duration = time.time() - start
    if duration < 0.2:
        print("Très écolo ✅")
    elif duration < 0.5:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
