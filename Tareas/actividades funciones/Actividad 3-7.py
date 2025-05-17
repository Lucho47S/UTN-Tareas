"""
Ejercicio 3-7: Realizar un programa que: 
asigne a las variables numero1 y numero2 los valores solicitados al usuario, 
valide los mismos entre 10 y 100, asigne a la variable operacion el valor solicitado al usuario: 
's'-sumar, 'r'-restar (validar), realice la operación de dichos valores a través de una función. 
Mostrar el resultado por pantalla.
"""
#Actividad 7
#Pedir al usuario los valores de las variables numero1 y numero2
numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
#Validar los valores de las variables numero1 y numero2

while numero1 < 10 or numero1 > 100 or numero2 < 10 or numero2 > 100:
    print("Error, los valores deben estar entre 10 y 100")
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segundo valor: "))

#Pedir al usuario el valor de la variable operacion
operacion = input("Ingrese la operacion a realizar: ").lower()

#Validar el valor de la variable operacion
while operacion != 's' and operacion != 'r':
    print("Error, la operacion debe ser 's' para sumar o 'r' para restar")
    operacion = input("Ingrese la operacion a realizar: ")

#Realizar la operacion a traves de una funcion
def realizar_operacion(numero1, numero2, operacion):
    if operacion == 's':
      return numero1 + numero2
    elif operacion == 'r':
        return numero1 - numero2
        #Mostrar el resultado por pantalla

print("El resultado de la operacion es: ", realizar_operacion(numero1, numero2, operacion))

