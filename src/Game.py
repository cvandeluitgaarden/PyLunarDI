import pygame
from sys import exit
import numpy
from Grid import Grid

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Cell')
clock = pygame.time.Clock()

grid = Grid(screen,20)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    grid.draw()

    pygame.display.update()
    clock.tick(10)


