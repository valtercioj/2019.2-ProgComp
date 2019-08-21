a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C"))
if (a!=0):
   delta = b**2 - 4*a*c
   if (delta<0):
      print("Não existe raizes reais")
   elif (delta==0):
      x = -b / (2*a)
      print("Só tem uma raiz que é:", x)
   else:
      x1= -b + (delta**0.5) / (2*a)
      x2= -b - (delta**0.5) / (2*a)
      print("Valor de X1 é:", x1)
      print("Valor de X2 é:", x2)
print("Fim do programa.")
