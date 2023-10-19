import numpy as np

class No:
    def __init__(self, content):
        self.content = content
        self.next = None
        self.prev = None
        self.left = None
        self.right = None

    def getContent(self):
        return self.content
    
    def setContent(self, content):
        self.content = content

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
    def setPrevious(self, prev):
        self.prev = prev

    def getPrevious(self):
        return self.prev
    
      def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def setRigt(self, right):
        self.right = right

    cor_azul_claro = "#3B8ED0"
    cor_azul_escuro = "#ad8c1d"
    cor_branca = "#fffdfa"


