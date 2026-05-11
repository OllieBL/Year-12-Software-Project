dict_test = {
    (0, 0) : "tile_1",
    (0, -1) : "tile_2",
    (-1, -1) : "tile_3",
    (1, 1) : "tile_4"
}

value = 0
print(dict_test[(value+1, value+1)], dict_test[(value-1, value-1)])