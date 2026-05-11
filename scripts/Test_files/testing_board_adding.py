import numpy as np
from game import board

tile1 = board.Tile()
tile2 = board.Tile()
tile3 = board.Tile()

board0 = board.Board({(0,0):tile1})

board0.add_tile(tile2)
board0.print_tiles()

board0.add_tile(tile3)
board0.print_tiles()