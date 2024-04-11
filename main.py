import pygame
from snake import *
from food import Food
from time import sleep
import pygame_menu
from pygame_menu import themes
import webbrowser

def main():
  pygame.init()
  bounds = (800,600)
  window = pygame.display.set_mode(bounds)
  pygame.display.set_caption("Snake")
  snake1Image = pygame.image.load("snake_pngs\snake.png").convert_alpha()
  snake1Image = pygame.transform.scale(snake1Image , (200,100))
  block_size = 20
  snake = Snake(block_size, bounds)
  food = Food(block_size,bounds)
  font = pygame.font.SysFont('comicsans',60, True)

  run = True
  while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
      snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
      snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
      snake.steer(Direction.DOWN)
      
    snake.move()
    snake.check_for_food(food)

    if snake.check_bounds() == True or snake.check_tail_collision() == True:
      text = font.render('Game Over', True, (255,255,255))
      window.blit(text, (20,120))
      pygame.display.update()
      pygame.time.delay(1000)
      snake.respawn()
      food.respawn()

    window.fill((0,0,0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
    window.blit(snake1Image,(snake.body[0][0],snake.body[0][1]), (0,0,200,200))
    pygame.display.update()
 
pygame.init()
surface = pygame.display.set_mode((800, 600))
 
def open_web():
    webbrowser.open("https://sepsistrust.org/")
 
def start_the_game():
    main()
 
 
 
mainmenu = pygame_menu.Menu('Welcome to Septic Shock', 600, 400, theme=themes.THEME_ORANGE)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Education', open_web)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

 
mainmenu.mainloop(surface)

