#Exemple Objet

class Test:
    val = 0

    def increment(self):
        Test.val += 1

t1 = Test()
t2 = Test()

print("t1.val : ",t1.val)
print("t2.val : ",t2.val)

print("Appel t1.increment() ")
t1.increment()
print("t1.val : ",t1.val)
print("t2.val : ",t2.val)
