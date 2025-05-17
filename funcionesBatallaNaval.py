def verificar_coordenadas(tablero :list, x :int, y :int) -> bool:
    if tablero[x][y] == 1: #revisa si hay un barco en la casilla y lo remplaza
        tablero[x][y] = 0
        return True
    
    elif tablero[x][y] == 0:
        return False

def pedir_coordenadas():
    Flag = True

    while Flag == True:
            x = int(input("Ingrese la coordenada de la fila (0-4): "))
            y = int(input("Ingrese la coordenada de la columna (0-4): "))

            if 0 <= x <= 4 and 0 <= y <= 4: #revisa que el usuario ponga un valor valido
                Flag = False
                return x, y
            
            else:
                print("Coordenadas fuera de rango. Por favor, ingrese valores entre 0 y 4.")

def jugar(tablero :list):
    barcos_hundidos = 0
    Flag = True
    
    while Flag == True:
        x, y = pedir_coordenadas()
        resultado = verificar_coordenadas(tablero, x, y) #envia los datos para verificar

        if resultado == True:
            print("Hundido")
            barcos_hundidos += 1

        else:
            print("Agua")
        respuesta = input("¿Desea seguir disparando? (s/n): ")

        if respuesta != "s":
            Flag = False

    print(f"Juego terminado. Barcos hundidos: {barcos_hundidos}")
