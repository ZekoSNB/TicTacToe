import pygame

class Mouse():
    def __init__(self, screen, game) -> None:
        """
        Initialize the Mouse class.

        Args:
            screen: The screen object.
            game: The game object.
        """
        super().__init__()
        self.screen = screen
        self.game = game
    
    def triggered(self) -> int:
        """
        This function checks if the mouse click is within a specific area and returns the index of the area.

        """
        self.mx, self.my = pygame.mouse.get_pos()
        trigers_on = [[0, 0, 300, 300], [300, 0, 600, 300], [600, 0, 900, 300], [0, 300, 300, 600], [300, 300, 600, 600], [600, 300, 900, 600], [0, 600, 300, 900], [300, 600, 600, 900], [600, 600, 900, 900]]
        for i, item in enumerate(trigers_on):
            if self.mx > item[0] and self.mx < item[2] and self.my > item[1] and self.my < item[3]:
                return i

    def hover_on(self, x,y, width, height) -> bool:
        # Gets the position of the mouse
        mx,my = pygame.mouse.get_pos()

        # Checks if the mouse is within the bounds of the button
        inside_button = mx >= x and mx <= x+width and my >= y and my <= y+height 

        return inside_button
