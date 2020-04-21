import json
# from urllib.request import urlopen
#
# response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf-8')
# data = json.loads(response)[0]
#
# print('Titulo: ',data['title'])
# print('URL: ', data['url'])

'''Copiando o conteúdo deu arquivo para outro'''

arq_fonte = 'files/dados.json'
arq_destino = 'files/json_data2.txt'

#Método 1

# with open('files/dados.json','r') as infile:
#     text = infile.read()
#     with open('files/json_data2.txt', 'w') as outfile:
#         outfile.write(text)
#Método 2

open(arq_destino, 'w').write(open(arq_fonte,'r').read())

#Leitura de arquivo

with open('files/json_data2.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)