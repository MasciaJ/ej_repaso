import os
os.system("cls")

lugares = []
for i in range (5):
    ingresar = input("Ingrese un lugar: ")
    lugares.append(ingresar)
os.system("cls")
print(f"lugar original: {lugares}")
lugares_ordenados = sorted(lugares)
print(f"lugar ordenado: {lugares_ordenados}")
lugares_vuelta = sorted(lugares, reverse=True)
print(f"lugares dados vuelta: {lugares_vuelta}")