contador = 1

while (contador <= 10):
    numero = int(input('Informe um Número: '))
    if (numero > 0):
        contador += 1
        if (numero % 2 == 0):
            print('O número ', numero, 'é PAR...')