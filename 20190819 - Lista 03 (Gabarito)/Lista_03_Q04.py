base   = float(input('Informe o Valor da Base (B): '))
altura = float(input('Informe o Valor da Altura (H): '))

if (base>0) and (altura>0):
    area = base * altura / 2
    print('A área do Triangulo de Base = ',base, ' e Altura = ', altura, ' e = ', area)
else:
    print('Valores Invalidos...')

print('Fim do Programa...')