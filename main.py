import pygame
from snake import *
from food import Food


pygame.init()
height = 600
width = 800
bounds = (width, height)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Septic Shock")

block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
font = pygame.font.SysFont('comicsans',60, True)


snake_height_origin = height/2
snake_height = snake_height_origin

run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  mouseheight = pygame.mouse.get_pos()[1]
  movement = snake_height - mouseheight
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif movement > 0:
    snake.steer(Direction.UP)
  elif movement < 0:
    snake.steer(Direction.DOWN)
  elif snake_height == mouseheight:
    snake.steer(Direction.RIGHT)
    
  snake.move()
  snake.check_for_food(food)
  
  snake_height = snake.body[0][1]
  
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
  pygame.display.update()