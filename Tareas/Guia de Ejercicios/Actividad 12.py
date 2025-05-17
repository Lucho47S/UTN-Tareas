"""
12.Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
"""
#Actividad 12
def solicitar_cadena():
    cadena = str(input("Ingrese una cadena/string: "))
    return cadena

cadena_ingresada = solicitar_cadena()
print("La cadena ingresada es:", cadena_ingresada)