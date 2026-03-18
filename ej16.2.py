import os
os.system("cls")
glosario = {
    "rio Nilo" : "Egipto",
    "Rio de la plata" : "Buenos Aires",
    "Rio amazonas" : "Brasil",
    "Rio missisippi" : "Estados unidos",
    "Rio danubio" : "Europa"
}
for rio, pais in set(glosario.items()):
    print(f"El {rio} pasa por {pais}")