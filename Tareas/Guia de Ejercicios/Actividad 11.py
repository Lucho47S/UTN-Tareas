"""
11.Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
"""
#Actividad 11
def solicitar_numero():
    numero = float(input("Ingrese un número flotante: "))
    return numero

numero = solicitar_numero()
print("El número flotante ingresado es:", numero)