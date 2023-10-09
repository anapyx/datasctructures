# -*- coding: utf-8 -*-

import customtkinter

class FL:
    def __init__(self, size):
        self.dados = [None]*size
        self.len = len(self.dados)
        self.node_radius = 45

    # Verifica se a lista esta vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Verifica se a lista esta cheia
    def full(self):
        if self.empty() == True:
            return False
        elif self.empty() == False:
            if None in self.dados:
                return False
            else:
                return True
    
    # Retorna o tamanho da lista
    def size(self):
        self.len = len(self.dados)
        return self.len
    
    # Printa os elementos da lista
    def printList(self):
        print(self.dados)

    #!! !  ! ! ! ! ! !! ! ! ! ! ! ! ! !
    # retorna o primeiro elemento da fila
    def element(self):
        for i in range(self.len -1, -1, -1):

            if self.dados[i] != None:
                return self.dados[i]
    
    
    
    # Insercao de elemento em uma determinada posicao
    def appendList(self, elem):
        
        for i in range (self.len - 1, 0, -1):
            if self.dados[i-1] is not None:
                self.dados[i] = self.dados[i-1]
        self.dados[0] = elem
        return True
        
    # Remocao no fim da fila
    def removeList(self):

        for i in range(self.len -1, -1, -1):

            if self.dados[i] != None:
                self.dados[i] = None
                return True
    
        return False


    # Ordena a lista para que todos os elementos nulos fiquem no final
    def sortList(self):
        self.dados[:self.len] = sorted(self.dados[:self.len], key=lambda x: x is None)
        return True
    
    def draw_sequential_list(self, canvas, size):
        canvas.delete("all")
        x = 500
        y = 370  
        node_spacing_horizontal = 100

        if size != 1:
            for i in range(1, size):
                x-=50

        for i in range(1, size + 1):
            self.round_rectangle(canvas, x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill="#fffdfa", outline="#3B8ED0", width=4)
            try: 
                canvas.create_text(x, y, text=self.dados[i-1], font=("Arial", 20))
            except: canvas.create_text(x, y, text=None, font=("Arial", 16))
            x = x + node_spacing_horizontal
    
    def round_rectangle(self, canvas, x1, y1, x2, y2, radius=40, **kwargs):
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