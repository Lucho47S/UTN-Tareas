"""
3.Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.
"""

#Actividad 3
def verificar_par_impar(numero :int):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

Num = int(input("Ingresa un numero: "))
verificar_par_impar(Num)