
import pickle

import exo11_Objet_6 as PersonneClass

if __name__ == "__main__":
    maListe = []
    for i in range(10) :

        maListe.append(PersonneClass.Personne("Prenom"+str(i),"NOM"+str(i)))

    #maChaine = "maChaine"

    monFichierPickle = open("MesPersonnes.sav","wb")
    #pickle.dump(maChaine,monFichierPickle)

    for j in maListe:
        pickle.dump(j,monFichierPickle)

    monFichierPickle.close()
