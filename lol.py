prestamos = []

def registrar():
    print("\n--- REGISTRAR PRÉSTAMO ---")

    codigo = input("Código del estudiante: ")
    nombre = input("Nombre del estudiante: ")
    material = input("Material solicitado: ")

    if codigo == "" or nombre == "" or material == "":
        print("Complete todos los datos.")
        return

    try:
        dias = int(input("Días del préstamo: "))

        if dias < 1 or dias > 30:
            print("Ingrese entre 1 y 30 días.")
            return

    except ValueError:
        print("Ingrese un número válido.")
        return

    prestamo = [codigo, nombre, material, dias]
    prestamos.append(prestamo)

    archivo = open("prestamos.txt", "a")
    archivo.write(codigo + ";" + nombre + ";" + material + ";" + str(dias) + "\n")
    archivo.close()

    print("Préstamo registrado correctamente.")


def consultar():
    print("\n--- LISTA DE PRÉSTAMOS ---")

    try:
        archivo = open("prestamos.txt", "r")

        for linea in archivo:
            datos = linea.strip().split(";")

            print("\nCódigo:", datos[0])
            print("Estudiante:", datos[1])
            print("Material:", datos[2])
            print("Días:", datos[3])

        archivo.close()

    except FileNotFoundError:
        print("Todavía no hay préstamos registrados.")


while True:
    print("\n===== BIBLIOTECA =====")
    print("1. Registrar préstamo")
    print("2. Consultar préstamos")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar()

    elif opcion == "2":
        consultar()

    elif opcion == "3":
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción incorrecta.")