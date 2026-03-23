class heladerias:
    def __init__(self, nombre, sabores):
        self.nombre = nombre
        self.sabores = sabores
    
    def mostrar_sabores(self):
        for sabor in self.sabores:
            print(sabor)

heladeria1 = heladerias("grido", ["dulce de leche", "crema americana", "chocolate"])
heladeria1.mostrar_sabores()