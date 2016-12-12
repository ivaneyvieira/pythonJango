import urllib.request

l = 'http://www.pintos.com.br'

resposta = urllib.request.urlopen(l).readlines()

arquivo = open('index.html', 'w')

print(resposta)
for linha in resposta:
    linhaStr=linha.decode("utf-8")
    print(linhaStr)
    arquivo.write(linhaStr)

arquivo.close()