from pokemon import Pokemon
from base_conocimiento import *
from trainer import Trainer
from EquipoPokemon import EquipoPokemon

#Inicia la batalla entre los dos entrenadores

def iniciar_batalla(entrenador1 : Trainer, entrenador2 : Trainer) -> None:
    print("¡Comienza la batalla Pokémon!")

    while entrenador1.Equipo.equipoVivo() and entrenador2.Equipo.equipoVivo(): #Mientras ambos equipos estén con vida
        if entrenador1.Equipo.activo.velocidad >= entrenador2.Equipo.activo.velocidad: #Ataca primero el que tenga el pokemon más rápido
            if turno(entrenador1, entrenador2): #Si el pokemon del contrincante ha muerto
                if not entrenador2.Equipo.equipoVivo(): #Si ya no tiene equipo vivo
                    print(f"¡{entrenador1.Nombre} gana la batalla!")
                    return
            else: #Idem
                if turno(entrenador2, entrenador1):
                    if not entrenador1.Equipo.equipoVivo():
                        print(f"¡{entrenador2.Nombre} gana la batalla!")
                        return
        else: #Idem
            if turno(entrenador2, entrenador1):
                if not entrenador1.Equipo.equipoVivo():
                    print(f"¡{entrenador2.Nombre} gana la batalla!")
                    return
            else: #Idem
                if turno(entrenador1, entrenador2):
                    if not entrenador2.Equipo.equipoVivo():
                        print(f"¡{entrenador1.Nombre} gana la batalla!")
                        return

#Ejecuta todos los pasos que se realizan dentro de un turno, teniendo al atacante y al defensor

def turno(atacante : Trainer, defensor : Trainer) -> bool:
    atacante_pokemon = atacante.Equipo.activo #Obtiene el pokemon activo en ese momento del entrenador
    defensor_pokemon = defensor.Equipo.activo
    
    MostrarBatalla(atacante_pokemon,defensor_pokemon)

    if atacante_pokemon.salud <= 0: #Si el pokemon sigue vivo (caso preventivo)
        print(f"{atacante.Nombre}, tu {atacante_pokemon.nombre} ya no puede combatir.")
        cambiar_pokemon(atacante)
        return

    print("\n")
    print(f"{atacante.Nombre}, elige una habilidad para {atacante_pokemon.nombre}:")
    
    turno = True
    while turno: #Mientras que el atacante tenga su turno realiza una opcion
        opcion = input("Escribe tu opcion: ")
        if opcion.lower() == "cambio": #Si desea cambiar de pokemon (pierde turno)
            CambiarPokemon(atacante)
            turno = False
        elif opcion in atacante_pokemon.habilidades: #Si ha escogido una habilidad que tenga su pokemon
            if atacante_pokemon.Estado():
                atacante_pokemon.Ataque(opcion,defensor_pokemon)
            turno = False
        else: #Se le advierte de que su opcion es invalida y vuelve a pedirlo
            print("Por favor, escribe una opcion válida.")

    if defensor_pokemon.salud <= 0: #Si el pokemon enemigo ha muerto
        if defensor.Equipo.equipoVivo(): #Si aún le quedan pokemons vivos
            CambiarPokemon(defensor)
        return True
    
    return False

def CambiarPokemon(entrenador : Trainer) -> None:
    print(f"{entrenador.Nombre}, selecciona otro Pokémon:")
    for i, pokemon in enumerate(entrenador.Equipo.Pokemons): #Muestra todos los pokemons vivos que tiene el entrenador
        if pokemon.salud > 0:
            print(f"{i}. {pokemon.nombre} (Salud: {pokemon.salud}/{pokemon.saludMaxima})")
    
    turno = True
    while turno: #Mientras que sea su turno de cambiar digita el pokemon que quiere usar
        encontrado = False
        nombre = input("Escribe el nombre del Pokémon: ")
        for elem in entrenador.Equipo.Pokemons: #Comprueba si el pokemon digitado está en su equipo
            if nombre == elem.nombre and nombre != entrenador.Equipo.activo: #Si el pokemon no es el que ya tiene desplegado
                entrenador.seleccionarPokemon(nombre)
                print(f"{entrenador.Nombre} ha seleccionado a {entrenador.Equipo.activo.nombre}")
                encontrado = True
        if encontrado: #Si lo ha encontrado -> rompe el bucle
            turno = False
        else: #Si no lo ha encontrado se le pide de nuevo el pokemon
            print("Índice no válido, el Pokémon seleccionado no puede combatir o no puedes seleccionar al mismo.")

#Muestra la batalla creando dos ventanas muy chulas, siendo el último perteneciente al pokemon que va a atacar

def MostrarBatalla(atacante : Pokemon, defensor : Pokemon) -> None:
    CuadroPokemon(defensor)
    CuadroPokemon(atacante)

#Crea la ventana con toda la información necesaria del pokemon

def CuadroPokemon(pokemon : Pokemon) -> None:
    lista = []
    for i in range(4): #Obtiene las habilidades del pokemon (tambien es compatible para menos de 4 habilidades)
        if i + 1 <= len(pokemon.habilidades):
            lista.append(pokemon.habilidades[i])
        else:
            lista.append("")
    
    salud = str(pokemon.salud) + '/' + str(pokemon.saludMaxima)
    barra_vida = saludPokemon(pokemon.salud,pokemon.saludMaxima)
    barra_inferior = 'Estado: ' + pokemon.estado.value + '      ' + 'Tipo: ' + pokemon.tipo
    
    print(f"\n{'****************************************':>50}")
    print(f"{'*':>11}",end = "")
    print(f"{pokemon.nombre:^38}",end="")
    print("*")
    print(f"{'*':>11}",end="")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'*':>11}",end="")
    print(f"{salud:>10}",end="")
    print(f"  {barra_vida:<26}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{lista[0] + '   ' + lista[1]:^38}",end = "")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{lista[2] + '   ' + lista[3]:^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{barra_inferior:^38}",end="")
    print("*")
    print(f"{'*':>11}",end = "")
    print(f"{'':^38}",end="")
    print("*")
    print(f"{'****************************************':>50}\n")

#Obtiene la salud del pokemon como una barra de vida, similar a los juegos de verdad

def saludPokemon(salud : int, saludMaxima : int) -> str:
    barra = ""
    vida = int(round(salud/saludMaxima,1) * 15) #Calcula cuantos caracteres de 'vida' tiene el pokemon
    noVida = 15 - vida #Cuantos caracteres de 'novida' tiene el pokemon
    
    for i in range(vida): #Crea la barra de vida
        barra += "\u2588"
    for i in range(noVida):
        barra += "\u2591"
    
    return barra

#Restablece la vida a los pokemons del entrenador

def CurarPokemon(pokemons : list[Pokemon]) -> None:
    for pokemon in pokemons: #Por cada pokemon le da toda la vida
        pokemon.RecibirSalud(999)
        pokemon.estado = EstadoPokemon.NORMAL

if __name__ == "__main__": #Caso prueba
    Charizard = Pokemon('Charizard', 300, list(habilidades.keys())[14:21:2], 'Fuego', 120)
    Blastoise = Pokemon('Blastoise', 280, list(habilidades.keys())[2:6], 'Agua', 130)
    Venusaur = Pokemon('Venusaur', 275, list(habilidades.keys())[5:9], 'Planta', 135)

    equipo1 = EquipoPokemon([Charizard, Venusaur])
    equipo2 = EquipoPokemon([Blastoise])

    entrenador1 = Trainer("Ash", 10, "Pueblo Paleta", equipo1)
    entrenador2 = Trainer("Gary", 11, "Ciudad Verde", equipo2)
    
    iniciar_batalla(entrenador1, entrenador2)