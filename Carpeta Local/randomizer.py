import random
import math

def sortear_torneo(entrenadores):
    """
    Realiza el sorteo del torneo de forma aleatoria y retorna el bracket.
    
    Args:
        entrenadores (list): Lista de entrenadores participantes.
    
    Returns:
        list: Lista de rondas con los enfrentamientos (listas anidadas).
    """
    if len(entrenadores) < 2:
        print("Debe haber al menos 2 entrenadores para realizar el torneo.")
        return []
    
    print("\n¡Sorteo del torneo Pokémon!")
    random.shuffle(entrenadores)  # Mezclar aleatoriamente los entrenadores
    
    # Ajustar la cantidad de entrenadores al número más cercano de potencia de 2
    num_participantes = 2 ** math.ceil(math.log2(len(entrenadores)))
    while len(entrenadores) < num_participantes:
        entrenadores.append(None)  # Añadir "vacíos" para completar el bracket
    
    # Crear el bracket inicial
    bracket = [[(entrenadores[i], entrenadores[i + 1]) for i in range(0, len(entrenadores), 2)]]
    
    # Completar el bracket para simular la progresión
    while len(bracket[-1]) > 1:
        bracket.append([(None, None)] * (len(bracket[-1]) // 2))
    
    return bracket


def mostrar_bracket(bracket, n):
    """
    Muestra los enfrentamientos en formato compacto y legible.
    
    Args:
        bracket (list): Lista de rondas con los enfrentamientos.
    """
    for ronda in bracket:
        print(f"\nRonda {n}:")
        linea = ""
        for enfrentamiento in ronda:
            e1 = enfrentamiento[0].Nombre if enfrentamiento[0] else "(vacío)"
            e2 = enfrentamiento[1].Nombre if enfrentamiento[1] else "(vacío)"
            linea += f"({e1}) vs ({e2})    "  # Formato compacto
        print(linea.strip())
        n += 1
