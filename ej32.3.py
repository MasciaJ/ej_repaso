ruta_archivo = "learning_python.txt"

with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        linea_modificada = linea.replace("Python", "C")
        print(linea_modificada.rstrip())
