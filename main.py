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

  # mouseheight = pygame.mouse.get_pos()[1]
  # movement = snake_height - mouseheight
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.LEFT]:
    snake.steer(Direction.LEFt)
  elif keys[pygame.UP]:
    snake.steer(Direction.UP)  
  elif keys[pygame.DOWN]:
    snake.steer(Direction.DOWN)

  # elif movement > 0:
  #   snake.steer(Direction.UP)
  # elif movement < 0:
    # snake.steer(Direction.DOWN)
  # elif snake_height == mouseheight:
  #   snake.steer(Direction.RIGHT)
    
  snake.move()
  snake.check_for_food(food)
  
  snake_height = snake.body[0][1]

  if snake.check_bounds() == True :
    text = font.render('Game Over', True, (255,255,255))
    window.blit(text, (20,120))
    pygame.display.update()
    pygame.time.delay(1000)
    snake.respawn()

    window.fill((0,0,0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
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

