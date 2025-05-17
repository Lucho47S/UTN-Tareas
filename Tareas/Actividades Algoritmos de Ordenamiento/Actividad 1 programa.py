"""
Ejercicio 1: Dadas las siguientes listas: 
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente. 
"""
#Actividad 2
from Act1Funcion import ordenar_por_nombre 
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 


ordenar_por_nombre(Nombres, Edades)

for i in range(len(Nombres)):
    print(Nombres[i], "-", Edades[i])