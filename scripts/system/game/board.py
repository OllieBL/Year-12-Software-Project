import pygame
import numpy as np
import json
import random

class Board: 
    def __init__(self, tiles):
        self._tiles = tiles
        self._adjacent_non_tiles = []

    def add_tile(self, added_tile):
        self._tiles.update({added_tile._pos : added_tile})
        self.score_board()

    def print_tiles(self):
        print(self._tiles)


    # Scores all of the tile adjacencies and outputs a score 
    def score_board(self):
        tiles = self._tiles
        self._adjacent_non_tiles = []

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

        for testing_tile in tiles:
            tile_pos = testing_tile
            tile_adjacencies = tiles[testing_tile].get_adjacencies()
            tile_score = 0
            new_score = tile_score
            old_score = tile_score
            for looped_pos in adjacency_looper:
                # This is in a try so I can avoid searching the list before hand for improved performance
                try:
                    adj_tile_coord = tuple(np.add(np.array(tile_pos), np.array(looped_pos)).tolist())
                    adjacent_tile = self._tiles[adj_tile_coord]    # finds new tile that is adjacent
                    new_score += tile_adjacencies[adjacent_tile.get_type()]                                          # updates tile score with adjacency
                    old_score = new_score                                                                            # old score stops new score from becoming non-int
                except KeyError:
                    if adj_tile_coord not in self._adjacent_non_tiles:
                        self._adjacent_non_tiles.append(adj_tile_coord)
                except:
                    new_score = old_score



                
    def generate_board_display(self, screen):
        tiles = self._tiles
        tiles = tiles.keys()
        non_tiles = self._adjacent_non_tiles
        display_tiles = []

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
        
        total_range = (high_tile[0][0]-low_tile[0][0]+3, high_tile[1][1]-low_tile[1][1]+3)

        centre_tile = (round((high_tile[0][0]+low_tile[0][0])/2), round((high_tile[1][1]+low_tile[1][1])/2))

        tile_size = min(round((3/4*screen.get_width())/total_range[0]), round((3/4*screen.get_height())/total_range[1]))

        tile_screen_pos = {}
        for i in tiles:
            screen_pos = ((i[0]-centre_tile[0])*tile_size+screen.get_width()/2, (-i[1]+centre_tile[1])*tile_size+screen.get_height()/2)
            tile_screen_pos[i] = screen_pos

        for i in tile_screen_pos:
            display_tile = pygame.Rect(tile_screen_pos[i][0], tile_screen_pos[i][1], tile_size, tile_size)
            pygame.draw.rect(screen, (255, 255, 255), display_tile)
            display_tiles.append(display_tile)
            tile_image = pygame.image.load(self._tiles[i].get_image()).convert_alpha()
            tile_image = pygame.transform.scale(tile_image, (tile_size, tile_size))
            screen.blit(tile_image, (tile_screen_pos[i][0], tile_screen_pos[i][1]))


        non_tile_screen_pos = {}
        for i in non_tiles:
            screen_pos = ((i[0]-centre_tile[0])*tile_size+screen.get_width()/2, (-i[1]+centre_tile[1])*tile_size+screen.get_height()/2)
            non_tile_screen_pos[i] = screen_pos

        for i in non_tile_screen_pos:
            display_tile = pygame.Rect(non_tile_screen_pos[i][0], non_tile_screen_pos[i][1], tile_size, tile_size)
            if display_tile.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), display_tile)
            else:
                pygame.draw.rect(screen, (10, 10, 10), display_tile)





class Tile:
    def __init__(self, pos, tile_type):
        self._pos = pos
        self._type = tile_type

        # loads up the json file for tile features
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
    
    def get_adjacencies(self):
        return self._adjacencies
    






class Hand:
    def __init__(self):
        self._tiles = []
        self._loop_range = (1,6) # How many of each kind of tile there are


    def create_hand(self):
        with open('scripts/system/game/tile_types.json') as f:
            type_features = json.load(f)

        for tiletype in type_features:
            n = 0
            loop_amount = random.randrange(self._loop_range[0], self._loop_range[1]) # so a random amount of tiles are produced within the range
            while n <= loop_amount:
                self._tiles.append(tiletype)
        
        random.shuffle(self._tiles)
    


pygame.init()

screen = pygame.display.set_mode((1920, 1080))

tile1 = Tile((0,0), tile_type="forest")
tile2 = Tile((1,0), tile_type="forest")
tile3 = Tile((0,1), tile_type="forest")
tile4 = Tile((-1,1), tile_type="forest")
tile5 = Tile((1,1), tile_type="forest")
tile6 = Tile((-1,0), tile_type="forest")

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
