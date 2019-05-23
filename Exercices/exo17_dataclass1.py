from dataclasses import dataclass


class Inv:
    n: str="a"
    px: float=1.0
    nb: int=1

    def cost(self) -> float:
        return self.px * self.nb


# la methode init est implicite
@dataclass
class Inventaire:
    nom: str="a"
    prix_unitaire: float=1.5
    nbr: int = 2

    def cout(self) -> float:
            return self.prix_unitaire * self.nbr

if __name__ == "__main__":

    a = Inv()
    print("attributs de a(Inv) : ",a.__dict__)
    print("a.cost() : ",a.cost())
    print("")
    
    b = Inventaire()
    print("attributs de b(Invenaire) : ",b.__dict__)
    print("b.cout() : ",b.cout())
