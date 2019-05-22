class Employee:
    def __init__(self,prenom,nom):
        self._nom = nom
        self._prenom = prenom

    def affiche(self):
        print("Bonjour " + self._nom + " " + self._prenom + " avec affiche")
        

    def __str__(self):
        retour = "Bonjour " + self._nom + " " + self._prenom + " avec self.__str__"
        return retour

personne = Employee("Jean-Francois","MARECHAL")
personne.affiche()
print("Acces direct :",personne._nom)
print("personne :  ",personne)
print(dir(Employee))

personne = Employee("titi","azerty")
print(personne)
