#Ejemploemplo1
print('Ejemploemplo1\n')
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}")
#Ejemplo2
print('Ejemplo2\n')
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
suma = num1 + num2
print(f"La suma es: {suma}")


#Ejemplo3
print('Ejemplo3\n')
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")


#Ejemplo4
print('Ejemplo4\n')
nombre = input("Ingresa tu nombre: ")
comision = input("Ingresa tu número de comisión: ")
asignatura = input("Ingresa la asignatura: ")
docente = input("Ingresa el nombre del docente: ")
presente = input("¿Estuviste presente? (Sí/No): ")

print(f"Nombre: {nombre}")
print(f"Comisión: {comision}")
print(f"Asignatura: {asignatura}")
print(f"Docente: {docente}")
print(f"Estuvo presente: {presente}")


#Ejemplo5
print('Ejemplo5\n')
lado = float(input("Ingresa el lado del cuadrado: "))
superficie = lado ** 2
print(f"La superficie del cuadrado es: {superficie}")

#Ejemplo6
print('Ejemplo6\n')
lado1 = float(input("Ingresa el primer lado del rectángulo: "))
lado2 = float(input("Ingresa el segundo lado del rectángulo: "))
superficie = lado1 * lado2
print(f"La superficie del rectángulo es: {superficie}")

#Ejemplo7
print('Ejemplo7\n')
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
superficie = (base * altura) / 2
print(f"La superficie del triángulo es: {superficie}")

#Ejemplo8
print('Ejemplo8\n')
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
iva = precio * 0.21  # Suponiendo un 21% de IVA
precio_total = precio + iva
print(f"Producto: {producto}")
print(f"Precio sin IVA: {precio}")
print(f"IVA: {iva}")
print(f"Precio total con IVA: {precio_total}")

#Ejemplo9
print('Ejemplo9\n')
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"Nombre: {nombre} {apellido}")
print(f"Promedio: {promedio}")

#Ejemplo10
print('Ejemplo10H\n')
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
edad_futura = edad + 10
print(f"Hola {nombre}, en 10 años tendrás {edad_futura} años.")