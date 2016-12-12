dicionario = {}
dicionario['nome'] = 'Ivaney'
dicionario['sobrenome']='Sales'
dicionario['telefone']='999985558'
dicionario['idade'] = '100 anos'
print(dicionario['nome'])

print("\nlistagem direta")
print(dicionario)

print('\nListagem completa usando for')

for (chave, valor) in dicionario.items():
    print(chave, ':', valor)