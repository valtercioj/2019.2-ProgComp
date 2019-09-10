fibN =int(input("Digite o númmero de Fibonacci que você deseja: "))
fib1 = 1
fib2 = 1
fibA = fib1 +fib2

if(fibN==1):
   print(fib1)
elif (fibN>1):
   print(fib1)
   print(fib2)
   while (fibN>2):
      print(fibA)
      fib1= fib2 
      fib2= fibA
      fibA= fib1+fib2
      fibN = fibN-1