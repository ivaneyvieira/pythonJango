fator = int(input("Qual é a tabuada: "))

for num in range(11):
    print('%2d x %2d = %d' % (num, fator, fator*num))