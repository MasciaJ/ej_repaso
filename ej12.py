import os
os.system("cls")

mis_pizzas = {"muzzarella", "tomate", "cebolla"}
amigo_pizzas = mis_pizzas.copy()
amigo_pizzas.add("anana")
pizza=input("ingresa una pizza que te guste: ")
mis_pizzas.add(pizza)

for pizza in mis_pizzas:
    print("Me gust la piza de ", pizza)
for pizza in amigo_pizzas:
    print("A mi amigo le gusta la piza de ", pizza)