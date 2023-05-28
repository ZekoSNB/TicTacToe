 #* Importing libraries that are used in this game
import pygame,json
from TicTacToe.mouse import Mouse
from TicTacToe.render import Rendering
import random


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
        self.win = False
        self.inmenu = True
        self.start = True 
        self.win_state = [[1,2,3],[4,5,6],[7,8,9], [1,4,7], [2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.mouse = Mouse(self.screen, self)
        #* This indicates whether the square is empty or there is X or O
        #* E = Empty | 
        self.grid_index = ['E','E','E','E','E','E','E','E','E']
        #* Who's turn it is | 0 = X| 1 = O| 
        self.turn = 0
        self.but_ind = 2
        self.pos_i = None
        self.player_state = 0
        self.render = Rendering(self.data["WIDTH"],self.data["HEIGHT"], self.screen)
        
    
    #* Resets data to default for a new game, but the game score is saved
    def restart(self):
        self.grid_index = ['E','E','E','E','E','E','E','E','E']
        self.win = False

    #* Iterates through loop and checks and checks for the same positions
    def check_win(self):
        win_state = [[1,2,3],[4,5,6],[7,8,9], [1,4,7], [2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in self.win_state:
            
            if self.grid_index[i[0]-1] == self.grid_index[i[1]-1] and self.grid_index[i[1]-1] == self.grid_index[i[2]-1] and self.grid_index[i[0]-1] != 'E':
                self.win = True
                self.pos_i = i

    #* Event functions that checks for keyboard presses and manipulation with the game
    def events(self):
        
        if not self.win and not self.inmenu and self.player_state == 1 and self.turn%2 == 1:
            randomint = random.randint(0,8)
            if self.grid_index[randomint] == 'E':
                    self.grid_index[randomint] = 'O'
                    self.turn += 1
        else:
            pass
        
        for event in pygame.event.get():
            
            #* Checks if the close button is pressed
            if event.type == pygame.QUIT:
                self.quit = True

            #* Checks if the keyboard is pressed and which key to call function/change variable
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    self.restart()

                if event.key == pygame.K_ESCAPE:
                    self.quit = True

            #* If the mouse button is pressed (any button) the function will find which square it is located 
            if event.type == pygame.MOUSEBUTTONDOWN and not self.win and not self.inmenu and self.player_state == 1:
                box = self.mouse.triggered()
                

                if self.turn%2 == 0 and self.grid_index[box] == 'E':
                    self.grid_index[box] = 'X'
                    self.turn += 1

                else:
                    pass
           # Checks when mouse is pressed and if the game is being played and whethre the player is playing one or two player game 
            if event.type == pygame.MOUSEBUTTONDOWN and not self.win and not self.inmenu and self.player_state == 2:
                box = self.mouse.triggered()
                

                if self.turn%2 == 0 and self.grid_index[box] == 'E':
                    self.grid_index[box] = 'X'
                    self.turn += 1
                elif self.turn%2 == 1 and self.grid_index[box] == 'E':
                    self.grid_index[box] = 'O'
                    self.turn += 1
                else:
                    pass 
                # Checks if the game is won by player X || O and draws line across the winning combination
                self.check_win()

            if event.type == pygame.MOUSEBUTTONDOWN and self.start and self.inmenu:
                if self.but_ind == 0:
                    self.start = False
                    self.inmenu = False
                    self.player_state = 1
                    self.one_player_loop()

                if self.but_ind == 1:
                    self.start = False
                    self.inmenu = False
                    self.player_state = 2
                    self.two_player_loop()
                
    def start_loop(self):
        text_1_col = (255,255,255)
        text_2_col = (255,255,255)

        
        while not self.quit:
            self.events()

            if self.mouse.hover_on(self.data["WIDTH"] / 4 - 64, self.data["HEIGHT"] / 2, 200, 25):
                self.but_ind = 0
                text_1_col = (200,200,200)

            elif self.mouse.hover_on(self.data["WIDTH"]/ 2 + 64, self.data["HEIGHT"] / 2, 240, 25):
                self.but_ind = 1
                text_2_col = (200,200,200)

            else:
                self.but_ind = 2
                text_2_col = (255,255,255)
                text_1_col = (255,255,255) 

            #* Button one for one player but_ind - 0
            self.render.render_text((self.data["WIDTH"]/4-64), (self.data["HEIGHT"]/2), 'ONE PLAYER', text_1_col,32)
                
            #* Button two for two player but_ind - 1
            self.render.render_text((self.data["WIDTH"]/2+64),self.data["HEIGHT"]/2, 'TWO PLAYERS', text_2_col,32)

            self.render.render_text((self.data["WIDTH"]/4+10  ),self.data["HEIGHT"]/6,'TIC TAC TOE', (255,255,255),64)
            pygame.display.flip()

    def two_player_loop(self):
        while not self.quit:
            self.screen.fill((0,0,0))
            if self.win:
                self.render.render_win(self.win_state,self.pos_i)

            self.events()
            #* Draws a grid to show places to put X or O
            self.render.drawGrid()
            #* Renders players X or O
            self.render.render_grid(self.grid_index)
            pygame.display.update()
    
    def one_player_loop(self):
        while not self.quit:
            self.screen.fill((0,0,0))
            if self.win:
                self.render.render_win(self.win_state,self.pos_i)

            self.events()
            #* Draws a grid to show places to put X or O
            self.render.drawGrid()
            #* Renders players X or O
            self.render.render_grid(self.grid_index)
            self.check_win()
            pygame.display.update()
                
            
