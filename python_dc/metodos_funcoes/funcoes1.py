#Funções

def primeiraFunc():
    print('Hello World!!')

#chamando a função
primeiraFunc()

#segunda funcao

def primeiraFunc(nome):
    print('Hello %s!!' %(nome))

primeiraFunc('Marcos')



listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)