"""
9.Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
Por defecto es del 1 al 10.
"""
#Actividad 9
def tabla_multiplicar_desde_input() -> None:
    try:
        numero = int(input("Ingresá el número para la tabla: "))

        inicio_input = input("Ingresá el valor inicial del rango (por defecto 1): ")
        fin_input = input("Ingresá el valor final del rango (por defecto 10): ")

        inicio = int(inicio_input) if inicio_input.strip() != "" else 1
        fin = int(fin_input) if fin_input.strip() != "" else 10

        print(f"\nTabla del {numero} del {inicio} al {fin}:")
        for i in range(inicio, fin + 1):
            print(f"{numero} x {i} = {numero * i}")

    except ValueError:
        print("Por favor ingresá solo números válidos.")

tabla_multiplicar_desde_input()
