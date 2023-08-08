import numpy
import pygame

class Grid:
    def __init__(self, screen:pygame.Surface, resolution:int):
        self.screen = screen
        self.resolution = resolution
        self.x = screen.get_width()
        self.y = screen.get_height()
        self.cols = int(self.x / resolution)
        self.rows = int(self.y / resolution)
        self.grid = self.makegrid(self.cols, self.rows)
        

    def makegrid(self, x:int, y:int):
        grid = numpy.random.randint(0, 1, size=(x, y))

        grid[0][4] = 1
        grid[0][5] = 1
        grid[1][4] = 1
        grid[1][5] = 1


        grid[10][4] = 1
        grid[10][5] = 1
        grid[10][6] = 1

        grid[11][3] = 1
        grid[11][7] = 1

        grid[12][2] = 1
        grid[12][8] = 1

        grid[13][2] = 1
        grid[13][8] = 1

        grid[14][5] = 1

        grid[15][3] = 1
        grid[15][7] = 1

        grid[16][4] = 1
        grid[16][5] = 1
        grid[16][6] = 1

        grid[17][5] = 1

        grid[20][2] = 1
        grid[20][3] = 1
        grid[20][4] = 1

        grid[21][2] = 1
        grid[21][3] = 1
        grid[21][4] = 1

        grid[22][1] = 1
        grid[22][5] = 1

        grid[24][0] = 1
        grid[24][1] = 1
        grid[24][6] = 1
        grid[24][7] = 1

        grid[34][2] = 1
        grid[34][3] = 1

        grid[35][2] = 1
        grid[35][3] = 1
        

        return grid
        
    
    def next_gen(self):
        next_grid = self.makegrid(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):

                neighbors = self.neighbors(self.grid, i, j)
                state = self.grid[i][j]

                if state == 0 and neighbors == 3:
                    next_grid[i][j] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = state
        
        return next_grid


    def diff(self, grid1, grid2):

        diff = []
        for i in range(self.cols):
            for j in range(self.rows):
                if grid1[i][j] != grid2[i][j]:
                    diff.append((i,j, grid2[i][j]))

        return diff
        
    
    def draw(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        next_gen = self.next_gen()
        diff = self.diff(self.grid, next_gen)

        for i in range(len(diff)):
            x = diff[i][0]
            y =  diff[i][1]
            state = diff[i][2]

            if state == 1:
                pygame.draw.rect(self.screen, WHITE, [x * self.resolution, y * self.resolution, self.resolution - 1, self.resolution - 1])
            else:
                pygame.draw.rect(self.screen, BLACK, [x * self.resolution, y * self.resolution, self.resolution - 1, self.resolution - 1])


        # for i in range(self.cols):
        #     for j in range(self.rows):
        #         if self.grid[i][j] == 1:
        #             pygame.draw.rect(self.screen, WHITE, [i * self.resolution, j * self.resolution, self.resolution - 1, self.resolution - 1])
        #         else:
        #             pygame.draw.rect(self.screen, BLACK, [i * self.resolution, j * self.resolution, self.resolution - 1, self.resolution - 1])

        self.grid = next_gen

    def neighbors(self, grid, x, y):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):

                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows

                sum += grid[col][row]

        sum -= grid[x][y]
        return sum
