"""
Ejercicio 2: Dadas las siguientes listas: 
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias 
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"] }
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, 
si el nombre es el mismo, debe ordenar por puntos de manera descendente.
"""


def ordenar_por_nombre(nombres: list, puntos: list)-> None:
    n = len(nombres) #definir n
    #Usando el algoritmo bubble sort: (dos bucles anidados para comparar e intercambiar elementos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nombres[j] > nombres[j + 1]: #Comprueba si los nombres estan desordenados(mayor > menor) y los intercambia
                # Intercambiamos los nombres
                temp_nombre = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = temp_nombre

                temp_edad = puntos[j] #También se intercambian las edades en la misma posición 
                puntos[j] = puntos[j + 1]
                puntos[j + 1] = temp_edad 