from random import randint
import threading as th
from time import sleep

counter = 0 
results = {}

def compute (name):
    global counter
    counter += 1
    attend = randint(3,10)
    sleep(attend)
    print("..Pour...",name,"...compteur...",counter,'...Attente...',attend)
    results[name] = counter

if __name__ == "__main__":
    threads = [th.Thread(target=compute,args=(name,)) for name in ['Dan','Tom']]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Fin results=> ", results)




