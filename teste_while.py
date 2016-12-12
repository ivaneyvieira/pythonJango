while True:
    palavra = input('Digite uma palavra: ')
    if palavra.upper() == 'SAIR':
        break
    print("A palavra '%s' tem %d caracteres" % (palavra, len(palavra)))

