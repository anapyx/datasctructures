import numpy as np

from No import No

class LSE:
    def __init__(self, head=None):
        self.head = head
        self.len = len(self.head)

    def __str__(self):
        if self.head:
            return f"{self.head} eh o primeiro elemento da lista de tamanho {self.len}."

    # Verifica se a lista está vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False
        
    def full(self):
        if self.empty() == True:
            return False
        else:
            return True

    # Retorna o tamanho da lista
    def size(self):
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

    # Adiciona Nó ao início da lista
    def appendList(self, elem):
        newnode = No(elem)
        newnode.setNext(self.head)
        self.head = newnode
        self.len += 1

    # Adiciona Nó no meio da lista
    def appendAtMiddle(self, pos, elem):
        newnode = No(elem)
        aux = self.head

        for i in range(1, pos - 1):
            aux = aux.getNext()

        newnode.setNext(aux.getNext())
        aux.setNext(newnode)
        self.len += 1

    # Adiciona Nó no fim da lista
    def appendAtEnd(self, elem):
        newnode = No(elem)
        current = self.head

        if current:
            while current.getNext():
                current = current.getNext()
            current.setNext(newnode)
            self.len += 1
        else:
            self.head = newnode
            self.len += 1
        
    # Inserção de Nó em uma determinada posição
    def appendInPosition(self, pos, elem):
        if self.empty() and pos != 1:
            return False
        if pos <= 0 or pos > (self.len + 1):
            return False
        if pos == 1:
            return self.append(elem) 
        elif pos == self.len+1:
            return self.appendAtEnd(elem)
        else:
            return self.appendAtMiddle(pos, elem) 

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