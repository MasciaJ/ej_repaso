lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
for persona, lenguaje in lenguajes_favoritos.items():
    if persona in lenguajes_favoritos:
        print(f"el lenguaje favorito de {persona} es {lenguaje}")
    else:
        print(f"parece que {persona} no tiene un lenguaje favorito")
        