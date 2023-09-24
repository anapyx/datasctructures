# -*- coding: utf-8 -*-

import customtkinter
import subprocess
import os
import sys

customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1100x780")

import sys
if len(sys.argv) > 1:
    list_type = sys.argv[1]
else:
    list_type = "Lista"

app.title("Projeto 1 - Estrutura de dados")

sys.path.insert(0, "..")

current_directory = os.path.dirname(os.path.abspath(__file__))
directory_path = 'list-project/linkedlists'
current_directory = os.getcwd()
full_path = os.path.join(current_directory, directory_path)
os.chdir(full_path)

from LS import LS
from LSE import LSE
from LDE import LDE
from No import No

defaultfont = customtkinter.CTkFont(size=15, weight='bold')
defaultfont2 = customtkinter.CTkFont(size=25, weight='bold')
customFont = customtkinter.CTkFont(size=42, weight='bold')

app.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

app.frame1 = customtkinter.CTkFrame(app, corner_radius=10)
app.frame1.grid(row=1, rowspan=4, column=0, padx=20, sticky="nsew")
app.frame1.grid_columnconfigure(1, weight=0)
app.frame1.grid_rowconfigure(7, weight=1)

app.frame2 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=10)
app.frame2.grid(row=1, rowspan=4, column=1, columnspan=4, padx=(0, 20), sticky="nsew")

app.canvas_in_frame2 = customtkinter.CTkCanvas(app.frame2, width=1000, height=800)  # Ajuste a largura e altura conforme necessário
app.canvas_in_frame2.pack()
app.canvas_in_frame2.configure(bg='#2b2b2b', highlightbackground='#2b2b2b')

def open_tela1():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela1_path = os.path.join(parent_directory, 'list-app', 'tela1.py')
    subprocess.run(["python", tela1_path])

def create_head():
    global myList
    if list_type == 'Lista Sequencial':
        myList = LS(10000)
    elif list_type == 'Lista Simplesmente Encadeada':
        myList = LSE()
    elif list_type == 'Lista Duplamente Encadeada':
        myList = LDE()
    else:
        return

    dialog = customtkinter.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    pos = 1
    elem = int(elem)
    result = myList.appendList(elem, pos)
    
    if result is True:
        if list_type == 'Lista Sequencial':
            myList.draw_sequential_list(app.canvas_in_frame2)
        elif list_type == 'Lista Simplesmente Encadeada':
            myList.draw_singly_linked_list(app.canvas_in_frame2)
        elif list_type == 'Lista Duplamente Encadeada':
            myList.draw_doubly_linked_list(app.canvas_in_frame2)
    else:
        print("Operação Inválida.")

def add_element():
    global myList

    if myList is None:
        print("Cabeça da lista não foi criada.")
        return

    dialog = customtkinter.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    dialog.destroy()
    dialog2 = customtkinter.CTkInputDialog(text="Digite a posição que o número deve ser inserido: ", title="Adicionar")
    pos = dialog2.get_input()

    try:
        pos = int(pos)
        elem = int(elem)
        
        result = myList.appendList(elem, pos)

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame2)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame2)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame2)
        else:
            print("Operação Inválida.")
    except ValueError:
        print("A posição e/ou o elemento deve ser um número inteiro válido.")

def remove_element():
    global myList

    if myList is None:
        print("Cabeça da lista não foi criada.")
        return

    dialog = customtkinter.CTkInputDialog(text="Digite a posição do número a ser removido: ", title="Remover")
    pos = dialog.get_input()

    try:
        pos = int(pos) 
        result = myList.removeList(pos) 

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame2)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame2)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame2)
        else:
            print("Operação Inválida.")
    except ValueError:
        print("A posição deve ser um número inteiro válido.")

def search_element(canvas):
    canvas.delete("result_text") 
    
    if myList is None:
        canvas.create_text(30, 30, text="Cabeça da lista não foi criada.", tags="result_text")
        return

    dialog = customtkinter.CTkInputDialog(text="Digite o valor do número a ser buscado: ", title="Buscar")
    elem = dialog.get_input()

    try:
        positions = myList.position(elem)
        positions_str = ", ".join(map(str, positions))
        canvas.create_text(400, 50, text=f"O elemento {elem} foi encontrado nas posições: {positions_str}", font=("Arial", 22), tags="result_text")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 22), tags="result_text")

def search_position(canvas):
    canvas.delete("result_text") 
    
    if myList is None:
        canvas.create_text(400, 30, text="Cabeça da lista não foi criada.", font=("Arial", 16), tags="result_text")
        return

    dialog = customtkinter.CTkInputDialog(text="Digite a posição a ser buscada: ", title="Buscar")
    pos = int(dialog.get_input())

    try:
        element = myList.element(pos)
        canvas.create_text(400, 50, text=f"O elemento na posição {pos} é: {element}", font=("Arial", 16), tags="result_text")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 16), tags="result_text")


app.button_1 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Criar Cabeça", font=defaultfont, command=create_head)
app.button_1.grid(row=0, column=0, padx=20, pady=(40, 20))

app.button_2 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Adicionar\nElemento", font=defaultfont, command=add_element)
app.button_2.grid(row=1, column=0, padx=20, pady=20)

app.button_3 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Remove", font=defaultfont, command=remove_element)
app.button_3.grid(row=2, column=0, padx=20, pady=20)

app.button_4 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Busca pelo\nElemento", font=defaultfont, command= lambda: search_element(app.canvas_in_frame2))
app.button_4.grid(row=3, column=0, padx=20, pady=20)

app.button_5 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Busca na\nPosição", font=defaultfont, command= lambda: search_position((app.canvas_in_frame2)))
app.button_5.grid(row=4, column=0, padx=20, pady=20)

app.button_6 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Retornar", font=defaultfont, command=open_tela1)
app.button_6.grid(row=5, column=0, padx=20, pady=20)

label = customtkinter.CTkLabel(master=app, text=list_type, text_color='white')
label.configure(width=app.winfo_screenwidth(), height=100, font=customFont, pady=10, padx=20, corner_radius=10)
label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
label.configure(fg_color='#142c59')


app.mainloop()
