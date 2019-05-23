#Ligne de commande

import sys

if __name__ == '__main__':
    i = 1 
    for argument in sys.argv:
        print("Argument",i, " : ", argument)
        i += 1
