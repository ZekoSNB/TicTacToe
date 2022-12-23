import pygame


class Rendering:
    def __init__(self, width, height,screen) -> None:
        self.WIDTH,self.HEIGHT = width,height
        self.screen = screen
        self.spfont = pygame.freetype.Font('assets/fonts/oldfont.ttf', 32)

    
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

    def render_win(self,pos_wi,i):
        #TODO Menu
        triggers_on = [[0,0,300,300],[300,0,600,300],[600,0,900,300],[0,300,300,600],[300,300,600,600],[600,300,900,600],[0,600,300,900],[300,600,600,900],[600,600,900,900]]

        for j,item in enumerate(pos_wi):
            if item == i and j <= 2:
                start_xy = (triggers_on[i[0]-1][0],triggers_on[i[0]-1][1]+150)
                end_xy = (triggers_on[i[2]-1][2],triggers_on[i[2]-1][3]-150)
            elif item == i and j >= 3 and j <= 5:
                start_xy = (triggers_on[i[0]-1][0]+150,triggers_on[i[0]-1][1])
                end_xy = (triggers_on[i[2]-1][2]-150,triggers_on[i[2]-1][3])
            elif item == i and j > 5:
                start_xy = (triggers_on[i[0]-1][0],triggers_on[i[0]-1][1])
                end_xy = (triggers_on[i[2]-1][2],triggers_on[i[2]-1][3])
        pygame.draw.line(self.screen, (0,255,255),start_xy, end_xy , 15)

    def render_text(self,x,y,text,color):
        #* Rendering any text 
        self.spfont.render_to(self.screen, (x,y), text, color)
 