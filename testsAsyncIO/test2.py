import asyncio
import time

async def maTache(nom):
    aff = "Tache " + nom
    print("aff : ", aff)
    time.sleep(2)
     
    return aff

async def Lanceur():
    for i in range(5):
        nom = "tache" + str(i)
        recept = asyncio.ensure_future(maTache(nom))
        print("retour ",recept)
        
if __name__ == "__main__" : 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Lanceur())
    print("Fin des Taches")
    loop.close()
