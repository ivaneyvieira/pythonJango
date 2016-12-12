#!/usr/bin/env python3
'''
1. – Escreva um programa que conte a quantidade de vogais em um texto,
     considere criar uma função para tanto.

2. - Melhore o programa criando do item 1. para que conte as vogais do
     texto independente de estarem em maiúsculas ou minúsculas.

3. – Melhore o programa do item 2. para que armazene a quantidade de
     vogais como chave e o texto como valor em um dicionário.
'''


def contaVogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    resultado = []
    for letra in texto.lower():
        if letra in vogais:
            resultado.append(letra)
    return len(resultado)


def contaVogais2(texto):
    dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto.lower():
        if letra in dict.keys():
            dict[letra] = dict[letra] + 1
    return dict


vogais = ['a', 'e', 'i', 'o', 'u']
texto = input('Entre com um texto: ')
countVogais = contaVogais(texto)
dictVogais = contaVogais2(texto)
print('O texto tem %d vogais' % (countVogais))
print()
print('Contagem de vogais:')
print(dictVogais)
