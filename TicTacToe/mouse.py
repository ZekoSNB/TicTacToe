import pygame

class Mouse():
    def __init__(self, screen, game) -> None:
        super().__init__()
        self.screen = screen
        self.game = game
    
    def triggered(self):
        self.mx,self.my = pygame.mouse.get_pos()
        trigers_on = [[0,0,300,300],[300,0,600,300],[600,0,900,300],[0,300,300,600],[300,300,600,600],[600,300,900,600],[0,600,300,900],[300,600,600,900],[600,600,900,900]]
        for i,item in enumerate(trigers_on):
            if self.mx > item[0] and self.mx < item[2] and self.my > item[1] and self.my < item[3]:
                return i

    def hover_on(self, x,y, width, height):
        # pygame.draw.line(self.screen,(255,0,0,),(x,y), (x+width, y+height), 4)
        mx,my = pygame.mouse.get_pos()

        in_x = mx >= x and mx <= x+width
        in_y = my >= y and my <= y+height

        if in_x and in_y:
            return True
        else:
            return False
