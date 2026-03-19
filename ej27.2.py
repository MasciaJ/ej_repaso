class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
restaurante1 = Restaurante("La Buena Mesa", "italiana")
restaurante2 = Restaurante("Sabor Argentino", "argentina")
restaurante3 = Restaurante("Sushi World", "japonesa")
restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()
