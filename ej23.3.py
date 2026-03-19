def hacer_album(artista, titulo, canciones=None):
    album = {"artista": artista, "titulo": titulo}
    if canciones is not None:
        album["canciones"] = canciones
    return album
artista = input("Ingrese el nombre del artista: ")
titulo = input("Ingrese el título del álbum: ")
album = hacer_album(artista, titulo)
print(album)