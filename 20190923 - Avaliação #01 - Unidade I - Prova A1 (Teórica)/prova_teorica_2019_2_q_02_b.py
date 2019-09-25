A = 0
B = 1
C = A + B
D = 10

for X in range(0, D-1):
   C = A - B
   A = B
   B = C
   
print(C)