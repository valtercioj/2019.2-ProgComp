soma_positivo = 0
leitura = True

while leitura:
    numero = int(input('Informe um número: '))
    if (numero == 0):
        leitura = False
    else:
        if (numero > 0):
            soma_positivo += numero

print('A soma dos números pares é ', soma_positivo)
