import os
os.system ("cls")
numero1 = int(input("digite un numero"))
numero2 = int(input("digite un numero"))
if numero1 == numero2:
    print("Neutro")
elif numero1 < numero2:
    print("Numero 2 es mayor")
else:
    print("Numero 1 es mayor")