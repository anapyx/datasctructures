import numpy as np

from No import No

class LSE:
    def __init__(self, head=None):
        self.head = head
        if head == None:
            self.len = 0
        else:
            self.len = 1

    def __str__(self):
        if self.head:
            return f"{self.head} eh o primeiro elemento da lista de tamanho {self.len}."

    # Verifica se a lista está vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False
        
    # Verifica se a lista está cheia    
    def full(self):
        if self.empty() == True:
            return False
        else:
            return True

    # Retorna o tamanho da lista
    def size(self):
        self.len
        return self.len
    
    # Printa os elementos da lista
    def printList(self):
        current = self.head
        while current:
            print(current.content)
            current = current.next
            
    # Checa o elemento de determinada posição
    def element(self, pos):
        current = self.head
        aux = 1
        if self.empty() == True:
            raise ValueError("A lista esta vazia.")
        if pos < 1 or pos > self.len:
            raise ValueError("Posicao invalida.")    
        while aux < pos:
            current = current.getNextnext()
            aux+=1
        return current.getContent()

    # Checa as posições de um determinado elemento
    def position(self, elem):
        current = self.head
        auxpos = []
        if self.empty() == True:
            raise ValueError("A lista esta vazia.")
        for i in range(1, self.len):
            current = current.next
            if current == elem:
                auxpos.append(i+1)
            i+=1
        if len(auxpos) == 0:
            raise ValueError("Esse elemento nao foi encontrado.")
        else:            
            return auxpos

    # Adiciona Nó em determinada posição
    def appendAtStart(self,elem):
        newnode = No(elem)
        self.head = newnode

    def appendList(self, elem, pos=1):
        newnode = No(elem)
        current = self.head
        if self.empty()==True and pos != 1:
            return False
        elif pos <= 0 or pos > self.len:
            return False
        elif self.empty() == True and pos == 1:
            self.head = newnode
            return True
        elif self.empty() == False and pos == 1:
            newnode.setNext(self.head)
            self.head = newnode
            self.len += 1
            return True
        elif pos == self.len:
            while current.getNext():
                current = current.getNext()
            current.setNext(newnode)
            self.len += 1
            return True
        else:
            for i in range(1,pos-1):
                before = current
                current = current.getNext()
            before.setNext(newnode)
            newnode.setNext(current)
            self.len += 1
            return True

    # Remove Nó no início da lista
    def removeAtStart(self):
        aux = self.head
        
        removed = aux.getContent()
        
        self.head = aux.getNext()
        self.len -= 1
        
        p = None
        
        return removed
    
    # Remove Nó em uma determinada posição
    def removeAtPosition(self, pos):
        current = None
        previous = None
        value = -1
        count = 1
        
        current = self.head
        
        while count < pos and current is not None:
            previous = current
            current = current.getNext()
            count += 1
            
        if current is None:
            raise ValueError("Posicao invalida")
        
        value = current.getContent()
        previous.setNext(current.getNext())
        self.len -= 1
        
        current = None
        
        return value
    
    # Controle da remoção de Nós em posições determinadas
    def remove(self, pos):
    
        if self.empty():
            raise ValueError("A lista esta vazia.")
        if pos <= 0 or pos >= self.len:
            raise ValueError("Posicao invalida.")
        
        if pos == 1:
            return self.removeAtStart()
        else:
            return self.removeAtPosition(pos)