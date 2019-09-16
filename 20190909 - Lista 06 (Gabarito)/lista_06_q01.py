contador = 0
total_leitura = 15
lista_idades = [0, 0, 0, 0, 0]

# -------------------------------------------------------------
# Lendo as 15 idades
while contador < total_leitura:
    idade = int(input('Informe a idade: '))

    if (idade <= 0):
        print('Idade Inválida !!!!!')
        continue

    if (idade <= 15):
        lista_idades[0] += 1 #Soma na posição 0 da lista
    elif (idade <= 30):
        lista_idades[1] += 1 #Soma na posição 1 da lista
    elif (idade <= 45):
        lista_idades[2] += 1 #Soma na posição 2 da lista
    elif (idade <= 60):
        lista_idades[3] += 1 #Soma na posição 3 da lista
    else:
        lista_idades[4] += 1 #Soma na posição 4 da lista

    contador += 1

# -------------------------------------------------------------
# Imprimindo os resultados
posicao = 0
lista_faixas = ['Até 15 anos', 'De 16 a 30 anos', 'De 31 a 45 anos', 'De 46 a 60 anos', 'Acima de 60 anos']
print('FAIXA ETÁRIA         TOTAL          %')
while (posicao <= 4):
    faixa      = lista_faixas[posicao]
    qt_idades  = lista_idades[posicao]
    percentual = qt_idades / total_leitura * 100
    print('{0:<21}{1:<15}{2:>5,.1f}'.format(faixa, qt_idades, percentual))
    posicao += 1
