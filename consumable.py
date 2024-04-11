import pygame
import random

class Consumable:
    block_size = None
    color = (0,255,0)
    width = 0;
    height = 0;
    bounds = None
    blocks_in_width = None;
    blocks_in_height = None;
    effect = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.blocks_in_width = int(self.bounds[0]/self.block_size);
        self.blocks_in_height = int(self.bounds[1]/self.block_size);

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.width, self.height, self.block_size, self.block_size))

    def spawn(self):
        effect = 'increase multiplier' if random.choice([True, False]) else 'decrease multiplier'
        self.width = random.randint(0, self.blocks_in_width - 1) * self.block_size
        self.height = random.randint(0, self.blocks_in_height - 1) * self.block_size

    def is_collided_with(self, sprite):
        rect_consumable = pygame.Rect(left=self.width, top=self.height, width=self.blocks_in_width, height=self.blocks_in_height)
        return self.rect.colliderect(sprite.rect)

    def scroll(self):
        self.width -= blocks_in_width

    # TODO hardcore different effects here (default: increasing multiplier)
