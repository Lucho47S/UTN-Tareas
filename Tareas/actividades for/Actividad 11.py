"""
10.Ingresar un número. Determinar si el número es primo o no.
"""
#Actividad 10
numero = int(input("Ingresá un número: "))

if numero < 2:
    print(f"{numero} no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")
