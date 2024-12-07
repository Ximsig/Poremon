from pokemon import Pokemon
from trainer import Trainer
from equipo_pokemon import EquipoPokemon

def iniciar_batalla(entrenador1, entrenador2):
    print("¡Comienza la batalla Pokémon!")
    
    while entrenador1.Equipo.equipoVivo() and entrenador2.Equipo.equipoVivo():
        turno(entrenador1, entrenador2)
        if not entrenador2.Equipo.equipoVivo():
            print(f"¡{entrenador1.Nombre} gana la batalla!")
            return
        
        turno(entrenador2, entrenador1)
        if not entrenador1.Equipo.equipoVivo():
            print(f"¡{entrenador2.Nombre} gana la batalla!")
            return

def turno(atacante, defensor):
    atacante_pokemon = atacante.Equipo.activo
    defensor_pokemon = defensor.Equipo.activo

    # Verificar si el Pokémon activo del atacante puede combatir
    if atacante_pokemon.salud <= 0:
        print(f"{atacante.Nombre}, tu {atacante_pokemon.nombre} ya no puede combatir.")
        cambiar_pokemon(atacante)
        return

    # Seleccionar habilidad
    print(f"{atacante.Nombre} elige una habilidad para {atacante_pokemon.nombre}: {atacante_pokemon.MostrarHabilidades()}")
    habilidad = input("Escribe el nombre de la habilidad: ")
    
    # Validar habilidad y atacar
    if habilidad in atacante_pokemon.habilidades:
        atacante_pokemon.Ataque(habilidad, defensor_pokemon)
        
        if defensor_pokemon.salud <= 0:
            print(f"{defensor_pokemon.nombre} ha sido derrotado.")
            cambiar_pokemon(defensor)
    else:
        print("¡Habilidad no válida!")

def cambiar_pokemon(entrenador):
    print(f"{entrenador.Nombre}, selecciona otro Pokémon:")
    for i, pokemon in enumerate(entrenador.Equipo.Pokemons):
        if pokemon.salud > 0:
            print(f"{i}. {pokemon.nombre} (Salud: {pokemon.salud})")
    while True:
        try:
            indice = int(input("Escribe el índice del Pokémon: "))
            if 0 <= indice < len(entrenador.Equipo.Pokemons) and entrenador.Equipo.Pokemons[indice].salud > 0:
                entrenador.seleccionarPokemon(indice)
                print(f"{entrenador.Nombre} ha seleccionado a {entrenador.Equipo.activo.nombre}")
                break
            else:
                print("Índice no válido o el Pokémon seleccionado no puede combatir.")
        except ValueError:
            print("Por favor, escribe un número válido.")

if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", 200, ["Impactrueno","Placaje"], "Electrico", 40)
    charmander = Pokemon("Charmander", 170, ["Colmillo Ígneo","Lanzallamas"], "Fuego", 35)
    squirtle = Pokemon("Squirtle", 180, ["Hidrobomba","Pistola Agua","Placaje"], "Agua", 30)

    equipo1 = EquipoPokemon([pikachu, squirtle])
    equipo2 = EquipoPokemon([charmander])

    entrenador1 = Trainer("Ash", 10, "Pueblo Paleta", equipo1)
    entrenador2 = Trainer("Gary", 11, "Ciudad Verde", equipo2)
    
    iniciar_batalla(entrenador1, entrenador2)