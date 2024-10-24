# Solicitar al usuario que ingrese el peso en kilogramos
peso_kg = float(input("Por favor, ingresa tu peso en kilogramos: "))

# Solicitar al usuario que ingrese la estatura en metros
estatura_metros = float(input("Por favor, ingresa tu estatura en metros: "))

# Calcular el IMC
imc = peso_kg / (estatura_metros ** 2)

# Imprimir el IMC con dos decimales
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

