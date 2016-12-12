#!/usr/bin/env python3

nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 0 and idade <= 10:
    faixa_etaria = "Voce é criança"
elif idade >= 11 and idade <= 16:
    faixa_etaria = "Voce é jovem"
elif idade >= 17 and idade <= 30:
    faixa_etaria = "Voce é adulto"
elif idade > 30:
    faixa_etaria = "Voce é experiente"
else:
    faixa_etaria = "Caso não previsto"

print(nome)
print(faixa_etaria)
