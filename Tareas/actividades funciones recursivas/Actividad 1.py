"""
1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero: int) -> int
    pass:
"""
def sumar_naturales(numero: int) -> int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

num = int(input("Ingrese un número natural: "))
if num < 1:
    print("El número debe ser un natural (mayor o igual a 1).")
else:
    print(f"La suma de los primeros {num} números naturales es: {sumar_naturales(num)}")