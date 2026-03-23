import random
class dado:
    def __init__ (self, lados):
        self.lados = lados

    def tirar(self):
        print(f"dado de {self.lados} caras")
        for i in range(10):
            print(f"{random.randint(1, self.lados)}")

dado6 = dado(6)
dado10 = dado(10)
dado20 = dado(20)

dado6.tirar()
dado10.tirar()
dado20.tirar()