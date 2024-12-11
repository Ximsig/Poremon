from pokemon import *


Charizard = Pokemon('Charizard', 300, list(habilidades.keys())[14:21:2], 'Fuego', 120)
Blastoise = Pokemon('Blastoise', 280, list(habilidades.keys())[2:6], 'Agua', 130)
Venusaur = Pokemon('Venusaur', 275, list(habilidades.keys())[5:9], 'Planta', 135)
Raichu = Pokemon('Raichu', 200, list(habilidades.keys())[0:4], 'Eléctrico', 180)
Sandslash = Pokemon('Sandslash', 240, list(habilidades.keys())[7:11], 'Tierra', 150)
Alakazam = Pokemon('Alakazam', 210, list(habilidades.keys())[8:12], 'Psíquico', 175)
Gengar = Pokemon('Gengar', 220, list(habilidades.keys())[11:23:3], 'Fantasma', 165)
Onix = Pokemon('Onix', 350, list(habilidades.keys())[17:24:2], 'Roca', 90)
Dragonite = Pokemon('Dragonite', 320, list(habilidades.keys())[9:13], 'Dragón', 100)
Flareon = Pokemon('Flareon', 250, list(habilidades.keys())[2:6], 'Fuego', 140)
Vaporeon = Pokemon('Vaporeon', 270, list(habilidades.keys())[5:12:2], 'Agua', 135)
Jolteon = Pokemon('Jolteon', 210, list(habilidades.keys())[0:4], 'Eléctrico', 170)
Pidgeot = Pokemon('Pidgeot', 240, list(habilidades.keys())[3:10:2], 'Volador', 150)
Arbok = Pokemon('Arbok', 230, list(habilidades.keys())[13:17], 'Veneno', 155)
Nidoking = Pokemon('Nidoking', 260, list(habilidades.keys())[12:16], 'Tierra', 140)
Dugtrio = Pokemon('Dugtrio', 210, list(habilidades.keys())[12:16], 'Tierra', 180)
Golduck = Pokemon('Golduck', 275, list(habilidades.keys())[3:7], 'Agua', 130)
Machamp = Pokemon('Machamp', 340, list(habilidades.keys())[3:15:3], 'Lucha', 91)
Golem = Pokemon('Golem', 350, list(habilidades.keys())[7:11], 'Roca', 80)
Rapidash = Pokemon('Rapidash', 220, list(habilidades.keys())[2:6], 'Fuego', 165)
Slowbro = Pokemon('Slowbro', 320, list(habilidades.keys())[16:23:2], 'Psíquico', 100)
Magneton = Pokemon('Magneton', 250, list(habilidades.keys())[0:4], 'Eléctrico', 140)
Dodrio = Pokemon('Dodrio', 210, list(habilidades.keys())[6:10], 'Volador', 175)
Cloyster = Pokemon('Cloyster', 280, list(habilidades.keys())[3:7], 'Agua', 125)
Hypno = Pokemon('Hypno', 270, list(habilidades.keys())[8:12], 'Psíquico', 130)
Kingler = Pokemon('Kingler', 260, list(habilidades.keys())[3:7], 'Agua', 140)
Electrode = Pokemon('Electrode', 200, list(habilidades.keys())[0:4], 'Eléctrico', 190) 
Marowak = Pokemon('Marowak', 240, list(habilidades.keys())[7:14:2], 'Tierra', 150)
Hitmonlee = Pokemon('Hitmonlee', 220, list(habilidades.keys())[1:11:3], 'Lucha', 160)
Rhydon = Pokemon('Rhydon', 340, list(habilidades.keys())[10:17:2], 'Roca', 85)


Pokemons = [Charizard, Blastoise, Venusaur, Raichu, Sandslash,
            Alakazam, Gengar, Onix, Dragonite, Flareon,
            Vaporeon, Jolteon, Pidgeot, Arbok, Nidoking, Dugtrio,
            Golduck, Machamp, Golem, Rapidash, Slowbro,
            Magneton, Dodrio, Cloyster, Hypno, Kingler, Electrode,
            Marowak, Hitmonlee, Rhydon]
if __name__ == '__main__':
    print(len(Pokemons))