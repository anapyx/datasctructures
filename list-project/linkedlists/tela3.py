# -*- coding: utf-8 -*-
import customtkinter as cttk
import tkinter as tk
import subprocess
import os
import sys

cttk.set_default_color_theme("blue")

app = cttk.CTk()
app.geometry("1100x780")

import sys
if len(sys.argv) > 1:
    structure_type = sys.argv[1]
else:
    structure_type = "Estrutura"

app.title("Projeto Estrutura de dados Parte 2")

sys.path.insert(0, "..")

from PL import PL
from FL import FL
from ABP import ABP
from Node import Node

mystructure = None

defaultfont = cttk.CTkFont(size=15, weight='bold')
defaultfont2 = cttk.CTkFont(size=25, weight='bold')
customFont = cttk.CTkFont(size=42, weight='bold')

app.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

app.frameMenu = cttk.CTkFrame(app, corner_radius=10)
app.frameMenu.grid(row=1, rowspan=4, column=0, padx=20, sticky="nsew")
app.frameMenu.grid_columnconfigure(1, weight=0)
app.frameMenu.grid_rowconfigure(7, weight=1)

app.frameBlank = cttk.CTkFrame(app, width=140, height=140, corner_radius=10)
app.frameBlank.grid(row=1, rowspan=4, column=1, columnspan=4, padx=(0, 20), sticky="nsew")

app.canvas_in_frame = cttk.CTkCanvas(app.frameBlank, width=1000, height=800)
app.canvas_in_frame.pack()
app.canvas_in_frame.configure(bg='#2b2b2b', highlightbackground='#2b2b2b')

# Funcao de percorrer entre telas
def open_tela1():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela1_path = os.path.join(parent_directory,'linkedlists', 'tela1.py')
    subprocess.call(["python", tela1_path])

# Funcoes do canvas para filas
def define_size(canvas):
    global mystructure
    global size
    dialog = cttk.CTkInputDialog(text="Digite o valor do tamanho da fila: ", title="Criar")
    size = int(dialog.get_input())
    mystructure = FL(size)

    if size > 0 and size < 11:
        mystructure.draw_queue(app.canvas_in_frame,size)
    elif size < 1:
        canvas.create_text(400, 50, text="Digite um valor válido.", font=("Arial", 22), tags="result_text", fill = "white")
    else:
        canvas.create_text(400, 50, text="A fila não pode ter mais de 10 elementos.", font=("Arial", 22), tags="result_text", fill = "white")
        return

# Inicialização da ABP – criação da raiz
def create_head(canvas):
    canvas.delete("result_text")
    global mystructure
    if structure_type == 'Árvores Binárias de Pesquisa':
        mystructure = ABP()
    else:
        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    result = mystructure.appendList(elem)
    
    if result is True:
        if structure_type == 'Árvores Binárias de Pesquisa':
            mystructure.draw_tree(app.canvas_in_frame)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

# Adição de elementos
def add_element(canvas):
    global mystructure
    canvas.delete("result_text")

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    dialog.destroy()

    try:
        elem = int(elem)

        result = mystructure.appendList(elem)

        if result is True:
            if structure_type == 'Fila':
                mystructure.draw_queue(app.canvas_in_frame, size)
            elif structure_type == 'Árvores Binárias de Pesquisa':
                mystructure.draw_tree(app.canvas_in_frame)
            elif structure_type == 'Pilhas':
                mystructure.draw_scratch(app.canvas_in_frame)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill="white")
    except ValueError:
        canvas.create_text(400, 50, text="O elemento deve ser um número inteiro válido.", font=("Arial", 22), tags="result_text", fill="white")

# Remoção de elementos na Árvore
def remove_element(canvas):
    global mystructure
    canvas.delete("result_text")

    try:
        if mystructure is None:
            canvas.create_text(400, 50, text="A estrutura não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
            return
    except:
        canvas.create_text(400, 50, text="A estrutura não foi criada", font=("Arial", 22), tags="result_text", fill = "white")

    dialog = cttk.CTkInputDialog(text="Digite o número a ser removido: ", title="Remover")
    value = int(dialog.get_input())
    result = mystructure.removeList(value) 
    if result is True:
        if structure_type == 'Árvores Binárias de Pesquisa':
            mystructure.draw_tree(app.canvas_in_frame)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

# Remoção de elementos na Fila
def remove_element_queue(canvas):
    global mystructure
    canvas.delete("result_text")

    try:
        if mystructure is None:
            canvas.create_text(400, 50, text="A estrutura não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
            return
    except:
        canvas.create_text(400, 50, text="A estrutura não foi criada", font=("Arial", 22), tags="result_text", fill = "white")

    result = mystructure.removeList() 

    if result is True:
        if structure_type == 'Fila':
            mystructure.draw_queue(app.canvas_in_frame, size)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

# Retorna o 1o elemento da Fila
def search_queue(canvas):
    canvas.delete("result_text") 
    
    if mystructure is None:
        canvas.create_text(400, 50, text="A estrutura não foi criada", font=("Arial", 22), tags="result_text", fill = "white")
        return

    try:
        elemento = mystructure.element()
        canvas.create_text(400, 50, text=f"O elemento {elemento} foi encontrado na primeira posição", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 22), tags="result_text", fill = "white")

# Função de caminhamento (exibição sequencial + animação)
def search(canvas, mystructure):
    root = cttk.CTk()
    root.geometry("700x400")
    root.title("Exibição Sequencial da Árvore")

    cttk.CTkLabel(root, text="Selecione o tipo de exibição:", font=("Arial", 22)).pack()

    if mystructure is None:
        cttk.CTkLabel(root, text="A estrutura não foi criada", font=("Arial", 22)).pack()
        return

    def display_tree(mode):
        mystructure.draw_tree_sequence(canvas, mode)

    exibicao_var = cttk.StringVar(root)
    exibicao_var.set("Selecionar")

    op = cttk.CTkOptionMenu(root, values=["In-Ordem", "Pré-Ordem", "Pós-Ordem"], variable=exibicao_var, command=lambda mode: display_tree(mode))
    op.pack(pady=20)

    canvas = cttk.CTkCanvas(root, width=700, height=300)
    canvas.configure(bg='#242424', highlightbackground='#242424')
    canvas.pack()

    animation_button = cttk.CTkButton(root, text='Animar')
    animation_button.pack()

    root.mainloop()

if structure_type == 'Árvores Binárias de Pesquisa':
    app.buttonSize = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Criar Raiz", font=defaultfont, command= lambda: create_head((app.canvas_in_frame)))
    app.buttonSize.grid(row=0, column=0, padx=20, pady=(20, 20))
    app.buttonRem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Remove", font=defaultfont, command= lambda: remove_element(app.canvas_in_frame))
    app.buttonRem.grid(row=2, column=0, padx=20, pady=20)
    app.buttonElem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Caminhamento", font=defaultfont, command= lambda: search(app.canvas_in_frame, mystructure))
    app.buttonElem.grid(row=3, column=0, padx=20, pady=20)
elif structure_type == 'Pilhas':
    mystructure = PL()
elif structure_type == 'Fila':
    app.buttonSize = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Definir Tamanho", font=defaultfont, command= lambda: define_size((app.canvas_in_frame)))
    app.buttonSize.grid(row=0, column=0, padx=20, pady=(20, 20))
    app.buttonRem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Remove", font=defaultfont, command= lambda: remove_element_queue(app.canvas_in_frame))
    app.buttonRem.grid(row=2, column=0, padx=20, pady=20)
    app.buttonElem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Primeiro\nElemento", font=defaultfont, command= lambda: search_queue(app.canvas_in_frame))
    app.buttonElem.grid(row=3, column=0, padx=20, pady=20)

app.buttonAdd = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Adicionar\nElemento", font=defaultfont, command= lambda: add_element(app.canvas_in_frame))
app.buttonAdd.grid(row=1, column=0, padx=20, pady=20)

app.buttonGoBack = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Retornar", font=defaultfont, command=open_tela1)
app.buttonGoBack.grid(row=4, column=0, padx=20, pady=20)

label = cttk.CTkLabel(master=app, text=structure_type, text_color='white')
label.configure(width=app.winfo_screenwidth(), height=100, font=customFont, pady=10, padx=20, corner_radius=10)
label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
label.configure(fg_color='#142c59')

app.mainloop()