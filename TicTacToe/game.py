import pygame,json,pathlib

class Game:
    def __init__(self) -> None:
        pygame.init()
        with open('settings.json') as f:
            self.data = json.load(f)
            f.close()
        self.screen = pygame.display.set_mode((self.data["WIDTH"], self.data["HEIGHT"]))
        self.quit = False
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
    
    def Loop(self):
        while not self.quit:
            self.events()
            pygame.display.flip()
                
                    




    