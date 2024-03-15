import os
os.system ("cls")
numero1 = int(input("digite un numero"))

if numero1 == 0:
    print("Neutro")
elif numero1 < 0:
    print("Negativo")
else:
    print("positivo")