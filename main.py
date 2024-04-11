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

run = True
while run:
  pygame.time.delay(timestep)

  # TODO scroll background — shift consumable left by a number of pixels

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  mouseheight = pygame.mouse.get_pos()[1]
  movement = snake_height - mouseheight
  # keys = pygame.key.get_pressed()
  # if keys[pygame.K_RIGHT]:
  #   snake.steer(Direction.RIGHT)
  if movement > 0:
    snake.steer(Direction.UP)
  elif movement < 0:
    snake.steer(Direction.DOWN)
  elif snake_height == mouseheight:
    snake.stop()

  snake_height = snake.body[0][1]

  snake.move()
  consumable.spawn()

  # TODO check for consumables — consumables themselves should have collision check, because they know which one they are, whereas snake doesn't
  if consumable.is_collided_with(snake):
      if consumable.effect == 'increase multiplier':
          multiplier += 0.1
      elif consumable.effect == 'decrease multiplier':
          multiplier -= 0.1
      else:
          pass

  if snake.check_bounds() == True:
    text = font.render('You Died', True, (255,255,255))
    window.blit(text, (20,120))
    pygame.display.update()
    pygame.time.delay(1000)
    consumable.spawn()

  window.fill((0,0,0))
  snake.draw(pygame, window)
  window.load
  consumable.draw(pygame, window)
  snake_face = pygame.image.load('snake_pngs/snake.png')
  window.blit(snake_face, (200,200))

  pygame.display.update()
