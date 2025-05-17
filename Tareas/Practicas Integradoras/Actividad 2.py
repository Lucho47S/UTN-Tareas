"""
Enunciado/s:
TabladePosicionesdeTorneodePing-Pong
Cargarlosdatosdelosjugadoresconelpropósitoderealizarestadísticas(nosesabecuántos):.
Losdatosquesecargaránson:
Nombredeljugador
Edad(validar)
Cantidaddepuntos(validar-númeroenteropositivo,hasta60).
Númerodepartidosganados(validar-númeroenteropositivo,hasta35).
Tipodesaque("plano","liftado","cortado")
Categoría("elite","experto","avanzado")
Senecesitasaber
TemaA:
1-Cantidaddejugadoresdelacategoría"elite"contipodesaque“plano”,cuyaedadestéentre19y25añosinclusive.
2-NombreyCategoríadeljugadordemenoredadconmásde50puntos.
3-Porcentajedejugadoresdecategoría"experto".
4-Mostrarelpromediodeedaddelosjugadorescuyacategoríaes“avanzado”.
5-Determinareltipodesaquemásusadoporlosjugadores,cuyacategoríasea“elite”.
Repaso
"""
contador_elite_plano = 0
nombre_menor_50p = None
categoria_menor_50p = None
edad_menor_50p = None
hay_mayor_50 = False
total_jugadores = 0
contador_experto = 0
suma_edad_avanzado = 0
contador_avanzado = 0

saques_elite = {"plano": 0, "liftado": 0, "cortado": 0}

seguir = "si"
while seguir.lower() == "si":
    print("\n--- Nuevo jugador ---")

    nombre = input("Nombre del jugador: ")

    edad_valida = False
    while not edad_valida:
        edad = int(input("Edad del jugador: "))
        if edad > 0 and edad < 100:
            edad_valida = True
        else:
            print("La edad debe ser mayor que 0 y menor a 100.")

    puntos_validos = False
    while not puntos_validos:
        puntos = int(input("Cantidad de puntos (hasta 60): "))
        if 0 <= puntos <= 60:
            puntos_validos = True
        else:
            print("Debe ser un número positivo hasta 60.")

    partidos_validos = False
    while not partidos_validos:
        partidos = int(input("Cantidad de partidos ganados (hasta 35): "))
        if 0 <= partidos <= 35:
            partidos_validos = True
        else:
            print("Debe ser un número positivo hasta 35.")

    saque_valido = False
    while not saque_valido:
        tipo_saque = input("Tipo de saque (plano/liftado/cortado): ").lower()
        if tipo_saque in ["plano", "liftado", "cortado"]:
            saque_valido = True
        else:
            print("Saque no válido. Opciones: plano, liftado, cortado.")

    categoria_valida = False
    while not categoria_valida:
        categoria = input("Categoría (elite/experto/avanzado): ").lower()
        if categoria in ["elite", "experto", "avanzado"]:
            categoria_valida = True
        else:
            print("Categoría no válida. Opciones: elite, experto, avanzado.")

    total_jugadores += 1

    # Punto 1
    if categoria == "elite" and tipo_saque == "plano" and 19 <= edad <= 25:
        contador_elite_plano += 1

    # Punto 2
    if puntos > 50:
        if not hay_mayor_50 or edad < edad_menor_50p:
            hay_mayor_50 = True
            nombre_menor_50p = nombre
            categoria_menor_50p = categoria
            edad_menor_50p = edad

    # Punto 3
    if categoria == "experto":
        contador_experto += 1

    # Punto 4
    if categoria == "avanzado":
        suma_edad_avanzado += edad
        contador_avanzado += 1

    # Punto 5
    if categoria == "elite":
        saques_elite[tipo_saque] += 1

    # Continuar o no
    seguir = input("¿Deseás cargar otro jugador? (si/no): ")

# Resultados
print("\n--- Resultados ---")

print(f"1. Cantidad de jugadores 'elite' con saque 'plano' entre 19 y 25 años: {contador_elite_plano}")

if hay_mayor_50:
    print(f"2. Jugador de menor edad con más de 50 puntos: {nombre_menor_50p}, Categoría: {categoria_menor_50p}")
else:
    print("2. No hubo jugadores con más de 50 puntos.")

if total_jugadores > 0:
    porcentaje_expertos = (contador_experto / total_jugadores) * 100
    print(f"3. Porcentaje de jugadores con categoría 'experto': {porcentaje_expertos:.2f}%")
else:
    print("3. No se ingresaron jugadores.")

if contador_avanzado > 0:
    promedio_edad_avanzado = suma_edad_avanzado / contador_avanzado
    print(f"4. Promedio de edad de jugadores 'avanzado': {promedio_edad_avanzado:.2f}")
else:
    print("4. No hubo jugadores 'avanzado'.")

tipo_saque_mas_usado = max(saques_elite, key=saques_elite.get)
print(f"5. Tipo de saque más usado por jugadores 'elite': {tipo_saque_mas_usado}")