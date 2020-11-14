import pygame
import sys


class Grid:
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)

    def __init__(self, height, width):
        self.height = height
        self.width = width
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        self.clock = pygame.time.Clock()
        self.screen.fill(self.BLACK)
        self.draw_grid(height, width)

    def draw_grid(self, height, width):
        block_size = 20  # Set the size of the grid block
        for x in range(width):
            for y in range(height):
                rect = pygame.Rect(x * block_size, y * block_size,
                                   block_size, block_size)
                pygame.draw.rect(self.screen, self.WHITE, rect, 1)

    def run(self):
        while True:
            self.draw_grid(self.height, self.width)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
