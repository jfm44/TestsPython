if __name__ == "__main__" :

    keys = {'a','e','i', 'o', 'u', 'y'}
    values = [1]
    
    dictionnaire = dict.fromkeys(keys,values)
    print("dictionnaire  : ", dictionnaire )

    #Comme les valeurs sont des references a l'objet values
    #sa modification entraine la repercission sur les valeur de toutes les cles
    values.append(2)
    print("dictionnaire  : ", dictionnaire )
