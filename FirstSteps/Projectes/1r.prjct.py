# Definimos las tasas de cambio
tasa_usd_eur = 0.85  # 1 USD a EUR
tasa_usd_gbp = 0.73  # 1 USD a GBP
tasa_usd_jpy = 110.0  # 1 USD a JPY

# Solicitamos la cantidad y la moneda de origen
cantidad = float(input("Ingrese la cantidad a convertir: "))
moneda_origen = input("Ingrese la moneda de origen (USD, EUR, GBP, JPY): ").upper()

# Realizamos la conversión
if moneda_origen == "USD":
    eur = cantidad * tasa_usd_eur
    gbp = cantidad * tasa_usd_gbp
    jpy = cantidad * tasa_usd_jpy
    print(f"{cantidad} USD es igual a:")
    print(f"{eur} EUR")
    print(f"{gbp} GBP")
    print(f"{jpy} JPY")
else:
    print("Lo siento, esta versión del conversor solo admite USD como moneda de origen.")

