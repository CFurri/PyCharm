barras_vendidas = int(input("Barras vendidas que no son del dia: "))

precio_barra = 3.49
descuento = 0.6
coste = barras_vendidas * precio_barra * (1 - descuento)

print("El coste de una barra fresca es de " + str(precio_barra) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento *100))
print("El coste final total es de " + str(round(coste,2)))


