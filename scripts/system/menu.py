import pygame
import game.board as board
import login 

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self._user = ['','',0]


    def display_menu(self):

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        font = pygame.font.Font('freesansbold.ttf', 60)

        welcome_text = ''
        
        title = font.render('City Game', True, (255,255,255))
        play_button_text = font.render('Play', True, (0,0,0))
        sign_up_button_text = font.render('Sign up', True, (0,0,0))
        login_button_text = font.render('Login', True, (0,0,0))
        save_button_text = font.render('Save', True, (0,0,0))

        title_rect = title.get_rect()                                       # need to get the rect object for the placing and display
        play_button_rect = play_button_text.get_rect()
        sign_up_button_rect = sign_up_button_text.get_rect()
        login_button_rect = login_button_text.get_rect()
        save_button_rect = save_button_text.get_rect()
        
        title_rect.center = (screen_width*0.5, screen_height*0.1)
        play_button_rect.center = (screen_width*0.5, screen_height*0.2)
        sign_up_button_rect.center = (screen_width*0.5, screen_height*0.3)
        login_button_rect.center = (screen_width*0.5, screen_height*0.4)
        save_button_rect.center = (screen_width*0.5, screen_height*0.5)

        while True:
            self.screen.fill((0,0,0))
            login1 = login.Login(self.screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                tile1 = board.Tile((0,0), tile_type="forest")

                board1 = board.Board({})

                board1.add_tile(tile1)

                hand1 = board.Hand()
                hand1.create_deck()
                hand1.create_hand()
                new_score = board.loop_function(self.screen, board1, hand1)
                if new_score > self._user[2]:
                    self._user[2] = new_score
            if sign_up_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                tester = login1.display_signup()
                if tester != False:
                    self._user = tester
            if login_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                tester = login1.display_login()
                if tester != False:
                    self._user = tester
            if save_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                login1.set_score(self._user[2])
                login1.save_score(self._user[0], self._user[1])

            pygame.draw.rect(self.screen, (255,255,255), play_button_rect)
            pygame.draw.rect(self.screen, (255,255,255), sign_up_button_rect)
            pygame.draw.rect(self.screen, (255,255,255), login_button_rect)
            pygame.draw.rect(self.screen, (255,255,255), save_button_rect)

            self.screen.blit(title, title_rect)
            self.screen.blit(play_button_text, play_button_rect)
            self.screen.blit(sign_up_button_text, sign_up_button_rect)
            self.screen.blit(login_button_text, login_button_rect)
            self.screen.blit(save_button_text, save_button_rect)
            
            if self._user[0] != '':
                welcome_text = font.render(f'Welcome {self._user[0]}, try beat your score of {self._user[2]}', True, (255,255,255))
            else:
                welcome_text = font.render(f'Try logging in', True, (255,255,255))
            welcome_rect = welcome_text.get_rect()
            welcome_rect.center = (screen_width*0.5, screen_height*0.6)
            self.screen.blit(welcome_text, welcome_rect)

            pygame.display.flip()