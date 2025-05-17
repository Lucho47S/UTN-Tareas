"""
2.Escribe una función que calcule el área de un círculo. 
La función debe recibir el radio como parámetro y devolver el área.
"""
#Actividad 2
def area_circulo(radio) -> int:
    return 3.1416 * (radio ** 2)

xd = int(input("Ingreso el radio del círculo: "))
print(area_circulo(f"El radio del circulo es de: {xd}"))