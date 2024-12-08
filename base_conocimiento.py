
from enum import Enum

class EstadoPokemon(Enum):
    NORMAL = "normal"
    ENVENENADO = "envenenado"
    PARALIZADO = "paralizado"
    DORMIDO = "dormido"
    QUEMADO = "quemado"
    CONFUSO = "confuso"
    CONGELADO = "congelado"

class TipoHabilidad(Enum):
    NORMAL = "normal"
    EFECTO = "efecto"
    MULTIPLE = "multiple"

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
    "Impactrueno": { # 0
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Eléctrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Placaje": { # 1
        "daño": 20,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Normal",
        "estado": EstadoPokemon.NORMAL
    },
    "Lanzallamas": { # 2
        "daño": 90,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fuego",
        "estado": EstadoPokemon.QUEMADO
    },
    "Hidrobomba": { # 3
        "daño": 110,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Agua",
        "estado": EstadoPokemon.NORMAL
    },
    "Rayo Hielo": { # 4
        "daño": 80,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Hielo",
        "estado": EstadoPokemon.CONGELADO
    },
    "Gigadrenado": { # 5
        "daño": 75,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Planta",
        "estado": EstadoPokemon.NORMAL
    },
    "Tornado": { # 6
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Volador",
        "estado": EstadoPokemon.NORMAL
    },
    "Golpe Roca": { #7
        "daño": 50,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Roca",
        "estado": EstadoPokemon.CONFUSO
    },
    "Psicorrayo": { # 8
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Psíquico",
        "estado": EstadoPokemon.CONFUSO
    },
    "Furia Dragón": { # 9
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Dragón",
        "estado": EstadoPokemon.NORMAL
    },
    "Puño Trueno": { # 10
        "daño": 75,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Eléctrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Bola Sombra": { # 11
        "daño": 80,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fantasma",
        "estado": EstadoPokemon.CONFUSO
    },
    "Terremoto": { # 12
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Tierra",
        "estado": EstadoPokemon.NORMAL
    },
    "Veneno X": { # 13
        "daño": 60,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Veneno",
        "estado": EstadoPokemon.ENVENENADO
    },
    "Rayo Solar": { # 14
        "daño": 120,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Planta",
        "estado": EstadoPokemon.NORMAL
    },
    "Colmillo Ígneo": { # 15
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fuego",
        "estado": EstadoPokemon.QUEMADO
    },
    "Ataque Ala": { # 16
        "daño": 60,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Volador",
        "estado": EstadoPokemon.NORMAL
    },
    "Chispazo": { # 17
        "daño": 30,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Eléctrico",
        "estado": EstadoPokemon.NORMAL
    },
    "Pistola Agua": { # 18
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Agua",
        "estado": EstadoPokemon.NORMAL
    },
    "Alarido": { # 19
        "daño": 55,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Siniestro",
        "estado": "confuso"
    },
    "Doble Golpe": { # 20
        "daño": 15,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Normal",
        "estado": EstadoPokemon.NORMAL
    },
    "Colmillo Rayo": { # 21
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Eléctrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Polvo Veneno": { # 22
        "daño": 0,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Veneno",
        "estado": EstadoPokemon.ENVENENADO
    },
    "Hipnosis": { # 23
        "daño": 0,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Psíquico",
        "estado": EstadoPokemon.DORMIDO
    }
}
