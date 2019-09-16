lista = []

x = int(input('Informe a quantidade de elementos da Lista: '))

if (x > 0):
   while True:
      n = int(input('Informe um número (0 para sair): '))
      if (n == 0): break
      lista.append(n)
      if (len(lista) > x): lista.pop(0)
      print(lista)
