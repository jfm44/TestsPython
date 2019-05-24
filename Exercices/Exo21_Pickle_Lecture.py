import pickle

import exo11_Objet_6 as PersonneClass

if __name__ == "__main__":
    print("Lecture fichier des personnes")
    monFichier = open("MesPersonnes.sav","rb")

    maListe2 = []
    print("taille fichier :",monFichier.__sizeof__())

    while ():
        pers = pickle.load(monFichier)
        print("Lecture de pers >",pers,"<")
        maListe2.append(pers)
        

    fic.close()
        
    print("Affichage de la liste des personnes")
    for i in maListe2:
        print(i)

