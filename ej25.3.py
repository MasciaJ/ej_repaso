def hacer_auto(fabricante, modelo, **datos):
    auto_info = {}
    auto_info['fabricante'] = fabricante
    auto_info['modelo'] = modelo
    for clave, valor in datos.items():
        auto_info[clave] = valor
    return auto_info
auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)
print(auto)