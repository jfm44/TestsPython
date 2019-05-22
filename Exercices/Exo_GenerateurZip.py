#Test ZIP

scores = [100,25,17,28,43]
players = ["Sachin","Sehwang","Gambir","David","Raina"]

for pl, sc in zip(players,scores):
    print("Joueur %s score %d" %(pl,sc))


groupe = ['A','B','C','D']

ListeA = list(zip(players,scores,groupe))

print(ListeA)

GenerateurListe = zip(players,scores,groupe)
print(next(GenerateurListe))
print(next(GenerateurListe))
print(next(GenerateurListe))
print(next(GenerateurListe))              
print(next(GenerateurListe))              
