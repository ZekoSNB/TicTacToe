 #* Importing libraries that are used in this game
import pygame,json
from TicTacToe.mouse import Mouse


 #* Main game class containing main loop for the game
class Game:
    #* initializing all variables used in the game (There might be additional in other fiels)
    def __init__(self) -> None:
        pygame.init()
        #* Opening settings to set window size and framerate
        with open('settings.json') as f:
            self.data = json.load(f)
            f.close()
        #* Setting window size from 'settings.json'
        self.screen = pygame.display.set_mode((self.data["WIDTH"], self.data["HEIGHT"]))
        self.quit = False
        self.mouse = Mouse()
    
    #* Event functions that checks for keyboard presses and manipulation with the game
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.triggered(pygame.mouse.get_pos())
                
    
    def Loop(self):
        while not self.quit:
            self.events()
            pygame.display.flip()
                
                    




    