

class Mouse():
    def __init__(self) -> None:
        super().__init__()
    
    def triggered(self,pos):
        self.mx,self.my = pos
        print(self.mx)
        
