import os
os.system("cls")
opcion = None
pizza = []
while opcion != "salir":
    os.system("cls")
    opcion = input("que le quieres agregar a la pizza? (ongrese salir para terminar)")
    if opcion != "salir":
        pizza.append(opcion)
os.system("cls")
print("tu pizza es de:")
for ingrediente in pizza:
    print(ingrediente)