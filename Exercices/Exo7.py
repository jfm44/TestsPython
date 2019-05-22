def carre1(val1,v2=0):
    return val1 * val1

carre = lambda val,v2=0: val * val

sommeNB = lambda a,b=0 : a + b

def fun(a,b = None, callback = None):
    print(str(callback.__name__), " de {}".format(a))
    if callback:
        print("retour : ",callback(a,b))

print("appel carre1 ==>")
fun(2,callback = carre1)

print("appel carre ==>")
fun(2,callback = carre)

print("appel sommNB ==>")
fun(1,2,callback = sommeNB)

