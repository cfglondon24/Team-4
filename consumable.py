import pygame
import random

class Consumable:
    block_size = None
    color = (0,255,0)
    x = 0;
    y = 0;
    bounds = None
    effect = 'increase multiplier'

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.effect = effect

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))

    def spawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size;
        blocks_in_y = (self.bounds[1])/self.block_size;
        self.x = random.randint(150, blocks_in_x - 1) * self.block_size
        self.y = random.randint(150, blocks_in_y - 1) * self.block_size

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def scroll(self):
        self.x -=

    # TODO hardcore different effects here (default: increasing multiplier)
