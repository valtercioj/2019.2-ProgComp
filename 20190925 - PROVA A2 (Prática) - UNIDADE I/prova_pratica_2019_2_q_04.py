# Lendo um número inteiro
numero = int(input('Informe um número inteiro positivo: '))

if (numero <= 0):
   print('Número Inválido !!!!!')
else:
   # Calculando o quadrado do número informado
   quadrado = numero ** 2
   
   # Transformando o quadrado calculado em string
   str_quadrado = str(quadrado)

   # Extraindo a primeira parte do quadrado do número informado (posição 0 até a metade)
   # Caso a quantidade de dígitos seja impar será a metade-1
   p1_quadrado = str(str_quadrado[0:len(str_quadrado)//2])

   # Extraindo a segunda parte do quadrado do número informado (da metade até o final)
   p2_quadrado = str(str_quadrado[len(str_quadrado)//2:len(str_quadrado)])

   # Somando as duas partes 
   numero_k = int(p1_quadrado) + int(p2_quadrado)

   # Verificando se a soma é igual ao número informado (Número de KAPREKAR)
   if (numero == numero_k):
      print('O número {0} é um Número de Kaprekar !!!!!'.format(numero))
   else:
      print('O número {0} não é um Número de Kaprekar !!!!!'.format(numero))