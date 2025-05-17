
def verificar_tesoro(mapa: list, x: int, y: int):
    x_tesoro = 1
    y_tesoro = 3

    if mapa[x][y] == 1:
        return 0
    else:
        distancia = x - x_tesoro + y - y_tesoro
        return distancia
    
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