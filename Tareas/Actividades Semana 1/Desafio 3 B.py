numero = int(input("Ingresa un número: "))
incremento = int(input("introduce las veces que lo quieres incrementar: "))
#lo mismo pero usando un for para no hacerlo manualmente
#(lo adjunto separado porque aun no lo vimos)
for i in range(incremento):
    numero += 1
    print(f"Incremento {i + 1}: {numero}")
