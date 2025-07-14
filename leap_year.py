def leap_year():
    """
    Determina si un año ingresado por el usuario es bisiesto
    """
    anio = int(input("Ingrese un año: "))

    # Condición de año bisiesto con uso de 'and' y 'or'
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
