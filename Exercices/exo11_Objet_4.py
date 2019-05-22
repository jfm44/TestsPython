class Employee:
    def __init__(self,prenom,nom):
        self._nom = nom
        self._prenom = prenom

    def affiche(self):
        print("Bonjour " + self._nom + " " + self._prenom) 
        

    def __str__(self):
        retour = "Bonjour " + self._nom + " " + self._prenom 
        return retour

    def __add__(self,personneAAjouter):
        #nom = self._nom + " " + personneAAjouter._nom
        #prenom = self._prenom + " " + personneAAjouter._prenom
        #return Employee(nom,prenom)
        return Employee(self._nom + " " + personneAAjouter._nom,
                        self._prenom + " " + personneAAjouter._prenom)
    
personne1 = Employee("Jean-Francois","MARECHAL")
print("personne1 : ", personne1)
personne2 = Employee("titi","azerty")
print("personne2 : ", personne2)
personne3 = personne1.__add__(personne2)
print("personne3 = personne1.__add__(personne2) : ", personne3)
personne4 = personne2 + personne1
print("personne4 = personne2 + personne1 : ", personne4)
