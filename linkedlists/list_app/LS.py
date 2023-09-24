# -*- coding: utf-8 -*-

import customtkinter

class LS:
    def __init__(self, size):
        self.head = None
        self.dados = [None]*size
        self.len = len(self.dados)
        self.node_radius = 20
        self.node_spacing = 50
        self.vertical_position = 400

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

    # Checa o elemento de determinada posicao
    def element(self, pos):
        if pos > self.len or pos <= 0:
            raise ValueError("Posicao invalida.")
        return self.dados[pos-1]
    
    # Checa as posicoes de um determinado elemento
    def position(self, elem):
        auxPos = []
        aux = 0
        for i in range(0, self.len - 1):
            if self.dados[i] == elem:
                auxPos.append(i+1)
                aux = 1
        if aux == 1:
            return auxPos
        else:
            raise ValueError("Nenhum elemento foi encontrado.")
    
    # Insercao de elemento em uma determinada posicao
    def appendList(self, elem, pos):
        if pos < 1 or pos > self.len + 1:
            return "Posição inválida."

        if self.len == len(self.dados):
            self.dados.extend([None] * self.len)

        for i in range(self.len, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]

        self.dados[pos - 1] = elem
        self.len += 1
        
        return True


    # Remocao de uma determinada posicao
    def removeList(self, pos):
        if 1 <= pos <= self.len:
            for i in range(pos, self.len):
                self.dados[i - 1] = self.dados[i]
            self.dados[self.len - 1] = None
            self.len -= 1
            return True
        else:
            raise ValueError("Posição inválida.")

    # Remoção de determinado elemento em todas as aparicoes
    def removeData(self, elem):
        found = False
        for i in range(self.len):
            if self.dados[i] == elem:
                self.removeList(i + 1)
                found = True
        if found:
            return True
        else:
            raise ValueError("Elemento não encontrado na lista.")

    # Ordena a lista para que todos os elementos nulos fiquem no final
    def sortList(self):
        self.dados[:self.len] = sorted(self.dados[:self.len], key=lambda x: x is None)
        return True
    
    def draw_sequential_list(self, canvas):
        canvas.delete("all")
        current = self.head 
        x = 400  
        y = 350  
        node_spacing_horizontal = 150

        while current:
            if current.content is not None:
                canvas.create_rectangle(x - self.node_radius, y - self.node_radius,
                                        x + self.node_radius, y + self.node_radius,
                                        fill="#142c59")
                canvas.create_text(x, y, text=current, font=("Arial", 16))

            if current.next:
                start_x = x + self.node_radius
                start_y = y
                end_x = x + node_spacing_horizontal - self.node_radius
                end_y = y
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=customtkinter.LAST)

            current = current.next
            x += node_spacing_horizontal

