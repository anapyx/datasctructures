import numpy as np

from No import No
from LSE import LSE

class LDE(LSE):
    def __init__(self, head):
        self.head = None
        self.tail = None
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False
    
    def size(self):
        return self.len
    
    # Checa o elemento de determinada posição
    def element(self, pos):
        aux = self.head
        count = 1
        
        if self.empty():
            raise ValueError("A lista está vazia.")
        
        if pos < 1 or pos > self.len:
            raise ValueError("Posição inválida.")
        
        while count < pos:
            aux = aux.getNext()
            count += 1
        
        return aux.getContent()
    
    # Checa as posições de um determinado elemento
    def position(self, elem):
        count = 1
        
        if self.empty():
            raise ValueError("A lista está vazia.")
        
        aux = self.head
        
        while aux is not None:
            if aux.getContent() == elem:
                return count
            aux = aux.getNext()
            count += 1
            
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Adiciona Nó em lista vazia
    def append(self, elem):
        newnode = No()
        
        newnode.setContent(elem)
        newnode.setNext(self.head)
        newnode.setAnt(None)
        
        if self.empty():
            self.tail = newnode
        else:
            self.head.setAnt(newnode)
        
        self.head = newnode
        self.len += 1
        
        return True
    
    # Adiciona Nó no meio da lista
    def appendAtMiddle(self, pos, elem):
        count = 1
        
        newnode = No()
        newnode.setContent(elem)
        
        aux = self.head
        
        while count < pos-1 and aux is not None:
            aux = aux.getNext()
            count += 1

        if aux is None:
            return False
        
        newnode.setAnt(aux)
        newnode.setNext(aux.getNext())
        
        if aux.getNext() is not None:
            aux.getNext().setAnt(newnode)
        
        aux.setNext(newnode)
        
        self.len += 1
        
        return True
    
    # Adiciona Nó no fim da lista
    def appendAtEnd(self, elem):
        newnode = No()
        newnode.setContent(elem)
        
        aux = self.head
        
        while aux.getNext() is not None:
            aux = aux.getNext()
            
        newnode.setNext(None)
        aux.setNext(newnode)
        
        newnode.setAnt(self.tail)
        self.tail.setNext(newnode)
        self.tail = newnode
        
        self.len += 1
        
        return True
    
    # Inserção de Nó em uma determinada posição
    def appendInPosition(self, pos, elem):
        if self.empty() and pos != 1:
            return False
        
        if pos == 1:
            return self.append(elem)
        elif pos == self.len+1:
            return self.appendAtEnd(elem)
        else:
            return self.appendAtMiddle(pos, elem)
        
    # Remove Nó no início de uma lista unitária
    def removeUnitaryList(self):
        value = self.head.getContent()
        self.head = None
        self.tail = None
        self.len -= 1
        
        return value
    
    # Remove Nó no início da lista
    def removeAtStart(self):
        aux = self.head
        
        value = aux.getContent()
        
        self.head = aux.getNext()
        aux.getNext().setAnt(None)
        
        self.len -= 1
        
        aux = None
        
        return value
    
    # Remove Nó no meio da lista
    def removeAtMiddle(self, pos):
        aux = self.head
        count = 1
        
        while count <= pos-1 and aux is not None:
            aux = aux.getNext()
            count += 1
            
        if aux is None:
            raise ValueError("Posição inválida.")
        
        value = aux.getContent()
        
        aux.getAnt().setNext(aux.getNext())
        aux.getNext().setAnt(aux.getAnt())
        
        self.len -= 1
        
        aux = None
        
        return value
        
    # Remove Nó no fim da lista
    def removeAtEnd(self):
        aux = self.tail()
        
        value = aux.getContent()
        
        aux.getAnt().setNext(None)
        self.tail = aux.getAnt()
        
        self.len -= 1
        
        aux =  None
        
        return value
    
    # Controle da remoção de Nós em posições determinadas
    def remove(self, pos):
        if self.empty():
            raise ValueError("A lista está vazia")
        
        if pos == 1 and self.len == 1:
            return self.removeUnitaryList()
        elif pos == 1:
            return self.removeAtStart()
        elif pos == self.size():
            return self.removeAtEnd()
        else:
            return self.removeAtMiddle(pos)
        