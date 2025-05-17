"""
Ejercicio 6: Analizar los datos del archivo listas_personas.py. 
Utilizando el archivo listas_personas.py. 
Importar los nombres a una lista. Realizar una función que muestre los mismos.
"""
#Actividad 6
from listas_personas import nombres #Importar la variable nombres de lista_personas

#funcion
def mostrar_nombres(lista_nombres: list) -> None:#none pq no hay return
    i = 0 #para que el indice no exceda la lista
    while i < len(lista_nombres):
        print(lista_nombres[i])
        i += 1

#Programa
mostrar_nombres(nombres)

