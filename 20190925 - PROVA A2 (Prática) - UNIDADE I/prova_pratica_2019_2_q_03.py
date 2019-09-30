# Lendo um número inteiro
numero_inicial = int(input('Informe um número inteiro positivo: '))

numero_iteraracao = numero_inicial
constante_kaprekar = 6174
numero_kaprekar    = 0
iteracoes          = 0

if (numero_inicial < 1000) or (numero_inicial > 9999):
   print('Número Inválido !!!!!')
else:
   while numero_kaprekar != 6174:
      numero_crescente   = ''.join(sorted(str(numero_iteraracao)))
      numero_decrescente = numero_crescente[::-1]
      numero_kaprekar    = int(numero_decrescente) - int(numero_crescente)
      if (numero_kaprekar == 0): break
      numero_iteraracao  = numero_kaprekar
      iteracoes += 1
      print('({0:2}) {1} - {2} = {3}'.format(iteracoes,numero_decrescente,numero_crescente,numero_kaprekar))
   print('-'*50)
   print('O Número de Kaprekar foi atingido com {0} iterações'.format(iteracoes))
 