# -*- coding: utf-8 -*-

import customtkinter


class PL:
    def __init__(self, size):
        self.dados = [None]*size
        self.len = len(self.dados)
        self.node_radius = 45

    # Verifica se a pilha esta vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Verifica se a pilha esta cheia
    def full(self):
        if self.empty() == True:
            return False
        elif self.empty() == False:
            if None in self.dados:
                return False
            else:
                return True

    # Retorna o tamanho da pilha
    def size(self):
        self.len = len(self.dados)
        return self.len

    # Insercao de elemento no topo
    def appendList(self, elem):
        if self.dados[0] is not None:
            return False
        elif self.dados[self.len - 1] is None:
            self.dados[self.len - 1] = elem
            return True

        # Adiciona input no topo da pilha
        for i in range (0, self.len - 1):
            if self.dados[i+1] is not None:
                self.dados[i] = elem
                break
        return True

    # Construcao da pilha
    def draw_stack(self, canvas, size):
        canvas.delete("all")
        x = 500
        y = 370
        node_spacing_vertical = 90

        if size != 1:
            for i in range(1, size):
                y -= 50

        for i in range(1, size + 1):
            self.round_rectangle(canvas, x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill="#fffdfa", outline="#3B8ED0", width=4)
            try:
                canvas.create_text(x, y, text=self.dados[i-1], font=("Arial", 20))
            except:
                canvas.create_text(x, y, text=None, font=("Arial", 16))
            y = y + node_spacing_vertical

    # ********************* TODO
    def top_stack(self):
        for i in range(0, self.len):
            if self.dados[i] != None:
                return self.dados[i]

    # Remocao de do elemento no topo
    def removeList(self):
        for i in range(0, self.len):
            if self.dados[i] != None:
                self.dados[i] = None
                return True
        return False

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
