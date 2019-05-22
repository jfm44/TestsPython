import time

class Personne:
    def __init__(self,nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def __str__(self):
        retour = self._nom + " " + self._prenom 
        return retour

class Client(Personne):
    def __init__(self,nom,prenom,dateInscription):
        Personne.__init__(self,nom, prenom)
        self._dInsc = dateInscription
        self._ident = "CLI_" + str(time.time())
        
    def __str__(self):
        retour = Personne.__str__(self) + " inscrit le " + self._dInsc + " identifiant : " + self._ident
        return retour

class Employe(Personne):
    def __init__(self,nom,prenom,dateNaissance,dateInscription):
        Personne.__init__(self,nom,prenom)
        self._dNaiss = dateNaissance
        self._dInsc = dateInscription
        self._ident = "EMP_" + str(time.time())

    def __str__(self):
        retour = Personne.__str__(self) + " Ne le " + self._dNaiss + " inscrit le " + self._dInsc + " identifiant : " + self._ident
        return retour

class Vendeur(Employe):
    def __init__(self,nom,prenom,dateNaissance,dateInscription):
        Employe.__init__(self,nom,prenom,dateNaissance,dateInscription)
        
    def __str__(self):
        retour = Employe.__str__(self)
        return retour

personne1 = Personne("JF","MARECH")
print("personne1 : ",personne1)

personne2 = Client("Client","Monsieur","01/05/2019")
print("personne2 : ",personne2)

personne3 = Employe("EMPLOYEE","Madame","01/01/1965","01/01/2019")
print("personne3 : ",personne3)

personne4 = Vendeur("VENDEUR","Inconnu","01/01/1980","30/09/2018")
print("personne4 : ",personne4)

print("personne4._nom : ",personne4._nom)

