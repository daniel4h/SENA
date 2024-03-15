import os
os.system ('cls')
num = int(input("ingrese la cantidad de numeros a ingresar: "))
md=0
sum=0
for i in range (1,num+1):
    valor=int(input("ingrese un valor "))
    sum= sum + valor
    md = sum/num
    #print (mul)
print (f"la media es {md}")