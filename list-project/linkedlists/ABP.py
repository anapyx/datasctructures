# -*- coding: utf-8 -*-


import customtkinter

class ABP:
    def _init_(self, content=None):
        self.root = Node(content)
    
    def empty(self):
        return self.root is None
    
    def search(self, value):
        if self.empty():
            return 'A árvore está vazia'
        
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return None

        if node.getContent() == value:
            return node

        if value < node.getContent():
            return self._search(node.getLeft(), value)
        else:
            return self._search(node.getRight(), value)

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node:
            self._inOrder(node.getLeft())
            dados = node.getContent()
            self._inOrder(node.getRight())
    
    def preOrder(self):
        self._preOrder(self.root)

    def _preOrder(self, node):
        if node:
            print(node.getContent())
            self._preOrder(node.getLeft())
            self._preOrder(node.getRight())
    
    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, node):
        if node:
            self._postOrder(node.getLeft())
            self._postOrder(node.getRight())
            print(node.getContent())

    def append(self, elem):
        newnode = Node(elem)
        
        if self.empty():
            self.root = newnode
        else:
            self._append(self.root, newnode)

    def _append(self, current_node, new_node):
        if new_node.getContent() < current_node.getContent():
            if current_node.getLeft() is None:
                current_node.setLeft(new_node)
            else:
                self._append(current_node.getLeft(), new_node)
        else:
            if current_node.getRight() is None:
                current_node.setRight(new_node)
            else:
                self._append(current_node.getRight(), new_node)