import random

class Loteria:
    def __init__(self, numeros, letras):
        self.bolsa = list(numeros) + list(letras)

    def seleccionar_ganadores(self, cantidad=4):
        self.ganadores = random.sample(self.bolsa, cantidad)
        return self.ganadores

    def mostrar_resultado(self):
        if not hasattr(self, "ganadores"):
            raise ValueError("Debe seleccionar ganadores primero")
        print("--- RESULTADO LOTERÍA ---")
        print(f"Bolsa completa: {self.bolsa}")
        print(f"Ganadores (4 elementos): {self.ganadores}")
        print("Cualquier boleto que contenga estos 4 elementos gana un premio.")



numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letras = ("A", "B", "C", "D", "E")

sorteador = Loteria(numeros, letras)
seleccionados = sorteador.seleccionar_ganadores(4)
sorteador.mostrar_resultado()