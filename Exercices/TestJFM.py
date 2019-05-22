import asyncio


###################################################################
#                 Definition de la requete                        #
###################################################################
class maRequete :
    
    __init__(self):
        self.nom = ""
        self.executeur = ""
        self.cible = ""
        self.typeRequete = ""
        self.requete = ""

###################################################################
#                 Definition de la requete                        #
###################################################################
class maListeRequetes :

    __init__(self):
        self.nom = ""
        self.Liste = []

    ajoute(self,element):
        
