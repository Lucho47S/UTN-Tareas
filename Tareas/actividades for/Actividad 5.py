"""
5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.
"""
#Actividad 5
suma = 0
contador = 0

for i in range(10):
    numero = int(input("Ingresá un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("Suma de los números:", suma)
    print("Promedio de los números:", promedio)
else:
    print("No se ingresaron números.")

