import os
os.system ('cls')
num = int(input("ingrese la cantidad de numeros a ingresar: "))
md=0
sum=0
i=1
while i <=num:
    valor=int(input("ingrese un valor "))
    sum= sum + valor
    md = sum/num
    #print (mul)
    i=1+i
print (f"la media es {md}")