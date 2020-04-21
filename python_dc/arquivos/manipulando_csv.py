import csv

# with open('files/numeros.csv','w') as arquivo:
#     escrita = csv.writer(arquivo)
#     escrita.writerow(('primeira', 'segunda','terceira'))
#     escrita.writerow((55,93,76))
#     escrita.writerow((62,14,86))

#Leitura do arquivo csv escrito acima

# with open('files/numeros.csv', 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     for x in leitor:
#         print('Número de colunas', len(x))
#         print(x)
#Gerando uma lista de dados com o csv

with open('files/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

#Imprimindo a lista a partir do elemento na pos 1

for linha in dados[1:]:
    print(linha)