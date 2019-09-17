# Quantidade de elementos da sequencia de Fibonacci
qt_elementos = int(input('Informe a quantidade de elementos: '))

# Inicializando as variáveis
anterior  = 0
atual     = 1
fibonacci = anterior + atual

# Condição para checar se a quantidade de elementos é válida
if (qt_elementos <= 0):
   print('Informe um valor maior que ZERO...')
else:
   print('-'*50)
   print('A sequencia de Fibonacci tem ', qt_elementos, 'elemento(s) :')
   print('-'*50)
   for contador in range(0, qt_elementos):
       print(fibonacci, end=', ')
       # Modificando os valores
       fibonacci = anterior + atual
       anterior  = atual
       atual     = fibonacci
   print(' ')
   print('-'*50)
