import os
os.system('cls')
print(" DETERMINAR SI UN NÚMERO ES PRIMO.")
print("Ingrese un número:")
n = int( input())
con = 0

 if n % 2 == 0:
  con = con + 1
 if con == 0:
  print (n, " Es un número primo")
 else:
  print (n, " No Es un número primo")