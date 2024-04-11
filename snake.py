from enum import Enum
import pygame

class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3


class Snake:
  length = None
  direction = None
  body = None
  block_size = None
  color = (0,0,255)
  bounds = None


  def __init__(self, block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    self.respawn()


  def respawn(self):
    self.length = 3
    self.body = [(60,300),(40,300),(20,300)]
    self.direction = Direction.RIGHT


  def draw(self, game, window):
    self.body = pygame.image.load('snakes_png/shaking_snake.png').convert_alpha()
    self.rect = self.image.get_rect()
    for segment in self.body:
      game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))


  def move(self):
    curr_head = self.body[-1]
    if self.direction == Direction.DOWN:
      next_head = (curr_head[0], curr_head[1] + self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.UP:
      next_head = (curr_head[0], curr_head[1] - self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.RIGHT:
      next_head = (curr_head[0], curr_head[1])
      self.body.append(next_head)

    if self.length < len(self.body):
      self.body.pop(0)


  def steer(self, direction):
    if self.direction == Direction.DOWN and direction != Direction.UP:
      self.direction = direction
    elif self.direction == Direction.UP and direction != Direction.DOWN:
      self.direction = direction
    elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
      self.direction = direction

  def check_bounds(self):
    head = self.body[-1]
    if head[0] >= self.bounds[0]:
      return True
    if head[1] >= self.bounds[1]:
      return True

    if head[0] < 0:
        return True
    if head[1] < 0:
        return True

    return False

  
  def stop(self):
    pass

''' don't need these 2 I think?
  def eat(self):
    # TODO apply effect of consumable

  def check_for_consumables(self, consumable):
    head = self.body[-1]
    if head[0] == consumable.x and head[1] == consumable.y:
      self.eat()
      consumable.spawn()
'''