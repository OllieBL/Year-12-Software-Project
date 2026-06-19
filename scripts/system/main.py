import pygame
import menu


pygame.init()

size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode(size[0])

menu1 = menu.Menu(screen)

menu1.display_menu()