"""
Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, 
los guarde en una lista y la retorne. 
El programa principal debe invocar a la función y mostrar por pantalla el retorno.
"""
#Actividad 1

#funcion
def pedir_nombres() -> list:
    nombres = [""] * 10 #10 espacios vacios
    for i in range(10):
        nombres[i] = str(input(f"Ingrese el nombre {i+1}: ")) #pide un nombre y avanza 
    return nombres

#programa principal
nombres_lista = pedir_nombres()
print("Nombres ingresados:", nombres_lista)

