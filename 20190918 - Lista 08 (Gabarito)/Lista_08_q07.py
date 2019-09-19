# Lendo o CPF
cpf = input('Informe os 11 caracteres do CPF: ')

# Desmembrando o CPF
digitos_cpf = []
if (len(cpf) == 11):
   for i in cpf:
      digitos_cpf.append(int(i))

# Calculando o Primeiro Digito Verificador
auxiliar = 0
for d in range(0,9):
   auxiliar += digitos_cpf[d] * (10 - d)
digito_1 = 11 - (auxiliar % 11)
if (digito_1 == 10): digito_1 = 0

# Calculando o Segundo Digito Verificador
auxiliar = 0
for d in range(0,9):
   auxiliar += digitos_cpf[d] * (11 - d)
auxiliar += (digito_1 *2)
digito_2 = 11 - (auxiliar % 11)
if (digito_2 == 10): digito_2 = 0

# Verificando se o CPF informado é Válido
if (digito_1 == digitos_cpf[9]) and (digito_2 == digitos_cpf[10]):
   print('CPF Válido !!!!!')
else:
   print('CPF Inválido !!!!!')