import json
dicionario = {
    'nome': 'Marcos Wesley',
    'linguagem': 'Python',
    'similar': ['c','Modula-3','lisp'],
    'usuario': 10000
}

# for k,v in dict.items():
#     print(k,v)
aux = json.dumps(dicionario)
#print(aux)

#Criando um arquivo json

with open('files/dados1.json','w') as arquivo:
    arquivo.write((json.dumps(dicionario)))

#Leitura dos arquivos json
with open('files/dados1.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)
print(data['similar'])





