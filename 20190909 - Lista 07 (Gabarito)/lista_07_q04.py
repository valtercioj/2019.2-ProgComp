n1 = int(input('Informe o Primeiro Valor: '))
n2 = int(input('Informe o Segundo Valor: '))

soma_par = 0

# Invertendo caso n1 > n2
if (n1 > n2):
   n1, n2 = n2, n1

# Iterando entre n1 e n2 (inclusive)
for i in range(n1, n2+1):
   # verificando se é par e somando a variavel soma_par
   if (i % 2 == 0): 
      soma_par += i

print('A soma dos números pares é {0}'.format(soma_par))