#!/usr/bin/env python3


def copiaArquivo(origem, destino):
    forigem = open(origem, 'r')
    fdestino = open(destino, 'w')

    print('Copiando', end='')
    for texto in forigem:
        fdestino.write(texto)
        print('.', end='')

copiaArquivo('arquivoNum.txt', 'arquivoNum2.txt')