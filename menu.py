from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import webbrowser


 
pygame.init()
surface = pygame.display.set_mode((800, 600))
 
def open_web():
    webbrowser.open("https://sepsistrust.org/")
 
def start_the_game():
    pass
 
 
 
mainmenu = pygame_menu.Menu('Welcome to Septic Shock', 600, 400, theme=themes.THEME_ORANGE)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Education', open_web)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

 
mainmenu.mainloop(surface)