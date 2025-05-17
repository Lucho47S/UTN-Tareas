"""
Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe como parámetro.
"""
#Ejercicio 3-1
def mostrar_numero(numero):
    return numero

print(mostrar_numero(7))

#Ejercicio 3-4
def validar_numero(num, desde, hasta):
    num = int(input("Ingrese un número: "))
    if desde <= num <= hasta:
        return True
    else:
        return False

#Ejercicio 3-5