from trainer import Trainer
from EquipoPokemon import EquipoPokemon
from base_conocimiento import mostrar_habilidades

def menu():
    """
    Menú principal del programa.
    """
    salir = False
    entrenadores = []

    while not salir:
        print("\n" + "="*40)
        print("             MENÚ PRINCIPAL")
        print("="*40)
        print("1. Añadir entrenador")
        print("2. Elegir tu equipo Pokémon")
        print("3. Consultar base de conocimientos")
        print("4. Comenzar sorteo del Torneo")
        print("5. Salir")
        print("="*40)
        
        try:
            opcion = int(input("Selecciona una opción: "))
            print()  # Línea en blanco para separación
            if opcion == 1:
                print("Has seleccionado 'Añadir entrenador'.")
                nombre = input("Nombre del entrenador: ")
                edad = int(input("Edad del entrenador: "))
                ciudad = input("Ciudad del entrenador: ")
                equipo = EquipoPokemon([])  # Por defecto, el entrenador empieza sin Pokémon
                nuevo_entrenador = Trainer(nombre, edad, ciudad, equipo)
                entrenadores.append(nuevo_entrenador)
                print(f"Entrenador {nombre} añadido con éxito.")
            elif opcion == 2:
                print("Has seleccionado 'Elegir tu equipo Pokémon'.")
                if not entrenadores:
                    print("No hay entrenadores añadidos. Agrega un entrenador primero.")
                else:
                    print("Entrenadores disponibles:")
                    for idx, entrenador in enumerate(entrenadores):
                        print(f"{idx + 1}. {entrenador.Nombre}")
                    entrenador_idx = int(input("Selecciona un entrenador por índice: ")) - 1
                    if 0 <= entrenador_idx < len(entrenadores):
                        print(f"Seleccionando equipo para {entrenadores[entrenador_idx].Nombre}.")
                        # Aquí iría la lógica para asignar Pokémon al equipo
                    else:
                        print("Índice de entrenador no válido.")
            elif opcion == 3:
                print("Has seleccionado 'Consultar base de conocimientos'.")
                mostrar_habilidades()
            elif opcion == 4:
                print("Has seleccionado 'Comenzar sorteo del Torneo'.")
                # Aquí llamará al randomizador del torneo cuando esté implementado
                print("Funcionalidad en desarrollo.")
            elif opcion == 5:
                print("Saliendo del programa. ¡Hasta pronto!")
                salir = True
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Ingresa un número válido.")

# Llamar al menú principal si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
