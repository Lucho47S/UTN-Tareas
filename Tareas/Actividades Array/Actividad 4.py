"""
Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números y un número especificado. 
La misma debe buscar el número especificado en la lista y retornar “True” si existe.
"""

"""
#Actividad 4
numeros = [0] * 20 #lista con 20 valores
#funcion
def buscar_numero(numero :int) -> bool:
    for i in range(0, 20):
        numeros[i] += 1 + i

    for i in range(0, 20):
        if numeros[i] == numero:
            num = True
            return True
        else:
            num = False
            continue
    if num == False:
        return False        

#programa
numero = int(input("Ingresa un numero: "))
print(buscar_numero(numero))

"""

#funcion
def buscar_numero(numero :int, numeros :list) -> bool:
    for i in range(20): #asigna valores 
        numeros[i] = 1 + i
    return numero in numeros

#programa principal
numeros = [0] * 20 #define lista con 20 espacios
numero = int(input("Ingresa un numero: ")) #pide numero
print(buscar_numero(numero, numeros))
