import sys

def fib(n):
    a,b,c = 0,1,[]
    while a < n : 
        c.extend([a])
        a, b = b , a + b
    return c

def gen_fibonacci(max= sys.maxsize):
    a,b = 0, 1 
    while a < max :
        yield a
        a,b = b, a + b
        

print("fonction fib : ",fib(1000))
print("Fonction gen_Fib : ", list(gen_fibonacci(1000)))
    