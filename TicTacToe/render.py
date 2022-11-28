import pygame


class Rendering:
    def __init__(self, width, height,screen) -> None:
        self.WIDTH,self.HEIGHT = width,height
        self.screen = screen
    
    def drawGrid(self):
        blockSize = 300 #* Set the size of the grid block
        for x in range(0, self.WIDTH , blockSize):
            for y in range(0, self.HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, (255,255,255), rect, 1)
    
    def render_grid(self, grid):
        trigers_on = [[0,0,300,300],[300,0,600,300],[600,0,900,300],[0,300,300,600],[300,300,600,600],[600,300,900,600],[0,600,300,900],[300,600,600,900],[600,600,900,900]]
        for i,item in enumerate(grid):
            if item == 'X':
                pygame.draw.aaline(self.screen,(255,255,255), (trigers_on[i][0]+10,trigers_on[i][1]+10), (trigers_on[i][2]-10,trigers_on[i][3]-10), 20)
                pygame.draw.aaline(self.screen,(255,255,255), (trigers_on[i][2]-10,trigers_on[i][1]+10), (trigers_on[i][0]+10,trigers_on[i][3]-10), 20)
            if item == 'O':
                pygame.draw.circle(self.screen, (255,255,255),((trigers_on[i][0]+trigers_on[i][2])/2, (trigers_on[i][1]+trigers_on[i][3])/2),140, 3)