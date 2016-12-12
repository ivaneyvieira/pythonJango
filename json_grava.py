import json

arquivo = open('arquivo.json', 'w')

json.dump(32.3, arquivo)
json.dump([1, 4, 5, 6], arquivo)

arquivo.close()