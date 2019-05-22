nombres = [sum(range(nombre)) for nombre in range(0,10,2)]

print("type(nombres) :",type(nombres))
print("nombres : ", nombres)

nombresG = (sum(range(nombre)) for nombre in range(0,10,2))
print("type(nombresG) :",type(nombresG))
print("nombresG : ", nombresG)
