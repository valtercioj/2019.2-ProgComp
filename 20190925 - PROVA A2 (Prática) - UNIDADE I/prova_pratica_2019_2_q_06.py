# Solicitando os dados de entrada
coord_X_ini = int(input('Informe a Coordenada X: '))
coord_Y_ini = int(input('Informe a Coordenada Y: '))
mov_lido    = input('Informe a sequência de Movimentação: ').upper()
print('='*80)

# Calculando o quadrante inicial
if   (coord_X_ini > 0)  and (coord_Y_ini > 0) : quadrante_inicial = '1º Quadrante'
elif (coord_X_ini < 0)  and (coord_Y_ini > 0) : quadrante_inicial = '2º Quadrante'
elif (coord_X_ini < 0)  and (coord_Y_ini < 0) : quadrante_inicial = '3º Quadrante'
elif (coord_X_ini > 0)  and (coord_Y_ini < 0) : quadrante_inicial = '4º Quadrante'
elif (coord_X_ini > 0)  and (coord_Y_ini == 0): quadrante_inicial = 'Eixo X (Positivo)'
elif (coord_X_ini < 0)  and (coord_Y_ini == 0): quadrante_inicial = 'Eixo X (Negativo)'
elif (coord_X_ini == 0) and (coord_Y_ini > 0) : quadrante_inicial = 'Eixo Y (Positivo)'
elif (coord_X_ini == 0) and (coord_Y_ini < 0) : quadrante_inicial = 'Eixo Y (Negativo)'
else: quadrante_inicial = 'Origem do Plano Cartesiano'

# Calculando a movimentação do Robô
coord_X_fim = coord_X_ini
coord_Y_fim = coord_Y_ini
mov_validos = ''

#for posicao in movimentos:
for posicao in mov_lido:
   if posicao not in 'UDRLONEW': continue
   mov_validos = mov_validos + posicao
   if   (posicao == 'U'): # para cima
      coord_Y_fim += 1
   elif (posicao == 'D'): # para baixo
      coord_Y_fim -= 1
   elif (posicao == 'R'): # para a direita
      coord_X_fim += 1
   elif (posicao == 'L'): # para a esquerda
      coord_X_fim -= 1
   elif (posicao == 'O'): # para cima e esqueda
      coord_Y_fim += 1
      coord_X_fim -= 1
   elif (posicao == 'N'): # para cima e direita
      coord_Y_fim += 1
      coord_X_fim += 1
   elif (posicao == 'E'): # para baixo e direita
      coord_Y_fim -= 1
      coord_X_fim += 1
   elif (posicao == 'W'): # para baixo e esquerda
      coord_Y_fim -= 1
      coord_X_fim -= 1

# Calculando o quadrante final
if   (coord_X_fim > 0)  and (coord_Y_fim > 0) : quadrante_final = '1º Quadrante'
elif (coord_X_fim < 0)  and (coord_Y_fim > 0) : quadrante_final = '2º Quadrante'
elif (coord_X_fim < 0)  and (coord_Y_fim < 0) : quadrante_final = '3º Quadrante'
elif (coord_X_fim > 0)  and (coord_Y_fim < 0) : quadrante_final = '4º Quadrante'
elif (coord_X_fim > 0)  and (coord_Y_fim == 0): quadrante_final = 'Eixo X (Positivo)'
elif (coord_X_fim < 0)  and (coord_Y_fim == 0): quadrante_final = 'Eixo X (Negativo)'
elif (coord_X_fim == 0) and (coord_Y_fim > 0) : quadrante_final = 'Eixo Y (Positivo)'
elif (coord_X_fim == 0) and (coord_Y_fim < 0) : quadrante_final = 'Eixo Y (Negativo)'
else: quadrante_final = 'Origem do Plano Cartesiano'

# Exibindo os resultados finais
print('Posição Inicial do Robô ............: ({0},{1})'.format(coord_X_ini, coord_Y_ini))
print('Quadrante Inicial do Robô ..........: {0}'.format(quadrante_inicial))
print('Sequência de Movimentos Informados .: {0}'.format(mov_lido))
print('')
print('Sequência de Movimentos Válidos ....: {0}'.format(mov_validos))
print('Quantidade de Movimentos Realizados : {0}'.format(len(mov_validos)))
print('Posição Final do Robô ..............: ({0},{1})'.format(coord_X_fim, coord_Y_fim))
print('Quadrante Final do Robô ............: {0}'.format(quadrante_final))
print('')

