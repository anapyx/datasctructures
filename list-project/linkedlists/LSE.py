# -*- coding: utf-8 -*-

import numpy as np
import customtkinter
from No import No

class LSE:
    def __init__(self, head=None):
        self.head = head
        self.content = None
        if head == None:
            self.len = 0
        else:
            self.len = 1
        self.node_radius = 45
        self.node_spacing = 30
        self.vertical_position = 400
        
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
        if self.empty():
            raise ValueError("A lista está vazia.")
        if pos < 1 or pos > self.len:
            raise ValueError("Posição inválida.")
        while aux < pos:
            current = current.getNext()
            aux += 1
        return current.getContent() 


    # Checa as posições de um determinado elemento
    def position(self, elem):
        current = self.head
        auxpos = []
        if self.empty():
            raise ValueError("A lista está vazia.")

        for i in range(1, self.len + 1): 
            if str(current.getContent()) == elem:
                auxpos.append(i)  
            current = current.getNext()

        if not auxpos:
            raise ValueError("Esse elemento não foi encontrado.")
        else:
            return auxpos 


    # Adiciona Nó em determinada posição
    def appendList(self, elem, pos):
        newnode = No(elem)
        current = self.head

        if pos <= 0 or pos > self.len + 1:
            return False

        if self.empty() == True:
            if pos == 1:
                self.head = newnode
                self.len += 1
                return True
            else:
                return False

        if pos == 1:
            newnode.setNext(self.head)
            self.head = newnode
            self.len += 1
            return True
        elif pos == self.len + 1:
            while current.getNext():
                current = current.getNext()
            current.setNext(newnode)
            self.len += 1
            return True
        else:
            for i in range(1, pos):
                before = current
                current = current.getNext()
            before.setNext(newnode)
            newnode.setNext(current)
            self.len += 1
            return True

    # Remove Nó do início da lista
    def removeAtStart(self):
        if self.empty():
            raise ValueError("A lista está vazia.")
        
        removed = self.head.getContent()
        self.head = self.head.getNext()
        self.len -= 1
        return True

    # Remove Nó em uma determinada posição
    def removeAtPosition(self, pos):
        if self.empty():
            raise ValueError("A lista está vazia.")
        if pos <= 0 or pos > self.len:
            raise ValueError("Posição inválida.")
        
        current = self.head
        previous = None
        count = 1

        while count < pos:
            previous = current
            current = current.getNext()
            count += 1
            
        value = current.getContent()
        
        if previous:
            previous.setNext(current.getNext())
        else:
            self.head = current.getNext()
        
        self.len -= 1
        
        return True

    # Controle da remoção de Nós em posições determinadas
    def removeList(self, pos):
        if pos == 1:
            return self.removeAtStart()
        else:
            return self.removeAtPosition(pos)
    
        

    def draw_singly_linked_list(self, canvas):
        canvas.delete("all")

        current = self.head 
        x = 50
        y = 350  
        node_spacing_horizontal = 150

        

        while current:
            if current.content is not None:
                self.round_rectangle(canvas, x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill="#fffdfa", outline="#3B8ED0", width=4)
                canvas.create_text(x, y, text=str(current.content), font=("Arial", 20))

            if current.next:
                start_x = x + self.node_radius
                start_y = y
                end_x = x + node_spacing_horizontal - self.node_radius
                end_y = y
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=customtkinter.LAST, width=4, fill="#3B8ED0")

            current = current.next
            x += node_spacing_horizontal

    def round_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                x1 + radius, y1,
                x2 - radius, y1,
                x2 - radius, y1,
                x2, y1,
                x2, y1 + radius,
                x2, y1 + radius,
                x2, y2 - radius,
                x2, y2 - radius,
                x2, y2,
                x2 - radius, y2,
                x2 - radius, y2,
                x1 + radius, y2,
                x1 + radius, y2,
                x1, y2,
                x1, y2 - radius,
                x1, y2 - radius,
                x1, y1 + radius,
                x1, y1 + radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)