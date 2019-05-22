resultat = map(lambda x: x*2,[1,2,3,4,5])

print("resultats : ")
for i in resultat :
    print(i)

resultat2 = list(map(lambda x: x*2,[1,2,3,4,5]))
print("resultats2 : ", resultat2)

#   Attention map prend les cles par défaut sur les dictionnaire
resultat3 = list(map(lambda x: x*2,{'a':1,'b':2,'c':3,'d':4,'e':5}.values()))
print("resultats3 : ", resultat3)

#   Recherche dans une liste de dictionnaires par cle
ListeDeDictionnaires =[{'name':'python','point':10},{'name':'java','point':20}]
print(list(map(lambda x: x['name'] == 'python', ListeDeDictionnaires)))