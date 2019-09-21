lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

lista_t = []

for i in range(len(lista[0])):
    linha_transposta = []

    for linha in lista:
        linha_transposta.append(linha[i])
    
    lista_t.append(linha_transposta)

print(lista)

print(lista_t)