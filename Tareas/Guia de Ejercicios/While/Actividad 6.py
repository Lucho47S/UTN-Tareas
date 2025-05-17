"""
WHILE
Contadores - Acumuladores - Máximos y mínimos
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
"""
#Actividad 6
num = 0
contador = 0
flag = True
while flag == True:
    num += int(input("ingrese un numero para sumar: "))
    contador += 1
    continuar = str(input("Quieres seguir ingresando numeros?"))
    if continuar == "si" or continuar == "s":
        continue
    else:
        flag = False
        print(f"la suma de todos los numeros es: {num}")
    print(f"el promedio de todos los numeros es: {num / contador}")