from randomizer import sortear_torneo, mostrar_bracket  # Importar el randomizador y la función para mostrar brackets
from trainer import Trainer
from EquipoPokemon import EquipoPokemon
from base_conocimiento import mostrar_habilidades
from pokemons import *

def menu():
    """
    Menú principal del programa.
    """
    salir = False
    entrenadores = []  # Lista para almacenar a los entrenadores

    while not salir:
        print("\n" + "="*40)
        print("             MENÚ PRINCIPAL")
        print("="*40)
        print("1. Añadir entrenador")
        print("2. Mostrar equipos de entrenadores")
        print("3. Consultar base de conocimientos")
        print("4. Comenzar sorteo del Torneo")
        print("5. Salir")
        print("="*40)
        
        try:
            opcion = int(input("Selecciona una opción: "))
            print()  # Línea en blanco para separación
            if opcion == 1:
                # Añadir un entrenador
                print("Has seleccionado 'Añadir entrenador'.")
                nombre = input("Nombre del entrenador: ")
                edad = int(input("Edad del entrenador: "))
                ciudad = input("Ciudad del entrenador: ")

                equipo = []
                for _ in range(6):  # Elegimos 6 Pokémon
                    print('\nLista de Pokémon disponibles:')
                    for idx, pokemon in enumerate(Pokemons):
                        print(f'{idx} {pokemon.nombre}, ', end='') if idx % 5 != 0 or idx == 0 else print()
                    
                    while True:
                        try:
                            seleccionar = int(input('\nSelecciona un Pokémon (índice): '))
                            if 0 <= seleccionar < len(Pokemons):
                                equipo.append(Pokemons[seleccionar].nombre)
                                del Pokemons[seleccionar]
                                break
                            else:
                                print("Índice inválido. Por favor selecciona un índice correcto.")
                        except ValueError:
                            print("Por favor ingresa un número válido.")

                equipo_entrenador = EquipoPokemon(equipo)
                nuevo_entrenador = Trainer(nombre, edad, ciudad, equipo_entrenador)
                nuevo_entrenador.mostrarEquipo()

                entrenadores.append(nuevo_entrenador)
                print(f"\nEntrenador {nombre} añadido con éxito.")
            elif opcion == 2:
                # Mostrar equipos de los entrenadores
                print("Has seleccionado 'Mostrar equipos de entrenadores'.")
                if not entrenadores:
                    print("No hay entrenadores registrados.")
                else:
                    for idx, entrenador in enumerate(entrenadores, start=1):
                        print(f"Equipo de {entrenador.Nombre}:")
                        for pokemon in entrenador.Equipo.Pokemons:
                            print(f"- {pokemon}")
                        print("\n" + "="*20)  # Separador entre equipos
            elif opcion == 3:
                # Consultar la base de conocimientos
                print("Has seleccionado 'Consultar base de conocimientos'.")
                mostrar_habilidades()
            elif opcion == 4:
                # Comenzar el sorteo del torneo con brackets
                print("Has seleccionado 'Comenzar sorteo del Torneo'.")
                if len(entrenadores) < 2:
                    print("Debe haber al menos 2 entrenadores para comenzar un torneo.")
                else:
                    bracket = sortear_torneo(entrenadores)
                    print("\n¡El torneo se ha sorteado con éxito! Aquí están los brackets:")
                    mostrar_bracket(bracket)
            elif opcion == 5:
                # Salir del programa
                print("Saliendo del programa. ¡Hasta pronto!")
                salir = True
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Ingresa un número válido.")



# Llamar al menú principal si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
