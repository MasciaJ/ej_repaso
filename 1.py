#print(str.title(input("se pondra en mayuscula la primera letra de cada palabra que ingreses: ")))

#print(0.1*3)

import random
import os
def limpiar():
    input("enter para continuar...")
    os.system("cls")
os.system("cls")
num = random.randint(0,2)
lista=["Maradona", "Trump", "Maduro"]
for i in lista:
    print(f"hola {i} estas invitado a mi fiesta")
limpiar()
print(f"el invitado {lista[num]} no puede asistir a tu fiesta")
lista.pop(num)
limpiar()
print("nuevos invitados: mirta, peter parker y capusoto")
limpiar()
lista.insert(0,"mirta")
lista.append("capusoto")
lista.insert(2,"peter parker")
print(f"los invitados son:")
for i in lista:
    print(i)
limpiar()
print("parece que solo podes invitar a 2 personas")
while len(lista) > 2:
    print(lista)
    eliminado = input("a quien queres eliminar de la lista?: ")
    if eliminado in lista:
        lista.pop(eliminado)
        print(f"lo siento {eliminado}, no podes venir a mi fiesta")
    else:
        pass
    limpiar()
