ciudades = {
    "Ciudad1" : {
        "nombre" : "Buenos Aires",
        "habitantes" : "3.121.707",
        "dato" : "es la capital y ciudad más poblada de Argentina, reconocida como un centro cultural y turístico fundamental en Latinoamérica"
    } ,
    "Ciudad2" : {
        "nombre" : "Roma",
        "habitantes" : "2.800.000",
        "dato" : "Roma, la ""Ciudad Eterna"" y capital de Italia, fue fundada el 21 de abril del 753 a.C"
    
    }
}
for ciudad, info in ciudades.items():
    print(ciudad)
    print(f"nombre: {info["nombre"]}")
    print(f"habitantes: {info["habitantes"]}")
    print(f"datos: {info["dato"]}")