import random
from base_conocimiento import *

class Pokemon:
    def __init__(self, nombre: str, salud: int, habilidades: list[str], tipo: str, velocidad: int): 
        self.nombre = nombre
        self.salud = salud
        self.saludMaxima = salud
        # Normalizamos las habilidades
        self.habilidades = [habilidad.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') for habilidad in habilidades]
        self.tipo = tipo.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        self.estado = EstadoPokemon.NORMAL.value
        self.velocidad = velocidad

    def Ataque(self, habilidad: str, enemigo) -> None:
        habilidad_original = habilidad  # Conservamos el texto original para mensajes
        habilidad = habilidad.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        if habilidad not in self.habilidades:
            print(f"Habilidad {habilidad_original} no pertenece a {self.nombre}.")
            return

        if habilidad not in habilidades:
            print(f"Habilidad {habilidad_original} no está definida en el sistema.")
            return

        datos = habilidades[habilidad]
        danyo = datos["daño"]
        if datos["tipo_habilidad"] == TipoHabilidad.MULTIPLE:
            veces = random.randint(1, 5)
            for _ in range(veces - 1):
                danyo += datos["daño"]
            enemigo.RecibirDanyo(danyo, datos["tipo"])
            print(f"{self.nombre} ha atacado {veces} veces")

        elif datos["tipo_habilidad"] == TipoHabilidad.EFECTO:
            enemigo.RecibirDanyo(danyo, datos["tipo"])
            if random.random() <= 0.3:
                estado = datos["estado"]
                print(f"{enemigo.nombre} está {estado}")
                enemigo.CambiarEstado(estado)
        else:
            enemigo.RecibirDanyo(danyo, datos["tipo"])

    def RecibirDanyo(self, danyo: int, tipo: str) -> None:
        tipo = tipo.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        if tipo not in inmunidades:
            print(f"Tipo {tipo} no reconocido en las inmunidades.")
            return

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

    def CambiarEstado(self, estado) -> None:
        self.estado = estado

    def TipoPokemon(self) -> None:
        return self.tipo

    def RecibirSalud(self, objeto: int) -> None:
        self.salud += objeto
        if self.salud > self.saludMaxima:
            self.salud = self.saludMaxima

    def Estado(self):
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

    def envenenado(self) -> bool:
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del veneno")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True

    def quemado(self) -> bool:
        if random.random() < 0.2:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado del fuego")
        else:
            self.salud -= 5
            if self.salud <= 0:
                self.salud = 0
        return True

    def paralizado(self) -> bool:
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha recuperado de su parálisis")
        else:
            return False

        return True

    def dormido(self) -> bool:
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha despertado")
        else:
            return False

    def confuso(self) -> bool:
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} ha recuperado su razón")
        else:
            auto_danyo = random.randint(5, 15)
            self.salud -= auto_danyo
            return False

        return True

    def congelado(self) -> bool:
        if random.random() < 0.5:
            self.estado = EstadoPokemon.NORMAL
            print(f"{self.nombre} se ha descongelado")
        else:
            return False

        return True

    def MostrarHabilidades(self) -> None:
        for habilidad in self.habilidades:
            if habilidad not in habilidades:
                print(f"Habilidad {habilidad} no está definida en el sistema.")
                continue
            datos = habilidades[habilidad]
            print(f"Habilidad: {habilidad}", end=" ")
            print(f"  Daño: {datos['daño']}", end=" ")
            print(f"  Tipo: {datos['tipo']}", end=" ")
            print(f"  Tipo de Habilidad: {datos['tipo_habilidad'].value}", end=" ")
            print(f"  Estado: {datos['estado'].value}")
            print("_" * 30)

    def MostrarDatos(self) -> None:
        print(self.nombre)
        print(self.salud)
        print(self.saludMaxima)
        print(self.habilidades)
        print(self.tipo)
        print(self.estado)
        print("\n")