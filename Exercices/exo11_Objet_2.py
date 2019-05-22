class Employee:
    def __init__(self,prenom,nom):
        self._nom = nom
        self._prenom = prenom

    def affiche(self):
        print("Bonjour ",self._nom," ",self._prenom, " avec self._")


personne = Employee("Jean-Francois","MARECHAL")
personne.affiche()
print("Acces direct :",personne._nom)
print("personne :  ",personne)
