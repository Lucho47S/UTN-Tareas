"""
10.Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
"""
#Actividad 10
def solicitar_numero():
    numero = int(input("Ingrese un número entero: "))
    return numero

numero = solicitar_numero()
print("El número ingresado es:", numero)