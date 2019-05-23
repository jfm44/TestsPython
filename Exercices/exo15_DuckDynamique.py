#Attributs dyamiques pendant l'execution

def fun(value: int):
    if not isinstance(value, int):
        raise TypeError("La valeur doit etre entirere")

    
class Duck:
    def __init__(self,**tArguments):
        self.__dict__.update(tArguments)

    def afficheAttributs(self):
        print(map(lambda x: print(x), self.__dict__))

if __name__ == "__main__":
    Canard1 = Duck(Attribut1="valeur1",Attribut2="valeur2")

    Canard2 = Duck(monAttribut1="valeur3",monAttribut2="valeur4",monAttribut3="valeur5")

    print("Caranard1 : ",Canard1)
    print("Caranard1 : ",Canard2)

    print(" ")
    print("Classe de Caranard1 : ",Canard1.__class__.__name__)
    print("liste des attributs de Carnard1 : ",Canard1.__dict__)
    print("liste des attributs de Carnard2 : ",Canard2.__dict__)

    print(" ")
    print("Acces attribut 'attribut1' de Carnard1 : ",getattr(Canard1,'Attribut1',"Valeur Par Defaut"))

    print("Acces attribut 'monAttribut1' de Carnard1 : ",getattr(Canard1,'monAttribut1',"N'existe pas donc Valeur Par Defaut"))

    Canard1.afficheAttributs()
