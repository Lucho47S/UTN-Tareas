"""
Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos): 
Realizar el juego "Radar del Tesoro" 
Dado el siguiente mapa de 5x5 donde se encuentra oculto un único tesoro, marcado con un 1: 
mapa = [     [0, 0, 0, 0, 0],     [0, 0, 0, 1, 0],     [0, 0, 0, 0, 0],     [0, 0, 0, 0, 0],     [0, 0, 0, 0, 0]]  
Pedir al usuario una coordenada fila (x) entre 0 y 4 (inclusive). 
Pedir al usuario una coordenada columna (y) entre 0 y 4 (inclusive).  
Desarrollar una función con el siguiente prototipo:     
verificar_tesoro(mapa: list, x: int, y: int) -> int  
La función debe retornar: - 0 si el usuario encontró el tesoro.    
 - En caso contrario, retornar la distancia Manhattan entre la coordenada ingresada y la ubicación real del tesoro.  
 **Distancia Manhattan**:   
 distancia = |x_usuario - x_tesoro| + |y_usuario - y_tesoro|  
 Según el valor retornado, mostrar al usuario:     - "¡Encontraste el tesoro!" si retorna 0.     
 - "Fallaste. El tesoro está a X casilleros de distancia." si retorna otro número.  
 El juego continúa hasta que el usuario encuentre el tesoro o hasta que el usuario lo desee. 
 Nota: No se pueden utilizar funciones propias. 
"""
from FuncionesParcial import verificar_tesoro
mapa = [[0, 0, 0, 0, 0],     
        [0, 0, 0, 1, 0],     
        [0, 0, 0, 0, 0],     
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]  

flag = True

while flag == True:

    FilaX = int(input("Ingresa un numero de fila entre 0 y 4: "))
    while 0 > FilaX or FilaX > 4:
        FilaX = int(input("Numero Invalido\nEl numero debe estar entre 0 y 4, ingrese denuevo: "))

    ColumnaY = int(input("Ingresa un numero de columna entre 0 y 4: "))
    while 0 > ColumnaY or ColumnaY> 4:
        ColumnaY = int(input("Numero Invalido\nEl numero debe estar entre 0 y 4, ingrese denuevo: "))

    resultado = verificar_tesoro(mapa, FilaX, ColumnaY)

    if resultado == 0:
        print("¡Encontraste el tesoro!")
        flag = False
    else:
        print(f"Fallaste. El tesoro está a {resultado} casilleros de distancia.")
        continuar = str(input("Quieres volver a intentar? si/no: "))
        if continuar == "si" or continuar == "s":
            continue
        else:
            flag = False