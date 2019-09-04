contador = 1
qt_maiores = 0

while (contador <= 10):
    idade = int(input('Informe a Idade: '))
    if (idade > 0):
        contador += 1
        if (idade >= 18):
            qt_maiores += 1

print(qt_maiores)