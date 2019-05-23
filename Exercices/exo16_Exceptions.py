personnages = ['Luke','Han','Yoda','Leia']

i = 0

try:
    resultat = personnages[100/i]

except ZeroDivisionError:
    print("erreur division zero")
    i = 1

except IndexError:
    print("erreur d'index")

except NameError:
    print("erreur de nom d'objet")

    
print("Fin")
    
