entree = input("donner le nombre de lignes : ")
if entree.isdigit():
    max = int(entree) 
    for i in range(0,max,1) :
        espaces = " " * (max % 2 - i*2)
        chapeau = "^" * (i + 1) 
        print(espaces,chapeau)

else :
    print("Ce n'est pas un nombre")
