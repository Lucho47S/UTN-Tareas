"""
8. Realizar un programa que permita mostrar una pirámide de números.
"""
#Actividad 8
numero = int(input("Ingresá un número: "))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
