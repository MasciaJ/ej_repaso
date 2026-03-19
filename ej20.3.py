import os
encuesta = []

encuesta_activa = True

while encuesta_activa:
    os.system("cls")
    respuesta = input("a que lugar viajarias? (salir para terminar): ")
    if respuesta == "salir":
        encuesta_activa = False
    else:
        encuesta.append(respuesta)

os.system("cls")
print("resultado de la encuesta")
for i, destino in enumerate(encuesta, start = 1):
    print(f"{i},{destino}")