entree = input("donner un entier : ")
if entree.isdigit():
    if int(entree) % 2 == 0 :  # pair
        print("Ce nombre est pair")
    elif int(entree) % 3 == 0 : #impaire multiple de trois
            print("Ce nombre est impair et multiple de trois")
    else :
        print("Ce nombre n'est ni pair ni multiple de trois")
else :
    print("Ce n'est pas un nombre")
