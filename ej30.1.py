from restaurante import Restaurante

mi_restaurante = Restaurante("La Buena Mesa", "italiana")

print(f"Nombre: {mi_restaurante.nombre_restaurante}")
print(f"Tipo de cocina: {mi_restaurante.tipo_cocina}")
print(f"Clientes atendidos: {mi_restaurante.clientes_atendidos}")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()