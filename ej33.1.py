nombre = input("Ingresa tu nombre: ").strip()

with open("guest.txt", "w") as archivo:
    archivo.write(nombre + '\n')

print(f"¡Gracias, {nombre}! Tu nombre se ha guardado en guest.txt.")
