valor = int(input('Informe o valor: '))

if (valor < 0):
   print('Informe um valor maior ou igual a ZERO...')
elif (valor == 0):
   print('O Fatorial de ZERO é 1...')
else:
   fatorial = 1

   for i in range(1, valor+1):
      fatorial *= i

	print('{0}! = {1}'.format(valor, fatorial))
