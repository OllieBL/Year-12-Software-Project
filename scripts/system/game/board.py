import pygame
import numpy as np

class Board : 
    def __init__(self, tiles):
        self._tiles = tiles

    def add_tile(self, added_tile):
        self._tiles.update({added_tile._pos : added_tile})

    def print_tiles(self):
        print(self._tiles)

class Tile :
    def __init__(self, relative_pos, neighbour_tile=False, start_tile=False):
        if start_tile == False:
            self._pos = tuple(np.add(np.array(relative_pos), np.array(neighbour_tile._pos)).tolist())
        elif start_tile == True:
            self._pos = relative_pos
        else:
            raise Exception("start_tile must be a bool")


    def get_position(self):
        return self._pos