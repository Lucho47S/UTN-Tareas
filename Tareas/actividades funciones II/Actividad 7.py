"""
7.Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
"""
#Actividad 7
def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

Num = int(input("Ingrese un numero: "))
print(f"¿El número {Num} es primo? {es_primo(Num)}")