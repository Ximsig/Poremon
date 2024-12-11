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

def normalize_key(key):
    return key.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

def normalize_dict_keys(original_dict):
    return {normalize_key(k): [normalize_key(v) for v in values] for k, values in original_dict.items()}

def normalize_dict_values(original_dict):
    return {normalize_key(k): {sub_k: (normalize_key(v) if isinstance(v, str) else v) for sub_k, v in values.items()} for k, values in original_dict.items()}

debilidades = normalize_dict_keys({
    'Acero': ['Fuego', 'Lucha', 'Tierra'],
    'Agua': ['Planta', 'Electrico'],
    'Bicho': ['Fuego', 'Roca', 'Volador'],
    'Dragon': ['Dragón', 'Hada', 'Hielo'],
    'Electrico': ['Tierra'],
    'Fantasma': ['Fantasma', 'Siniestro'],
    'Fuego': ['Agua', 'Roca', 'Tierra'],
    'Hada': ['Acero', 'Veneno'],
    'Hielo': ['Acero', 'Fuego', 'Lucha', 'Roca'],
    'Lucha': ['Hada', 'Psiquico', 'Volador'],
    'Normal': ['Lucha'],
    'Planta': ['Bicho', 'Fuego', 'Hielo', 'Veneno', 'Volador'],
    'Psiquico': ['Bicho', 'Fantasma', 'Siniestro'],
    'Roca': ['Acero', 'Agua', 'Lucha', 'Planta', 'Tierra'],
    'Siniestro': ['Bicho', 'Hada', 'Lucha'],
    'Tierra': ['Agua', 'Hielo', 'Planta'],
    'Veneno': ['Psiquico', 'Tierra'],
    'Volador': ['Electrico', 'Hielo', 'Roca']
})

efectividades = normalize_dict_keys({
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
})

inmunidades = normalize_dict_keys({
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
})

habilidades = normalize_dict_values({
    "Impactrueno": {
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Electrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Placaje": {
        "daño": 20,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Normal",
        "estado": EstadoPokemon.NORMAL
    },
    "Lanzallamas": {
        "daño": 90,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fuego",
        "estado": EstadoPokemon.QUEMADO
    },
    "Hidrobomba": {
        "daño": 110,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Agua",
        "estado": EstadoPokemon.NORMAL
    },
    "Rayo Hielo": {
        "daño": 80,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Hielo",
        "estado": EstadoPokemon.CONGELADO
    },
    "Gigadrenado": {
        "daño": 75,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Planta",
        "estado": EstadoPokemon.NORMAL
    },
    "Tornado": {
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Volador",
        "estado": EstadoPokemon.NORMAL
    },
    "Golpe Roca": {
        "daño": 50,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Roca",
        "estado": EstadoPokemon.CONFUSO
    },
    "Psicorrayo": {
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Psiquico",
        "estado": EstadoPokemon.CONFUSO
    },
    "Furia Dragon": {
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Dragon",
        "estado": EstadoPokemon.NORMAL
    },
    "Puño Trueno": {
        "daño": 75,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Electrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Bola Sombra": {
        "daño": 80,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fantasma",
        "estado": EstadoPokemon.CONFUSO
    },
    "Terremoto": {
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Tierra",
        "estado": EstadoPokemon.NORMAL
    },
    "Veneno X": {
        "daño": 60,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Veneno",
        "estado": EstadoPokemon.ENVENENADO
    },
    "Rayo Solar": {
        "daño": 120,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Planta",
        "estado": EstadoPokemon.NORMAL
    },
    "Colmillo Igneo": {
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Fuego",
        "estado": EstadoPokemon.QUEMADO
    },
    "Ataque Ala": {
        "daño": 60,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Volador",
        "estado": EstadoPokemon.NORMAL
    },
    "Chispazo": {
        "daño": 30,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Electrico",
        "estado": EstadoPokemon.NORMAL
    },
    "Pistola Agua": {
        "daño": 40,
        "tipo_habilidad": TipoHabilidad.NORMAL,
        "tipo": "Agua",
        "estado": EstadoPokemon.NORMAL
    },
    "Alarido": {
        "daño": 55,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Siniestro",
        "estado": EstadoPokemon.CONFUSO
    },
    "Doble Golpe": {
        "daño": 15,
        "tipo_habilidad": TipoHabilidad.MULTIPLE,
        "tipo": "Normal",
        "estado": EstadoPokemon.NORMAL
    },
    "Colmillo Rayo": {
        "daño": 65,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Electrico",
        "estado": EstadoPokemon.PARALIZADO
    },
    "Polvo Veneno": {
        "daño": 0,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Veneno",
        "estado": EstadoPokemon.ENVENENADO
    },
    "Hipnosis": {
        "daño": 0,
        "tipo_habilidad": TipoHabilidad.EFECTO,
        "tipo": "Psiquico",
        "estado": EstadoPokemon.DORMIDO
    }
})
