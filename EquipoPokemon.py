
from Pokemon import *

class EquipoPokemon:
    def __init__(self, Pokemons: list[Pokemon]):
        self.Pokemons = Pokemons
        self.activo = Pokemons[0] if Pokemons else None

    def OutPokemon(self):
        return self.Pokemons
    
    def InPokemon(self,Pokemon):
        self.Pokemons.append(Pokemon)
    
    def equipoVivo(self):
        """Verifica si al menos un Pokémon tiene salud mayor que 0."""
        return any(pokemon.salud > 0 for pokemon in self.Pokemons)

    def seleccionarPokemon(self,pokemon):
        for i in range(len(Pokemons)):
            if Pokemons[i].nombre == pokemon and Pokemons[i].salud > 0:
                self.activo = self.Pokemons[i]
                return
        
        print("Error. Pokemon no encontrado")
