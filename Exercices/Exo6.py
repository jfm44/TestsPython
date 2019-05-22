#
#   Passage de fonction en parametre
#
def affichage(somme):
    print("Somme = {}".format(somme))

def fun(a,b, callback = None):
    print("ajout {} + {}".format(a,b))
    if callback:
        callback(a+b)

fun(1,2,affichage)
fun(2,3)
