#!/usr/bin/env python3

import random

def numsAleatorios(quant, arquivoNome):
    arquivo = open(arquivoNome, 'w')
    for i in range(quant):
        num = random.randint(0, 100)
        #print(num)
        arquivo.write(str(num) + '\n')
    arquivo.close()


quant = int(input("Quantos número vc que? "))
numsAleatorios(quant, 'arquivoNum.txt')