

class Mouse():
    def __init__(self) -> None:
        super().__init__()
    
    def triggered(self,pos):
        self.mx,self.my = pos
        if self.mx >= 0 and self.mx <= 300 and self.my >= 0 and self.my <= 300:
            print("it is in the first box")
        