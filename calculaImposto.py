#!/usr/bin/env python3

#Entrada de dados
valor_salario=float(input("Entre com o valor do seu Salário: "))


#Procesasmento
aliquota=7.5

if valor_salario > 1500.00:
    imposto_cobrado= valor_salario * aliquota/100
else:
    imposto_cobrado=0

if imposto_cobrado > 0:
    print("O valor do importo cobrado é %5.2f", imposto_cobrado)
