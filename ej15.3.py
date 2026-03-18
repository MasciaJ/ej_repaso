import os
os.system("cls")
glosario = {
    "diccionario" : "En Python un diccionario es una colección de pares key-value",
    "listas" : "Una lista es una colección de items en un orden particular",
    "Tuplas" : "Una tupla no es más que una lista “inmutable”. Es decir, una lista cuyo contenido no varía",
    "strings" : "Un string es una serie de caracteres (una cadena de letras)",
    "floats" : "son numeros no enteros o con decimales"
}
for y, x in glosario.items():
    print(f"{y}: {x}")