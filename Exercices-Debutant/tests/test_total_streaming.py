from total_streaming import total_streaming
import time, random

def run_tests():
    assert total_streaming([1,2,-1]) == 3
    assert total_streaming([]) == 0

    big_list = [random.randint(-5,10) for _ in range(10000)]
    start = time.time()
    total_streaming(big_list)
    duration = time.time() - start
    if duration < 0.2:
        print("Très écolo ✅")
    elif duration < 0.5:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
