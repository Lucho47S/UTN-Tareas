# Función para mostrar productos y sus ventas
def mostrar_productos_ventas(productos :list, ventas :list) -> None:
    print("\nVentas trimestrales (en miles de $):")
    print("Producto | T1 | T2 | T3 | Total")
    print("-------------------------------")
    for i in range(len(productos)):
        total = 0
        for valor in ventas[i]:
            total += valor
        print(f"{productos[i]} | {ventas[i][0]} | {ventas[i][1]} | {ventas[i][2]} | {total}")

# Función para ordenar productos por ventas anuales de mayor a menor
def ordenar_por_ventas(productos :list, ventas :list) -> None:
    totales = [0] * len(ventas)
    for i in range(len(ventas)):
        for valor in ventas[i]:
            totales[i] += valor
    for i in range(len(totales) - 1):
        for j in range(i + 1, len(totales)):
            if totales[i] < totales[j]:
                totales[i], totales[j] = totales[j], totales[i]
                productos[i], productos[j] = productos[j], productos[i]
                ventas[i], ventas[j] = ventas[j], ventas[i]
    print("\nProductos ordenados por ventas anuales descendente.")

# Función para buscar producto por nombre
def buscar_producto(productos :list, ventas :list, nombre :str) -> None:
    if nombre in productos:
        indice = productos.index(nombre)
        print(f"\nVentas del producto {nombre}: T1={ventas[indice][0]}, T2={ventas[indice][1]}, T3={ventas[indice][2]}")
    else:
        print("\nProducto no encontrado.")

# Función para buscar un valor de venta en la matriz
def buscar_valor_venta(productos :list, ventas :list, valor :int):
    encontrado = False
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == valor:
                print(f"\nValor encontrado: Producto {productos[i]}, Trimestre T{j+1}")
                encontrado = True
    if not encontrado:
        print("\nValor no encontrado en la matriz.")

# Menú principal
def menu(productos :list, ventas :list) -> None:
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar productos y ventas")
        print("2. Ordenar productos por ventas anuales (desc)")
        print("3. Buscar producto por nombre")
        print("4. Buscar monto de venta en la matriz")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_productos_ventas(productos, ventas)
        elif opcion == "2":
            ordenar_por_ventas(productos, ventas)
        elif opcion == "3":
            nombre = str(input("Ingrese el nombre del producto a buscar (A, B, C): ").upper())
            buscar_producto(productos, ventas, nombre)
        elif opcion == "4":
                valor = int(input("Ingrese el monto de venta a buscar: "))
                buscar_valor_venta(productos, ventas, valor)
        elif opcion == "5":
            print("\nGracias por utilizar el sistema.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")
