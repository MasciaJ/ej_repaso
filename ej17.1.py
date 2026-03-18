users = {
    "persona1" : {"nombre" : "Joaquin","apellido" : "Mascia","edad" : "16","ciudad" : "Buenos Aires"},
    "persona2" : {"nombre" : "Facundo","apellido" : "Carrera","edad" : "16","ciudad" : "Buenos Aires"}
}

for persona, info in users.items():
    print(persona)
    print(f"nombre: {info["nombre"]}")
    print(f"apellido: {info["apellido"]}")
    print(f"edad: {info["edad"]}")
    print(f"ciudad: {info["ciudad"]}")