def line():
    """
    Calcula la distancia entre dos puntos sobre una recta de primer grado
    y muestra sus coordenadas completas.
    La recta es de la forma: y = ax + b
    """
    # Entrada de datos
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el valor de X1: "))
    x2 = float(input("Ingrese el valor de X2: "))

    # Cálculo de coordenadas sobre la recta
    y1 = a * x1 + b
    y2 = a * x2 + b

    # Distancia entre los dos puntos en el plano
    distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    # Resultados
    print(f"\nEl coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El valor de X1 es: {x1}")
    print(f"El valor de X2 es: {x2}\n")

    print("Para la siguiente ecuación:")
    print(f"\tY = {a}X + {b}\n")

    print("Dados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})\n")

    print(f"La distancia entre ellos es: {distancia}")
