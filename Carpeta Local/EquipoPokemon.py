from pokemon import *

class EquipoPokemon: #Clase de tipo EquipoPokemon que servirá de esqueleto para todos los equipos pokemons
    def __init__(self, Pokemons: list[Pokemon]): #Constructor
        self.Pokemons = Pokemons
        self.activo = Pokemons[0] if Pokemons else None

    def OutPokemon(self) -> list[Pokemon]: #Devuelve todo su equipo pokemon
        return self.Pokemons
    
    def InPokemon(self,Pokemon) -> None: #Añade un nuevo pokemon a su equipo
        self.Pokemons.append(Pokemon)
    
    def equipoVivo(self) -> bool: #Si existe algún pokemon vivo devuelve True, si no False
        return any(pokemon.salud > 0 for pokemon in self.Pokemons)

    def seleccionarPokemon(self,pokemon) -> None: #Selecciona un pokemon vivo dentro del equipo
        for i in range(len(self.Pokemons)):
            if self.Pokemons[i].nombre == pokemon and self.Pokemons[i].salud > 0:
                self.activo = self.Pokemons[i]
                return
        
        print("Error. Pokemon no encontrado")