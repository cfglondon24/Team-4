import pygame
from snake import *
from consumable import Consumable
from time import sleep
import pygame_menu
from pygame_menu import themes
import webbrowser

def main():
  pygame.init()
  bounds = (800,600)
  window = pygame.display.set_mode(bounds)
  pygame.display.set_caption("Septic Shock")
  snake1Image = pygame.image.load("snake_pngs\snake.png").convert_alpha()
  snake1Image = pygame.transform.scale(snake1Image , (200,100))
  block_size = 20
  snake = Snake(block_size, bounds)
  consumable = Consumable(block_size,bounds)
  font = pygame.font.SysFont('comicsans',60, True)
  timestep = 100
  multiplier = 1
  consumable_exists = True

  run = True
  while run:
    pygame.time.delay(timestep)

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

    head = snake.body[-1]

    if head[0] < 0 or (head[0] < 2 and snake.direction == Direction.LEFT):
      snake.direction = Direction.RIGHT
    elif head[0] > bounds[0] or (head[0] > bounds[0] - 2 and snake.direction == Direction.RIGHT):
      snake.direction = Direction.LEFT

    if head[1] < 0 or (head[1] < 2 and snake.direction == Direction.UP):
      snake.direction = Direction.DOWN
    elif head[1] > bounds[1] or (head[1] > bounds[1] - 2 and snake.direction == Direction.DOWN):
      snake.direction = Direction.UP

    if not consumable_exists:
      consumable.spawn()
      consumable_exists = True

    snake_height = snake.body[1][1]

    # TODO check for consumables — consumables themselves should have collision check, because they know which one they are, whereas snake doesn't

    if head[0] == consumable.x and head[1] == consumable.y:
      consumable_exists = False
      if consumable.effect == 'increase multiplier':
        multiplier += 0.1
      elif consumable.effect == 'decrease multiplier':
        multiplier -= 0.1

    window.fill((0,0,0))
    snake.draw(pygame, window)
    consumable.draw(pygame, window)
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
