def hacer_camiseta(tamaño, mensaje):
    print(f"la camiseta es de tamaño {tamaño} y el mensaje es {mensaje}")

hacer_camiseta("grande", "me encanta python")
hacer_camiseta("mediana", "me encanta python")
mensaje = input("ingresa el mensaje para la camiseta: ")
hacer_camiseta("pequeña", mensaje)