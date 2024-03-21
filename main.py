from tile import Tile
from point import Point

filename = '00-trailer.txt'

golden = []
silver = []
tiles = []

with open(filename, 'r') as file:
    line_pointer = 0
    for line in file:
        if line_pointer == 0:
            width, height, golden_count, silver_count, tile_count = map(int, line[3:].strip().split(' '))
            line_pointer += 1
            continue
        if line_pointer < 1 + golden_count:
            x, y = map(int, line.strip().split(' '))
            golden.append(Point(x, y, None))
            line_pointer += 1
            continue
        if line_pointer < 1 + golden_count + silver_count:
            x, y, value = map(int, line.strip().split(' '))
            silver.append(Point(x,y, value))    
            line_pointer += 1
            continue
        if line_pointer < 1 + golden_count + silver_count + tile_count:
            id, cost, number = line.strip().split(' ')
            for i in range(int(number)):
                tiles.append(Tile(id, int(cost)))  
            line_pointer += 1
            continue
    for tile in tiles:
        print(tile.can_connect())
            
