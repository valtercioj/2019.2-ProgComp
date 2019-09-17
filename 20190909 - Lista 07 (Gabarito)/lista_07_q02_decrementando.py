valor = int(input('Informe o valor: '))

if (valor < 0):
   print('Informe um valor maior ou igual a ZERO...')
elif (valor == 0):
   print('O Fatorial de ZERO é 1...')
else:
   fatorial = valor

   for i in range(valor-1, 1, -1):
      fatorial *= i
      
   print('{0}! = {1}'.format(valor, fatorial))
