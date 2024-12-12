from EquipoPokemon import EquipoPokemon

class Trainer: #Clase de tipo Trainer que servirá como esqueleto para todos los entrenadores
    def __init__(self, Nombre: str, Edad: int, Ciudad: str, Equipo: EquipoPokemon): #Constructor
        '''
        Clase entrenador:
        Recibe un nombre, edad, ciudad y un objeto de la clase equipo pokemon
        '''
        self.Nombre = Nombre
        self.Edad = Edad
        self.Ciudad = Ciudad
        self.medallas = 0 # Torneos ganados
        self.Equipo = Equipo

    def sumarMedalla(self) -> None: #Suma una medalla
        self.medallas + 1

    def mostrarMedallas(self) -> int: #Devuelve las medallas que tiene
        return self.medallas
    
    def mostrarEquipo(self) -> None: #Muestra todo su equipo pokemon
        print(f'El equipo de {self.Nombre} es:')
        for pokemon in self.Equipo.Pokemons:
            print(f'{pokemon} ' ,end='') 
    
    def seleccionarPokemon(self, indice) -> None: #Selecciona un pokemon en base a su indice o valor dado
        self.Equipo.seleccionarPokemon(indice)