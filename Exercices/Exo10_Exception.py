import sys

def error():
        a=42
        raise RuntimeError("Mon message d'erreur",a)
    
def div(x,y):
    if y == 0:
        raise RuntimeError("Pas de division par zero")
    result = x // y

try:
    print("resultat : ",div(4,2))
except RuntimeError as err :
    print(err)


try:
    print("resultat : ",div(5,0))
except RuntimeError as err :
    print(err)

