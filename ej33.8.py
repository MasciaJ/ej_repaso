import json
fav_num = input('Ingresa tu número favorito: ').strip()

try:
    fav_num_int = int(fav_num)
except ValueError:
    print("No ingresaste un número válido. Se guardará el valor como texto")
    fav_num_int = fav_num

with open("favorite_number.json", "w") as f:
    f.write(json.dumps(fav_num_int))

print("Número favorito guardado en favorite_number.json")

with open("favorite_number.json", "r") as f:
    contenido = f.read()

try:
    numero = json.loads(contenido)
    print(f"¡Sé cuál es tu número favorito! Es {numero}")
except json.JSONDecodeError:
    print("No pude leer el número favorite_number.json")
