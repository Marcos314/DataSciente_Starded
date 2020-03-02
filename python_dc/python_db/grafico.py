import sqlite3
import random
import datetime
import matplotlib.pyplot as plt


#Criando uma conexão
conn = sqlite3.connect('dsa.db')
#Criando um cursos
c = conn.cursor()

def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')

# Função para inserir uma linha

def data_insert():
    c.execute("INSERT INTO produtos VALUES(1, '2020-03-01', 'Teclado', 120.00)")
    conn.commit()
    c.close()
    conn.close()

# Leitura dos registros
def selecionar_all():
    c.execute("SELECT * FROM produtos")
    for l in c.fetchall():
        print(l)

# selecionar_all()
# Leitura dos registros com condição
def selecionar_especifico():
    c.execute("SELECT * FROM produtos WHERE valor > 60.0")
    for l in c.fetchall():
        print(l)

# Leitura dos registros retornando apenas uma coluna
def selecionar_indice():
    c.execute("SELECT * FROM produtos")
    for l in c.fetchall():
        print(l[0:2])
#selecionar_indice()

#Gerando gráfico

def dados_graf():
    c.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = c.fetchall()

    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids, valores)
    plt.show()

dados_graf()