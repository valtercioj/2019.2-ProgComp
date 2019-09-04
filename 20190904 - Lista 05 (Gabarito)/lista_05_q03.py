soma_h = soma_m = qt_h = qt_m = 0

while (qt_h+qt_m <= 10):
    idade = int(input('Informe a Idade: '))
    sexo = input('Informe o sexo (H ou M): ')
    if (idade > 0):
        if (sexo == 'H') or (sexo == 'h'):
            soma_h += idade
            qt_h += 1
        elif (sexo == 'M') or (sexo == 'm'):
            soma_m += idade
            qt_m += 1

print('A média geral das idade é ', (soma_h+soma_m)/10)

print('A média das idades dos Homens é ', soma_h / qt_h)

print('A média das idades das Mulheres é ', soma_m / qt_m)