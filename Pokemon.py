import random
from base_conocimientos import *

class Pokemon:
    def __init__ (self, nombre : str, salud : int, habilidades : list[str], tipo : str, velocidad : int): #Constructor
        self.nombre = nombre
        self.salud = salud
        self.saludMaxima = salud
        self.habilidades = habilidades
        self.tipo = tipo
        self.estado = EstadoPokemon.NORMAL.value
        self.velocidad = velocidad
    
    def Ataque(self, habilidad : str, enemigo): #El pokemon ataca al enemigo con una habilidad
        
        if habilidad not in habilidades:
            print(f"Habilidad {habilidad} no está definida.")
            return
        
        datos = habilidades[habilidad]
        if habilidad in self.habilidades:
            danyo = datos["daño"]
            if datos["tipo_habilidad"] == TipoHabilidad.MULTIPLE: #Si es una habilidad que se activa multiples veces
                veces = random.randint(1,5)
                for i in range(veces - 1):
                    danyo += datos["daño"]
                enemigo.RecibirDanyo(danyo,datos["tipo"])
                print(f"{self.nombre} ha atacado {veces} veces")
            
            elif datos["tipo_habilidad"] == TipoHabilidad.EFECTO: #Si es una habilidad que puede otorgar efectos
                enemigo.RecibirDanyo(danyo,datos["tipo"])
                if random.random() <= 0.5:
                    estado = datos["estado"]
                    print(f"{enemigo.nombre} esta {estado}")
                    enemigo.CambiarEstado(estado)
            else:
                enemigo.RecibirDanyo(danyo,datos["tipo"])
        else:
            print(f"{habilidad} no pertenece a {self.nombre}\n")
            
    def RecibirDanyo(self, danyo : int, tipo : str): #Recibe daño en base del ataque anterior y de su tipo
        
        if tipo in inmunidades[self.tipo]:
            print("No ha tenido efecto")
            return
        
        if tipo in debilidades[self.tipo]:
            print("Es muy efectivo")
            danyo *= 2
        if tipo in efectividades[self.tipo]:
            print("Es poco efectivo")
            danyo = danyo // 2
        
        self.salud -= danyo
        if self.salud <= 0:
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"\n{self.nombre} ahora tiene {self.salud} puntos de salud\n")
            
    def CambiarEstado(self, estado): #Retorna el estado actual del pokemon
        self.estado = estado.value
    
    def TipoPokemon(self): #Retorna el tipo del pokemon
        return self.tipo
    
    def RecibirSalud(self, objeto): #Aumenta salud al darle un objeto
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
            EstadoPokemon.CONGELADO: self.congelado,
        }

        if self.estado in estados_efectos:
            return estados_efectos[self.estado]()
        
        return True
    
    def envenenado(self):
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del veneno")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def quemado(self):
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del fuego")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def paralizado(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado de su paralisis")
        else:
            return False
        
        return True
    
    def dormido(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha despertado")
        else:
            return False

    def confuso(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} ha recuperado su razon")
        else:
            auto_danyo = random.randint(5,15)
            self.salud -= auto_danyo
            return False
        
        return True
    
    def congelado(self):
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha descongelado")
        else:
            return False
        
        return True
    
    def MostrarHabilidades(self):
        for habilidad in self.habilidades:
            datos = habilidades[habilidad]
            print(f"Habilidad: {habilidad}", end=" ")
            print(f"  Daño: {datos['daño']}", end=" ")
            print(f"  Tipo: {datos['tipo']}", end=" ")
            print(f"  Tipo de Habilidad: {datos['tipo_habilidad'].value}", end=" ")
            print(f"  Estado: {datos['estado'].value}")
            print("_" * 30)
    
    def MostrarDatos(self): #Muestra todos los datos del pokemon
        print(self.nombre)
        print(self.salud)
        print(self.saludMaxima)
        print(self.habilidades)
        print(self.tipo)
        print(self.estado.value)
        print("\n")

