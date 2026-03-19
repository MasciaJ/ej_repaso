def construir_perfil(nombre, apellido, **datos):
    info_usuario = {}
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    for clave, valor in datos.items():
        info_usuario[clave] = valor
    return info_usuario

perfil_usuario = construir_perfil("Joaquin", "Mascia",
    nacionalidad="argentino", edad="16", nacimiento="8/9/2009")
print(perfil_usuario)