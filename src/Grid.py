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

        self.glider = [[0,1,0],[0,0,1], [1,1,1]]
        self.gun = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1]]
        

    def makegrid(self, x:int, y:int):
        grid = numpy.random.randint(0, 1, size=(x, y))

        
        # x = 10
        # grid[x +0][x +4] = 1
        # grid[x +0][x +5] = 1
        # grid[x +1][x +4] = 1
        # grid[x +1][x +5] = 1


        # grid[x +10][x +4] = 1
        # grid[x +10][x +5] = 1
        # grid[x +10][x +6] = 1

        # grid[x +11][x +3] = 1
        # grid[x +11][x +7] = 1

        # grid[x +12][x +2] = 1
        # grid[x +12][x +8] = 1

        # grid[x +13][x +2] = 1
        # grid[x +13][x +8] = 1

        # grid[x +14][x +5] = 1

        # grid[x +15][x +3] = 1
        # grid[x +15][x +7] = 1

        # grid[x +16][x +4] = 1
        # grid[x +16][x +5] = 1
        # grid[x +16][x +6] = 1

        # grid[x +17][x +5] = 1

        # grid[x +20][x +2] = 1
        # grid[x +20][x +3] = 1
        # grid[x +20][x +4] = 1

        # grid[x +21][x +2] = 1
        # grid[x +21][x +3] = 1
        # grid[x +21][x +4] = 1

        # grid[x +22][x +1] = 1
        # grid[x +22][x +5] = 1

        # grid[x +24][x +0] = 1
        # grid[x +24][x +1] = 1
        # grid[x +24][x +6] = 1
        # grid[x +24][x +7] = 1

        # grid[x +34][x +2] = 1
        # grid[x +34][x +3] = 1

        # grid[x +35][x +2] = 1
        # grid[x +35][x +3] = 1
        

        return grid
    
    def insert(self, arr, col, row):
        rows = len(arr)
        for i in range(rows):
            cols = len(arr[i])
            for j in range(cols):
                self.grid[i + col][j + row] = arr[i][j]
    
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

    def add(self, prc):
        for i in range(int(self.cols * self.rows * (prc / 100))):
            x = numpy.random.randint(0, self.cols)
            y = numpy.random.randint(0, self.rows)
            self.grid[x][y] = 1

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
                pygame.draw.rect(self.screen, WHITE, [x * self.resolution, y * self.resolution, self.resolution - 1, self.resolution - 1], border_radius=5)
            else:
                pygame.draw.rect(self.screen, BLACK, [x * self.resolution, y * self.resolution, self.resolution - 1, self.resolution - 1], border_radius= 5)


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
