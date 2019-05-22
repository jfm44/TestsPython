if __name__ == "__main__" :
    i = 1
    res = 0 
    while i < 100 :
        res = float(res/100) + float(i)
        i = i + 1
        print("En cours  :" ,res)

    print("resultat :" ,res)