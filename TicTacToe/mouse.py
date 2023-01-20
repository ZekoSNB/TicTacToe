import pygame

class Mouse():
    def __init__(self, screen) -> None:
        super().__init__()
        self.screen = screen
    
    def triggered(self):
        mx,my = pygame.mouse.get_pos()
        trigers_on = [[0,0,300,300],[300,0,600,300],[600,0,900,300],[0,300,300,600],[300,300,600,600],[600,300,900,600],[0,600,300,900],[300,600,600,900],[600,600,900,900]]
        for i,item in enumerate(trigers_on):
            if mx > item[0] and mx < item[2] and my > item[1] and my < item[3]:
                return i
    def Clicks_on(self, width,height):
        mx,my = pygame.mouse.get_pos()
        pygame.draw.line(self.screen,(255,255,255,),((width/2+64),(height/2-30),), ((width/2+64+32*7.2),(height/2-30)), 4)
        

        