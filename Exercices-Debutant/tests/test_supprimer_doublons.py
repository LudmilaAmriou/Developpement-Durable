from supprimer_doublons import supprimer_doublons
import time

def run_tests():
    assert supprimer_doublons(['a','b','a']) == ['a','b']
    assert supprimer_doublons([]) == []

    big_list = ['f'+str(i%10) for i in range(10000)]
    start = time.time()
    supprimer_doublons(big_list)
    duration = time.time() - start
    if duration < 0.2:
        print("Très écolo ✅")
    elif duration < 0.5:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
