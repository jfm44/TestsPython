# Les decorateurs
# Chaine de caracteres qui placee apres une fonction permet de changer cette fonction
def mon_decorateur(fonc):
    def wrapper():
        print("Quelque chose arrive avant l'appel d la fonction")
        fonc()
        print("Quelque chose arrive apres l'appel d la fonction")
    return wrapper

def dit_Woua():
    print("Woua!!")
dit_Woua = mon_decorateur(dit_Woua)

if __name__ == "__main__":
    dit_Woua()