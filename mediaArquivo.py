#!/usr/bin/env python3


def mediaArquivo(arquivoNome):
    arquivo = open(arquivoNome, 'r')
    soma = 0
    quant = 0
    for linha in arquivo.readlines():
        if linha != '\n':
            quant=quant+1
            num = eval(linha)
            soma = soma + num
    arquivo.close()
    print(soma, quant)
    return soma/quant

print(mediaArquivo('arquivoNum.txt'))

