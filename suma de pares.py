print("Ingresa numero inicial")
i = int(input("Ingresa numero inicial"))
print("Ingresa numero final")
f = int(input("Ingresa numero final"))
suma = 0
print("**Los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
    i+=1
    suma=suma+1
print("La suma de numeros es:", suma)