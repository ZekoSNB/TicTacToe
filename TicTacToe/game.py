 #* Importing libraries that are used in this game
import pygame,json
from TicTacToe.mouse import Mouse
from TicTacToe.render import Rendering


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
        #* This indicates whether the square is empty or there is X or O
        #* E = Empty | 
        self.grid_index = ['E','E','E','E','E','E','E','E','E']
        #* Who's turn it is | 0 = X| 1 = O| 
        self.turn = 0
        self.render = Rendering(self.data["WIDTH"],self.data["HEIGHT"], self.screen)
    
    #* Event functions that checks for keyboard presses and manipulation with the game
    def events(self):
        for event in pygame.event.get():

            #* Checks if the close button is pressed
            if event.type == pygame.QUIT:
                self.quit = True

            #* Checks if the keyboard is pressed and which key to call function/change variable
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True

            #* If the mouse button is pressed (any button) the function will find which square it is located 
            if event.type == pygame.MOUSEBUTTONDOWN:
                box = self.mouse.triggered(pygame.mouse.get_pos())
                if self.turn%2 == 0 and self.grid_index[box] == 'E':
                    self.grid_index[box] = 'X'
                elif self.turn%2 == 1 and self.grid_index[box] == 'E':
                    self.grid_index[box] = 'O'
                else:
                    pass
                self.turn += 1
                pass
                
    
    def Loop(self):
        while not self.quit:
            self.events()
            self.render.drawGrid()
            self.render.render_grid(self.grid_index)
            pygame.display.flip()
                
                    




    