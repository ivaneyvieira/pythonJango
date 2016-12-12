#!/usr/bin/env python3
'''
Fórmulas de conversão de temperaturas
Conversão de	para	Fórmula
Grau Celsius	Grau Fahrenheit	°F = °C × 1,8 + 32
Grau Fahrenheit	Grau Celsius	°C = (°F − 32) / 1,8
Grau Celsius	kelvin	K = °C + 273,15
Kelvin	Grau Celsius	°C = K − 273,15
Grau Celsius	Rankine	°R = (°C + 273,15) × 1,8
Rankine	Grau celsius	°C = (°R ÷ 1,8) – 273,15
'''

import os

def menu():
    cls()
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Kelvin para Celsius")
    print("4 - Celsius para Kelvin")
    print("5 - Kelvin para Fahrenheit")
    print("6 - Fahrenheit para Kelvin")
    print("7 - Encerrar o programa")
    return int(input("Escolha a opcao: "))

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def lerCelsius():
    return float(input("Entre coma a temperatua em graus Celsius: "))

def lerFahrenheit():
    return float(input("Entre coma a temperatua em graus Fahrenheit: "))

def lerKelvin():
    return float(input("Entre coma a temperatua em graus Kelvin: "))

def converteCelsiusFahrenheit(c):
    k = converteCelsiusKelvin(c)
    return converteKelvinFahrenheit(k)

def converteFahrenheitCelsius(f):
    return (f - 32.0) / 1.8

def converteKelvinCelsius(k):
    f = converteKelvinFahrenheit(k)
    return converteFahrenheitCelsius(f)

def converteCelsiusKelvin(c):
    return c + 273.15

def converteFahrenheitKelvin(f):
    c = converteFahrenheitCelsius(f)
    return converteCelsiusKelvin(c)

def converteKelvinFahrenheit(k):
    return (k - 273.15) * 1.8 + 32

opcao = 0

while opcao != 7:
    opcao = menu()
    cls()
    if opcao == 1:
        c = lerCelsius()
        f = converteCelsiusFahrenheit(c)
        print("Resultado = %.2f" % f)
    elif opcao == 2:
        f = lerFahrenheit()
        c = converteFahrenheitCelsius(f)
        print("Resultado = %.2f" % c)
    elif opcao == 3:
        k = lerKelvin()
        c = converteKelvinCelsius(k)
        print("Resultado = %.2f" % c)
    elif opcao == 4:
        c = lerCelsius()
        k = converteCelsiusKelvin(c)
        print("Resultado = %.2f" % k)
    elif opcao == 5:
        f = lerFahrenheit()
        k = converteCelsiusKelvin(f)
        print("Resultado = %.2f" % k)
    elif opcao == 6:
        k = lerKelvin()
        f = converteCelsiusKelvin(k)
        print("Resultado = %.2f" % f)
    else:
        print ("Opção Inválida")
    input("Pression ENTER")

print("Fim de programa")

