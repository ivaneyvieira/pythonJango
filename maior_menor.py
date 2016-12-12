lista=[1,9,41,12,3,74,15,0]
lista=[199,94,416,121,3,744,15,440]

maior = lista[0]
menor = lista[0]

for numero in lista:
    if(numero > maior):
        maior = numero
    if(numero < menor):
        menor = numero
    print(maior, menor, numero)
    
    for a in [1,2,3,4]:
        print(a)
