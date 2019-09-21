height = 5
width = 4

for i in range(height):
    for j in range(width):
        print("*", end="")
    print()

print('')

i = 1
while i <= height:
    print('*'*width)
    i += 1