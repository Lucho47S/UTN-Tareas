edad = int(input("Ingrese su edad: "))

match edad:
    case _ if edad >= 18:
        print("Eres mayor de edad.")
    case _ if 13 <= edad <= 17:
        print("Eres adolescente.")
    case _ if 13 > edad > 0:
        print("Eres niño.")
    case _:
        print("Esa edad no es valida")
