"""
UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.
Las posibles aplicaciones son las siguientes:
● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.
"""
cantidad_especial = 0
cantidad_no_ia_condicional = 0
total_empleados = 10
mayor_edad_masculino = -1
nombre_mayor_masculino = ""
tecnologia_mayor_masculino = ""

for i in range(total_empleados):
    print(f"\n--- Encuesta {i + 1} ---")
    
    nombre = input("Nombre del empleado: ")

    edad_valida = False
    while edad_valida == False:
            edad = int(input("Edad (mayor o igual a 18): "))
            if edad >= 18:
                edad_valida = True
            else:
                print("La edad debe ser 18 o mayor.\n Ingrese una Edad (mayor o igual a 18)")

    # Validación de género sin usar break
    genero_valido = False
    while genero_valido == False:
        genero = input("Género (Masculino/Femenino/Otro): ").capitalize()
        if genero in ["Masculino", "Femenino", "Otro", "M", "F", "O"]:
            genero_valido = True
        else:
            print("Género no válido. Intentá de nuevo.")

    # Validación de tecnología sin usar break
    tecnologia_valida = False
    while tecnologia_valida == False:
        tecnologia = input("Tecnología (IA/RV/RA/IOT): ").upper()
        if tecnologia in ["IA", "RV", "RA", "IOT"]:
            tecnologia_valida = True
        else:
            print("Tecnología no válida. Intentá de nuevo.")

    # Punto 1
    if genero == "Masculino" and 25 <= edad <= 50 and tecnologia in ["IA", "IOT"]:
        cantidad_especial += 1

    # Punto 2
    if tecnologia != "IA" and (genero != "Femenino" or 33 <= edad <= 40):
        cantidad_no_ia_condicional += 1

    # Punto 3
    if genero == "Masculino" and edad > mayor_edad_masculino:
        mayor_edad_masculino = edad
        nombre_mayor_masculino = nombre
        tecnologia_mayor_masculino = tecnologia

# Resultados
print("\n--- Resultados ---")
print(f"1. Cantidad de empleados masculinos que votaron por IA o IOT entre 25 y 50 años: {cantidad_especial}")
porcentaje = (cantidad_no_ia_condicional / total_empleados) * 100
print(f"2. Porcentaje de empleados que no votaron por IA según condiciones: {porcentaje:.2f}%")
if mayor_edad_masculino != -1:
    print(f"3. Empleado masculino de mayor edad: {nombre_mayor_masculino}, Tecnología votada: {tecnologia_mayor_masculino}")
else:
    print("3. No hubo empleados masculinos en la encuesta.")
