# Уровень - список, в котором 82 элемента - это карта уровня, а так же ещё 3 элемента - это кортеж
# с координатами появления противников, координаты появления игрока и координаты его базы.
# (Координаты от 0 до 40! А на карте уровня '-' - ничего, 'b' - кирпич, 'w' - вода, 'g' - трава)
NOTHING = '-'
BRICK = 'b'
WATER = 'w'
GRASS = 'g'
levels = []
levels.append(['----------------------------------------',
               '----------------------------------------',
               '----------------------------------------',
               '----------------------------------------',
               'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--bbbww',
               '-----------------------------------bbbww',
               '-----------------------------------bbbww',
               '--ggggggggggggggggggggggggggggggggggggww',
               '--ggggggggggggggggggggggggggggggggggggww',
               '--bbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
               '--bbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '--bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
               '----------------------------------------',
               '----------------------------------------',
               ((0, 0), (19, 0)), (18, 19), (19, 19)])
