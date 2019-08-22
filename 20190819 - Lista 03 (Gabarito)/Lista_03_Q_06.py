valor_a  = float(input('Informe o Valor de A: '))
valor_b  = float(input('Informe o Valor de B: '))
valor_c  = float(input('Informe o Valor de C: '))

if (a == 0):
   print('Não é uma Equação do 2º Grau...')
else:
   delta = b**2 - 4*a*c
   if (delta < 0):
      print('Não há Raizes nos Números Reais...')
   elif (delta == 0):
      print('Raízes Reais e Iguais...')
      x1 = (-b + delta**(1/2)) / (2*a)
      print('X1 = X2 =', x1)
   else:
      print('Raízes Reais e Diferentes...')
      x1 = (-b + delta**(1/2)) / (2*a)
      x2 = (-b - delta**(1/2)) / (2*a)
      print('X1 =', x1)
      print('X2 =', x2)
