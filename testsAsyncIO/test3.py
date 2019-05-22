import asyncio
import time

async def maTache(nom,num):
    nbSec = num * 2
    aff = "Tache " + nom + " en cours pour " + str(nbSec) + " secondes..."
    print("affichage inerne coroutine : ", aff)
    nbSec = num * 2
    time.sleep(nbSec)
     
    return aff

async def Lanceur(maCoroutine):   
    for future in asyncio.as_completed(maCoroutine):
        print("affichage lanceur coroutine", await future)
        
if __name__ == "__main__" : 
    loop = asyncio.get_event_loop()
    mesCoroutines =[maTache("tache" + str(i),i) for i in range(5)]

    loop.run_until_complete(Lanceur(mesCoroutines))
    print("Fin des Taches")
    loop.close()
