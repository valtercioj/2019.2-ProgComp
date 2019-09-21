vogais = 'AEIOUÃÕÁÉÍÓÚ'

texto = input('Informe o texto: ').upper()

contador = 0

for letra in texto:
    if (letra in vogais):
        contador += 1

print('Foram digitadas {0} vogais'.format(contador))