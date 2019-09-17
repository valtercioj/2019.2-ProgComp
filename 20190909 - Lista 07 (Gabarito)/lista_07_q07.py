while True:

   n = int(input('Informe um número: '))

   divisores = 0

   for divisor in range (1, n+1):
      if (n % divisor == 0):
         print('{0},'.format(divisor), end = ' ')
         divisores += 1

   print(' ')

   if divisores == 2: print('O número {0} é primo'.format(n))

   continuar = ''
   while continuar != 'S' and continuar != 'N':
      continuar = input('Deseja Continuar (S/N)? ').upper()

   if continuar == 'N': break