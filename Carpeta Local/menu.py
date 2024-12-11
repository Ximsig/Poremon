from randomizer import sortear_torneo, mostrar_bracket
from batalla import iniciar_batalla
from trainer import Trainer
from EquipoPokemon import EquipoPokemon
from pokemons import Pokemons
import random

def menu():
    entrenadores = []
    while True:
        print("\n" + "="*40)
        print("             MENÚ PRINCIPAL")
        print("="*40)
        print("1. Registrar Entrenador")
        print("2. Mostrar Entrenadores Registrados")
        print("3. Sortear y Mostrar Bracket")
        print("4. Iniciar Torneo")
        print("5. Salir")
        print("="*40)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            while True:
                try:
                    nombre = input("Nombre del entrenador: ").strip()
                    if not nombre:
                        raise ValueError("El nombre no puede estar vacío.")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    edad = int(input("Edad del entrenador: "))
                    if edad <= 0:
                        raise ValueError("La edad debe ser un número positivo.")
                    break
                except ValueError:
                    print("Por favor ingresa un número válido para la edad.")

            while True:
                try:
                    ciudad = input("Ciudad del entrenador: ").strip()
                    if not ciudad:
                        raise ValueError("La ciudad no puede estar vacía.")
                    break
                except ValueError as e:
                    print(e)

            equipo = []
            num_pokemons_por_equipo = int(input("Numero de pokemons por equipo: "))
            for _ in range(num_pokemons_por_equipo):  # Elegimos el número configurado de Pokémon
                print('\nLista de Pokémon disponibles:')
                for idx, pokemon in enumerate(Pokemons):
                    print(f'{idx} {pokemon.nombre}, ', end='') if idx % 5 != 0 or idx == 0 else print()
                
                while True:
                    try:
                        seleccionar = int(input('\nSelecciona un Pokémon (índice): '))
                        if 0 <= seleccionar < len(Pokemons):
                            equipo.append(Pokemons[seleccionar])
                            del Pokemons[seleccionar]
                            break
                        else:
                            print("Índice inválido. Por favor selecciona un índice correcto.")
                    except ValueError:
                        print("Por favor ingresa un número válido.")

            equipo_entrenador = EquipoPokemon(equipo)
            entrenador = Trainer(nombre, edad, ciudad, equipo_entrenador)
            entrenadores.append(entrenador)
            print(f"Entrenador {nombre} registrado con éxito.")

        elif opcion == "2":
            if not entrenadores:
                print("No hay entrenadores registrados.")
            else:
                for entrenador in entrenadores:
                    print(f"Entrenador: {entrenador.Nombre}, Ciudad: {entrenador.Ciudad}")
                    print(f"El equipo de {entrenador.Nombre} es:")
                    for pokemon in entrenador.Equipo.Pokemons:
                        print(f"- {pokemon.nombre} (Salud: {pokemon.salud}/{pokemon.saludMaxima}, Tipo: {pokemon.tipo.capitalize()})")

        elif opcion == "3":
            if len(entrenadores) < 2:
                print("Se necesitan al menos 2 entrenadores para el sorteo.")
            else:
                bracket = sortear_torneo(entrenadores)
                mostrar_bracket(bracket)

        elif opcion == "4":
            if len(entrenadores) < 2:
                print("Se necesitan al menos 2 entrenadores para iniciar un torneo.")
            else:
                bracket = sortear_torneo(entrenadores)
                print("\n¡El torneo se ha sorteado con éxito! Aquí están los brackets:")
                mostrar_bracket(bracket)

                # Progresión del torneo
                print("\n¡Comienzan las batallas!")
                ronda_actual = 1
                while len(bracket) > 0:
                    print(f"\n--- Ronda {ronda_actual} ---")
                    ronda = bracket.pop(0)
                    ganadores = []
                    for enfrentamiento in ronda:
                        entrenador1, entrenador2 = enfrentamiento
                        if entrenador1 and entrenador2:
                            iniciar_batalla(entrenador1, entrenador2)
                            ganador = entrenador1 if entrenador1.Equipo.equipoVivo() else entrenador2
                            ganadores.append(ganador)
                        elif entrenador1:
                            ganadores.append(entrenador1)
                        elif entrenador2:
                            ganadores.append(entrenador2)

                    print("\nGanadores de esta ronda:")
                    for ganador in ganadores:
                        print(f"- {ganador.Nombre}")

                    if len(ganadores) == 1:
                        print(f"\n¡El ganador del torneo es {ganadores[0].Nombre}!")
                        break

                    # Preparar el bracket para la siguiente ronda
                    nueva_ronda = []
                    for i in range(0, len(ganadores), 2):
                        emparejamiento = (ganadores[i], ganadores[i+1] if i+1 < len(ganadores) else None)
                        nueva_ronda.append(emparejamiento)
                    bracket.append(nueva_ronda)
                    mostrar_bracket([nueva_ronda])

                    ronda_actual += 1

        elif opcion == "5":
            print("Gracias por usar el simulador Pokémon. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
