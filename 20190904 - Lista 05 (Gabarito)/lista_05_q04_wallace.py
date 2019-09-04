SP = 0
L = True
while (L): 
    numero = int(input('Digite um number aqui'))
    if (numero == 0):   
        L = False
        print('programa encerrado')
    else:
        if (numero > 0):
            SP += numero
print(SP)
