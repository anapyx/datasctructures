
class Node:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        
    def getContent(self):
        return self.content
    
    def setContent(self, content):
        self.content = content
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right