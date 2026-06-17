import pygame
import numpy as np
import json
import random

class Board: 
    def __init__(self, tiles):
        self._tiles = tiles
        self._adjacent_non_tiles = []
        self._score = 0

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
            old_score = self._score
            new_score = old_score
            for looped_pos in adjacency_looper:
                # This is in a try so I can avoid searching the list before hand for improved performance
                try:
                    adj_tile_coord = tuple(np.add(np.array(tile_pos), np.array(looped_pos)).tolist())
                    adjacent_tile = self._tiles[adj_tile_coord]                                                      # finds new tile that is adjacent
                    new_score += tile_adjacencies[adjacent_tile.get_type()]                                          # updates tile score with adjacency
                    old_score = new_score                                                                            # old score stops new score from becoming non-int
                except KeyError:
                    if adj_tile_coord not in self._adjacent_non_tiles and adj_tile_coord not in tiles:               # makes sure the tile isn't in tiles or nontiles before adding it
                        self._adjacent_non_tiles.append(adj_tile_coord)
                except:
                    new_score = old_score                                                                            # stops horrific errors where I get stuff going through the filter and getting nonint answers
            
        self._score = new_score



                
    def generate_board_display(self, screen, hand):
        tiles = self._tiles
        tiles = tiles.keys()
        non_tiles = self._adjacent_non_tiles
        display_tiles = []
        screen_height = screen.get_height()
        screen_width = screen.get_width()

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

        centre_tile = (round((high_tile[0][0]+low_tile[0][0])*0.5), round((high_tile[1][1]+low_tile[1][1])*0.5))

        tile_size = min(round((0.75*screen_width)/total_range[0]), round((0.5*screen_height)/total_range[1]))

        tile_screen_pos = {}
        for i in tiles:
            screen_pos = ((i[0]-centre_tile[0])*tile_size+screen_width*0.5, (-i[1]+centre_tile[1])*tile_size+(screen_height*0.625)*0.5)
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
            screen_pos = ((i[0]-centre_tile[0])*tile_size+screen_width*0.5, (-i[1]+centre_tile[1])*tile_size+(screen_height*0.625)*0.5)
            non_tile_screen_pos[i] = screen_pos

        for i in non_tile_screen_pos:
            display_tile = pygame.Rect(non_tile_screen_pos[i][0], non_tile_screen_pos[i][1], tile_size, tile_size)
            if display_tile.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), display_tile)
                if pygame.mouse.get_pressed()[0] and hand.get_click_state():
                    tile = Tile(i, hand.get_clicked_tile())
                    self.add_tile(tile)
                    hand.unclick()
                    hand.create_hand()
            else:
                pygame.draw.rect(screen, (10, 10, 10), display_tile)
            
        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render('score: ' + str(self._score), True, (255,255,255))

        textRect = text.get_rect()
        
        textRect.center = (screen_width/2, screen_height*0.1)

        screen.blit(text, textRect)





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
        self._loop_range = (5,10) # How many of each kind of tile there are
        self.selected_tile = ''
        self._hand = []
        self._isclicking = False


    def create_deck(self):
        with open('scripts/system/game/tile_types.json') as f:
            type_features = json.load(f)

        for tiletype in type_features:
            n = 0
            loop_amount = 10 #random.randrange(self._loop_range[0], self._loop_range[1]) # so a random amount of tiles are produced within the range
            while n <= loop_amount:
                self._tiles.append(tiletype)
                n += 1
        
        random.shuffle(self._tiles)

    def create_hand(self):
        x = 5
        while x != len(self._hand) and len(self._tiles) != 0:
            self._hand.append(self._tiles[0])
            self._tiles.pop(0)

    
    def display_hand(self, screen):
        hand = self._hand
        screen_height = screen.get_height()
        screen_width = screen.get_width()
        with open('scripts/system/game/tile_types.json') as f:
            type_features = json.load(f)

        handlen = len(hand)
        if handlen == 0:
            return
        handlenrecip = 1/handlen

        centre_point = 0.5*handlen

        tile_size = min(0.75*screen_width*handlenrecip, 0.375*screen_height) 
        
        hand_tile_pos = []
        for i in range(len(hand)):
            screen_pos = ((i - centre_point)*tile_size + screen_width*0.5, screen_height - tile_size)
            hand_tile_pos.append(screen_pos)
        
        display_tiles = []
        removed_tile = ''
        for i in range(len(hand_tile_pos)):
            display_tile = pygame.Rect(hand_tile_pos[i][0], hand_tile_pos[i][1], tile_size, tile_size)
            pygame.draw.rect(screen, (255, 255, 255), display_tile)
            #display_tiles.append(display_tile)                         # I'm just as confused what this was for as you are
            tile_image = pygame.image.load(type_features[hand[i]]["image"]).convert_alpha()
            tile_image = pygame.transform.scale(tile_image, (tile_size, tile_size))
            screen.blit(tile_image, (hand_tile_pos[i][0], hand_tile_pos[i][1]))
            if display_tile.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self._isclicking:
                removed_tile = i
        if removed_tile != '':
            self._clicked_tile = self._hand[removed_tile]
            self._hand.pop(removed_tile)
            self._isclicking = True
        
        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render('Tiles Left: ' + str(len(self._tiles)), True, (255,255,255))

        textRect = text.get_rect()
        
        textRect.center = (100, screen_height - 100)

        screen.blit(text, textRect)

    def get_click_state(self):
        return self._isclicking
    
    def get_clicked_tile(self):
        return self._clicked_tile

    def unclick(self):
        self._isclicking = False

    


pygame.init()

screen = pygame.display.set_mode((1920, 1080))

tile1 = Tile((0,0), tile_type="forest")

board0 = Board({})

board0.add_tile(tile1)

hand0 = Hand()
hand0.create_deck()
hand0.create_hand()

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    board0.generate_board_display(screen, hand0)
    hand0.display_hand(screen)
    
    pygame.display.flip()
