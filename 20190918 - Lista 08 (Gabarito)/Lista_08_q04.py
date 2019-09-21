# Digitando um texto
texto = input('Informe o valor: ').upper()

# Variável para montar a string invertida
texto_invertido = ''

# Iterando o texto digitado para montar a string invertida
for letra in texto:
    texto_invertido = letra + texto_invertido

# Imprimindo os valores
print('O valor digitado foi: {0}'.format(texto))
print('O valor invertido é: {0}'.format(texto_invertido))

# Informando se é ou não palíndromo
if (texto == texto_invertido):
    print('São Palíndromos...')
else:
    print('Não são Palíndromos...')