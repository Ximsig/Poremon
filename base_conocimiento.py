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
        "estado": None  # No inflige estado
    },
    "Lanzallamas": {
        "daño": 90,
        "tipo_habilidad": "efecto",
        "tipo": "Fuego",
        "estado": "quemado"
    },
    "Hidrobomba": {
        "daño": 110,
        "tipo_habilidad": "efecto",
        "tipo": "Agua",
        "estado": None
    },
    "Rayo Hielo": {
        "daño": 80,
        "tipo_habilidad": "efecto",
        "tipo": "Hielo",
        "estado": "congelado"
    },
    "Gigadrenado": {
        "daño": 75,
        "tipo_habilidad": "curación",
        "tipo": "Planta",
        "estado": None
    },
    "Tornado": {
        "daño": 60,
        "tipo_habilidad": "daño continuo",
        "tipo": "Volador",
        "estado": None
    },
    "Golpe Roca": {
        "daño": 50,
        "tipo_habilidad": "efecto",
        "tipo": "Roca",
        "estado": "atontado"
    },
    "Psicorrayo": {
        "daño": 65,
        "tipo_habilidad": "efecto",
        "tipo": "Psíquico",
        "estado": "confuso"
    },
    "Furia Dragón": {
        "daño": 40,
        "tipo_habilidad": "daño fijo",
        "tipo": "Dragón",
        "estado": None
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
        "estado": "bajado defensa especial"
    },
    "Terremoto": {
        "daño": 100,
        "tipo_habilidad": "multiple",
        "tipo": "Tierra",
        "estado": None
    },
    "Veneno X": {
        "daño": 60,
        "tipo_habilidad": "efecto",
        "tipo": "Veneno",
        "estado": "envenenado"
    },
    "Rayo Solar": {
        "daño": 120,
        "tipo_habilidad": "carga",
        "tipo": "Planta",
        "estado": None
    },
    "Colmillo Ígneo": {
        "daño": 65,
        "tipo_habilidad": "efecto",
        "tipo": "Fuego",
        "estado": "quemado"
    },
    "Ataque Ala": {
        "daño": 60,
        "tipo_habilidad": "directo",
        "tipo": "Volador",
        "estado": None
    },
    "Chispazo": {
        "daño": 70,
        "tipo_habilidad": "multiple",
        "tipo": "Eléctrico",
        "estado": "paralizado"
    },
    "Pistola Agua": {
        "daño": 40,
        "tipo_habilidad": "directo",
        "tipo": "Agua",
        "estado": None
    },
    "Alarido": {
        "daño": 55,
        "tipo_habilidad": "efecto",
        "tipo": "Siniestro",
        "estado": "bajado ataque especial"
    }
}
