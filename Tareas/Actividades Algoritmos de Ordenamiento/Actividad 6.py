"""
6.Diseña una función que calcule la potencia de un número. 
La función debe recibir la base y el exponente como argumentos y devolver el resultado.
"""
#Actividad 6
def potencia(base :int, exponente :int) -> int:
    return base ** exponente

num1 = int(input("Ingresa el numero base: "))
num2 = int(input("Ingresa el exponente: "))

resultado = potencia(num1, num2)
print(resultado)
