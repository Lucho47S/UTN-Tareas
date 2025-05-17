"""
Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango especificado, 
validar los números solicitados dentro de ese rango, guardar en una lista y retornarla. 
El programa principal debe invocar a la función y mostrar por pantalla el retorno.
"""
#Actividad 3

#funcion
def cargar_lista() -> list:
    numeros = [0] * 10  # Inicializa la lista con diez ceros

    flag = True
    rango_inferior = int(input("Ingrese el límite inferior del rango: "))

    while flag: #en caso de que el limite superior no sea valido
        rango_superior = int(input("Ingrese el límite superior del rango: "))
        if(rango_superior < rango_inferior):
            print("Límite Invalido. El límite superior no puede ser menor al límite inferior")
        else:
            flag = False #rompe el bucle

    for i in range(10): #for para introducir los numeros
        numero = int(input(f"Ingrese el número {i + 1} dentro del rango {rango_inferior} a {rango_superior}: "))
        while numero < rango_inferior or numero > rango_superior: #en caso de que el numero no este dentro del rango
            numero = int(input(f"Número inválido. Ingrese un número dentro del rango {rango_inferior} a {rango_superior}: "))
        numeros[i] = numero #remplazar un 0 de la lista por el numero introducido
    return numeros #retornar lista

# Programa principal
resultado = cargar_lista()
print("Numeros resultantes:", resultado)