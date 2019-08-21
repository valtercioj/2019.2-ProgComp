A = int(input('Informe um valor de A: '))
B = int(input('Informe um valor de B: '))
C = int(input('Informe um valor de C: '))

if (A <= 0) or (B <=0) or (C <= 0):
    print ('foi informada um valor invalido')   
elif (A + B + C != 180):
    print ('os angulos informados nao formam um triangulo')
elif (A<90) and (B<90) and (C<90):
    print ('triangulo acutangulo')
elif (A == 90) or (B == 90) or (C == 90):
    print ('triangulo retangulo')
else:
    print ('triangulo obtusangulo')