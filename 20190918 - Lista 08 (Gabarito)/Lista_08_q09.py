# Informando as coordenadas do ponto P1
pos_x_1 = int(input('Informe a Coordenada X1: '))
pos_y_1 = int(input('Informe a Coordenada Y1: '))

# Informando as coordenadas do ponto P2
pos_x_2 = int(input('Informe a Coordenada X2: '))
pos_y_2 = int(input('Informe a Coordenada Y2: '))

# Calculando a distância entre P1 e P2
distancia = ((pos_x_2 - pos_x_1)**2 + (pos_y_2 - pos_y_1)**2) ** (1/2)

print('Ponto P1({0},{1})'.format(pos_x_1,pos_y_1))
print('Ponto P2({0},{1})'.format(pos_x_2,pos_y_2))
print('A distância entre os pontos P1 e P2 é {0}'.format(distancia))
