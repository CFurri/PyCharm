interés = 4
n1 = 1
n2 = 2
n3 = 3

dinero_cuenta = float(input("Dinero en cuenta: "))
formula1 = dinero_cuenta * ( 4/100 + 1) ** n1
formula2 = dinero_cuenta * ( 4/100 + 1) ** n2
formula3 = dinero_cuenta * ( 4/100 + 1) ** n3

print(round(formula1,2))
print(round(formula2,2))
print(round(formula3,2))

