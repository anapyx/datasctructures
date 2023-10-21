from No import No
import customtkinter as ctk
import time
import random
class ABP(No):
    def __init__(self, content=None):
        self.root = super().__init__(content)

    def empty(self):
        if self.root is None:
            return True
        else:
            return False

    def search(self, value):
        if self.empty():
            return 'A árvore está vazia'

        return self._search(self.root, value)
    
    def _search(self, No, value):
        if No is None:
            return None

        if No.getContent() == value:
            return No

        if value < int(No.getContent()):
            return self._search(No.getLeft(), value)
        else:
            return self._search(No.getRight(), value)

    def appendList(self, elem):
        newNo = No(elem)

        if self.empty():
            self.root = newNo
            return True
        else:
            return self._append(self.root, newNo)

    def _append(self, current_No, new_No):
        if current_No is None:
            return False

        current_content = current_No.getContent()
        new_content = new_No.getContent()

        if current_content is not None and new_content is not None:
            if int(new_content) < int(current_content):
                if current_No.getLeft() is None:
                    current_No.setLeft(new_No)
                    return True 
                else:
                    return self._append(current_No.getLeft(), new_No)
            elif int(new_content) > int(current_content):
                if current_No.getRight() is None:
                    current_No.setRight(new_No)
                    return True  
                else:
                    return self._append(current_No.getRight(), new_No)
            else:
                return False
        else:
            return False

    def removeList(self, value):
        if self.empty():
            return False  
        
        No_to_remove = self._search(self.root, value)

        if No_to_remove is None:
            return False  
        
        self.root = self._remove(self.root, value)
        return True  
    
    def _remove(self, No, value):
        if No is None:
            return No

        if value < int(No.getContent()):
            No.setLeft(self._remove(No.getLeft(), value))
        elif value > int(No.getContent()):
            No.setRight(self._remove(No.getRight(), value))
        else:
            if No.getLeft() is None and No.getRight() is None:
                return None
            elif No.getLeft() is None:
                return No.getRight()
            elif No.getRight() is None:
                return No.getLeft()

            min_No = self._find_min(No.getRight())
            No.setContent(min_No.getContent())
            No.setRight(self._remove(No.getRight(), min_No.getContent()))

        return No

    
    def _find_min(self, No):
        while No.getLeft() is not None:
            No = No.getLeft()
        return No
    
    def draw_tree(self, canvas):
        canvas.delete("all") 
        
        x = canvas.winfo_reqwidth() // 2
        y = 120
        spacing = 100

        self._draw_tree_recursive(self.root, canvas, x, y, spacing)
    
    def _draw_tree_recursive(self, No, canvas, x, y, spacing):
        if No:
            if No.getLeft():
                start_x = x
                start_y = y + 25
                end_x = x - spacing
                end_y = y + 75
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=ctk.LAST, width=4)
                self._draw_tree_recursive(No.getLeft(), canvas, x - spacing, y + 75, spacing // 2)

            if No.getRight():
                start_x = x
                start_y = y + 25
                end_x = x + spacing
                end_y = y + 75
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=ctk.LAST, width=4)
                self._draw_tree_recursive(No.getRight(), canvas, x + spacing, y + 75, spacing // 2)

            if No.getContent() is not None:
                canvas.create_oval(x - 35, y - 35, x + 35, y + 35, fill="white")
                canvas.create_text(x, y, text=str(No.getContent()), font=("Arial", 20))

    def draw_tree_sequence(self, canvas, mode):
        root = self.root 
        values = []  
        spacing = 80

        def in_order(No):
            if No:
                in_order(No.left)
                values.append(str(No.getContent())) 
                in_order(No.right)

        def pre_order(No):
            if No:
                values.append(str(No.getContent())) 
                pre_order(No.left)
                pre_order(No.right)

        def pos_order(No):
            if No:
                pos_order(No.left)
                pos_order(No.right)
                values.append(str(No.getContent())) 

        if mode == 'In-Ordem':
            in_order(root) 
        if mode == 'Pré-Ordem':
            pre_order(root) 
        if mode == 'Pós-Ordem':
            pos_order(root) 

        total_width = len(values) * spacing

        x = (canvas.winfo_reqwidth() - total_width) / 2

        y = 50

        for value in values:
            canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="white")
            canvas.create_text(x, y, text=value, font=("Arial", 16))
            x += spacing