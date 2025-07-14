def line():
    # Entrada de datos
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))

    # Cálculo de coordenadas Y
    y1 = a * x1 + b
    y2 = a * x2 + b

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Resultados
    print(f"\nEl coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}\n")

    print("Para la siguiente ecuación:")
    print(f"\tY = {a}X + {b}\n")

    print("Dados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})\n")

    print(f"La distancia entre ellos es: {distancia}")
