valor = int(input('Informe um número: '))
valor_informado = valor

if (valor == 1) or (valor == 0):
    print('1! = 1')
elif (valor < 0):
    print('Não existe Fatorial para o número informado...')
else:
    fatorial = valor
    while (valor > 1):
        valor -= 1
        fatorial *= valor

print(valor_informado, '!=', fatorial)