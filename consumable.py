import pygame
import random

class Consumable:
    block_size = None
    color = (0,255,0)
    x = 0;
    y = 0;
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
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))

    def spawn(self):
        effect = 'increase multiplier' if random.choice([True, False]) else 'decrease multiplier'
        self.x = random.randint(20, self.blocks_in_width - 1) * self.block_size
        self.y = random.randint(0, self.blocks_in_height - 1) * self.block_size

    # TODO hardcore different effects here (default: increasing multiplier)
