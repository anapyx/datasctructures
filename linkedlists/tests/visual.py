# -*- coding: utf-8 -*-

import customtkinter as ctk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return  # Elemento removido
            prev = current
            current = current.next
        return  # Elemento n�o encontrado

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Estrutura de Dados")

        self.canvas = ctk.CTkCanvas(root, width=400, height=400)
        self.canvas.pack()

        self.label = ctk.CTkLabel(root, text="Digite um valor:")
        self.label.pack()

        self.entry = ctk.CTkEntry(root)
        self.entry.pack()

        self.button1 = ctk.CTkButton(root, text="Inserir na Lista Sequencial", command=self.insert_sequential)
        self.button1.pack()

        self.button2 = ctk.CTkButton(root, text="Inserir na Lista Simplesmente Encadeada", command=self.insert_singly_linked)
        self.button2.pack()

        self.button3 = ctk.CTkButton(root, text="Inserir na Lista Duplamente Encadeada", command=self.insert_doubly_linked)
        self.button3.pack()

        self.labelnull = ctk.CTkLabel(root, text=" ")
        self.labelnull.pack()

        self.label2 = ctk.CTkLabel(root, text="Remover da Lista:")
        self.label2.pack()

        self.entry2 = ctk.CTkEntry(root)
        self.entry2.pack()

        self.button4 = ctk.CTkButton(root, text="Remover", command=self.remove_singly_linked)
        self.button4.pack()

        self.sequential_list = []
        self.singly_linked_list = LinkedList()
        self.doubly_linked_list = LinkedList()

        self.node_radius = 20
        self.node_spacing = 50
        self.vertical_position = 100

    def insert_sequential(self):
        value = self.entry.get()
        self.sequential_list.append(value)
        self.draw_sequential_list()
        self.entry.delete(0, ctk.END)

    def insert_singly_linked(self):
        value = self.entry.get()
        self.singly_linked_list.insert(value)
        self.draw_singly_linked_list()
        self.entry.delete(0, ctk.END)

    def insert_doubly_linked(self):
        value = self.entry.get()
        self.doubly_linked_list.insert(value)
        self.draw_doubly_linked_list()
        self.entry.delete(0, ctk.END)

    def remove_singly_linked(self):
        value = self.entry2.get()
        if value:
            self.singly_linked_list.remove(value)
            self.draw_singly_linked_list()
        self.entry2.delete(0, ctk.END)

    def draw_sequential_list(self):
        self.canvas.delete("all")
        x = 100
        for value in self.sequential_list:
            self.canvas.create_rectangle(x - self.node_radius, self.vertical_position - self.node_radius,
                                         x + self.node_radius, self.vertical_position + self.node_radius,
                                         fill="lightblue")
            self.canvas.create_text(x, self.vertical_position, text=str(value))
            x += self.node_spacing

    def draw_singly_linked_list(self):
        self.canvas.delete("all")
        current = self.singly_linked_list.head
        x = 100
        while current:
            self.canvas.create_rectangle(x - self.node_radius, self.vertical_position - self.node_radius,
                                         x + self.node_radius, self.vertical_position + self.node_radius,
                                         fill="lightblue")
            self.canvas.create_text(x, self.vertical_position, text=str(current.data))
            if current.next:
                self.canvas.create_line(x + self.node_radius, self.vertical_position,
                                        x + self.node_spacing - self.node_radius, self.vertical_position, arrow=ctk.LAST)
            current = current.next
            x += self.node_spacing

    def draw_doubly_linked_list(self):
        self.canvas.delete("all")
        current = self.doubly_linked_list.head
        x = 100
        while current:
            self.canvas.create_rectangle(x - self.node_radius, self.vertical_position - self.node_radius,
                                         x + self.node_radius, self.vertical_position + self.node_radius,
                                         fill="lightblue")
            self.canvas.create_text(x, self.vertical_position, text=str(current.data))
            if current.next:
                self.canvas.create_line(x + self.node_radius, self.vertical_position,
                                        x + self.node_spacing - self.node_radius, self.vertical_position, arrow=ctk.LAST)
            if current.prev:
                self.canvas.create_line(x - self.node_radius, self.vertical_position,
                                        x - self.node_spacing + self.node_radius, self.vertical_position, arrow=ctk.FIRST)
            current = current.next
            x += self.node_spacing

if __name__ == "__main__":
    root = ctk.CTk()
    gui = GUI(root)
    root.mainloop()
