soma_h=0
soma_m=0
qt_h=0
qt_m=0
while (qt_h + qt_m < 10 ):
    idade = int(input("Digite sua idade:"))
    sexo = input("Digite H para Homem e M para Mulher:")
    if(idade>0):
        if (sexo == "H") or (sexo == "h"):
            soma_h+=idade
            qt_h+=1
        elif(sexo == "M") or (sexo == "m"):
            soma_m+=idade
            qt_m+=1


print("Média das idades",(soma_h + soma_m)/10) 
print("Média de homens",soma_h/qt_h)
print("Média de mulheres",soma_m/qt_m)