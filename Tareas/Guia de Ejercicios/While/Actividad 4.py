"""
WHILE
Contadores - Acumuladores - Máximos y mínimos
Mostrar la suma de los números pares desde el 1 hasta el 10.
"""

#Actividad 4
num = 0
suma = 0
while num < 10:
    if num % 2 == 0:
        suma += num
        num += 1
    else:
        num += 1

print(f"la suma de los numeros pares es igual a {suma}")