while True:
    try:
        entrada1 = input("Ingresa el primer número: ")
        numero1 = int(entrada1)

        entrada2 = input("Ingresa el segundo número: ")
        numero2 = int(entrada2)

        suma = numero1 + numero2
        print(f"La suma es: {suma}")
        break

    except ValueError:
        print("Error: por favor ingresa solo valores numéricos enteros. Intentá de nuevo")
