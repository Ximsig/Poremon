from pokemon import Pokemon
from base_conocimiento import *
from trainer import Trainer
from EquipoPokemon import EquipoPokemon

def iniciar_batalla(entrenador1: Trainer, entrenador2: Trainer) -> None:
    print("¡Comienza la batalla Pokémon!")

    while entrenador1.Equipo.equipoVivo() and entrenador2.Equipo.equipoVivo():
        if entrenador1.Equipo.activo.velocidad >= entrenador2.Equipo.activo.velocidad:
            turno(entrenador1, entrenador2)
            if not entrenador2.Equipo.equipoVivo():
                print(f"¡{entrenador1.Nombre} gana la batalla!")
                return

            turno(entrenador2, entrenador1)
            if not entrenador1.Equipo.equipoVivo():
                print(f"¡{entrenador2.Nombre} gana la batalla!")
                return
        else:
            turno(entrenador2, entrenador1)
            if not entrenador1.Equipo.equipoVivo():
                print(f"¡{entrenador2.Nombre} gana la batalla!")
                return

            turno(entrenador1, entrenador2)
            if not entrenador2.Equipo.equipoVivo():
                print(f"¡{entrenador1.Nombre} gana la batalla!")
                return

def turno(atacante: Trainer, defensor: Trainer) -> None:
    atacante_pokemon = atacante.Equipo.activo
    defensor_pokemon = defensor.Equipo.activo

    MostrarBatalla(atacante_pokemon, defensor_pokemon)

    # Verificar si el Pokémon activo del atacante puede combatir
    if atacante_pokemon.salud <= 0:
        print(f"{atacante.Nombre}, tu {atacante_pokemon.nombre} ya no puede combatir.")
        CambiarPokemon(atacante)
        return

    # Seleccionar habilidad
    print("\n")
    print(f"{atacante.Nombre}, elige una habilidad para {atacante_pokemon.nombre}:")

    turno_activo = True
    while turno_activo:
        opcion = input("Escribe tu opcion: ").strip().lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        if opcion == "cambio":
            CambiarPokemon(atacante)
            turno_activo = False
        elif opcion in [h.lower() for h in atacante_pokemon.habilidades]:
            atacante_pokemon.Ataque(opcion, defensor_pokemon)
            turno_activo = False
        else:
            print("Por favor, escribe una opción válida.")

    if defensor_pokemon.salud <= 0:
        if defensor.Equipo.equipoVivo():
            CambiarPokemon(defensor)

def CambiarPokemon(entrenador: Trainer) -> None:
    print(f"{entrenador.Nombre}, selecciona otro Pokémon:")
    for pokemon in entrenador.Equipo.Pokemons:
        if pokemon.salud > 0:
            print(f"{pokemon.nombre} (Salud: {pokemon.salud}/{pokemon.saludMaxima})")

    turno = True
    while turno:
        nombre = input("Escribe el nombre del Pokémon: ").strip().capitalize()  # Normaliza el nombre
        for pokemon in entrenador.Equipo.Pokemons:
            if pokemon.nombre == nombre and pokemon.salud > 0 and pokemon != entrenador.Equipo.activo:
                entrenador.Equipo.activo = pokemon
                print(f"{entrenador.Nombre} ha seleccionado a {pokemon.nombre}")
                turno = False
                break
        else:
            print("El Pokémon seleccionado no puede combatir o no es válido.")

def MostrarBatalla(atacante: Pokemon, defensor: Pokemon) -> None:
    CuadroPokemon(defensor)
    CuadroPokemon(atacante)

def CuadroPokemon(pokemon: Pokemon) -> None:
    lista = []
    for i in range(4):
        if i < len(pokemon.habilidades):
            lista.append(pokemon.habilidades[i])
        else:
            lista.append("")

    salud = f"{pokemon.salud}/{pokemon.saludMaxima}"

    print(f"\n{'****************************************':>50}")
    print(f"{'*':>11}{pokemon.nombre:^38}{'*':<1}")
    print(f"{'*':>11}{'':^38}{'*':<1}")
    print(f"{'*':>11}{salud:^38}{'*':<1}")
    print(f"{'*':>11}{'':^38}{'*':<1}")
    print(f"{'*':>11}{lista[0] + '   ' + lista[1]:^38}{'*':<1}")
    print(f"{'*':>11}{'':^38}{'*':<1}")
    print(f"{'*':>11}{lista[2] + '   ' + lista[3]:^38}{'*':<1}")
    print(f"{'*':>11}{'':^38}{'*':<1}")
    print(f"{'*':>11}{pokemon.estado:^38}{'*':<1}")
    print(f"{'*':>11}{'':^38}{'*':<1}")
    print(f"{'****************************************':>50}\n")

if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", 200, ["Impactrueno", "Placaje", "Puño Trueno", "Chispazo"], "Eléctrico", 40)
    charmander = Pokemon("Charmander", 170, ["Colmillo Ígneo", "Lanzallamas", "Alarido", "Furia Dragón"], "Fuego", 35)
    squirtle = Pokemon("Squirtle", 180, ["Hidrobomba", "Pistola Agua", "Placaje", "Rayo Hielo"], "Agua", 30)

    equipo1 = EquipoPokemon([pikachu, squirtle])
    equipo2 = EquipoPokemon([charmander, pikachu])

    entrenador1 = Trainer("Ash", 10, "Pueblo Paleta", equipo1)
    entrenador2 = Trainer("Gary", 11, "Ciudad Verde", equipo2)

    iniciar_batalla(entrenador1, entrenador2)