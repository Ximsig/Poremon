from Pokemon import *


Charizard = Pokemon('Charizard', 110, list(habilidades.keys())[14:21:2], 'Fuego', 160)
Blastoise = Pokemon('Blastoise', 120, list(habilidades.keys())[2:6], 'Agua', 140)
Venusaur = Pokemon('Venusaur', 115, list(habilidades.keys())[5:9], 'Planta', 145)
Raichu = Pokemon('Raichu', 85, list(habilidades.keys())[0:4], 'Eléctrico', 200)
Sandslash = Pokemon('Sandslash', 100, list(habilidades.keys())[7:11], 'Tierra', 170)
Alakazam = Pokemon('Alakazam', 75, list(habilidades.keys())[8:12], 'Psíquico', 220)
Gengar = Pokemon('Gengar', 80, list(habilidades.keys())[11:23:3], 'Fantasma', 210)
Onix = Pokemon('Onix', 145, list(habilidades.keys())[17:24:2], 'Roca', 70)
Dragonite = Pokemon('Dragonite', 135, list(habilidades.keys())[9:13], 'Dragón', 90)
Flareon = Pokemon('Flareon', 95, list(habilidades.keys())[2:6], 'Fuego', 180)
Vaporeon = Pokemon('Vaporeon', 110, list(habilidades.keys())[5:12:2], 'Agua', 155)
Jolteon = Pokemon('Jolteon', 70, list(habilidades.keys())[0:4], 'Eléctrico', 240)
Pidgeot = Pokemon('Pidgeot', 90, list(habilidades.keys())[3:10:2], 'Volador', 190)
Arbok = Pokemon('Arbok', 95, list(habilidades.keys())[13:17], 'Veneno', 175)
Nidoking = Pokemon('Nidoking', 125, list(habilidades.keys())[12:16], 'Tierra', 120)
Dugtrio = Pokemon('Dugtrio', 80, list(habilidades.keys())[12:16], 'Tierra', 205)
Golduck = Pokemon('Golduck', 105, list(habilidades.keys())[3:7], 'Agua', 160)
Machamp = Pokemon('Machamp', 140, list(habilidades.keys())[3:15:3], 'Lucha', 80)
Golem = Pokemon('Golem', 150, list(habilidades.keys())[7:11], 'Roca', 50)
Rapidash = Pokemon('Rapidash', 85, list(habilidades.keys())[2:6], 'Fuego', 195)
Slowbro = Pokemon('Slowbro', 130, list(habilidades.keys())[16:23:2], 'Psíquico', 95)
Magneton = Pokemon('Magneton', 100, list(habilidades.keys())[0:4], 'Eléctrico', 165)
Dodrio = Pokemon('Dodrio', 75, list(habilidades.keys())[6:10], 'Volador', 215)
Cloyster = Pokemon('Cloyster', 135, list(habilidades.keys())[3:7], 'Agua', 85)
Hypno = Pokemon('Hypno', 115, list(habilidades.keys())[8:12], 'Psíquico', 140)
Kingler = Pokemon('Kingler', 120, list(habilidades.keys())[3:7], 'Agua', 130)
Electrode = Pokemon('Electrode', 70, list(habilidades.keys())[0:4], 'Eléctrico', 235)
Marowak = Pokemon('Marowak', 105, list(habilidades.keys())[7:14:2], 'Tierra', 155)
Hitmonlee = Pokemon('Hitmonlee', 90, list(habilidades.keys())[1:11:3], 'Lucha', 185)
Rhydon = Pokemon('Rhydon', 145, list(habilidades.keys())[10:17:2], 'Roca', 65)


if __name__ == '__main__':
    pokmn = Blastoise
    print(pokmn.habilidades)