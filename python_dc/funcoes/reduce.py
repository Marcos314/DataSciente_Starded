from functools import reduce

lista = [47,11,42,13]

print(lista)

def mult(a,b):
    return a+b

aux = reduce(mult,lista)

print(aux)

lista2 = [1,2,3,4,5]

aux2 = reduce((lambda x,y:x+y), lista)

print(aux2)