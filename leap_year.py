def leap_year():
    # Solicitar el año al usuario
    anio = int(input("Ingrese un año: "))

    # Verificar si es bisiesto según las reglas del calendario gregoriano
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
