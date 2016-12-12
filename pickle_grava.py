import pickle

arquivo = open('arquivo.dat', 'wb')

pickle.dump(32.3, arquivo)
pickle.dump([1, 4, 5, 6], arquivo)

arquivo.close()