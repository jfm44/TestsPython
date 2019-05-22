ListeCartes = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
listeCouleurs = ['Coeur','Carreau','Pique','trefle']

separateurs = [",","."," ",";"]
listeSaisie = input("donnez votre liste : ")

listeSaisie = [e for e in listeSaisie if e not in separateurs]
print(" ")
print("liste saisie ", listeSaisie)


JeuComplet = [(v,c) for v in ListeCartes for c in listeCouleurs]
print(" ")
print("Jeu complet ", JeuComplet)

JeuSansTetes = [(v,c) for v in ListeCartes if v.isdigit() for c in listeCouleurs]

print(" ")
print("Jeu Sans Tete ", JeuSansTetes)

JeuTrefleSansTetes = [(v,c) for v in ListeCartes if v.isdigit() for c in listeCouleurs if c == 'trefle']
print(" ")
print("Jeu Trefle Sans Tete ", JeuTrefleSansTetes)
