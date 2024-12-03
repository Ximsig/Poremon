class Trainer:
    def __init__(self, Nombre, Edad, Ciudad):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Ciudad = Ciudad
        self.medallas = 0 # Torneos ganados

    def sumarMedalla(self):
        self.medallas + 1

    def mostrarMedallas(self):
        return self.medallas 