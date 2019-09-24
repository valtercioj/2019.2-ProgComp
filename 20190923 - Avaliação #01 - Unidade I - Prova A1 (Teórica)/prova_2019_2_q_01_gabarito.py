A = 0
B = -10

# Imprimindo os valores iniciais das variáveis antes do laço
print('  A  |  B  |  C ')
print('================')
print(' {0:3} | {1:3} | '.format(A,B))
print('================')

while (A > B):
   if (A > B):
     B = 2 * A + B
     A += 1

   if (B < 0):
     C = (B-1) ** 2
   else:
     C = A ** 2

   # Imprimindo os valores das variáveis a cada iteração do laço
   print(' {0:3} | {1:3} | {2:3} '.format(A,B,C))
   print('----------------')

# Imprimindo o valor das variáveis solicitadas na questão
print('Resposta: A = {0} / B = {1} / C = {2}'.format(A,B,C))
