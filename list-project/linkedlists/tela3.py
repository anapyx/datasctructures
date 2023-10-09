# -*- coding: utf-8 -*-
import customtkinter as cttk
import subprocess
import os
import sys

cttk.set_default_color_theme("blue")

app = cttk.CTk()
app.geometry("1100x780")

import sys
if len(sys.argv) > 1:
    structure_type = sys.argv[1]
#else:
#    structure_type = "Lista"

app.title("Projeto Estrutura de dados Parte 2")

sys.path.insert(0, "..")

from PL import PL
from FL import FL
from ABP import ABP
from No import No

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

# Funcoes do canvas para listas
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


def create_head(canvas):
    canvas.delete("result_text")
    global mystructure
    if structure_type == 'Lista Simplesmente Encadeada':
        mystructure = LSE()
    elif structure_type == 'Lista Duplamente Encadeada':
        mystructure = LDE()
    else:
        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    pos = 1
    #elem = int(elem)
    result = mystructure.appendList(elem, pos)
    
    if result is True:
        if structure_type == 'Lista Simplesmente Encadeada':
            mystructure.draw_singly_linked_list(app.canvas_in_frame)
        elif structure_type == 'Lista Duplamente Encadeada':
            mystructure.draw_doubly_linked_list(app.canvas_in_frame)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

def add_element(canvas):
    global mystructure
    canvas.delete("result_text")
    
    #    if structure_type == 'Fila':
    #        limit_size = 10
    #    else:
    #        limit_size = 6
    #
    #    if mystructure.size() > limit_size:
    #        canvas.create_text(400, 50, text="A lista já está no tamanho máximo.", font=("Arial", 22), tags="result_text", fill = "white")
    #        return
    #
    #    if mystructure is None:
    #        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
    #        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    dialog.destroy()

    try:
        elem = int(elem)

        result = mystructure.appendList(elem)

        if result is True:
            if structure_type == 'Fila':
                mystructure.draw_queue(app.canvas_in_frame, size)
            elif structure_type == 'Lista Simplesmente Encadeada':
                mystructure.draw_singly_linked_list(app.canvas_in_frame)
            elif structure_type == 'Lista Duplamente Encadeada':
                mystructure.draw_doubly_linked_list(app.canvas_in_frame)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError:
        canvas.create_text(400, 50, text="A posição e/ou o elemento deve ser um número inteiro válido.", font=("Arial", 22), tags="result_text", fill = "white")

def remove_element(canvas):
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
        elif structure_type == 'Lista Simplesmente Encadeada':
            mystructure.draw_singly_linked_list(app.canvas_in_frame)
        elif structure_type == 'Lista Duplamente Encadeada':
            mystructure.draw_doubly_linked_list(app.canvas_in_frame)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

def search(canvas):
    canvas.delete("result_text") 
    
    if mystructure is None:
        canvas.create_text(400, 50, text="A estrutura não foi criada", font=("Arial", 22), tags="result_text", fill = "white")
        return

    try:
        elemento = mystructure.element()
        canvas.create_text(400, 50, text=f"O elemento {elemento} foi encontrado na primeira posição", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 22), tags="result_text", fill = "white")


# Botoes do menu da tela 2

if structure_type == 'Fila':
    app.buttonSize = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Definir Tamanho", font=defaultfont, command= lambda: define_size((app.canvas_in_frame)))
    app.buttonSize.grid(row=0, column=0, padx=20, pady=(20, 20))

app.buttonAdd = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Adicionar\nElemento", font=defaultfont, command= lambda: add_element(app.canvas_in_frame))
app.buttonAdd.grid(row=1, column=0, padx=20, pady=20)

app.buttonRem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Remove", font=defaultfont, command= lambda: remove_element(app.canvas_in_frame))
app.buttonRem.grid(row=2, column=0, padx=20, pady=20)

app.buttonElem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Consulta\nElemento", font=defaultfont, command= lambda: search(app.canvas_in_frame))
app.buttonElem.grid(row=3, column=0, padx=20, pady=20)

app.buttonGoBack = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Retornar", font=defaultfont, command=open_tela1)
app.buttonGoBack.grid(row=4, column=0, padx=20, pady=20)

label = cttk.CTkLabel(master=app, text=structure_type, text_color='white')
label.configure(width=app.winfo_screenwidth(), height=100, font=customFont, pady=10, padx=20, corner_radius=10)
label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
label.configure(fg_color='#142c59')


app.mainloop()
