# -*- coding: utf-8 -*-

import customtkinter

class LS:
    def __init__(self, size):
        self.head = None
        self.dados = [None]*size
        self.len = len(self.dados)
        self.node_radius = 45
        self.node_spacing = 30
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
            #print(type(self.dados[i]), type(elem))
            if str(self.dados[i]) == elem:
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

        #NAO SEI PARA QUE SERVEM, MAS ESTAVAM DANDO ERRO
        #if self.len == len(self.dados):
        #    self.dados.extend([None] * self.len)

        #for i in range(self.len, pos - 1, -1):
        #    self.dados[i] = self.dados[i - 1]

        self.dados[pos - 1] = elem
        self.len += 1

        return True


    # Remocao de uma determinada posicao
    def removeList(self, pos):
        if 1 <= pos <= self.len:

            self.dados[pos-1] = None

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
    
    def draw_sequential_list(self, canvas, size):
        canvas.delete("all")
        x = 500
        y = 370  
        node_spacing_horizontal = 100

        for i in range(1, size,1):
            if size == 1:
                break
            x-=50

        for i in range(1, size + 1, 1):
            canvas.create_rectangle(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill= "#fffdfa", outline = "#142c59", width = 2)
            try: 
                canvas.create_text(x, y, text=self.dados[i-1], font=("Arial", 16))
            except: canvas.create_text(x, y, text=None, font=("Arial", 16))
            x = x + node_spacing_horizontal

    
