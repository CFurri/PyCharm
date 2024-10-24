a = input("Sección: ").lower()

if a == "pastes fines":
    pastes_fines = input("Quin problema tens? ").lower()
    if pastes_fines == "màquina":
        print("Truca al 4202")
    elif pastes_fines == "qualitat":
        print("Truca al 4570")

elif a == "llescats":
    print("Quin problema tens?")

elif a == "picat":
    print("Quin problema tens?")

else:
    print("No has triat cap opció vàlida. Recorda escriure correctament el nom de la secció. "
          "Pots triar entre Paté, Picat, Pastes fines, LLescats, Pal·letització, Molls...")
    print(f"El que has escrit té " + str(len(a)) + " lletres")


