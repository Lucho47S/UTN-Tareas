
edad = int(input("Ingrese la edad: "))
estado_civil = input("Ingrese el estado civil (Soltero, Casado, Divorciado): ")
        
if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero.")

if edad < 0:
    print("La edad no puede ser negativa.")