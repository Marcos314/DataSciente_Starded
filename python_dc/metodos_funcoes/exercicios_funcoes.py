# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e  depois faça uma chamada à função para listar os números

# def imprimirPar():
#
#     lista = []
#     for i in range(0,22,2):
#         print(i)
#         lista.append(i)
#
#
#
#     print('Lista: ',lista)
#
# imprimirPar()

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e imprima a lista

# def gerarLista(lista):
#
#     cont = 0
#     while(cont < 1):
#
#         i = input('Digite 1º número:')
#         lista.append((i))
#         j = input('Digite 2º número:')
#         lista.append((j))
#         cont+=1
#     print(lista)
#
#
# lista1 = [1,2,3,4]
# gerarLista(lista1)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2  números como parâmetro e retornar a soma deles
from typing import Any, Callable

# soma = lambda x,y: x+y
#
# print(soma(9,3))




# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2;
    print ("Dentro da função o total é: ", total)
    return total

soma( 10, 20 )
print ("Fora da função o total é: ", total)