import random
from base_conocimiento import *

class Pokemon: #Clase de tipo Pokemon que servira como esqueleto para todos los pokemons
    def __init__ (self, nombre : str, salud : int, habilidades : list[str], tipo : str, velocidad : int): #Constructor
        self.nombre = nombre
        self.salud = salud
        self.saludMaxima = salud
        self.habilidades = habilidades
        self.tipo = tipo
        self.estado = EstadoPokemon.NORMAL
        self.velocidad = velocidad
    
    def Ataque(self, habilidad : str, enemigo) -> None: #El pokemon ataca al enemigo con una habilidad
        
        if habilidad not in habilidades: #Si la habilidad no está registrada, entonces no se produce el ataque
            print(f"Habilidad {habilidad} no está definida.")
            return
        
        datos = habilidades[habilidad] #Obtiene los datos de la habilidad (daño, tipo, etc)
        if habilidad in self.habilidades: #Si la habilidad lo tiene el pokemon
            danyo = datos["daño"]
            if datos["tipo_habilidad"] == TipoHabilidad.MULTIPLE: #Si es una habilidad que se activa multiples veces
                veces = random.randint(1,5)
                for i in range(veces - 1): #Suma el daño entre 1 y 5 veces
                    danyo += datos["daño"]
                enemigo.RecibirDanyo(danyo,datos["tipo"])
                print(f"{self.nombre} ha atacado {veces} veces")
            
            elif datos["tipo_habilidad"] == TipoHabilidad.EFECTO: #Si es una habilidad que puede otorgar efectos
                enemigo.RecibirDanyo(danyo,datos["tipo"])
                if random.random() <= 0.3:
                    estado = datos["estado"]
                    print(f"{enemigo.nombre} esta {estado}")
                    enemigo.CambiarEstado(estado)
            else: #Si es un ataque normal
                enemigo.RecibirDanyo(danyo,datos["tipo"])
        else:
            print(f"{habilidad} no pertenece a {self.nombre}\n")
    
    def RecibirDanyo(self, danyo : int, tipo : str) -> None: #Recibe daño en base del ataque anterior y su tipo
        
        if tipo in inmunidades[self.tipo]: #Si el pokemon es inmune contra el tipo del ataque
            print("No ha tenido efecto")
            return
        
        if tipo in debilidades[self.tipo]: #Si el pokemon es debil contra el tipo del ataque
            print("Es muy efectivo")
            danyo *= 2
        if tipo in efectividades[self.tipo]: #Si el pokemon es resistente contra el tipo del ataque
            print("Es poco efectivo")
            danyo = danyo // 2
        
        self.salud -= danyo
        if self.salud <= 0: #Si ha sido derrotado
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado")
        else: #Si no ha sido derrotado muestra cuanta vida le queda
            print(f"\n{self.nombre} ahora tiene {self.salud} puntos de salud\n")
            
    def CambiarEstado(self, estado) -> None: #Establece el estado nuevo del pokemon
        self.estado = estado
    
    def TipoPokemon(self) -> str: #Retorna el tipo del pokemon
        return self.tipo
    
    def RecibirSalud(self, objeto : int) -> None: #Aumenta salud al darle un objeto
        self.salud += objeto
        if self.salud > self.saludMaxima: #Si le da más vida que su máxima capacidad, lo limita a su máximo
            self.salud = self.saludMaxima
    
    def Estado(self): #Comprueba el estado del pokemon y aplica el efecto que tenga
        estados_efectos = { #Establece un diccionario de todos los estados existentes
            EstadoPokemon.ENVENENADO: self.envenenado,
            EstadoPokemon.QUEMADO: self.quemado,
            EstadoPokemon.PARALIZADO: self.paralizado,
            EstadoPokemon.DORMIDO: self.dormido,
            EstadoPokemon.CONFUSO: self.confuso,
            EstadoPokemon.CONGELADO: self.congelado,
        }

        if self.estado in estados_efectos: # Si el estado está dentro del diccionario
            return estados_efectos[self.estado]() #Ejecuta una función en base de su estado
        
        return True
    
    def envenenado(self) -> bool: #Caso en el que su estado es envenenado
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del veneno")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def quemado(self) -> bool: #Caso en el que su estado es quemado
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del fuego")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True
    
    def paralizado(self) -> bool: #Caso en el que su estado es paralizado
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado de su paralisis")
        else:
            print(f"{self.nombre} aún no puede moverse")
            return False
        
        return True
    
    def dormido(self) -> bool: #Caso en el que su estado es dormido
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha despertado")
        else:
            print(f"{self.nombre} sigue durmiendo")
            return False

    def confuso(self) -> bool: #Caso en el que su estado es confuso
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} ha recuperado su razon")
        else:
            auto_danyo = random.randint(5,15)
            self.salud -= auto_danyo
            if self.salud <= 0:
                self.salud = 0
            print(f"{self.nombre} está confuso y se ataca a sí mismo")
            return False
        
        return True
    
    def congelado(self) -> bool: #Caso en el que su estado es congelado
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha descongelado")
        else:
            print(f"{self.nombre} sigue congelado")
            return False
        
        return True
    
    def MostrarHabilidades(self) -> None: #Muestra todas las habilidades del pokemon de manera detallada
        for habilidad in self.habilidades:
            datos = habilidades[habilidad]
            print(f"Habilidad: {habilidad}", end=" ")
            print(f"  Daño: {datos['daño']}", end=" ")
            print(f"  Tipo: {datos['tipo']}", end=" ")
            print(f"  Tipo de Habilidad: {datos['tipo_habilidad'].value}", end=" ")
            print(f"  Estado: {datos['estado'].value}")
            print("_" * 30)
    
    def MostrarDatos(self) -> None: #Muestra todos los datos del pokemon
        print(self.nombre)
        print(self.salud)
        print(self.saludMaxima)
        print(self.habilidades)
        print(self.tipo)
        print(self.estado.value)
        print("\n")

