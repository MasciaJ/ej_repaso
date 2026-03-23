from admin import Administrador

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