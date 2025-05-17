"""
1-A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""

#Actividad 1
Altura = int(input("Ingresa la altura del jugador en la cancha "))

if Altura >= 0:
    if Altura < 160:
        print("el jugador se encuentra en la base")
    elif 160 <= Altura <= 179:
        print("El jugador se encuentra en Escolta")
    elif 180 <= Altura <= 199:
        print("El jugador se encuentra en Alero")
    else:
        print("El jugador se encuentra en el Ala-Pívot")
else:
    print("Altura invalida")