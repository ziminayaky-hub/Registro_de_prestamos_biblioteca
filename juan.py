import csv
import os

NOMBRE_ARCHIVO = "prestamos.csv"


def cargar_prestamos():
    """Carga los préstamos desde el archivo CSV si existe."""
    prestamos = []
    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(
                NOMBRE_ARCHIVO, mode="r", encoding="utf-8", newline=""
            ) as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    fila["dias"] = int(fila["dias"])
                    prestamos.append(fila)
        except Exception as e:
            print(f"Error al cargar la información: {e}")
    return prestamos


def guardar_prestamos(prestamos):
    """Guarda la lista de préstamos en el archivo CSV."""
    try:
        with open(
            NOMBRE_ARCHIVO, mode="w", encoding="utf-8", newline=""
        ) as archivo:
            campos = ["codigo", "nombre", "titulo", "dias"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(prestamos)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")


def registrar_prestamo(prestamos):
    """Registra un nuevo préstamo validando los datos ingresados."""
    print("\n--- REGISTRO DE NUEVO PRÉSTAMO ---")

    # Validación del código
    while True:
        codigo = input("Ingrese el código del estudiante: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío.")
            continue

        # Verificar si el código ya existe
        duplicado = False
        for p in prestamos:
            if p["codigo"].lower() == codigo.lower():
                duplicado = True
                break

        if duplicado:
            print("Error: Ya existe un préstamo registrado para este código.")
            return
        break

    # Validación del nombre
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if not nombre:
            print("Error: El nombre del estudiante no puede estar vacío.")
        else:
            break

    # Validación del título
    while True:
        titulo = input("Ingrese el título del material: ").strip()
        if not titulo:
            print("Error: El título del material no puede estar vacío.")
        else:
            break

    # Validación de la cantidad de días (1 a 30)
    while True:
        try:
            dias = int(
                input("Ingrese la cantidad de días de préstamo (1-30): ")
            )
            if 1 <= dias <= 30:
                break
            else:
                print("Error: La cantidad de días debe ser entre 1 y 30.")
        except ValueError:
            print("Error: Ingrese un valor entero válido.")

    # Crear el nuevo registro
    nuevo_prestamo = {
        "codigo": codigo,
        "nombre": nombre,
        "titulo": titulo,
        "dias": dias,
    }

    prestamos.append(nuevo_prestamo)
    guardar_prestamos(prestamos)
    print("\n¡Préstamo registrado y guardado con éxito!")


def consultar_prestamos(prestamos):
    """Muestra la lista de préstamos registrados."""
    print("\n--- LISTA DE PRÉSTAMOS REGISTRADOS ---")

    if not prestamos:
        print("No hay préstamos registrados actualmente.")
        return

    print(
        f"{'Código':<15} | {'Estudiante':<25} | {'Material':<25} | {'Días':<5}"
    )
    print("-" * 75)
    for p in prestamos:
        print(
            f"{p['codigo']:<15} | {p['nombre']:<25} | {p['titulo']:<25} | {p['dias']:<5}"
        )


def main():
    """Función principal que controla el menú del programa."""
    prestamos = cargar_prestamos()

    while True:
        print("\n====================================")
        print("    SISTEMA DE PRÉSTAMOS DE BIBLIOTECA")
        print("====================================")
        print("1. Registrar un nuevo préstamo")
        print("2. Consultar préstamos registrados")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            registrar_prestamo(prestamos)
        elif opcion == "2":
            consultar_prestamos(prestamos)
        elif opcion == "3":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()