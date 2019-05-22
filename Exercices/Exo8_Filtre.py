liste = [1,2,3,4,5,6,7,8,9,10]

resultat = list(filter(lambda x: x%2 == 0 , liste ))

print('resultat : ', resultat)


# Ne fonctionne pa un filtre ne peut avoir q'un paramétre
# 
#a = [1,2,3,4,5,6]
#b = [1,2,3,4,50,60,66,99,23]
#resultat2 = list(filter(lambda x,y: x%2 == 0 and y > 50 , [a, b] ))