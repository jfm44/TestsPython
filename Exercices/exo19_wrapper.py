class Wrapper:
    def __init__(self,param1):
        self._container = param1
        self.Contenu = [i for i in range(10)]
        self.indice = 0
        print(param1)
        print("==========")

    def __enter__(self):
        print("traitement avant....")
        # Ce qui est utillise 'par le as'
        return [self.Contenu, self.indice]
    
    def __exit__(self, type, value, traceback):
        print("===========")
        print("    FIN")
        print("===========")

    def __str__(self):
        return "travaux en cours...>" + str(self.indice) + '< valeur >' + self.Contenu[self.indice] +  '<'
        
        
if __name__ == "__main__":
    with Wrapper("Traitements personnels....") as monWrap:
            for j in range(2,8,1):
                monWrap[1] = j
                print("travaux en cours...>" + str(monWrap[1]) + '< valeur >' + str(monWrap[0][monWrap[1]]) +  '<')
    
