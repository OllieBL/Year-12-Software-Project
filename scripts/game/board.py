import pygame
import numpy as np

class Board : 
    def __init__(self, tiles):
        self._tiles = tiles

    def add_tile(self, added_tile, added_tile_pos, neighbour_tile_pos):
        pos = tuple(np.add(np.array(added_tile_pos), np.array(neighbour_tile_pos)).tolist())
        self._tiles.update({pos : added_tile})

    def print_tiles(self):
        print(self._tiles)

class Tile :
    def __init__(self, relative_pos):
        

    def get_position(self):
        return self._position