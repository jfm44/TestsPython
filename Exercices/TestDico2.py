import datetime

if __name__ == "__main__" :

    keys = {'a','e','i', 'o', 'u', 'y'}
    values = [1]

    dictionnaire = {cle : list(values) for cle in keys}
    print("dictionnaire  : ", dictionnaire)

    values.append(2)

    #for cle in keys : dictionnaire.update({cle:values})
    
    #dictionnaire.update({cle2 : list(values) for cle2 in keys})
    
    #dictionnaire = {cle : list(values) for cle in keys}
    
    #for cle in list(dictionnaire) : dictionnaire.update({cle:values})
    
    for cle in dictionnaire.keys() : dictionnaire.update({cle:values})

    print("dictionnaire  : ", dictionnaire)
