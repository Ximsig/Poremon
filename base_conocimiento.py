from enum import Enum

class EstadoPokemon(Enum): #Enumeraciones para los estado pokemon
    NORMAL = "normal"
    ENVENENADO = "envenenado"
    PARALIZADO = "paralizado"
    DORMIDO = "dormido"
    QUEMADO = "quemado"
    CONFUSO = "confuso"
    CONGELADO = "congelado"

class TipoHabilidad(Enum): #Enumeraciones para los tipo de habilidad
    NORMAL = "normal"
    EFECTO = "efecto"
    MULTIPLE = "multiple"

debilidades = { #Diccionario que contiene las debilidades
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

efectividades = { #Diccionario que contiene las efectividades
    'Acero': ['Hada', 'Hielo', 'Roca'],
    'Agua': ['Fuego', 'Roca', 'Tierra'],
    'Bicho': ['Hada', 'Planta', 'Psiquico'],
    'Dragon': ['Dragon'],
    'Electrico': ['Agua', 'Volador'],
    'Fantasma': ['Fantasma', 'Psiquico'],
    'Fuego': ['Acero', 'Bicho', 'Hielo', 'Planta'],
    'Hada': ['Dragon', 'Lucha', 'Siniestro'],
    'Hielo': ['Dragon', 'Planta', 'Tierra', 'Volador'],
    'Lucha': ['Acero', 'Hielo', 'Normal', 'Roca', 'Siniestro'],
    'Normal': [],
    'Planta': ['Agua', 'Roca', 'Tierra'],
    'Psiquico': ['Lucha', 'Veneno'],
    'Roca': ['Bicho', 'Fuego', 'Hielo', 'Volador'],
    'Siniestro': ['Fantasma', 'Psiquico'],
    'Tierra': ['Electrico', 'Fuego', 'Roca', 'Veneno', 'Acero'],
    'Veneno': ['Hada', 'Planta'],
    'Volador': ['Bicho', 'Lucha', 'Planta']
}

inmunidades = { #Diccionario que contiene las inmunidades
    'Acero': ['Veneno'],
    'Agua': [],
    'Bicho': [],
    'Dragon': [],
    'Electrico': [],
    'Fantasma': ['Normal', 'Lucha'],
    'Fuego': [],
    'Hada': ['Dragon'],
    'Hielo': [],
    'Lucha': ['Fantasma'],
    'Normal': ['Fantasma'],
    'Planta': [],
    'Psiquico': ['Fantasma'],
    'Roca': [],
    'Siniestro': ['Psiquico'],
    'Tierra': ['Electrico'],
    'Veneno': [],
    'Volador': ['Tierra']
}

habilidades = { #Diccionario que contiene las habilidades existentes
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

def mostrar_habilidades() -> None:
    """
    Muestra todas las habilidades disponibles en la base de conocimiento.
    """
    print("Habilidades disponibles en la base de conocimientos:")
    for habilidad, info in habilidades.items():
        print(f"Habilidad: {habilidad}")
        print(f"  Daño: {info['daño']}")
        print(f"  Tipo: {info['tipo']}")
        print(f"  Tipo de Habilidad: {info['tipo_habilidad'].value}")
        estado = info['estado']
        estado_value = estado.value if isinstance(estado, EstadoPokemon) else estado
        print(f"  Estado: {estado_value}")
        print("-" * 30)
