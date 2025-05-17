"""
Ejercicio 8: Crear una función para cada opción de menú.
Ejercicio 9: Desarrollar las funciones en una biblioteca.
Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación de las listas.
"""
#Actividad 8
# main.py
import Actividad_7 as fu

listas_importadas = False
continuar = True

while continuar == True:
    print("\nMenú de Opciones")
    print("1-Importar listas")
    print("2-Listar datos de usuarios de México")
    print("3-Listar nombre, mail y teléfono de usuarios de Brasil")
    print("4-Listar datos del/los usuario/s más joven/es")
    print("5-Promedio de edad")
    print("6-Mayor edad entre usuarios de Brasil")
    print("7-Usuarios de México y Brasil con CP > 8000")
    print("8-Usuarios italianos mayores a 40 años")
    print("0-Salir")
    
    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        break #cerrar el programa

    if opcion == "1":
        nombres, telefonos, mails, address, postalZip, region, country, edades = fu.importar_listas()
        listas_importadas = True
        print("Listas importadas correctamente.") #Importa todas las listas de datos

    elif not listas_importadas:
        print("Debe importar las listas primero (opción 1).")
    elif opcion == "2":
        fu.usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades)
    elif opcion == "3":
        fu.usuarios_brasil_contacto(nombres, telefonos, mails, country)
    elif opcion == "4":
        otros_datos = [telefonos, mails, address, postalZip, region, country]
        fu.mas_jovenes(nombres, edades, otros_datos)
    elif opcion == "5":
        fu.promedio_edad(edades)
    elif opcion == "6":
        fu.brasil_mayor_edad(nombres, telefonos, mails, address, postalZip, region, country, edades)
    elif opcion == "7":
        fu.postal_mexico_brasil(nombres, telefonos, mails, address, postalZip, region, country, edades)
    elif opcion == "8":
        fu.italianos_mayores_40(nombres, mails, telefonos, country, edades)
    else:
        print("Opción inválida.")