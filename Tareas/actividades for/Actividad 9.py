"""
9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
"""
#Actividad 9
numero = int(input("Ingresá un número: "))
contador = 0

print(f"Divisores de {numero}:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1

print(f"Cantidad de divisores: {contador}")
