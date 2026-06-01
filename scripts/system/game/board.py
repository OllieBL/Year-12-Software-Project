import pygame
import numpy as np
import json
import random

class Board: 
    def __init__(self, tiles):
        self._tiles = tiles

    def add_tile(self, added_tile):
        self._tiles.update({added_tile._pos : added_tile})

    def print_tiles(self):
        print(self._tiles)


    # Scores all of the tile adjacencies and outputs a score 
    def score_board(self):

        # allows me to loop over a set of coordinates that are adjacent
        adjacency_looper = [
            (-1,-1),
            (0,-1),
            (1,-1),
            (-1,0),
            (1,0),
            (-1,1),
            (0,1),
            (1,1)
        ]

        for testing_tile in self._tiles:
            tile_pos = testing_tile.get_position()
            tile_adjacencies = testing_tile.get_adjacencies()
            tile_score = 0
            new_score = tile_score
            for looped_pos in adjacency_looper:
                # This is in a try so I can avoid searching the list before hand for improved performance
                try:
                    adjacent_tile = self._tiles[tuple(np.add(np.array(tile_pos), np.array(looped_pos)).tolist())]    # finds new tile that is adjacent
                    new_score += tile_adjacencies[adjacent_tile.get_type()]                                          # updates tile score with adjacency
                except:
                    continue



                
    def generate_board_display(self, screen):
        tiles = self._tiles
        tiles = tiles.keys()
        low_tile = [(0,0),(0,0)]
        high_tile = [(0,0),(0,0)]

        for i in tiles:
            if low_tile[0][0] > i[0]:
                low_tile[0] = i
            elif high_tile[0][0] < i[0]:
                high_tile[0] = i

            if low_tile[1][1] > i[1]:
                low_tile[1] = i
            if high_tile[1][1] < i[1]:
                high_tile[1] = i
        
        total_range = (high_tile[0][0]-low_tile[0][0]+1, high_tile[1][1]-low_tile[1][1]+1)

        centre_tile = (round(total_range[0]/2), round(total_range[1]/2))

        tile_size = min(round((3/4*screen.get_width())/total_range[0]), round((3/4*screen.get_height())/total_range[1]))

        tile_screen_pos = {}
        for i in tiles:
            screen_pos = ((i[0]-centre_tile[0])*tile_size+screen.get_width()/2, (i[1]-centre_tile[1])*tile_size+screen.get_height()/2)
            tile_screen_pos[i] = screen_pos

        for i in tile_screen_pos:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(tile_screen_pos[i][0], tile_screen_pos[i][1], tile_size, tile_size))
            tile_image = pygame.image.load(self._tiles[i].get_image()).convert_alpha()
            tile_image = pygame.transform.scale(tile_image, (tile_size, tile_size))
            screen.blit(tile_image, (i[0], i[1]))


class Tile:
    def __init__(self, pos, tile_type):
        self._pos = pos
        self._type = tile_type

        with open('scripts/system/game/tile_types.json') as f:
            type_features = json.load(f)
        self._image = type_features[self._type]["image"]
        self._adjacencies = type_features[self._type]["adjacencies"]


    def get_position(self):
        return self._pos
    
    def get_image(self):
        return self._image
    
    def get_type(self):
        return self._type
    






class Hand:
    def __init__(self):
        self._tiles = []
        self._loop_range = 


    def create_hand(self):
        with open('scripts/system/game/tile_types.json') as f:
            type_features = json.load(f)

        for tiletype in type_features:
            n = 0
            while n < 4:
                self._tiles.append(tiletype)
        
        random.shuffle(self._tiles)
    

'''
pygame.init()

screen = pygame.display.set_mode((1920, 1080))

tile1 = Tile((0,0), tile_type="forest")
tile2 = Tile((1,0), tile_type="forest")
tile3 = Tile((0,1), tile_type="forest")
tile4 = Tile((-1,1), neighbour_tile=tile1, tile_type="forest")
tile5 = Tile((1,1), neighbour_tile=tile2, tile_type="forest")
tile6 = Tile((0,1), neighbour_tile=tile3, tile_type="forest")

board0 = Board({tile1._pos:tile1})

board0.add_tile(tile2)
board0.add_tile(tile3)
board0.add_tile(tile4)
board0.add_tile(tile5)
board0.add_tile(tile6)
while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    board0.generate_board_display(screen)
    pygame.display.flip()
'''