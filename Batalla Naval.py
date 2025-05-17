'''
Realizar el juego de la Batalla Naval
Dado el siguiente tablero con los barcos ubicados de la siguiente forma:
tablero 
= [[O, 0, 1, 0, 0].
[0, 1, 0, 1, 0].
[1,0, 0, 1, 0].
[0, 0, 1, 0, 1].
[0, 0, 0, 0, 1]]
Pedirle una coordenada al usuario para la fila (x) [validar 0-4]
Pedirle una coordenada al usuario para la columna (V) [validar 0-4]
Desarrollar una función con el siguiente prototipo:
verificar_coordenadas( tablero list, x int, y int )->bool:
La función debe retornar "True" si el barco fue hundido (1) y "False" si disparó en el agua (0)
Según lo retornado por la función, mostrar al usuario los siguientes mensajes:
"Hundido"
"Agua"
El usuario puede realizar tantos disparos como quiera, cuando no quiera seguir disparando, se le debe informar
cuantos barcos fueron hundidos.
'''
from funcionesBatallaNaval import verificar_coordenadas, pedir_coordenadas, jugar 
tablero = [[0, 0, 1, 0, 0],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 1, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 1]]

jugar(tablero)

#pruebaaaaaa