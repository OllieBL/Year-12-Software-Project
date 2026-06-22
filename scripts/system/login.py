import pygame
import pickle

class Login:
    def __init__(self, screen):
        self._username = ''
        self._password = ''
        self.screen = screen


    def display_login(self):

        '''screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        while True:
            self.screen.fill((0,0,0))'''
        
        self._username = input('Username: ')
        self._password = input('Password: ')

        login_details = [self._username, self._password]

        with open('scripts/system/login_details.txt', 'rb') as f:
            my_list = pickle.load(f)
        
        for i in my_list:
            if i[0] == login_details[0] and i[1] == login_details[1]:
                print('Login Successful: ', i[0], i[1])
                return


'''
with open('scripts/system/login_details.txt', 'wb') as f:
    pickle.dump([['','',0]], f)


login0 = Login(0)

login0.display_login()'''