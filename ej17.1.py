users = {
    persona = {"nombre" : "Joaquin","apellido" : "Mascia","edad" : "16","ciudad" : "Buenos Aires"}
    persona1 = {"nombre" : "Facundo","apellido" : "Carrera","edad" : "16","ciudad" : "Buenos Aires"}
}

for persona, info in users.items():
    print(f"nombre: {info}")