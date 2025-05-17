def calcular_precio_final(precio, tipo_cliente):
    tipo_cliente = tipo_cliente.lower()
    
    match tipo_cliente:
        case "premiun" | "premium":
            descuento = 0.20
        case "regular":
            descuento = 0.15 if precio >= 100 else 0.0
        case "nuevo":
            descuento = 0.10
        case _:
            print("Cliente invalido")
            return
    
    precio_final = precio * (1 - descuento)
    print(f"Precio final: ${precio_final}")


precio = float(input("Ingrese el precio del producto: "))
tipo_cliente = input("Ingrese el tipo de cliente (Premiun, Regular, Nuevo): ")
calcular_precio_final(precio, tipo_cliente)