class Node:
    """
    docstring
    """
    def __init__(self, data):
        """
        docstring
        """
        self.data = data
        self.parent = None
        self.son = list()
        self.deuda = False
    
    def AddChild(self, child):
        """
        docstring
        """
        child.AddParent(self)
        self.son.append(child) 
    
    def AddParent(self, parent):
        """
        docstring
        """
        self.parent = parent
    
    def EditRemaining(self, n):
        """
        docstring
        """
        self.remaining = n
    
    def EditDeuda(self, deuda):
        """
        docstring
        """
        self.deuda = deuda
    
    def PrintChildren(self):
        """
        docstring
        """
        if hasattr(self, 'son'):
            for n in self.son:
                print(n.data)
        else:
            print("No children")
    
    def DeleteNode(self):
        """
        docstring
        """
        temp = self.parent
        temp.son.remove(self)
        del self
    
    def CalculateDepth(self):
        """
        docstring
        """
        if hasattr(self.parent, 'son'):
            return 1 + self.parent.CalculateDepth()
        else:
            return 0