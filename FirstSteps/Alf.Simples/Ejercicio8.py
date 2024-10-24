peso = float(input("Peso: "))
estatura = float(input("Estatura: "))
imc = (peso) / (estatura ** 2)

respuesta = print(f"Tu índice de masa corporal es de {imc:.2f}")

if imc < 18.5:
    print("Te faltan unos Kilos")
    print(f"Te faltan {18.5 - imc:.2f} puntos")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso saludable :)")
elif 25 <= imc < 29.0:
    print("Tienes sobrepeso")
elif imc < 30:
    print("Tienes obesidad")





