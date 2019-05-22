def multiarguments(*arguments, **dicoArguments):
    for n in arguments:
        print("positionnels : ", n)

    for k in dicoArguments.keys():
        print("dico ", k, "==>" , dicoArguments[k])


def multiarguments2(**dicoArguments):
    for k in dicoArguments.keys():
        print("dico ", k, "==>" , dicoArguments[k])

if __name__ == "__main__":
    print("Appel tuple ===>")
    multiarguments("a",1)

    print("Appel dico ===>")
    multiarguments(a=125,b=65465)
    
    print("Appel mixte1 ===>")
    multiarguments("valeur",a=125,b=65465)

    print("Appel mixte2 ===>")
    multiarguments({"c":531,"d":"hsfekjh"},a=125,b=65465)

    print("Appel mixte3 ===>")
    #multiarguments(c=531,d="hsfekjh","valeur2")

    print("Appel multiarguments2 dico ===>")
    multiarguments2(a=125,b=65465,c=10,f=20)
