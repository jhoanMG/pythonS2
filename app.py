# Capturar información del primer colegio
nombreC1 = input("Inserte el nombre del primer colegio: ")
while True:
    try:
        estudiantes1 = int(input("Inserte el número de estudiantes en {}:".format(nombreC1)))
        if estudiantes1 <= 0:
            raise ValueError("El número de estudiantes debe ser mayor que cero.")
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el número de estudiantes.")

# Capturar información del segundo colegio
nombreC2 = input("Inserte el nombre del segundo colegio: ")
while True:
    try:
        estudiantes2 = int(input("Inserte el número de estudiantes en {}:".format(nombreC2)))
        if estudiantes2 <= 0:
            raise ValueError("El número de estudiantes debe ser mayor que cero.")
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el número de estudiantes.")

# Imprimir la información de los colegios
print("Nombre del primer colegio:", nombreC1)
print("Estudiantes del colegio", nombreC1 + ":", estudiantes1)
print("Nombre del segundo colegio:", nombreC2)
print("Estudiantes del colegio", nombreC2 + ":", estudiantes2)

# Calcular y mostrar el promedio
promedio = (estudiantes1 + estudiantes2) / 2
print("El promedio de estudiantes entre {} y {} es: {:.2f}".format(nombreC1, nombreC2, promedio))
