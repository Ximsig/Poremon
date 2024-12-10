
from EquipoPokemon import EquipoPokemon

class Trainer:
    def __init__(self, Nombre: str, Edad: int, Ciudad: str, Equipo: EquipoPokemon):
        '''
        Clase entrenador:
        Recibe un nombre, edad, ciudad y un objeto de la clase equipo pokemon
        '''
        self.Nombre = Nombre
        self.Edad = Edad
        self.Ciudad = Ciudad
        self.medallas = 0 # Torneos ganados
        self.Equipo = Equipo

    def sumarMedalla(self):
        self.medallas + 1

    def mostrarMedallas(self):
        return self.medallas
    
    def mostrarEquipo(self):
        print(f'El equipo de {self.Nombre} es:')
        for pokemon in self.Equipo.Pokemons:
            print(f'{pokemon} ' ,end='') 
    
    def seleccionarPokemon(self, indice):
        self.Equipo.cambiarActivo(indice)
