from Nodes.Node import Node

class Stack:
    def __init__(self):
        self.node = Node()

    def Push(self,data)->None:
        if(self.node is None):
            self.node = Node(data, Next=None)
            return
        
        self.node = Node(data, self.node)

    def Pop(self):
        pointer = self.node
        self.node = pointer.Next

        result = pointer.Data
        return result
    
    def __len__(self)->int:
        pointer = self.node

        count = 0
        while pointer.Next is not None:
            count += 1
            pointer = pointer.Next

        return count


    def __str__(self):
        pointer = self.node

        listStr = " ---\n"
        while pointer.Next.Next is not None:
            #print(pointer.Data)
            listStr += "| "+str(pointer.Data)+" |\n ---\n"
            pointer = pointer.Next
        
        listStr += f"| {pointer.Data} |\n ---"

        return listStr