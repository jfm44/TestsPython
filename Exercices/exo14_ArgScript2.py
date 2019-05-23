#Ligne de commande

import getopt, sys

if __name__ == '__main__':
    try:
        options, arguments = getopt.getopt(sys.argv[1:], 'ho:', ['help', 'output='])
    except getopt.GetoptError as err:
        print("Erreur parametre...", err)
        sys.exit(2)

    for o,a in options:
        print("Les arguments....",o," ",a)
        if o in ('-h','--help'):
            #usage()
            print("Usage....")
            sys.exit()
        elif o in ('-o', '--output'):
            outputfile = a
            print("outputfile = ",a)
            
