# Informando as coordenadas X e Y
pos_x = int(input('Informe a Coordenada X: '))
pos_y = int(input('Informe a Coordenada Y: '))

# Verificando o quadrante
if (pos_x > 0) and (pos_y > 0):
    msg = 'no 1o Quadrante'
elif (pos_x < 0) and (pos_y > 0):
    msg = 'no 2o Quadrante'
elif (pos_x < 0) and (pos_y < 0):
    msg = 'no 3o Quadrante'
elif (pos_x > 0) and (pos_y < 0):
    msg = 'no 4o Quadrante'
elif (pos_x != 0) and (pos_y == 0):
    msg = 'sobre Eixo X'
elif (pos_x == 0) and (pos_y != 0):
    msg = 'sobre Eixo Y'
else:
    msg = 'na Origem'

print('O ponto P({0},{1}) está {2}'.format(pos_x,pos_y,msg))