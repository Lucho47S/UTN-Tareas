"""
4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 …
"""
#Actividad 4
num = int(input("ingresa un numero: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")