from nettoyer_mails import nettoyer_mails
import time

def run_tests():
    assert nettoyer_mails(['spam','ok','pub']) == ['ok']
    assert nettoyer_mails([]) == []

    big_list = ['spam','ok','pub']*5000
    start = time.time()
    nettoyer_mails(big_list)
    duration = time.time() - start
    if duration < 0.2:
        print("Très écolo ✅")
    elif duration < 0.5:
        print("Écolo 👍")
    else:
        print("Peut mieux faire ⚠️")

if __name__ == "__main__":
    run_tests()
