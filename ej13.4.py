import os
os.system("cls")
persona_edad = int(input("Ingrese su edad: "))
if persona_edad < 2:
    print("Eres un bebé")
elif persona_edad < 4 and persona_edad >= 2:
    print("Eres un niño/a pequeño/a")
elif persona_edad < 13 and persona_edad >= 4:
    print("Eres un niño/a")
elif persona_edad < 20 and persona_edad >= 13:
    print("Eres un adolescente")
elif persona_edad < 65 and persona_edad >= 20:
    print("Eres un adulto")
else:
    print("Eres un anciano")