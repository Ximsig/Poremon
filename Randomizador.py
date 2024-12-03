import random
from trainer import Entrenador  # Importamos la clase Personaje del archivo correspondiente
from equipo_pokemon import equipo_pokemon  # Importamos la función para generar equipos

class TorneoPokemon:
    def __init__(self, max_players):
        self.max_players = max_players
        self.jugadores = []

    def agregar_jugadores(self):
        for i in range(self.max_players):
            nombre = f'Entrenador_{i + 1}'  # Creamos nombres de entrenadores
            equipo = equipo_pokemon()  # Generamos el equipo para cada jugador
            jugador = Entrenador(nombre, equipo)  # Creamos una instancia de Personaje
            self.jugadores.append(jugador)

    def randomizar_jugadores(self):
        if len(self.jugadores) % 2 != 0:
            print("Esperando a un entrenador más para comenzar el draft")
        else:
            random.shuffle(self.jugadores)
            print("Jugadores aleatorizados:")
            for jugador in self.jugadores:
                print(f'{jugador.nombre} con equipo {jugador.equipo}')

# Ejemplo de uso
if __name__ == "__main__":
    max_players = 5  #CAMBIAR SEGUN NUMERO DE JUGADORES
    torneo = TorneoPokemon(max_players)
    torneo.agregar_jugadores()
    torneo.randomizar_jugadores()