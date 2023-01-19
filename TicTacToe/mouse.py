import pygame

class Mouse():
    def __init__(self, screen) -> None:
        super().__init__()
        self.screen = screen
    
    def triggered(self,pos):
        self.mx,self.my = pos
        trigers_on = [[0,0,300,300],[300,0,600,300],[600,0,900,300],[0,300,300,600],[300,300,600,600],[600,300,900,600],[0,600,300,900],[300,600,600,900],[600,600,900,900]]
        for i,item in enumerate(trigers_on):
            if self.mx > item[0] and self.mx < item[2] and self.my > item[1] and self.my < item[3]:
                return i
    def hover_on(self, width,height):
        pygame.draw.line(self.screen,(255,255,255,),((width/2+64),(height/2-30),), ((width/2+64+32*7.2),(height/2-30)), 4)
        