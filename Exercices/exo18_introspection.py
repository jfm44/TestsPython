class MaClasse:
    '''Documentation de la classe MaClasse'''
    
    def methodedInstance(self):
        return "Méthode d'instance",self.__dict__

    @classmethod
    def classmethode(cls):
        return "méthode de classe appelée",cls.__dict__

    @staticmethod
    def staticmethode():
        return "méthode statique appelée"

class Pizza:
    def __init__(self, *ingredients):
        self.ingredients = ingredients

    @classmethod
    def margarita(cls):
        return cls(['mozarella','tomates'])

    @classmethod
    def margarita(cls):
        self._container = cls

    @staticmethod
    def info(menu):
        return "voici la fabrique a pizza", menu["disponible"]

    def __repr__(self):
        return "Pizza(%r)" % self.ingredients
    
if __name__ == "__main__":

    a = MaClasse()

    print("Appel methodedInstance : ",a.methodedInstance())

    print("Appel classmethode : ",a.classmethode())

    b=Pizza(["tomates","olives"])

    print("Pissa b : ",b)
