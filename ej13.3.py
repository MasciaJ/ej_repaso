import random, os
os.system("cls")
color_alien = ["verde", "amarillo", "rojo", "azul"]

while True:
    random_color = random.choice(color_alien)
    if random_color == "verde":
        print("el alien es verde, el jugador acaba de ganar 5 puntos")
    elif random_color == "amarillo":
        print("el alien es amarillo, el jugador acaba de ganar 10 puntos")
    elif random_color == "rojo":
        print("el alien es rojo, el jugador gano 15 puntos")
    else:
        print("el alien es azul, el jugador no gana puntos")
    input("enter para continuar...")
    os.system("cls")