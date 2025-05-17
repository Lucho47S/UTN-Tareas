numeros = []
    
while len(numeros) < 5:
        try:
            num = int(input("Ingrese un número distinto de 0: "))
            if num == 0:
                print("El número no puede ser 0. Intente nuevamente.")
            else:
                numeros.append(num)
        except ValueError:
            print("Ingrese un número válido.")
    
pares = 0
impares = 0
menor = numeros[0]
mayor_par = None
suma_positivos = 0
producto_negativos = 1
hay_negativos = False
    
for num in numeros:
        if num % 2 == 0:
            pares += 1
            if mayor_par is None or num > mayor_par:
                mayor_par = num
        else:
            impares += 1
        
        if num < menor:
            menor = num
        
        if num > 0:
            suma_positivos += num
        elif num < 0:
            producto_negativos *= num
            hay_negativos = True
    
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("El menor número ingresado:", menor)
print("El mayor número par ingresado:", mayor_par if mayor_par is not None else "No se ingresaron pares")
print("Suma de los positivos:", suma_positivos)
print("Producto de los negativos:", producto_negativos if hay_negativos else "No se ingresaron negativos")