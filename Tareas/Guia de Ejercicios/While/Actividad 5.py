"""
WHILE
Contadores - Acumuladores - Máximos y mínimos
Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
"""

#Actividad 5
contador = 0
num = 0
while contador < 6:
    contador += 1
    num += int(input("ingrese un numero para sumar: "))

print(f"la suma de todos los numeros es: {num}")
print(f"el promedio de todos los numeros es: {num / 5}")