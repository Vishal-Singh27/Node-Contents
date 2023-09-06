class Node:
    # Initializing the node
    def __init__(self):
        self.back = None
        self.content = None
        self.start = self
        
    # Instance method that makes a next node
    def create_nextnode(self):
        self.ahead = Node()
        (self.ahead).back = self
        (self.ahead).start = self.startpoint()
        
    # Returns startpoint of the node
    def startpoint(self):
        while self.back != None:
            self = self.back
        return self
    
    # If someone tries to print self, it prints the content
    def __str__(self):
        return str(self.content)
    
    
def main():
    # Testing our node initialization
    node = Node()
    node.content = "Vishal"
    
    # Testing create_nextnode
    node.create_nextnode()
    
    # Going to next node
    node = node.ahead
    node.content = "Rahul"
    
    # Printing current node's content
    print(node.start)
    

if __name__ == "__main__":
    main()