#!/usr/bin/env python3

print("Programa da Linguagem de programação Python")
print("*" * 50)

# Entrada de dados
num0 = int(input("Entre com um número Inteiro: "))
num1 = int(input("Entre com um número Inteiro: "))
nome = input("Entem com seu nome: ")

# Processamento
soma = num0 + num1
if num0 % 2 == 0:
    msg0 = "É par"
else:
    msg0 = "É impar"

if num1 % 2 == 0:
    msg1 = "É par"
else:
    msg1 = "É impar"

if soma % 2 == 0:
    msgSoma = "A soma é par"
else:
    msgSoma = "A soma é impar"

# Saída de dados
print("*" * 50)
print(nome + " voce digitou ", num0, num1)
print("A soma dos dois numero é: ", num0 + num1)
print("O primeiro número " + msg0)
print("O segundo número " + msg1)
print(msgSoma)