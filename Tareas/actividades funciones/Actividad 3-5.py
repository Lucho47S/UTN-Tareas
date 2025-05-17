"""
Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en sus 4 combinaciones.
 Restar1(int, int)->int:
 Restar2()->int:
 Restar3(int, int):
 Restar4():
"""
#Actividad 5
# Restar1: recibe dos números y devuelve el resultado
def restar1(a: int, b: int) -> int:
    return a - b

# Restar2: no recibe nada, pide los números y devuelve el resultado
def restar2() -> int:
    a: int = int(input("Ingresá el primer número: "))
    b: int = int(input("Ingresá el segundo número: "))
    return a - b

# Restar3: recibe dos números, resta y muestra el resultado (no devuelve nada)
def restar3(a: int, b: int) -> None:
    resultado: int = a - b
    print("El resultado de la resta es:", resultado)

# Restar4: no recibe nada, pide los números y muestra el resultado
def restar4() -> None:
    a = int(input("Ingresá el primer número: "))
    b = int(input("Ingresá el segundo número: "))
    resultado = a - b
    print("El resultado de la resta es:", resultado)

# Usando restar1
res1 = restar1(10, 3)
print("Restar1:", res1)

# Usando restar2
res2 = restar2()
print("Restar2:", res2)

# Usando restar3
restar3(20, 5)

# Usando restar4
restar4()