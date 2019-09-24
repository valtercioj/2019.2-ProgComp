A = 0
B = 1
C = A + B
D = 10

# Imprimindo os valores iniciais das variáveis antes do laço
print('  A  |  B  |  C  |  D ')
print('=======================')
print(' {0:3} | {1:3} | {2:3} | {3:3}  '.format(A,B,C,D))
print('=======================')

for X in range(0, D-1):
   C = A + B
   A = B
   B = C

   # Imprimindo os valores das variáveis a cada iteração do laço
   print(' {0:3} | {1:3} | {2:3} | {3:3}  '.format(A,B,C,D))
   print('-----------------------')
   
print(C)
