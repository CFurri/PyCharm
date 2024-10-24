peso_payaso = 112
peso_muñeca = 75

nº_payasos = int(input("Nº de payasos: "))
nº_muñecas = int(input("Nº de muñecas: "))

formula = peso_payaso * nº_payasos + peso_muñeca * nº_muñecas

print("Tu paquete va a pesar " + str(formula) + " gramos")
