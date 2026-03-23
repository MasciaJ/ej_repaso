ruta_archivo = "learning_python.txt"

with open(ruta_archivo, "r",) as archivo:
    contenido = archivo.read()

print("--- Leyendo todo el archivo ---")
print(contenido)

with open(ruta_archivo, "r") as archivo:
    lineas = archivo.readlines()

print("--- Leyendo línea por línea desde lista ---")
for linea in lineas:
    print(linea.rstrip())
