"""
Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. 
Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.
La función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el programa principal realizando la invocación o llamada.
"""
#Ejercicio 3-3
def es_par(num):
    num = int(input("ingrese un numero"))
    if num % 2 == 0:
        print("el numero es par")
        return True
    else:
        print("el numero no es par")
        return False

print(es_par(4))