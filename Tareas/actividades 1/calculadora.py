operacion = input("¿Qué operación deseas hacer (multiplica/suma/resta/divide)? ").strip().lower()
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))


def calcular(operacion, num1, num2):
    match operacion:
        case "multiplica" | "multiplicar":
            return num1 * num2
        case "suma" | "sumar":
            return num1 + num2
        case "resta" | "restar":
            return num1 - num2
        case "divide" | "dividir":
            return num1 / num2 if num2 != 0 else "Error: División por cero"
        case _:
            return "Operación no válida" 
        
resultado = calcular(operacion, num1, num2)
print("El resultado es:", resultado)
