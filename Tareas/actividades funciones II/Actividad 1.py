"""
1.Escribir una función que calcule el área de un rectángulo. 
La función recibe la base y la altura y retorna el área.
"""

def area_rectangulo() -> int:
    base = int(input("Ingresa la base del rectangulo "))
    altura = int(input("Ingresa la altura del rectangulo "))
    return base * altura
print(f"El area del rectangulo es: {area_rectangulo()}")

