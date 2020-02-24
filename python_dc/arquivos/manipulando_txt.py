import os
texto = "Cientista de dados é a profissão que mais tem crescido no mundo. \n"
texto = texto + "Esses profissionais precisam saber estatistica, programação e ML, "
texto += "e claro, Big Data!!"
# #
# # print(texto)
# #
# arq = open(os.path.join('files/cientista2.txt'),'w')
#
# #split, separa a string por cada espaço em branco que encontra (default)
#
# for palavra in texto.split():
#     arq.write(palavra+' + ')
#
# arq.close()

# arquivo = open('files/cientista2.txt')
# conteudo = arquivo.read()
# arquivo.close()
#
# print(conteudo)


# USANDO WITH + slicing

with open('./files/cientista2', 'w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[::-1])

arquivo = open('files/cientista2','r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
