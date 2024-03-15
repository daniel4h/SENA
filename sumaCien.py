import os
os.system ("cls")
numero1 = int(input("digite un numero"))
numero2 = int(input("digite un numero"))

suma = numero1 + numero2
if suma == 100:
    print("Neutro")
elif suma < 100:
    print("Es menor a 100")
else:
    print("Es mayor a 100")