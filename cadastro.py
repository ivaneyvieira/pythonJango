'''
Programa para cadastrar nome, telenone e email
Gravar em arquivo
ler e escrever
'''
import pickle

nome_arquivo = "agenda.dat"

# Indices para os campos
NOME = 0
TELEFONE = 1
EMAIL = 2


def tupla_registro(nome, telefone, email):
    return (nome, telefone, email)


def ler_registro():
    print('Preencha os campos')
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('E-mail: ')
    return tupla_registro(nome=nome, telefone=telefone, email=email)


def escreve_registro(registro):
    print("Nome    : ", registro[NOME])
    print("Telefone: ", registro[TELEFONE])
    print("E-mail  : ", registro[EMAIL])


def grava_arquivo(registros):
    arquivo = open(nome_arquivo, 'wb')
    pickle.dump(registros, arquivo)
    arquivo.close()


def ler_arquivo():
    try:
        arquivo = open(nome_arquivo, 'rb')
        registros = pickle.load(arquivo)
        return registros
    except:
        return []


def exec_grava_registros():
    registro = ler_registro()
    registros = ler_arquivo()
    registros.append(registro)
    grava_arquivo(registros)


def exec_ler_registros():
    registros = ler_arquivo()
    for registro in registros:
        print('-------------------------------')
        escreve_registro(registro)


def menu():
    print("+======================+")
    print("| Agenda Telefonica    |")
    print("+======================+")
    print("| Menu principal       |")
    print("+======================+")
    print("| 1 - Grava registro   |")
    print("| 2 - Ler registro     |")
    print("| S - Sair             |")
    print("+======================+")
    print()
    return input("Opção: ")


while True:
    opcao = menu()
    if opcao == '1':
        exec_grava_registros()
    elif opcao == '2':
        exec_ler_registros()
    elif str(opcao).lower() == 's':
        break
    else:
        print('Opção inválida....')
