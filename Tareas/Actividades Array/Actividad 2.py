"""
Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, 
pida posición y número a guardar al usuario, 
lo guarde en una lista en la posición solicitada aleatoriamente y la retorne. 
El programa principal debe invocar a la función y mostrar por pantalla el retorno.
"""
#Actividad 2

#funcion
def cargar_lista() -> list:
    numeros = [0] * 10  # Inicializa la lista con diez ceros
    posicion = int(input("Ingrese la posición (0 a 9): "))
    while posicion < 0 or posicion >= 10:
        posicion = int(input("Posición inválida. Ingrese un valor entre 0 y 9: "))
    numero = int(input("Ingrese el número a guardar: "))
    numeros[posicion] = numero  # Guarda el número en la posición indicada
    return numeros

# Programa principal
resultado = cargar_lista()
print("Lista resultante:", resultado)
