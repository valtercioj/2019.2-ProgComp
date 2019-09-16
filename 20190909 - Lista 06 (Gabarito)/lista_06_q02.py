'''
Escreva um programa para ler um valor (em reais). Após ser informado 
o valor, o programa deverá calcular e exibir quantas cédulas de 
100, 50, 20, 10, 5 e 2 e quantas moedas de 1, 0.5, 0.25, 0.10, 0.05 e 0.01 
são necessárias.
'''

lista_valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
lista_qt      = [  0,  0,  0,  0, 0, 0, 0,   0,    0,    0,    0,    0]

# Lendo o valor do saque
valor = float(input('Informe o valor: '))

# Separando a parte inteira da parte decimal
parte_cedulas = int(valor)
parte_moedas = valor - parte_cedulas

# Calculando a quantidade de cédulas/moeda da parte inteira
p1 = 0
while (parte_cedulas > 0):
    lista_qt[p1] = parte_cedulas // lista_valores[p1]
    parte_cedulas = parte_cedulas % lista_valores[p1]
    p1 += 1

# Calculando a quantidade de moedas
p2 = 7 
while (parte_moedas > 0):
    # CORRIGIR FÓRMULA
    lista_qt[p2] = (parte_moedas*100) // (lista_valores[p2]*100)
    parte_moedas = int(parte_moedas) % (lista_valores[p2]*100)
    p2 += 1

print(lista_valores)
print(lista_qt)

#print(parte_moedas)