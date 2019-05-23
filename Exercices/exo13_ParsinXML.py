import xml.etree.ElementTree as ET

arbre = ET.parse("test.xml")

racine = arbre.getroot()

print("Racine :",racine.tag)

for monElement in racine:
    print("Enfant de la racine : ", monElement.tag, " valeur : ", monElement.attrib)
    for mesInfos in monElement:
        print(" Informations  de l'element : ", mesInfos.tag, " valeur : ", mesInfos.attrib, " Texte >", mesInfos.text, "<" ) 


print("Autre methode")
for mesElem in racine.findall('country'):
    print(mesElem.get('name')," était n°", mesElem.find('rank').text," pour l'annee ",mesElem.find('year').text)
