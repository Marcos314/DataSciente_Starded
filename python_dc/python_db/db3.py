import sqlite3
import random
import time
import datetime

conn = sqlite3.connect('dsa.db')

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')

#Função para inserir uma linha

def data_insert():
    c.execute("INSERT INTO produtos VALUES(1, '2020-03-01', 'Teclado', 120.00)")
    conn.commit()
    c.close()
    conn.close()

#Usando variáveis para inserir dados

def data_insert_var():
    new_data = datetime.datetime.now()
    new_prod = 'Monitor'
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_data,new_prod, new_valor))
    conn.commit()

for i in range(10):
    data_insert_var()
    time.sleep(1)

c.close()
conn.close()




