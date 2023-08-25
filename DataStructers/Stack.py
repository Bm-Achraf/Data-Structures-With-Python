from Nodes.Node import Node

class Stack:
    def __init__(self):
        self.node = Node()

    def Push(self,data):
        if(self.node is None):
            self.node = Node(data, Next=None)
            return
        
        self.node = Node(data, self.node)

    def Pop(self):
        pointer = self.node
        self.node = pointer.Next

        result = pointer.Data
        return result
    
    def display(self):
        pointer = self.node

        while pointer.Next is not None:
            print(pointer.Data)
            pointer = pointer.Next