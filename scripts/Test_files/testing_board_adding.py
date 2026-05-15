import numpy as np
from scripts.system.game import board

tile1 = board.Tile((2,21), start_tile=True)
tile2 = board.Tile((1,0), tile1)
tile3 = board.Tile((0,1), tile2)

board0 = board.Board({tile1._pos:tile1})

board0.add_tile(tile2)
board0.print_tiles()

board0.add_tile(tile3)
board0.print_tiles()