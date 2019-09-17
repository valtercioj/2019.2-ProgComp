valor_inicial = float(input('Informe o valor mensal a ser aplicado (R$): '))

juros_mes = float(input('Informe a taxa de juros mensal (%): '))

acumulado = 0
ano = 1

while True:
   for mes in range(1, 13):
      acumulado += valor_inicial + (acumulado * juros_mes / 100)

   print('O valor acumulado do {0}º ano é R$ {1:.2f}'.format(ano, acumulado))

   confirma = ''
   while confirma != 'S' and confirma != 'N':
      confirma = input('Deseja calcular mais um ano (S/N)? ').upper()

   if (confirma == 'N'): break

   ano += 1
   continue


