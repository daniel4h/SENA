import os
os.system('cls')
print("-------------------------------------------------------")
print(" DETERMINAR SI UN NÚMERO ES PRIMO.")
print("-------------------------------------------------------")
print("Ingrese un número:")
n = int( input())
con = 0
for i in range(2, n):
 if n % i == 0:
  con = con + 1



print("-------------------------------------------------------")
if con == 0:
 print (n, " Es un número primo")
else:
 print (n, " No Es un número primo")