"""
Ejercicio 1: Dadas las siguientes listas: 
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente. 
"""


def ordenar_por_nombre(nombres: list, edades: list)-> None:
    n = len(nombres) #definir n
    #Usando el algoritmo bubble sort: (dos bucles anidados para comparar e intercambiar elementos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nombres[j] > nombres[j + 1]: #Comprueba si los nombres estan desordenados(mayor > menor) y los intercambia
                # Intercambiamos los nombres
                temp_nombre = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = temp_nombre

                temp_edad = edades[j] #También se intercambian las edades en la misma posición 
                edades[j] = edades[j + 1]
                edades[j + 1] = temp_edad 