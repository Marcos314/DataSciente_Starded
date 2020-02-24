import pandas as pd

file_name = 'files/salarios.csv'

df2 = pd.read_csv(file_name)
aux = df2.head()

print(aux)

