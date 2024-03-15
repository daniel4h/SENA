import os
os.system('cls')
n = int(input("ingrese el numero de posiciones "))
a, b = 0, 1
print("1:", a)
print("2:", b)

for i in range(3, n+1):
    b = a + b
    a = b - a  
    print(f"{i}: {b}")