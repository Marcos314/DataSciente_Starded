# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

# dia = input('Qual o dia da semana?')
# if dia == 'Domingo' or dia == 'sabado':
#     print('Hoje é dia de descanso!!')
# else:
#     print('Você precisa trabalhar!')


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lista = ['banana','goiaba','uva','laranja','morango']

for i in lista:
    if i == 'morango':
        print('faz parte!')
        break
    else:
        pass



# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma  lista

tp = (2,4,6,8)
lista = []
for i in tp:
    i *= 2
    lista.append(i)
print(lista)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela


for i in range(100,150,2):
    print(i)
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, imprima as temperaturas na tela

temperatura  = 40

while(temperatura>35):
    print('Temperatura = %i' %temperatura)
    temperatura-=1