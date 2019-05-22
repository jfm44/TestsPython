def tab(fonction, inf,sup,pas):
    for i in range(inf,sup,pas):
        y = fonction(i)
        print("f({}) = {}".format(i,y))


def maFonction(x):
    return 2 * x + 3


if __name__ == "__main__":
    tab(maFonction,-4,4,2)

    tab(toto,-4,4,2)

    tab("toto",-4,4,2)
    
        
