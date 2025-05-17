"""
Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line.
Para ello necesita un programa que le permita acceder a los datos relevados.
Realizar una función con el siguiente Menú de Opciones:
1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
"""
#Actividad 7
#importa funciones_usuarios.py

def importar_listas():
    from listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades
    return nombres, telefonos, mails, address, postalZip, region, country, edades #importa todo el contenido de Listas_personas.py

def usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades):
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])

def usuarios_brasil_contacto(nombres, telefonos, mails, country):
    for i in range(len(country)):
        if country[i] == "Brazil":
            print(nombres[i], mails[i], telefonos[i])

def mas_jovenes(nombres, edades, otros_datos):
    menor = edades[0]
    for edad in edades:
        if edad < menor:
            menor = edad
    for i in range(len(edades)):
        if edades[i] == menor:
            print(nombres[i], "Edad:", edades[i])
            for dato in otros_datos:
                print(dato[i])

def promedio_edad(edades):
    total = 0
    for edad in edades:
        total += edad
    print("Promedio de edad:", total / len(edades))

def brasil_mayor_edad(nombres, telefonos, mails, address, postalZip, region, country, edades):
    mayor = -1
    indice = -1
    for i in range(len(country)):
        if country[i] == "Brazil" and edades[i] > mayor:
            mayor = edades[i]
            indice = i
    if indice != -1:
        print(nombres[indice], telefonos[indice], mails[indice], address[indice], postalZip[indice], region[indice], country[indice], edades[indice])

def postal_mexico_brasil(nombres, telefonos, mails, address, postalZip, region, country, edades):
    for i in range(len(country)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])

def italianos_mayores_40(nombres, mails, telefonos, country, edades):
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            print(nombres[i], mails[i], telefonos[i])
