"""
13.Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar validaciones.
(10.
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
11.
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
12.
Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.)def solicitar_dato(tipo):
"""
#Actividad 13
def solicitar_numero_entero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error. Por favor, ingrese un número entero.")

def solicitar_numero_flotante():
    while True:
        try:
            numero = float(input("Ingrese un número flotante: "))
            return numero
        except ValueError:
            print("Error. Por favor, ingrese un número flotante.")

def solicitar_cadena():
    while True:
        cadena = input("Ingrese una cadena: ")
        if cadena:
            return cadena
        else:
            print("Error. La cadena no puede estar vacía.")

def solicitar_dato(tipo):
    if tipo == "entero":
        return solicitar_numero_entero()
    elif tipo == "flotante":
        return solicitar_numero_flotante()
    elif tipo == "cadena":
        return solicitar_cadena()
    else:
        raise ValueError("Tipo de dato no válido")

# Ejemplo de uso
numero_entero = solicitar_dato("entero")
numero_flotante = solicitar_dato("flotante")
cadena = solicitar_dato("cadena")

print("Número entero:", numero_entero)
print("Número flotante:", numero_flotante)
print("Cadena:", cadena)