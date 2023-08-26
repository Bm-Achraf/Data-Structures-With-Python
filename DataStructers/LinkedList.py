from Nodes.Node import Node

class LinkedList:

    def __init__(self):
        self.node = Node()





    def AddLast(self, data):

        if(self.node.Data is None):
            self.node.Data = data
            self.node.Next = None
            return
        
        pointer = self.node

        while(pointer.Next != None):
            pointer = pointer.Next
        
        pointer.Next = Node(data, Next=None)






    def Init(self, *args):
        for i in args:
            self.AddLast(i)






    def AddFirst(self, data):
        self.node = Node(data, Next=self.node)






    def InsertAfter(self, target, data):
        pointer = self.node

        while(pointer.Data != target):
            pointer = pointer.Next
        

        if(pointer.Next == None):
            pointer.Next = Node(data,None)
            return

        pointer.Next = Node(data, pointer.Next)
        return
          





    def InsertBefore(self, target, data):
        pointer = self.node
        prepointer = self.node

        while(pointer.Data != target):
            prepointer = pointer
            pointer = pointer.Next

        prepointer.Next = Node(data, pointer)        




    def RemoveLast(self):
        pointer = self.node

        while(pointer.Next.Next != None):
            pointer = pointer.Next

        pointer.Next = None
        


    def RemoveFirst(self):
        if(self.node.Next is not None):
            self.node = self.node.Next
            return
        
        self.node = None
        



    def RemoveNth(self, data):
        pointer = self.node
        prepointer = self.node

        if(pointer.Data == data):
            if(pointer.Next is not None):
                self.node = self.node.Next
            else:
                self.node = None

            return

        while(pointer.Data != data):
            prepointer = pointer
            pointer = pointer.Next  

        if(pointer.Next is not None):
            prepointer.Next = pointer.Next
        else:
            prepointer.Next = None
            


    def Clear(self):
        self.node = None

    def __len__(self):
        pointer = self.node
        count = 0
        while pointer.Next is not None:
            count += 1
            pointer = pointer.Next

        return count



    def __str__(self):
        pointer = self.node

        listStr = "[ "

        while pointer.Next is not None:
            listStr += str(pointer.Data)+", "
            pointer = pointer.Next
        
        listStr += f"{pointer.Data} ]"
        return listStr