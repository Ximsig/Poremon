import random
from base_conocimiento import efectividades, inmunidades, debilidades, habilidades, EstadoPokemon, TipoHabilidad

class Pokemon:
    def __init__(self, nombre, salud, habilidades, tipo, velocidad):  # Constructor
        self.nombre = nombre
        self.salud = salud
        self.saludMaxima = salud
        self.habilidades = habilidades
        self.tipo = tipo
        self.estado = EstadoPokemon.NORMAL  # Estado inicial
        self.velocidad = velocidad

    def Ataque(self, habilidad, enemigo):
        if habilidad not in habilidades:
            print(f"Habilidad {habilidad} no está definida.")
            return

        info_habilidad = habilidades[habilidad]
        if habilidad in self.habilidades:
            danyo = info_habilidad["daño"]
            tipo_habilidad = info_habilidad["tipo_habilidad"]

            if tipo_habilidad == TipoHabilidad.MULTIPLE:
                veces = random.randint(1, 5)
                for _ in range(veces):
                    enemigo.RecibirDanyo(danyo, info_habilidad["tipo"])
                print(f"{self.nombre} ha atacado {veces} veces")

            elif tipo_habilidad == TipoHabilidad.EFECTO:
                enemigo.RecibirDanyo(danyo, info_habilidad["tipo"])
                if random.random() <= 0.5:
                    estado = info_habilidad["estado"]
                    print(f"{self.nombre} causa el estado {estado.value} a {enemigo.nombre}")
                    enemigo.CambiarEstado(estado)
            else:
                enemigo.RecibirDanyo(danyo, info_habilidad["tipo"])
        else:
            print(f"{habilidad} no pertenece a {self.nombre}\n")

    def RecibirDanyo(self, danyo, tipo):
        if tipo in inmunidades[self.tipo]:
            print(f"{self.nombre}: El ataque no tuvo efecto.")
            return

        if tipo in debilidades[self.tipo]:
            danyo *= 0.5
        if tipo in efectividades[self.tipo]:
            danyo *= 2

        self.salud -= danyo
        if self.salud <= 0:
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ahora tiene {self.salud} puntos de salud")

    def CambiarEstado(self, estado):
        if isinstance(estado, EstadoPokemon):
            self.estado = estado
            print(f"{self.nombre} ahora está {estado.value}.")

    def MostrarHabilidades(self):
        for habilidad in self.habilidades:
            if habilidad in habilidades:
                info_habilidad = habilidades[habilidad]
                print(f"Habilidad: {habilidad}")
                print(f"  Daño: {info_habilidad['daño']}")
                print(f"  Tipo: {info_habilidad['tipo']}")
                print(f"  Tipo de Habilidad: {info_habilidad['tipo_habilidad'].value}")
                print(f"  Estado: {info_habilidad['estado'].value}")
                print("-" * 30)
