def menu():
    """
    Menú principal del programa.
    """
    while True:
        print("\n" + "="*40)
        print("             MENÚ PRINCIPAL")
        print("="*40)
        print("1. Opción 1 - [Descripción breve]")
        print("2. Opción 2 - [Descripción breve]")
        print("3. Opción 3 - [Descripción breve]")
        print("4. Salir")
        print("="*40)
        
        try:
            opcion = int(input("Selecciona una opción: "))
            print()  # Línea en blanco para separación
            if opcion == 1:
                # TODO: Agregar funcionalidad para la opción 1
                print("Has seleccionado la Opción 1.")
            elif opcion == 2:
                # TODO: Agregar funcionalidad para la opción 2
                print("Has seleccionado la Opción 2.")
            elif opcion == 3:
                # TODO: Agregar funcionalidad para la opción 3
                print("Has seleccionado la Opción 3.")
            elif opcion == 4:
                print("Saliendo del programa. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Ingresa un número válido.")

# Llamar al menú principal si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
