base   = float(input('Informe o Valor da Base (B): '))
altura = float(input('Informe o Valor da Altura (H): '))

if (base>0) and (altura>0):
    area = base * altura / 2
    print('A área do Triangulo de Base = ',base, ' e Altura = ', altura, ' e = ', area)
elif (base<=0):
    print('Valor da BASE Invalido...')
else:
    print('Valor da ALTURA Invalido...')

print('Fim do Programa...')