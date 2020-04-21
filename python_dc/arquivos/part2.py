# f = open('files/salarios.csv' , 'r')
# data = f.read()
# linhas = data.split('\n')
#
# #print(linhas)
# lista_1 = []
#
# for i in linhas:
#     split_row = i.split(",")
#     lista_1.append(split_row)
#
# print(lista_1)
#
# count_lines = 0
#
# for i in lista_1:
#     count_lines+=1
#
# print(count_lines)

# FAZENDO A CONTAGEM DAS COLUNAS
f = open('files/salarios.csv', 'r')
data = f.read()
linhas = data.split('\n')

#print(linhas)
lista_1 = []

for i in linhas:
    split_row = i.split(",")
    lista_1.append(split_row)
    #???????????????
    first_row = lista_1[0]

#print(lista_1)

count_coluns = 0

for col in first_row:
    count_coluns+=1

print(count_coluns)