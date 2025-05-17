"""
5.Define una función que encuentre el máximo de tres números. 
La función debe aceptar tres argumentos y devolver el número más grande.
sin utilizar max o min
"""
#Actividad 5
def max_of_three(a, b, c) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: return c

Num1 = int(input("Ingresa el primer numero: "))
Num2 = int(input("Ingresa el segundo numero: "))
Num3 = int(input("Ingresa el tercer numero: "))

print("El número máximo es:", max_of_three(Num1, Num2, Num3))
