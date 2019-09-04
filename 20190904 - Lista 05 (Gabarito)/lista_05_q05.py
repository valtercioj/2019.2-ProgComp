valor = int(input('Informe um número: '))

menor = maior = valor
leitura = True

while leitura:
    valor = int(input('Informe um número: '))
    if (valor == 0):
        leitura = False
    else:
        if (valor > maior):
            maior = valor
        else
            menor = valor

print('O maior número digitado foi, ' maior)
print('O menor número digitado foi, ' menor)