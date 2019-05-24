import multiprocessing as mp
import random
import  time

def temp(city):
    print("lance",city)
    time.sleep(random.randint(0,3))
    return random.randint(0,25)

if __name__ == "__main__":
    with mp.Pool(3) as pool:
        for city in ['Belgium','Australia','China']:
            print(">",city,pool.apply_async(temp,(city,)))

