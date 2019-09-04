soma_par = soma_impar = 0

while True:
    valor = int(input('Informe um número: '))
    if (valor == 0): break
    if (valor % 2 == 0):
        soma_par += valor
    else:
        soma_impar += valor

print('A soma dos números pares informados é ', soma_par)
print('A soma dos números ímpares informados é ', soma_impar)