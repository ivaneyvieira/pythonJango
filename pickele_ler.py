import pickle

arquivo = open('arquivo.dat', 'rb')

valor1 = pickle.load(arquivo)
valor2 = pickle.load(arquivo)

print(valor1, valor2)
arquivo.close()