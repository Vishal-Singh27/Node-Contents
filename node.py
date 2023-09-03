class Node():
    def __init__(self):
        self.back = None
        self.content = None
        self.ahead = None
        
    def create_node(self):
        self.ahead = Node()
        (self.ahead).back = self.ahead
    
    def go_back(self):
        self = self.back
    
    def go_ahead(self):
        self = self.ahead
    
    def startpoint(self):
        tmp = self
        while not tmp.back:
            tmp = self.back
        return tmp