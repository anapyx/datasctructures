import tkinter as tk

class TreeVisualizer:
    def __init__(self, bst):
        self.bst = bst

        self.root = tk.Tk()
        self.root.title("Visualização de Árvore Binária de Pesquisa")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.label = tk.Label(self.root, text="Inserir um número:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.insert_button = tk.Button(self.root, text="Inserir", command=self.insert)
        self.insert_button.pack()

    def insert(self):
        value = int(self.entry.get())
        self.bst.append(value)
        self.draw_tree(self.bst.root, 200, 50, 100)

    def draw_tree(self, node, x, y, spacing):
        if node:
            self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="white")
            self.canvas.create_text(x, y, text=str(node.getContent()))
            if node.getLeft():
                self.canvas.create_line(x, y + 15, x - spacing, y + 50, arrow=tk.LAST)
                self.draw_tree(node.getLeft(), x - spacing, y + 50, spacing // 2)
            if node.getRight():
                self.canvas.create_line(x, y + 15, x + spacing, y + 50, arrow=tk.LAST)
                self.draw_tree(node.getRight(), x + spacing, y + 50, spacing // 2)

    def run(self):
        self.root.mainloop()

value = int(self.entry.get())
        self.bst.insert(value)
        self.draw_tree(self.bst.root, 200, 50, 100)

    def draw_tree(self, node, x, y, spacing):
        if node:
            self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="white")
            self.canvas.create_text(x, y, text=str(node.value))
            if node.left:
                self.canvas.create_line(x, y + 15, x - spacing, y + 50, arrow=tk.LAST)
                self.draw_tree(node.left, x - spacing, y + 50, spacing // 2)
            if node.right:
                self.canvas.create_line(x, y + 15, x + spacing, y + 50, arrow=tk.LAST)
                self.draw_tree(node.right, x + spacing, y + 50, spacing // 2)

node = 200
