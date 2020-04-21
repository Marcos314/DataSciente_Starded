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



sql = 'select * from produtos'

c.execute(sql)

dados = c.fetchall()


for l in dados:
    print(l)

