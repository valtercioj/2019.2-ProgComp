print('Tabuada de Multiplicação')
print('')

valor = int(input('Informe o valor de N: '))

for multiplicador in range (1, 11):
   produto = multiplicador * valor
   print('{0:2} x {1:2} = {2:2}'.format(multiplicador, valor, produto))
