import os
os.system("cls")

usuarios = ["admin", "juan", "maria", "pedro", "lucia"]
usuarios_nuevos = ["ana", "carlos", "pedro", "luis", "lucia"]

for usuario in usuarios_nuevos:
    if usuario in usuarios:
        print(f"El nombre de usuario {usuario} ya está en uso. Por favor, elige otro.")
        usuario = input("Ingresa un nuevo nombre de usuario: ")
        usuarios.append(usuario)
    else:
        print(f"El nombre de usuario {usuario} está disponible.")
        usuarios.append(usuario)

os.system("cls")

for usuario in usuarios:
    if usuarios is None:
        print("Necesitamos encontrar algunos usuarios")

    elif usuario == "admin":
        print("Hola admin, ¿quieres ver un informe de estado?")
    else:
        print(f"Hola {usuario}, gracias por iniciar sesión")