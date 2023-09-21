import numpy as np

from No import No
from LSE import LSE

class LDE(LSE):
    def __init__(self, head=None):
        super().__init__()
        self.tail = None
    
    # A LDE herdou os metodos empty, size, full, printlist e element da LSE

    # Checa as posicoes de um determinado elemento
    def position(self, elem):
        count = 1
        
        if self.empty():
            raise ValueError("A lista esta vazia.")
        
        aux = self.head
        
        while aux is not None:
            if aux.getContent() == elem:
                return count
            aux = aux.getNext()
            count += 1
            
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Adiciona No em lista vazia
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
    
    # Adiciona No no meio da lista
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
    
    # Adiciona No no fim da lista
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
    
    # Insercao de No em uma determinada posicao
    def appendInPosition(self, pos, elem):
        if self.empty() and pos != 1:
            return False
        
        if pos == 1:
            return self.append(elem)
        elif pos == self.len+1:
            return self.appendAtEnd(elem)
        else:
            return self.appendAtMiddle(pos, elem)
        
    # Remove No no inicio de uma lista unitaria
    def removeUnitaryList(self):
        value = self.head.getContent()
        self.head = None
        self.tail = None
        self.len -= 1
        
        return value
    
    # Remove No no inicio da lista
    def removeAtStart(self):
        aux = self.head
        
        value = aux.getContent()
        
        self.head = aux.getNext()
        aux.getNext().setAnt(None)
        
        self.len -= 1
        
        aux = None
        
        return value
    
    # Remove No no meio da lista
    def removeAtMiddle(self, pos):
        aux = self.head
        count = 1
        
        while count <= pos-1 and aux is not None:
            aux = aux.getNext()
            count += 1
            
        if aux is None:
            raise ValueError("Posicao invalida.")
        
        value = aux.getContent()
        
        aux.getAnt().setNext(aux.getNext())
        aux.getNext().setAnt(aux.getAnt())
        
        self.len -= 1
        
        aux = None
        
        return value
        
    # Remove No no fim da lista
    def removeAtEnd(self):
        aux = self.tail()
        
        value = aux.getContent()
        
        aux.getAnt().setNext(None)
        self.tail = aux.getAnt()
        
        self.len -= 1
        
        aux =  None
        
        return value
    
    # Controle da remocao de Nos em posicoes determinadas
    def remove(self, pos):
        if self.empty():
            raise ValueError("A lista esta vazia")
        
        if pos == 1 and self.len == 1:
            return self.removeUnitaryList()
        elif pos == 1:
            return self.removeAtStart()
        elif pos == self.size():
            return self.removeAtEnd()
        else:
            return self.removeAtMiddle(pos)
        