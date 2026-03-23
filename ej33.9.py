import json
import os

archivo = "favorite_number.json"

if os.path.exists(archivo):
    with open(archivo, "r") as f:
        try:
            numero_favorito = json.load(f)
            print(f"Ya sé cuál es tu número favorito, Es {numero_favorito}")
        except json.JSONDecodeError:
            numero_favorito = None
            print("El archivo existe pero no pude leerlo correctamente")
else:
    numero_favorito = None

if numero_favorito is None:
    while True:
        entrada = input("No tengo tu número favorito. Ingresalo ahora: ").strip()
        if entrada == '':
            print("No ingresaste nada. Intentá de nuevo")
            continue
        try:
            numero_favorito = int(entrada)
        except ValueError:
            print("Por favor ingresa un número entero válido")
            continue

        with open(archivo, "w") as f:
            json.dump(numero_favorito, f)
        print(f"Guardé tu número favorito: {numero_favorito} (en {archivo})")
        break
