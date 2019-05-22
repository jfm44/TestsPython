
def ParseString(nom):
    ret = ""
    if (len(nom) != 0):
        ListeCaractees = list(nom)
        for c in ListeCaractees :
            if c.isalpha():
                ret = ret + c
        ret = ret.capitalize()
    else:
        ret = "Nom non renseigne"        
    
    return(ret)

if __name__ == "__main__":

    nomSaisi = input("Votre nom : ")

    pseudo = ParseString(nomSaisi)

    print("==> Nom : " , nomSaisi)
    print("    Pseudo : " , pseudo)
