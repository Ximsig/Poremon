from pokemon import *

class EquipoPokemon:
    def __init__(self, Pokemons: list[Pokemon]):
        self.Pokemons = Pokemons
        self.activo = self.Pokemons[0] if self.Pokemons else None
        
    def OutPokemon(self):
        return self.Pokemons
    
    def InPokemon(self,Pokemon):
        self.Pokemons.append(Pokemon)
    
    def cambiarActivo(self, indice: int):
        if 0 <= indice < len(self.Pokemons):
            self.activo = self.Pokemons[indice]

    def equipoVivo(self):
        return any(pokemon.salud > 0 for pokemon in self.Pokemons)