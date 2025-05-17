"""
4.Crea una función que verifique si un número dado es par o impar. 
La función retorna True si el número es par, False en caso contrario.
"""

#Actividad 4
def es_par(num) -> int:
    return num % 2 == 0

num = int(input("ingresa un numero: "))
print(es_par(num))