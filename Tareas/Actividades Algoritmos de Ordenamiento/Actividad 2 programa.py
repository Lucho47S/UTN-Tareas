"""
Ejercicio 2: Dadas las siguientes listas: 
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias 
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"] }
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, 
si el nombre es el mismo, debe ordenar por puntos de manera descendente.
"""

from Act2Funcion import ordenar_por_nombre 
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 

ordenar_por_nombre(Nombres, Puntos)

for i in range(len(Nombres)):
    print(Nombres[i], "-", Puntos[i])
