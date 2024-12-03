from enum import Enum
import random
from base_conocimiento import *

class EstadoPokemon(Enum):
    NORMAL = "normal"
    ENVENENADO = "envenenado"
    PARALIZADO = "paralizado"
    DORMIDO = "dormido"
    QUEMADO = "quemado"
    CONFUSO = "confuso"

class TipoHabilidad(Enum):
    NORMAL = "normal"
    EFECTO = "efecto"
    MULTIPLE = "multiple"

class Pokemon:
    def __init__ (self,nombre,salud,habilidades,tipo): #Constructor
        self.nombre = nombre
        self.salud = salud
        self.saludMaxima = salud
        self.habilidades = habilidades
        self.tipo = tipo
        self.estado = EstadoPokemon.NORMAL
    
    def Ataque(self,habilidad,enemigo): #El pokemon ataca al enemigo con una habilidad
        
        if "danyo" not in habilidad or "tipo_habilidad" not in habilidad:
            print("Error: Habilidad mal definida.")
            return
        
        nombre = habilidad["nombre"]
        if nombre in self.habilidades:
            danyo = self.habilidades[nombre]["danyo"]
            if habilidad["tipo_habilidad"] == TipoHabilidad.MULTIPLE: #Si es una habilidad que se activa multiples veces
                veces = random.randint(1,5)
                for i in range(veces):
                    enemigo.RecibirDanyo(danyo,habilidad["tipo"])
                print(f"{self.nombre} ha atacado {veces} veces")
            
            elif habilidad["tipo_habilidad"] == TipoHabilidad.EFECTO: #Si es una habilidad que puede otorgar efectos
                enemigo.RecibirDanyo(danyo)
                if random.random() <= 0.5:
                    estado = habilidad["estado"]
                    enemigo.CambiarEstado(estado)
            else:
                enemigo.RecibirDanyo(danyo)
            
    def RecibirDanyo(self,danyo,tipo): #Recibe daño en base del ataque anterior y de su tipo
        if tipo not in inmunes:
            if tipo in debilidades:
                danyo *= 0.5
            elif tipo in criticos:
                danyo *= 2
            self.salud -= danyo
            if self.salud <= 0:
                self.salud = 0
                print(f"{self.nombre} ha sido derrotado")
            else:
                print(f"{self.nombre} ahora tiene {self.salud} puntos de salud")
        else:
            print("No ha tenido efecto")
            
    def CambiarEstado(self,estado): #Retorna el estado actual del pokemon
        self.estado = estado
    
    def TipoPokemon(self): #Retorna el tipo del pokemon
        return self.tipo
    
    def RecibirSalud(self,objeto): #Aumenta salud al darle un objeto
        self.salud += objeto
        if self.salud > self.saludMaxima:
            self.salud = self.saludMaxima
    
    def Estado(self): #Comprueba el estado del pokemon y aplica el efecto que tenga
        estados_efectos = {
            EstadoPokemon.ENVENENADO: self.envenenado,
            EstadoPokemon.QUEMADO: self.quemado,
            EstadoPokemon.PARALIZADO: self.paralizado,
            EstadoPokemon.DORMIDO: self.dormido,
            EstadoPokemon.CONFUSO: self.confuso,
        }

        if self.estado in estados_efectos:
            return estados_efectos[self.estado]()
        
        return True
    
    def envenenado(self):
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def quemado(self):
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def paralizado(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
        else:
            return False
        
        return True
    
    def dormido(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
        else:
            return False

    def confuso(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
        else:
            auto_danyo = random.randint(5,15)
            self.salud -= auto_danyo
            return False
        
        return True

    def MostrarDatos(self): #Muestra todos los datos del pokemon
        print(self.nombre)
        print(self.salud)
        print(self.saludMaxima)
        print(self.habilidades)
        print(self.tipo)
        print(self.estado)