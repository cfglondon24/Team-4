import pygame
import random

class Consumable:
    block_size = None
    color = (0,255,0)
    x = 0;
    y = 0;
    bounds = None
    blocks_in_x = None;
    blocks_in_y = None;
    effect = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.blocks_in_x = int(self.bounds[0]/self.block_size);
        self.blocks_in_y = int(self.bounds[1]/self.block_size);

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))

    def spawn(self):
        effect = 'increase multiplier' if random.choice([True, False]) else 'decrease multiplier'
        self.x = random.randint(0, self.blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, self.blocks_in_y - 1) * self.block_size

    def is_collided_with(self, sprite):
        rect_consumable = pygame.Rect(left=self.x, top=self.y, width=self.blocks_in_x, height=self.blocks_in_y)
        return self.rect.colliderect(sprite.rect)

    def scroll(self):
        self.x -= blocks_in_x

    # TODO hardcore different effects here (default: increasing multiplier)
