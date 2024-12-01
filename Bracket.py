from Randomizador import TorneoPokemon
import random
import math

def generar_bracket(jugadores):
    if len(jugadores) % 2 != 0:
        print("Esperando a un entrenador más para completar el bracket.")
        return

    print("\n--- Bracket del Torneo ---")
    ronda = 1
    while len(jugadores) > 1:
        print(f"\nRonda {ronda}:")
        siguiente_ronda = []
        for i in range(0, len(jugadores), 2):
            jugador_1 = jugadores[i]
            jugador_2 = jugadores[i + 1]
            print(f'{jugador_1.nombre} vs {jugador_2.nombre}')
            ganador = None
            while ganador is None:
                resultado = input(f"¿Quién ganó? (1: {jugador_1.nombre}, 2: {jugador_2.nombre}): ")
                if resultado == '1':
                    ganador = jugador_1
                elif resultado == '2':
                    ganador = jugador_2
                else:
                    print("Entrada inválida. Por favor, ingresa 1 o 2.")
            siguiente_ronda.append(ganador)
            print(f'Ganador: {ganador.nombre}')
        jugadores = siguiente_ronda
        ronda += 1

    print(f"\nEl ganador del torneo es: {jugadores[0].nombre}")

# Ejemplo de uso
if __name__ == "__main__":
    max_players = 6  # Cambiar este valor según el número de jugadores que se deseen
    torneo = TorneoPokemon(max_players)
    torneo.agregar_jugadores()
    torneo.randomizar_jugadores()

    if len(torneo.jugadores) % 2 == 0:
        generar_bracket(torneo.jugadores)
    else:
        print("No se puede generar el bracket porque el número de jugadores es impar.")