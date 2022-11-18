import pygame


class Main():
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 600,900
        self.quit = False
        self.line_pos_start = [(200, 0), (400,0), (0,200), (0,400), (0,600)] 
        self.line_pos_end = [(200,600),(400,600),(600,200),(600,400),(600,600)]
        pygame.display.set_caption('TicTacToe')
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    def fevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
    def event(self):
        pass
    def line(self):
        for i,item in enumerate(self.line_pos_start):
            pygame.draw.line(self.screen, (255,255,255),item, self.line_pos_end[i], 3)
            

            




class Game(Main):
    def __init__(self) -> None:
        super().__init__()



    def run(self):
        while not self.quit:
            self.fevent()
            self.line()
            pygame.display.update()
            


Game().run()