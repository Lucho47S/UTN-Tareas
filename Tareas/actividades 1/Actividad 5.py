tarifa_base = 15000
    
estacion = ""
while estacion not in ["Invierno", "Verano", "Otoño", "Primavera"]:
    estacion = input("Ingrese la estación del año (Invierno, Verano, Otoño, Primavera): ")
    
localidad = ""
while localidad not in ["Bariloche", "Cataratas", "Mar del Plata", "Córdoba"]:
        localidad = input("Ingrese la localidad (Bariloche, Cataratas, Mar del Plata, Córdoba): ")
    
if estacion == "Invierno":
    if localidad == "Bariloche":
        tarifa_final = tarifa_base * 1.2
    elif localidad == "Mar del Plata":
        tarifa_final = tarifa_base * 0.8
    else:
        tarifa_final = tarifa_base * 0.9
elif estacion == "Verano":
    if localidad == "Bariloche":
        tarifa_final = tarifa_base * 0.8
    elif localidad == "Mar del Plata":
        tarifa_final = tarifa_base * 1.2
    else:
        tarifa_final = tarifa_base * 1.1
else:
    if localidad == "Córdoba":
        tarifa_final = tarifa_base
    else:
        tarifa_final = tarifa_base * 1.1
    
print("El precio final para", localidad, "en", estacion, "es:", tarifa_final)
