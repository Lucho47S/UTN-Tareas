"""
Ejercicio 5: Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, 
busque a las personas de menor edad (puede ser más de una) y las retorne. 
El programa principal deberá mostrar nombre y edad de los menores.
"""
#Actividad 5

nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]
#edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 22]
#funcion
def buscar_menores(lista_edades: list) -> list:
    menores = [0] * len(lista_edades)  # Lista para guardar índices de los menores
    i = 1
    minimo = lista_edades[0] #controla el numero minimo
    cantidad = 1 #cantidad de personas con dicha edad
    while i < len(lista_edades):
        if lista_edades[i] < minimo: #establece un nuevo minimo si el numero es menor al actual
            minimo = lista_edades[i]
            cantidad = 1
            menores[0] = i
        elif lista_edades[i] == minimo: #suma otra persona con la misma edad minima
            menores[cantidad] = i
            cantidad += 1
        i += 1

    resultado = [0] * cantidad #nueva lista con la cantidad de menores
    j = 0
    while j < cantidad:
        resultado[j] = menores[j]
        j += 1

    return resultado


# Programa principal
indices_menores = buscar_menores(edades)

print("Personas con menor edad:")
for i in indices_menores:
    print("Nombre:", nombres[i], "- Edad:", edades[i])