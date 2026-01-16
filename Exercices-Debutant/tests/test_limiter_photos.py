from limiter_photos import limiter_photos
import time

def run_tests():
    assert limiter_photos([1,2,3]) == [1,2,3]
    assert limiter_photos(list(range(2000))) == list(range(1000,2000))

    big_list = list(range(5000))
    start = time.time()
    limiter_photos(big_list)
    duration = time.time() - start
    if duration < 0.05:
        print("Très écolo ✅")
    elif duration < 0.1:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
