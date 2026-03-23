class Privilegios:
    def __init__(self, privilegios=None):
        self.privilegios = privilegios if privilegios else []
    
    def mostrar_privilegios(self, nombre_admin=""):
        if nombre_admin:
            print(f"\nPrivilegios de {nombre_admin}:")
        else:
            print("\nPrivilegios:")
        
        if self.privilegios:
            for privilegio in self.privilegios:
                print(f"  - {privilegio}")
        else:
            print("  Sin privilegios asignados")


class Usuario:
    def __init__(self, nombre, apellido, intentos_login=0, **datos):
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
            if atributo not in ['nombre', 'apellido', 'privilegios_obj']:
                print(f"{atributo.capitalize()}: {getattr(self, atributo)}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! Bienvenido/a.")


class Administrador(Usuario):
    def __init__(self, nombre, apellido, privilegios=None, intentos_login=0, **datos):
        super().__init__(nombre, apellido, intentos_login, **datos)
        self.privilegios_obj = Privilegios(privilegios)
    
    def mostrar_privilegios(self):
        self.privilegios_obj.mostrar_privilegios(f"{self.nombre} {self.apellido}")


# Crear una instancia de Administrador
admin1 = Administrador(
    "Carlos", 
    "Lopez", 
    privilegios=["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios", "puede ver estadísticas"],
    edad="35",
    nacionalidad="argentino"
)

admin1.describir_usuario()
admin1.saludar_usuario()
admin1.mostrar_privilegios()