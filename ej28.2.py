class Usuario:
    def __init__(self, nombre, apellido, intentos_login = 0, **datos):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_login = intentos_login
        for clave, valor in datos.items():
            setattr(self, clave, valor)

    def incrementar_intentos(self):
        self.intentos_login += 1
        print(f"ingresos: {self.intentos_login}")
    
    def reiniciar_intentos(self):
        self.intentos_login = 0
        print(f"ingresos: {self.intentos_login}")
      
    def describir_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        for atributo in self.__dict__:
            if atributo not in ['nombre', 'apellido']:
                print(f"{atributo.capitalize()}: {getattr(self, atributo)}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! Bienvenido/a.")
usuario1 = Usuario("Pedro", "Fernandez", nacionalidad="argentino", edad="18", nacimiento="14/10/2007")
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario1.incrementar_intentos()
usuario1.incrementar_intentos()
usuario1.reiniciar_intentos()