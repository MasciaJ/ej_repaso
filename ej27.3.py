class Usuario:
    def __init__(self, nombre, apellido, **datos):
        self.nombre = nombre
        self.apellido = apellido
        for clave, valor in datos.items():
            setattr(self, clave, valor)

    def describir_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        for atributo in self.__dict__:
            if atributo not in ['nombre', 'apellido']:
                print(f"{atributo.capitalize()}: {getattr(self, atributo)}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! Bienvenido/a.")
usuario1 = Usuario("Joaquin", "Mascia", nacionalidad="argentino", edad="16", nacimiento="8/9/2009")
usuario2 = Usuario("Maria", "Gomez", nacionalidad="chilena", edad="25", nacimiento="15/5/1998")
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario()