from Node import Node
import customtkinter as ctk
import time
import random
class ABP(Node):
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
    
    def _search(self, node, value):
        if node is None:
            return None

        if node.getContent() == value:
            return node

        if value < int(node.getContent()):
            return self._search(node.getLeft(), value)
        else:
            return self._search(node.getRight(), value)

    def appendList(self, elem):
        newnode = Node(elem)

        if self.empty():
            self.root = newnode
            return True
        else:
            return self._append(self.root, newnode)

    def _append(self, current_node, new_node):
        if current_node is None:
            return False

        current_content = current_node.getContent()
        new_content = new_node.getContent()

        if current_content is not None and new_content is not None:
            if int(new_content) < int(current_content):
                if current_node.getLeft() is None:
                    current_node.setLeft(new_node)
                    return True 
                else:
                    return self._append(current_node.getLeft(), new_node)
            elif int(new_content) > int(current_content):
                if current_node.getRight() is None:
                    current_node.setRight(new_node)
                    return True  
                else:
                    return self._append(current_node.getRight(), new_node)
            else:
                return False
        else:
            return False

    def removeList(self, value):
        if self.empty():
            return False  
        
        node_to_remove = self._search(self.root, value)

        if node_to_remove is None:
            return False  
        
        self.root = self._remove(self.root, value)
        return True  
    
    def _remove(self, node, value):
        if node is None:
            return node

        if value < int(node.getContent()):
            node.setLeft(self._remove(node.getLeft(), value))
        elif value > int(node.getContent()):
            node.setRight(self._remove(node.getRight(), value))
        else:
            if node.getLeft() is None and node.getRight() is None:
                return None
            elif node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()

            min_node = self._find_min(node.getRight())
            node.setContent(min_node.getContent())
            node.setRight(self._remove(node.getRight(), min_node.getContent()))

        return node

    
    def _find_min(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()
        return node
    
    def draw_tree(self, canvas):
        canvas.delete("all") 
        
        x = canvas.winfo_reqwidth() // 2
        y = 120
        spacing = 100

        self._draw_tree_recursive(self.root, canvas, x, y, spacing)
    
    def _draw_tree_recursive(self, node, canvas, x, y, spacing):
        if node:
            if node.getLeft():
                start_x = x
                start_y = y + 25
                end_x = x - spacing
                end_y = y + 75
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=ctk.LAST, width=4)
                self._draw_tree_recursive(node.getLeft(), canvas, x - spacing, y + 75, spacing // 2)

            if node.getRight():
                start_x = x
                start_y = y + 25
                end_x = x + spacing
                end_y = y + 75
                canvas.create_line(start_x, start_y, end_x, end_y, arrow=ctk.LAST, width=4)
                self._draw_tree_recursive(node.getRight(), canvas, x + spacing, y + 75, spacing // 2)

            if node.getContent() is not None:
                canvas.create_oval(x - 35, y - 35, x + 35, y + 35, fill="white")
                canvas.create_text(x, y, text=str(node.getContent()), font=("Arial", 20))

    def draw_tree_sequence(self, canvas, mode):
        root = self.root 
        values = []  
        spacing = 80

        def in_order(node):
            if node:
                in_order(node.left)
                values.append(str(node.getContent())) 
                in_order(node.right)

        def pre_order(node):
            if node:
                values.append(str(node.getContent())) 
                pre_order(node.left)
                pre_order(node.right)

        def pos_order(node):
            if node:
                pos_order(node.left)
                pos_order(node.right)
                values.append(str(node.getContent())) 

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