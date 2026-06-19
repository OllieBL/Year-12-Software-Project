import pygame
import game.board as board

class Menu:
    def __init__(self, screen):
        self.screen = screen


    def display_menu(self):

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        font = pygame.font.Font('freesansbold.ttf', 60)

        title = font.render('City Game', True, (255,255,255))
        button_text = font.render('Play', True, (0,0,0))

        title_rect = title.get_rect()
        button_rect = button_text.get_rect()
        
        title_rect.center = (screen_width*0.5, screen_height*0.1)
        button_rect.center = (screen_width*0.5, screen_height*0.2)

        while True:
            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
            
            if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                tile1 = board.Tile((0,0), tile_type="forest")

                board1 = board.Board({})

                board1.add_tile(tile1)

                hand1 = board.Hand()
                hand1.create_deck()
                hand1.create_hand()
                board.loop_function(self.screen, board1, hand1)
            pygame.draw.rect(self.screen, (255,255,255), button_rect)

            self.screen.blit(title, title_rect)
            self.screen.blit(button_text, button_rect)


            pygame.display.flip()