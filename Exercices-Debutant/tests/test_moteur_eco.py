from moteur_eco import recherche_eco
import time

def run_tests():
    assert recherche_eco(['Google','Ecosia','Qwant']) == ['Ecosia','Qwant']
    assert recherche_eco([]) == []

    big_list = ['Google','Ecosia','Qwant']*1000
    start = time.time()
    recherche_eco(big_list)
    duration = time.time() - start
    if duration < 0.2:
        print("Très écolo ✅")
    elif duration < 0.5:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
