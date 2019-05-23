try:
    with open("test.xml","r") as monFic:
        text = monFic.read()
        print(text)
except (IOError,OSError):
    print("Erreur fichier")


try:
    with open("test.xml","r") as monFic:
        for line in monFic:
            print(line)
except (IOError,OSError):
    print("Erreur fichier")



try:
    with open("test.xml","r") as monFic:
        for car in monFic.readline():
            print(car)

        print(monFic.readline())
        
except (IOError,OSError):
        print("Erreur fichier")


try:
    with open("test.xml","r") as monFic:
        for car in monFic.readlines():
            print(car)
except (IOError,OSError):
    print("Erreur fichier")
