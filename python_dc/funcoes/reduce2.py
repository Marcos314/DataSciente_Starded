from functools import reduce

lista = [1,4,8,3,50,45,78,65,43]

max = lambda x,y: x if (x > y) else y

result = reduce(max,lista)

print(result)