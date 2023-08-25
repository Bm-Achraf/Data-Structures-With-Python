from Nodes.TreeNode import TreeNode
from DataStructers.Queue import Queue

class BinnaryTree:

    def __init__(self, rootData):
        self.treeNode = TreeNode(Data=rootData)

    #-----------------------------------------------------
    def AddNodeTree(self,tree, data):

        if data<tree.Data and tree.Left is None:
            tree.Left = TreeNode(Data=data)
            return
        
        if data>=tree.Data and tree.Right is None:
            tree.Right = TreeNode(Data=data)
            return

        
        if data < tree.Data and tree.Left is not None:
            self.AddNodeTree(tree.Left, data)
            return

        if data >= tree.Data and tree.Right is not None:
            self.AddNodeTree(tree.Right, data)
            return
        
    def Add(self, data):
        self.AddNodeTree(self.treeNode, data)
    #-----------------------------------------------------

    def RegenrateTreePart(self, tree):
        RightPartTree = tree.Right
        LeftPartTree = tree.Left
        Root = tree

         
        if RightPartTree is not None:
             LeftTraker = RightPartTree
             while LeftTraker.Left is not None:
                LeftTraker = LeftTraker.Left
             

             Root.Left = None
             Root.Right = None

             if LeftPartTree is not None:
                LeftTraker.Left = LeftPartTree
             

             return RightPartTree
         

        if LeftPartTree is not None:
           return LeftPartTree

        return None
    


    def DeleteFromTree(self, tree, data): 
         
         preTraker = tree

         while preTraker.Data != data:

                if(preTraker.Left is not None and preTraker.Left.Data == data or
                   preTraker.Right is not None and preTraker.Right.Data == data):
                      break
                

                if preTraker.Data < data and preTraker.Right is not None:
                    preTraker = preTraker.Right
                elif preTraker.Data > data and preTraker.Left is not None:
                    preTraker = preTraker.Left
                
         

         if(preTraker.Left is not None and preTraker.Data > data):
            preTraker.Left = self.RegenrateTreePart(preTraker.Left)
        

         if preTraker.Right is not None and preTraker.Data < data:
            preTraker.Right = self.RegenrateTreePart(preTraker.Right)
         
    
    def Delete(self, data):
        self.DeleteFromTree(self.treeNode, data)
     



    #Left-Root-Right
    def DisplayLRR(self, tree):
        if tree.Left != None:
            self.DisplayLRR(tree.Left)

        print(tree.Data)

        if tree.Right != None:
            self.DisplayLRR(tree.Right)
        
        if tree.Left == None and tree.Right == None:
            return

    def DisplayLeftRootRight(self):
        self.DisplayLRR(self.treeNode)