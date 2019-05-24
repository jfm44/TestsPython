#Exemple complet
import time
############################################################################################
class CreditAccount:
    def __init__(self, encours):
        self._ident = "COUR_" + time.time()
        self._encours = encours

    def __str__(self):
        retour = "Compte courant [" + self._ident + "] valeur : " + self._balance
        return retour

    def depot(self,valeur):
        self._encours += valeur

    def retrait(self,valeur):
        self._encours -= valeur

    def balance(self):
        pass

class SavingAccount:
    def __init__(self, encours, interest):
        self._ident = "EPAR_" + time.time()
        self._encours = encours
        self._interest = interest

    def depot(self,valeur):
        self._encours += valeur

    def retrait(self,valeur):
        self._encours -= valeur

    def balance(self):
        pass

    def revenus():
        pass
    
    def __str__(self):
        retour = "Compte d'Epargne [" + self._ident + "] valeur : " + self._balance + " interets : " + self._interest
        return retour
    
############################################################################################
#                                     Interface sur les comptes
############################################################################################
class InterfaceCompte:
    def depot(compte,valeur):
        compte.depot(valeur)
    
    def retrait(compte):
        compte.retrait(valeur)
    
    def balance(compte):
        compte.balance()

############################################################################################
#                                     Classes sur les personnes
############################################################################################
class Personne:
    def __init__(self,nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def __str__(self):
        retour = self._nom + " " + self._prenom 
        return retour

class Client(Personne):
    def __init__(self,nom,prenom,dateInscription,dateNaissance):
        Personne.__init__(self,nom, prenom)
        self._dInsc = dateInscription
        self._dNaiss = dateNaissance
        self._ident = "CLI_" + str(time.time())
        self._listeComptesClients = (None,None,None,None,None)
        
    def __str__(self):
        retour = Personne.__str__(self) + " inscrit le " + self._dInsc + " identifiant : " + self._ident
        return retour
    
    def add_acount(self,compte):
        retour = True
        if (self._listeComptesClients.count(None) != 0):
            inice = self._listeComptesClients.index(None)
            maListe = list(self._listeComptesClients)
            maListe[index] = compte
            self._listeComptesClients = tuple(maListe)
        else:
            retour = False
         
        return retour
    
    def delete_account(self,noCompte)
        retour = True
        try:
            indice = self._listeComptesClients.index(noCompte)
            maListe = list(self._listeComptesClients)
            maListe[indice] = None
            self._listeComptesClients = tuple(maListe)
        except :
            retour = False
         
        return retour
    
    def seniority(self)
        pass
    
class Advisor(Personne):
    def __init__(self, nom, prenom, dateNaissance, dateInscription):
        Personne.__init__(self,nom,prenom,rang)
        self._Rang = ra,g
        self._ident = "ADV_" + str(time.time())
        self._clientsGeres = []
        

    def __str__(self):
        retour = Personne.__str__(self) + " Ne le " + self._dNaiss + " inscrit le " + self._dInsc + " identifiant : " + self._ident
        return retour

    def createAccount(self, client, typeCompte='C', montant=0):
        retour = True
        #creer un compte pour un client
        retour = client.CreditAccount(montant)    

        return retour

#####################################################################################################################################
#                                               Test
#####################################################################################################################################
if __name__ == "__main__":
    monClient = Client("Bossousoff","morlabar","23/05/2019","01/01/1970")

    print(" Client : ", monClient)
