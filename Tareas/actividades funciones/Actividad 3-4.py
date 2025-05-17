"""
Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 
para que valide el número en un rango determinado pasado por parámetro “desde”-“hasta”.
"""
def pedir_numero_en_rango(desde: int, hasta: int) -> int:
    while True:
        numero: int = int(input(f"Ingresá un número entre {desde} y {hasta}: "))
        if desde <= numero <= hasta:
            return numero
        else:
            print("El número está fuera del rango. Intentá de nuevo.")

def mostrar_numero_validado(numero: int, desde: int, hasta: int) -> None:
    if desde <= numero <= hasta:
        print(f"El número {numero} está dentro del rango ({desde}-{hasta}).")
    else:
        print(f"El número {numero} está fuera del rango ({desde}-{hasta}).")
        
numero_ingresado: int = pedir_numero_en_rango(1, 100)
mostrar_numero_validado(numero_ingresado, 1, 100)
