
def generate_board_display(board, screen):
    tiles = board._tiles
    low_tile = [(0,0),(0,0)]
    high_tile = [(0,0),(0,0)]

    for i in tiles:
        if low_tile[0][0] > i[0]:
            low_tile[0] = i
        elif high_tile[0][0] < i[0]:
            high_tile[0] = i

        if low_tile[1][1] < i[1]:
            low_tile[1] = i
        if high_tile[1][1] > i[1]:
            high_tile[1] = i
    
    total_range = (high_tile[0][0]-low_tile[0][0], high_tile[1][1]-low_tile[1][1])