"""
2. Realizar una función recursiva que calcule la potencia de un número:
"""
#Actividad 2
def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")
