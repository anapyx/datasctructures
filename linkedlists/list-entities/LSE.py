import numpy as np

from No import No

class LSE:
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    def __str__(self):
        if self.head:
            return f"{self.head} é o primeiro elemento da lista de tamanho {self.len}."

    # Verifica se a lista está vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Retorna o tamanho da lista
    def size(self):
        return self.len
    
    # Printa os elementos da lista
    def print(self):
        current = self.head
        while current:
            print(current.content)
            current = current.next

    # Adiciona Nó no fim da lista
    def append(self, newnode):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = No(newnode)
            self.len +=1
        else:
            self.head = No(newnode)
            self.len +=1

    # Checa o elemento de determinada posição
    def element(self, pos):
        current = self.head
        aux = 1
        if self.vazia():
            return 'A lista está vazia.'
        elif pos > self.len:
            return 'Posição maior que a lista.'
        else:
            while aux < pos:
                current = current.next
                aux+=1
            if pos == self.len:
                return current

    # Checa as posições de um determinado elemento
    def position(self, elem):
        current = self.head
        if vazia():
            return 'Não há elementos.'
        elif self.head == elem:
            return 1
        else:
            for i in range(1,self.len):
                current = current.next
                if current == elem:
                    return i
                i+=1

        