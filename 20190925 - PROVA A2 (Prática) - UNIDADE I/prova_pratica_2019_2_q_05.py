# Strings de apoio na verificação da senha
numeros = '0123456789'
letras_maiusculas = 'QWERTYUIOPASDFGHJKLZXCVBNM'
simbolos = '@#$&'

# Informando a senha
senha = input('Informe a senha: ')

# Total de Caracteres da senha
qt_total_caracteres = len(senha)

# Total de Letras maiúsculas, letras minúsculas, símbolos e números
qt_maiusculas = qt_numeros = qt_simbolos = qt_invalidos = 0
for letra in senha:
   if   (letra in letras_maiusculas): qt_maiusculas += 1
   elif (letra in simbolos): qt_simbolos += 1
   elif (letra in numeros): qt_numeros += 1
   else: qt_invalidos += 1

# Verificando se a senha informada atende os itens (a), (b), (c) e (d)
if (qt_invalidos != 0):
   print('Foram informados caracteres inválidos...')
if (qt_total_caracteres < 10) or (qt_total_caracteres > 15):
   print('Informe uma senha com 10 a 15 caracteres...')
elif (qt_maiusculas == 0):
   print('A senha deve possuir pelo menos 1 letra maiúscula...')
elif (qt_numeros < 3) or (qt_numeros > 5):
   print('A senha deve possuir entre 3 e 5 números...')
elif (qt_simbolos < 2):
   print('A senha deve possuir pelo menos 2 símbolos...')
else:
   # Verificando se a senha é FRACA, FORTE ou MÉDIA
   if (qt_total_caracteres == 10) and (qt_maiusculas == 1) and (qt_numeros == 3) and (qt_simbolos == 2):
      print('A senha informada é FRACA...')
   elif (qt_total_caracteres == 15) and (qt_maiusculas == 3) and (qt_numeros == 5) and (qt_simbolos == 4):
      print('A senha informada é FORTE...')
   else:
      print('A senha informada é MÉDIA...')
