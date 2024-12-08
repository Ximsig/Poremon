

debilidades = {
    'Acero' : ['Fuego','Lucha', 'Tierra'],
    'Agua' : ['Planta', 'Electrico'],
    'Bicho' : ['Fuego', 'Roca', 'Volador'],
    'Dragon' : ['Dragón', 'Hada', 'Hielo'],
    'Electrico' : ['Tierra'],
    'Fantasma' : ['Fantasma', 'Siniestro'],
    'Fuego' : ['Agua', 'Roca', 'Tierra'],
    'Hada' : ['Acero', 'Veneno'],
    'Hielo' : ['Acero', 'Fuego', 'Lucha', 'Roca'],
    'Lucha' : ['Hada', 'Psíquico', 'Volador'],
    'Normal' : ['Lucha'],
    'Planta' : ['Bicho', 'Fuego', 'Hielo', 'Veneno', 'Volador'],
    'Psiquico' : ['Bicho', 'Fantasma', 'Siniestro'],
    'Roca' : ['Acero', 'Agua', 'Lucha', 'Planta', 'Tierra'],
    'Siniestro' : ['Bicho', 'Hada', 'Lucha'],
    'Tierra' : ['Agua', 'Hielo', 'Planta'],
    'Veneno' : ['Psíquico', 'Tierra'],
    'Volador' : ['Eléctrico', 'Hielo', 'Roca']
}

efectividades = {
    'Acero': ['Hada', 'Hielo', 'Roca'],
    'Agua': ['Fuego', 'Roca', 'Tierra'],
    'Bicho': ['Hada', 'Planta', 'Psíquico'],
    'Dragon': ['Dragón'],
    'Eléctrico': ['Agua', 'Volador'],
    'Fantasma': ['Fantasma', 'Psíquico'],
    'Fuego': ['Acero', 'Bicho', 'Hielo', 'Planta'],
    'Hada': ['Dragón', 'Lucha', 'Siniestro'],
    'Hielo': ['Dragón', 'Planta', 'Tierra', 'Volador'],
    'Lucha': ['Acero', 'Hielo', 'Normal', 'Roca', 'Siniestro'],
    'Normal': [],
    'Planta': ['Agua', 'Roca', 'Tierra'],
    'Psíquico': ['Lucha', 'Veneno'],
    'Roca': ['Bicho', 'Fuego', 'Hielo', 'Volador'],
    'Siniestro': ['Fantasma', 'Psíquico'],
    'Tierra': ['Eléctrico', 'Fuego', 'Roca', 'Veneno', 'Acero'],
    'Veneno': ['Hada', 'Planta'],
    'Volador': ['Bicho', 'Lucha', 'Planta']
}

inmunidades = {
    'Acero': ['Veneno'],
    'Agua': [],
    'Bicho': [],
    'Dragón': [],
    'Eléctrico': [],
    'Fantasma': ['Normal', 'Lucha'],
    'Fuego': [],
    'Hada': ['Dragón'],
    'Hielo': [],
    'Lucha': ['Fantasma'],
    'Normal': ['Fantasma'],
    'Planta': [],
    'Psíquico': ['Fantasma'],
    'Roca': [],
    'Siniestro': ['Psíquico'],
    'Tierra': ['Eléctrico'],
    'Veneno': [],
    'Volador': ['Tierra']
}

habilidades = {
    "Impactrueno": {
        "daño": 40,
        "tipo_habilidad": "efecto",
        "tipo": "Eléctrico",
        "estado": "paralizado"
    },
    "Placaje": {
        "daño": 20,
        "tipo_habilidad": "multiple",
        "tipo": "Normal",
        "estado": "normal"
    },
    "Lanzallamas": {
        "daño": 90,
        "tipo_habilidad": "efecto",
        "tipo": "Fuego",
        "estado": "quemado"
    },
    "Hidrobomba": {
        "daño": 110,
        "tipo_habilidad": "normal",
        "tipo": "Agua",
        "estado": "normal"
    },
    "Rayo Hielo": {
        "daño": 80,
        "tipo_habilidad": "efecto",
        "tipo": "Hielo",
        "estado": "congelado"
    },
    "Gigadrenado": {
        "daño": 75,
        "tipo_habilidad": "normal",
        "tipo": "Planta",
        "estado": "normal"
    },
    "Tornado": {
        "daño": 40,
        "tipo_habilidad": "multiple",
        "tipo": "Volador",
        "estado": "normal"
    },
    "Golpe Roca": {
        "daño": 50,
        "tipo_habilidad": "efecto",
        "tipo": "Roca",
        "estado": "confuso"
    },
    "Psicorrayo": {
        "daño": 65,
        "tipo_habilidad": "efecto",
        "tipo": "Psíquico",
        "estado": "confuso"
    },
    "Furia Dragón": {
        "daño": 40,
        "tipo_habilidad": "normal",
        "tipo": "Dragón",
        "estado": "normal"
    },
    "Puño Trueno": {
        "daño": 75,
        "tipo_habilidad": "efecto",
        "tipo": "Eléctrico",
        "estado": "paralizado"
    },
    "Bola Sombra": {
        "daño": 80,
        "tipo_habilidad": "efecto",
        "tipo": "Fantasma",
        "estado": "confuso"
    },
    "Terremoto": {
        "daño": 40,
        "tipo_habilidad": "multiple",
        "tipo": "Tierra",
        "estado": "normal"
    },
    "Veneno X": {
        "daño": 60,
        "tipo_habilidad": "efecto",
        "tipo": "Veneno",
        "estado": "envenenado"
    },
    "Rayo Solar": {
        "daño": 120,
        "tipo_habilidad": "normal",
        "tipo": "Planta",
        "estado": "normal"
    },
    "Colmillo Ígneo": {
        "daño": 65,
        "tipo_habilidad": "efecto",
        "tipo": "Fuego",
        "estado": "quemado"
    },
    "Ataque Ala": {
        "daño": 60,
        "tipo_habilidad": "normal",
        "tipo": "Volador",
        "estado": "normal"
    },
    "Chispazo": {
        "daño": 30,
        "tipo_habilidad": "multiple",
        "tipo": "Eléctrico",
        "estado": "normal"
    },
    "Pistola Agua": {
        "daño": 40,
        "tipo_habilidad": "normal",
        "tipo": "Agua",
        "estado": "normal"
    },
    "Alarido": {
        "daño": 55,
        "tipo_habilidad": "efecto",
        "tipo": "Siniestro",
        "estado": "confuso"
    },
    "Doble Golpe": {
        "daño": 15,
        "tipo_habilidad": "multiple",
        "tipo": "Normal",
        "estado": "normal"
    },
    "Colmillo Rayo": {
        "daño": 65,
        "tipo_habilidad": "efecto",
        "tipo": "Eléctrico",
        "estado": "paralizado"
    },
    "Polvo Veneno": {
        "daño": 0,
        "tipo_habilidad": "efecto",
        "tipo": "Veneno",
        "estado": "envenenado"
    },
    "Hipnosis": {
        "daño": 0,
        "tipo_habilidad": "efecto",
        "tipo": "Psíquico",
        "estado": "dormido"
    }
}

# Estados posibles de un Pokémon
estados_pokemon = {
    "normal": "El Pokémon no tiene efectos secundarios.",
    "envenenado": "El Pokémon pierde salud lentamente.",
    "quemado": "El Pokémon pierde salud lentamente y su ataque físico se reduce.",
    "paralizado": "El Pokémon a veces no puede atacar.",
    "dormido": "El Pokémon no puede atacar por algunos turnos.",
    "confuso": "El Pokémon puede dañarse a sí mismo.",
    "congelado": "El Pokémon no puede atacar hasta descongelarse.",
}

# Tipos de habilidades
tipos_habilidad = {
    "normal": "Ataque básico sin efectos adicionales.",
    "efecto": "Ataque que puede causar un efecto secundario.",
    "multiple": "Ataque que puede golpear varias veces en un turno.",
}

# Permite mostrar al usuario todas las habilidades disponibles

def mostrar_habilidades(habilidades=habilidades): # mostrar habilidades disponibles
    for idx, habilidad in enumerate(habilidades.keys()):
        print(f'{idx}: {habilidad}  ', end='') if (idx % 5 != 0 or idx == 0) else print()


if __name__ == '__main__':
    mostrar_habilidades()