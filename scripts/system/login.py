import pygame
import pickle

class Login:
    def __init__(self, screen):
        self._username = ''
        self._password = ''
        self._score = 0
        self.screen = screen


    def display_login(self):

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        font = pygame.font.Font('freesansbold.ttf', int(screen_height*0.1))

        username_rect = pygame.Rect(0,0,screen_width*0.5, screen_height*0.1)
        username_rect.center = (screen_width*0.5, screen_height*0.1)
        password_rect = pygame.Rect(0,0,screen_width*0.5, screen_height*0.1)
        password_rect.center = (screen_width*0.5, screen_height*0.3)

        button_text = font.render('Login', True, (0,0,0))
        button_rect = button_text.get_rect()
        button_rect.center = (screen_width*0.5, screen_height*0.5)

        active = 0

        user_text = ['Username','Password']

        while True:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if username_rect.collidepoint(event.pos):
                        active = 1
                    elif password_rect.collidepoint(event.pos):
                        active = 2
                    elif button_rect.collidepoint(event.pos):
                        self.check_details(user_text[0], user_text[1])
                    else:
                        active = 0

                if event.type == pygame.KEYDOWN and active != 0:
                    if event.key == pygame.K_BACKSPACE:
                        user_text[active-1] = user_text[active-1][:-1]
                    else:
                        user_text[active-1] += event.unicode

            pygame.draw.rect(self.screen, (255,255,255), username_rect)
            pygame.draw.rect(self.screen, (255,255,255), password_rect)
            pygame.draw.rect(self.screen, (255,255,255), button_rect)

            username_text = font.render(user_text[0], True, (0,0,0))
            password_text = font.render(user_text[1], True, (0,0,0))

            self.screen.blit(username_text, username_rect)
            self.screen.blit(password_text, password_rect)
            self.screen.blit(button_text, button_rect)

            pygame.display.flip()


        
    def check_details(self, username, password):
        self._username = username
        self._password = password

        login_details = [self._username, self._password]

        with open('scripts/system/login_details.txt', 'rb') as f:
            my_list = pickle.load(f)
        
        for i in my_list:
            if i[0] == login_details[0] and i[1] == login_details[1]:
                return i
            
    def display_signup(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        font = pygame.font.Font('freesansbold.ttf', int(screen_height*0.1))

        username_rect = pygame.Rect(0,0,screen_width*0.5, screen_height*0.1)
        username_rect.center = (screen_width*0.5, screen_height*0.1)
        password_rect = pygame.Rect(0,0,screen_width*0.5, screen_height*0.1)
        password_rect.center = (screen_width*0.5, screen_height*0.3)

        button_text = font.render('Sign Up', True, (0,0,0))
        button_rect = button_text.get_rect()
        button_rect.center = (screen_width*0.5, screen_height*0.5)

        active = 0

        user_text = ['Username','Password']

        while True:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if username_rect.collidepoint(event.pos):
                        active = 1
                    elif password_rect.collidepoint(event.pos):
                        active = 2
                    elif button_rect.collidepoint(event.pos):
                        self.save_details(user_text[0], user_text[1])
                        return 
                    else:
                        active = 0

                if event.type == pygame.KEYDOWN and active != 0:
                    if event.key == pygame.K_BACKSPACE:
                        user_text[active-1] = user_text[active-1][:-1]
                    else:
                        user_text[active-1] += event.unicode

            pygame.draw.rect(self.screen, (255,255,255), username_rect)
            pygame.draw.rect(self.screen, (255,255,255), password_rect)
            pygame.draw.rect(self.screen, (255,255,255), button_rect)

            username_text = font.render(user_text[0], True, (0,0,0))
            password_text = font.render(user_text[1], True, (0,0,0))

            self.screen.blit(username_text, username_rect)
            self.screen.blit(password_text, password_rect)
            self.screen.blit(button_text, button_rect)

            pygame.display.flip()

    def save_details(self, username, password):
        with open('scripts/system/login_details.txt', 'rb') as f:
            my_list = pickle.load(f)
        my_list.append([username, password, 0])
        with open('scripts/system/login_details.txt', 'wb') as f:
            pickle.dump(my_list, f)

    def save_score(self, user):
        