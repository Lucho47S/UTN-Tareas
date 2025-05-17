"""
2-Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
"""
#Actividad 2
nota = int(input("Ingrese la nota recibida: "))

if 0 < nota < 4:
    print(f"Desaprobado, la nota es: {nota}")
elif 3 < nota < 6:
    print(f"Aprobado, la nota es: {nota}")
elif 5 < nota < 11:
    print(f"Promoción directa, la nota es: {nota}")
else:
    print("la nota ingresada no es valida")