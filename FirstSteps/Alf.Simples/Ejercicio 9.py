P = float(input("Cantidad a invertir: "))
i_str= float(input("Interés anual: "))
n = float(input("Por cuántos años: "))


print("Capital final" , str(round((P * ( i_str / 100 + 1 )) ** n , 2)))

