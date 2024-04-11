import pygame
from snake import *
from consumable import Consumable


pygame.init()
width = 800
height = 600
bounds = (width, height)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Septic Shock")

block_size = 20
snake = Snake(block_size, bounds)
consumable = Consumable(block_size,bounds)
font = pygame.font.SysFont('comicsans',60, True)
timestep = 100
multiplier = 1
snake_height_origin = height/2
snake_height = snake_height_origin
consumable_exists = True
snake_touching_edge = False

run = True
while run:
  print(snake.direction)

  pygame.time.delay(timestep)

  # TODO scroll background — shift consumable left by a number of pixels

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

  head = snake.body[-1]

  if head[0] < 0 or (head[0] < 2 and snake.direction == Direction.LEFT):
    snake.direction = Direction.RIGHT
  elif head[0] > bounds[0] or (head[0] > bounds[0] - 2 and snake.direction == Direction.RIGHT):
    snake.direction = Direction.LEFT

  if head[1] < 0 or (head[1] < 2 and snake.direction == Direction.UP):
    snake.direction = Direction.DOWN
  elif head[1] > bounds[1] or (head[1] > bounds[1] - 2 and snake.direction == Direction.DOWN):
    snake.direction = Direction.UP

  snake.move()

  if not consumable_exists:
    consumable.spawn()
    consumable_exists = True

  '''
  mouseheight = pygame.mouse.get_pos()[1]
  movement = snake_height - mouseheight

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif movement > 0:
    snake.steer(Direction.UP)
  elif movement < 0:
    snake.steer(Direction.DOWN)
  elif snake_height == mouseheight:
    snake.stop()
  '''

  snake_height = snake.body[1][1]

  # TODO check for consumables — consumables themselves should have collision check, because they know which one they are, whereas snake doesn't

  if head[0] == consumable.width and head[1] == consumable.height:
    consumable_exists = False

    if consumable.effect == 'increase multiplier':
      multiplier += 0.1
    elif consumable.effect == 'decrease multiplier':
      multiplier -= 0.1
    else:
      pass

  if snake.check_bounds() == True:
    snake_touching_edge = True
    text = font.render('You Died', True, (255,255,255))
    window.blit(text, (20,120))

  window.fill((0,0,0))
  snake.draw(pygame, window)
  consumable.draw(pygame, window)
  pygame.display.update()
