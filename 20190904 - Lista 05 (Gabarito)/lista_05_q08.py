valor = int(input('Informe um número: '))

if (valor > 3):
    anterior = atual = 1
    print(anterior)
    print(atual)

    posicao = 3
    while (posicao <= valor):
        proximo = anterior + atual
        print(proximo)
        anterior = atual
        atual = proximo
        posicao += 1
        