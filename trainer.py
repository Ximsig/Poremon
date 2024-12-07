from equipo_pokemon import EquipoPokemon

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
    
    def seleccionarPokemon(self, indice: int):
        self.Equipo.cambiarActivo(indice)