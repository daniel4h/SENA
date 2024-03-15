import os
os.system('cls')
sumimp=0
sumpar=0
c=1
for c in range (1, 100+1):
    if c % 2 == 1:
        print (c,"_IMPAR_")
        sumimp = sumimp+c
    else:
        print (c,"_PAR_")
        sumpar = sumpar+c
    c+=1       

print(f"la suma de los impares es: " ,sumimp)
print(f"la suma de los pares es: ",sumpar)    