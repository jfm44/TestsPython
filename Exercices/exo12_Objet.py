class Temperature:
    def __init__(self,value,unit='C'):
        self._value = float(value)
        self._unit = unit

    def __float__(self):
        if self._unit == 'C':
            return self._value

        if self._unit == 'K':
            return self._value - 273.15

        if self._unit == 'F':
            return (self._value - 32) *5/9

    def __repr__(self):
        return '%s %s' % (self._value,(self._unit !='K')*'°' + self._unit)
        
def maSomme(*iterable, depart=None, defaut=None):
    if depart is None:
        try:
            depart, *iterable = iterable
        except ValueError:
            return defaut

    for x in iterable:
        depart += x

    return depart


print(maSomme("a","b","c"))

print(maSomme("a","b","c",depart="b",defaut="rien"))

print(maSomme(depart="b",defaut="rien"))

print(maSomme(defaut="rien"))

print(maSomme(1,2,3))

t1 = Temperature(5)

t2 = Temperature(3,'K')

t3 = Temperature(30,'F')
print(t1)

print(t2)

print(t3)

try:
    print(maSomme(1,"3",t1,t2,t3))
except TypeError:
    print(maSomme(1.0,float("3"),float(t1),float(t2),float(t3)))

