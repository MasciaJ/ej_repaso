import os
os.system("cls")
persona_edad = int(input("Ingrese su edad: "))
if persona_edad < 3:
    print("ingresas gratis")
elif persona_edad < 12 and persona_edad >= 4:
    print("Pagas 10")
elif persona_edad >= 12:
    print("pagas 15")