import os
os.system("cls")
mis_frutas = ["manzana", "banana", "naranja"]
usuario_frutas = []
for i in range(3):
    fruta = input("ingresa una fruta que te guste: ")
    usuario_frutas.append(fruta)
os.system("cls")
for fruta in usuario_frutas:
    if fruta in mis_frutas:
        print(f"me gusta la {fruta} tambien")