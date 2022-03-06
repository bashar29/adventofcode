import math
from collections import defaultdict

def get_puzzle_input(filename):
    tiles = defaultdict(list)
    with open(filename,'r') as file:
        current_tile = -1
        for line in file:
            if line.strip() == '':
                pass
            elif 'Tile' in line.strip():
                current_tile = int(line.strip().split(' ')[1][:-1])
                tiles[current_tile] = []
            else:
                tiles[current_tile].append([*line.strip()]) 
        #print(tiles)
    return tiles

def first_star():
    tiles = get_puzzle_input('../data/inputday20.txt')
    image_width = int(math.sqrt(len(tiles)))
    

def second_star():
    pass

if __name__ == '__main__':
    first_star()
    second_star()
