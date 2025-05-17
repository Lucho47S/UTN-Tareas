"""
Ejercicio 3-6: 
Realizar un programa que: 
asigne a la variable numero1 un valor solicitado al usuario, valide el mismo entre 10 y 100, 
realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento(). 
Mostrar el resultado por pantalla. Atención: pueden reutilizarse funciones ya creadas.
"""
#Actividad 6
#Función para realizar descuento
def realizarDescuento(numero):
    return numero - numero * 0.05
#Función para solicitar un número al usuario
def solicitarNumero():
    flag = True 
    while flag == True:
        numero = float(input("Ingrese un número entre 10 y 100: "))
        if 10 <= numero <= 100:
            flag = False
            return numero
        else:
            print("El número debe estar entre 10 y 100")

#Función para calcular el descuento
def calcularDescuento(numero):
    descuento = realizarDescuento(numero)
    return descuento

#Función principal
numero1 = solicitarNumero()
descuento = calcularDescuento(numero1)
print(f"El precio con descuento es: {descuento}")