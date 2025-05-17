# A. Suma de los precios
precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))

suma = precio1 + precio2 + precio3
print(f"La suma de los precios es: {suma:.2f}")

# B. Promedio de los precios
promedio = suma / 3
print(f"El promedio de los precios es: {promedio:.2f}")

# C. Precio final con IVA (21%)
iva = suma * 0.21
precio_final = suma + iva
print(f"El precio final con IVA es: {precio_final:.2f}")
