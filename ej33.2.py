nombres = []

print("Ingrese nombres para el libro de visitas. Deje vacío y presione Enter para terminar.")

while True:
    nombre = input("Nombre: ").strip()
    if nombre == '':
        break
    nombres.append(nombre)

with open("guest_book.txt", "w") as archivo:
    for n in nombres:
        archivo.write(n + '\n')

print(f"Se guardaron {len(nombres)} nombres en guest_book.txt.")
