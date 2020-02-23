import pandas as pd
file_name = "/home/marcos/PycharmProjects/python_dc/arquivos/binary.csv"

def resumoArq(file):

    arquivo = pd.read_csv(file)

    print(arquivo.describe())
    return arquivo.describe()



resumoArq(file_name)

