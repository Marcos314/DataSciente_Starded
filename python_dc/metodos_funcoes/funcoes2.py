# var_g = 10
#
#
# def mult(n1, n2):
#     # var_g é na vdd uma váriavel local
#
#     var_g = n1 * n2
#
#     print(var_g)
#
#
# mult(2, 3)
#
# print(var_g)

import math
def numPrimo(num):
    # verificando primeiro caso de não ser primo
    if (num % 2) == 0 and num > 2:
        return "Número não é primo"

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Tbm ñ primo"
    return "É primo!!"


numPrimo(7)
