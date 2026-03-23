while True:
    entrada1 = input("Ingresa el primer número (o salir): ").strip()
    if entrada1.lower() == "salir":
        print("Programa terminado por el usuario")
        break

    entrada2 = input("Ingresa el segundo número (o salir): ").strip()
    if entrada2.lower() == "salir":
        print("Programa terminado")
        break

    try:
        numero1 = int(entrada1)
        numero2 = int(entrada2)
        suma = numero1 + numero2
        print(f"La suma es: {suma}")

    except ValueError:
        print("Error: por favor ingresa solo valores numéricos enteros. Intentá de nuevo")

    print('---')
