def hacer_album(artista, titulo, canciones=None):
    album = {"artista": artista, "titulo": titulo}
    if canciones is not None:
        album["canciones"] = canciones
    return album
album1 = hacer_album("The Beatles", "Abbey Road")
album2 = hacer_album("Pink Floyd", "The Dark Side of the Moon")
album3 = hacer_album("Led Zeppelin", "IV", canciones=8)
print(album1)
print(album2)
print(album3)
