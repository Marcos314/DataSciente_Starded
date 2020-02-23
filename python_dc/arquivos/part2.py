

f = open('arquivos/salarios.csv' , 'r')
data = f.read()
#print(data)

linhas = data.split('\n')

print(linhas)

