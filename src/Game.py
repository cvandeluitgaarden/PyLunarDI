import pygame
from sys import exit
import numpy
from Grid import Grid

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Cell')
clock = pygame.time.Clock()

grid = Grid(screen,10)
grid.insert(grid.gun, 5, 5)
grid.insert(grid.gun,100,50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid.add(5)

    grid.draw()

    pygame.display.update()
    clock.tick(10)


