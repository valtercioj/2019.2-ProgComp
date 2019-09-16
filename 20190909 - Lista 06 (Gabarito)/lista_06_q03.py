# Instanciando a lista
alunos = []

# Solicitando a quantidade de Alunos
n = int(input('Informe a Quantidade de Alunos: '))

# Instanciando o contador de alunos
contador_alunos = 0

# --------------------------------------------------------------------------------
# Efetuando a leitura dos dados dos alunos
if (n > 0):
   while contador_alunos < n:
      # Solicitando os dados dos alunos
      matricula = input('Informe a matrícula: ')
      nota_1    = int(input('Informe a Nota da Unidade I: '))
      nota_2    = int(input('Informe a Nota da Unidade II: '))
      
      # Retornando ao inicio do laço caso uma das notas seja inválida
      if (nota_1 < 0) or (nota_1 > 100) or (nota_2 < 0) or (nota_2 > 100): continue

      # Calculando a média
      media = ((nota_1 * 2) + (nota_2 * 3)) / 5

      # Definido a situação do aluno
      if (media >= 60): 
         situacao = 'Aprovado'
      elif (media >= 20): 
         situacao = 'Prova Final'
      else: 
         situacao = 'Reprovado'

      # Adicionando os dados do aluno na lista
      alunos.append([matricula, nota_1, nota_2, media, situacao])

      # Incrementando o contador de alunos
      contador_alunos += 1
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Imprimindo a lista de alunos
print('MATRÍCULA           NOTA 1      NOTA 2      MÉDIA       SITUAÇÃO')
for i in range(len(alunos)):
   print('{0:20}{1:<12}{2:<12}{3:<12,.0f}{4}'.format(alunos[i][0],alunos[i][1],alunos[i][2],alunos[i][3],alunos[i][4]))
print('---------------------------------------------------------------')
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Imprimindo dos dados finais
maior_media = menor_media = media_turma = alunos_acima = percentual = 0

print('Maior Nota: {0}           Menor Nota: {1}'.format(maior_media, menor_media)
print('Média da Turma: {0}'.format(media_turma))
print('Alunos Acima da Média: {0} ({1})'.format(alunos_acima, percentual))
# --------------------------------------------------------------------------------