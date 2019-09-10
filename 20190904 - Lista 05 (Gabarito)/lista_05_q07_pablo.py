n =  int(input("Digite o número que você quer fatorial: "))
cont = 2
fat =1
if(n<0):
   print("não existe fatorial de número negativo")
else:
   while (cont<=n):
      fat = fat*cont
      cont = cont+1
   print("Fatorial é: ", fat)