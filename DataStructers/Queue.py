from Nodes.Node import Node

class Queue:

    def __init__(self) -> None:
        self.node = Node()

    def isEmpty(self):
        if self.node is None:
            return True
        
        return False
    

    
    def EnQueue(self,data):
        self.node = Node(data, self.node)

    def DeQueue(self):

        if self.node.Next is None:
            result = self.node
            self.node = None
            return result
        
        pointer = self.node

        while pointer.Next.Next is not None:
            pointer = pointer.Next

        result = pointer
        pointer.Next = None

        return result
    

    def __len__(self):
        pointer = self.node

        count = 0
        while pointer.Next is not None:
            count += 1
            pointer = pointer.Next

        return count

    
    def __str__(self):
        pointer = self.node

        listStr = ""

        while pointer.Next is not None:
            listStr += " | "+str(pointer.Data)
            pointer = pointer.Next
        
        listStr += " |"

        return listStr