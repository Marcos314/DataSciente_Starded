# Manipulando Banco de Dados em Python

import os

os.remove('escola.db') if os.path.exists('escola.db') else None

import sqlite3

con = sqlite3.connect('escola.db')

# cursor para acessar o bd
cs = con.cursor()
print(type(cs))

sql_create = "create table cursos " \
             "(id integer primary key, " \
             "titulo varchar(100) , " \
             "categoria varchar(140))"

cs.execute(sql_create)
sql_insert = 'insert into cursos values (?, ?, ?)'

rec_set = [(1000, 'Ciencia de dados','Data Science'),
           (1001, 'Big data 1', 'big data'),
           (1002, 'python', 'python')]

for rec in rec_set:
    cs.execute(sql_insert,rec)

con.commit()

sql = 'select * from cursos'

cs.execute(sql)

dados = cs.fetchall()


for l in dados:
    print(l)

con.close()